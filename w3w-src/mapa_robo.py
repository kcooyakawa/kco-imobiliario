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
ENDPOINTS = ['https://overpass-api.de/api/interpreter', 'https://overpass.kumi.systems/api/interpreter']

Q = f"""[out:json][timeout:90];
(
  nwr["amenity"~"^(restaurant|bar|pub|cafe|ice_cream|fast_food|pharmacy|fuel|hospital|clinic|theatre|cinema|arts_centre|nightclub|bakery)$"]{BBOX};
  nwr["shop"~"^(bakery|confectionery|pastry|chocolate|supermarket|wine|deli)$"]{BBOX};
  nwr["leisure"~"^(park|garden|fitness_centre)$"]["name"]{BBOX};
  nwr["tourism"~"^(museum|gallery|hotel|attraction)$"]{BBOX};
);
out center tags;"""


def categoria(t):
    a, s, l, tu = t.get('amenity'), t.get('shop'), t.get('leisure'), t.get('tourism')
    cz = (t.get('cuisine') or '').lower()
    if a in ('restaurant', 'fast_food'):
        if 'pizza' in cz: return 'pizzarias'
        if any(k in cz for k in ('steak', 'barbecue', 'churrasc', 'brazilian_bbq')): return 'churrascarias'
        if any(k in cz for k in ('japanese', 'sushi', 'ramen')): return 'japoneses'
        if 'burger' in cz: return 'hamburguerias'
        return 'restaurantes'
    if a in ('bar', 'pub'): return 'bares'
    if a == 'nightclub': return 'noite'
    if a == 'cafe': return 'cafes'
    if a == 'ice_cream' or s in ('confectionery', 'pastry', 'chocolate'): return 'docerias'
    if a == 'bakery' or s == 'bakery': return 'padarias'
    if a == 'pharmacy': return 'farmacias'
    if a in ('hospital', 'clinic'): return 'saude'
    if a == 'fuel': return 'postos'
    if s in ('supermarket', 'wine', 'deli'): return 'mercados'
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
