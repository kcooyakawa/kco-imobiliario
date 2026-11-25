"""Robô do Mapa de Moema.

Busca no OpenStreetMap (Overpass API) os lugares de Moema e arredores, classifica por categoria
e grava em mapa/locais.json. Roda no GitHub Actions toda segunda e sexta (ver .github/workflows/mapa-moema.yml).
Dados © colaboradores do OpenStreetMap, licença ODbL.

Lugares curados pela W3W (destaques, parceiros, notas do concierge) ficam em mapa/curadoria.json
e têm prioridade sobre os dados automáticos.
"""
import json, os, sys, time, urllib.request, urllib.parse, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'mapa', 'locais.json')
CUR = os.path.join(ROOT, 'mapa', 'curadoria.json')
UA = os.environ.get('MAPA_UA', 'W3W-Mapa-Moema/1.0 (+https://kcooyakawa.github.io/kco-imobiliario/w3w/)')

# Moema e entorno imediato (sul, oeste, norte, leste)
BBOX = (-23.6180, -46.6820, -23.5860, -46.6450)
ENDPOINTS = ['https://overpass-api.de/api/interpreter', 'https://overpass.private.coffee/api/interpreter', 'https://overpass.kumi.systems/api/interpreter']

Q = f"""[out:json][timeout:90];
(
  nwr["amenity"~"^(restaurant|bar|pub|cafe|ice_cream|fast_food|pharmacy|fuel|hospital|clinic|dentist|veterinary|theatre|cinema|arts_centre|nightclub|bakery|car_wash|school|kindergarten|university|college|bank)$"]["name"]{BBOX};
  nwr["shop"~"^(bakery|confectionery|pastry|chocolate|supermarket|convenience|wine|deli|pet|laundry|dry_cleaning|locksmith|hairdresser|beauty|florist|tailor|car|car_repair|optician|books|bicycle)$"]["name"]{BBOX};
  nwr["craft"~"^(locksmith|tailor|dressmaker)$"]["name"]{BBOX};
  nwr["leisure"~"^(park|garden|fitness_centre)$"]["name"]{BBOX};
  nwr["tourism"~"^(museum|gallery|hotel|attraction)$"]{BBOX};
);
out center tags;"""


def categoria(t):
    a, s, l, tu = t.get('amenity'), t.get('shop'), t.get('leisure'), t.get('tourism')
    cz = (t.get('cuisine') or '').lower()
    nm = (t.get('name') or '').lower()
    if a == 'ice_cream' or 'ice_cream' in cz or 'sorvet' in nm or 'gelat' in nm: return 'sorveterias'
    if a in ('restaurant', 'fast_food', 'cafe', 'bakery') or s in ('bakery', 'confectionery', 'pastry'):
        if 'pizz' in nm: return 'pizzarias'
        if 'churrasc' in nm or 'steak' in nm: return 'churrascarias'
        if 'padaria' in nm or 'panific' in nm: return 'padarias'
        if any(k in nm for k in ('doce', 'confeit', 'brigadeir', 'chocolat', 'bolo')): return 'docerias'
    if a in ('restaurant', 'fast_food'):
        if 'pizza' in cz: return 'pizzarias'
        if any(k in cz for k in ('steak', 'barbecue', 'churrasc', 'brazilian_bbq')): return 'churrascarias'
        if any(k in cz for k in ('japanese', 'sushi', 'ramen')): return 'japoneses'
        if 'burger' in cz: return 'hamburguerias'
        return 'restaurantes'
    c = t.get('craft')
    if s == 'pet' or a == 'veterinary': return 'pet'
    if s in ('laundry', 'dry_cleaning'): return 'lavanderias'
    if a == 'car_wash': return 'lavarapido'
    if s == 'locksmith' or c == 'locksmith': return 'chaveiros'
    if s == 'tailor' or c in ('tailor', 'dressmaker'): return 'costureiras'
    if s == 'hairdresser': return 'cabeleireiros'
    if s == 'beauty': return 'estetica'
    if s == 'florist': return 'floriculturas'
    if s == 'car': return 'concessionarias'
    if s == 'car_repair': return 'oficinas'
    if a in ('school', 'kindergarten'): return 'escolas'
    if a in ('university', 'college'): return 'faculdades'
    if a == 'bank': return 'bancos'
    if a == 'dentist': return 'saude'
    if s in ('optician', 'books', 'bicycle'): return 'lojas'
    if a in ('bar', 'pub'): return 'bares'
    if a == 'nightclub': return 'noite'
    if a == 'cafe': return 'cafes'
    if s in ('confectionery', 'pastry', 'chocolate'): return 'docerias'
    if a == 'bakery' or s == 'bakery': return 'padarias'
    if a == 'pharmacy': return 'farmacias'
    if a in ('hospital', 'clinic'): return 'saude'
    if a == 'fuel': return 'postos'
    if s in ('supermarket', 'convenience', 'wine', 'deli'): return 'mercados'
    if a in ('theatre', 'cinema', 'arts_centre') or tu in ('museum', 'gallery', 'attraction'): return 'cultura'
    if l in ('park', 'garden'): return 'parques'
    if l == 'fitness_centre': return 'academias'
    if tu == 'hotel': return 'hoteis'
    return None


def fetch():
    body = urllib.parse.urlencode({'data': Q}).encode()
    for ep in ENDPOINTS:
        for tent in range(3):
            try:
                req = urllib.request.Request(ep, data=body, headers={'User-Agent': UA})
                with urllib.request.urlopen(req, timeout=120) as r:
                    return json.load(r)
            except Exception as e:
                print('falhou', ep, tent, e, file=sys.stderr); time.sleep(10)
    raise SystemExit('Overpass indisponível')


def main():
    data = fetch()
    locais, vistos = [], set()
    for el in data.get('elements', []):
        t = el.get('tags', {})
        nome, cat = t.get('name'), categoria(t)
        if not nome or not cat: continue
        lat = el.get('lat') or (el.get('center') or {}).get('lat')
        lon = el.get('lon') or (el.get('center') or {}).get('lon')
        if lat is None: continue
        k = (nome.lower(), cat)
        if k in vistos: continue
        vistos.add(k)
        rua = ' '.join(x for x in [t.get('addr:street'), t.get('addr:housenumber')] if x)
        h = t.get('opening_hours', '')
        locais.append({
            'id': f"{el['type'][0]}{el['id']}", 'nome': nome, 'cat': cat,
            'lat': round(lat, 6), 'lon': round(lon, 6),
            'horario': h, 'h24': h.strip() == '24/7', 'end': rua,
            'tel': t.get('phone') or t.get('contact:phone') or '',
            'site': t.get('website') or t.get('contact:website') or '',
            'insta': t.get('contact:instagram') or '',
        })
    if os.path.exists(CUR):  # curadoria W3W tem prioridade
        cur = json.load(open(CUR, encoding='utf-8'))
        porid = {c['id']: c for c in cur if c.get('id')}
        for l in locais:
            if l['id'] in porid: l.update(porid.pop(l['id']))
        locais += [c for c in porid.values() if c.get('lat')]
        locais += [c for c in cur if not c.get('id') and c.get('lat')]
    locais.sort(key=lambda l: (not l.get('destaque'), l['cat'], l['nome']))
    out = {'atualizado': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).isoformat(timespec='minutes'),
           'fonte': '© colaboradores do OpenStreetMap', 'total': len(locais), 'locais': locais}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('ok', len(locais), 'lugares')


if __name__ == '__main__':
    main()
