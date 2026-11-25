"""Robô do Mapa de Moema.

Busca no OpenStreetMap (Overpass API) os lugares de Moema e arredores, classifica por categoria
e grava em mapa/locais.json. Roda no GitHub Actions toda segunda e sexta (ver .github/workflows/mapa-moema.yml).
Dados © colaboradores do OpenStreetMap, licença ODbL.

Lugares curados pela W3W (destaques, parceiros, notas do concierge) ficam em mapa/curadoria.json
e têm prioridade sobre os dados automáticos.
"""
import json, os, sys, time, re, unicodedata, urllib.request, urllib.parse, datetime

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


# ---------- Foursquare (opcional, roda só com FSQ_TOKEN) ----------
# ordem importa: do mais específico ao mais genérico; casamento por palavra inteira
FSQ_MAP = [
    (r'ice cream|gelato|frozen yogurt|sorvet', 'sorveterias'),
    (r'pizz', 'pizzarias'),
    (r'steakhouse|churrasc|brazilian steak|barbecue|bbq', 'churrascarias'),
    (r'japanese|sushi|ramen|izakaya|temaki', 'japoneses'),
    (r'burger', 'hamburguerias'),
    (r'barbershop|barber|hair salon|hairdresser|salão de beleza|cabeleireir', 'cabeleireiros'),
    (r'nail salon|manicure|beauty salon|beauty|cosmetic|spa|esthetic|estética|waxing|eyebrow|lash', 'estetica'),
    (r'bakery|padaria|panificadora', 'padarias'),
    (r'dessert|pastry|patisserie|confectioner|candy|chocolate|cake|doceria|brigadeir|donut', 'docerias'),
    (r'coffee|café|cafe|cafeteria|tea room|juice', 'cafes'),
    (r'night ?club|nightlife|dance club|karaoke|lounge', 'noite'),
    (r'cocktail|wine bar|beer bar|beer garden|sports bar|pub|brewery|boteco|\bbar\b|\bbars\b', 'bares'),
    (r'\bpet store|\bpet service|\bpet supplies|\bpet grooming|veterinar|animal shelter|\bpet\b', 'pet'),
    (r'laundry|laundromat|dry clean|lavanderia', 'lavanderias'),
    (r'car wash|lava[- ]?r[aá]pido', 'lavarapido'),
    (r'locksmith|chaveir', 'chaveiros'),
    (r'tailor|seamstress|alteration|costur', 'costureiras'),
    (r'\bbank\b|\batm\b|credit union|banco', 'bancos'),
    (r'pharmacy|drugstore|farm[aá]cia|drogaria', 'farmacias'),
    (r'hospital|clinic|medical|doctor|dentist|dental|physiotherap|physical therap|laborator|diagnostic|health|psycholog|optometrist|chiropract|cl[ií]nica|consult[oó]rio', 'saude'),
    (r'car dealer|auto dealer|dealership|concession[aá]ri', 'concessionarias'),
    (r'auto repair|auto garage|mechanic|tire|car service|oficina', 'oficinas'),
    (r'gas station|fuel|posto', 'postos'),
    (r'university|college|faculdade', 'faculdades'),
    (r'school|preschool|kindergarten|daycare|language school|col[eé]gio|escola', 'escolas'),
    (r'gym|fitness|yoga|pilates|crossfit|martial arts|dance studio|academia', 'academias'),
    (r'\bhotel\b|hostel|\bmotel\b|\binn\b|bed and breakfast|pousada', 'hoteis'),
    (r'\bpark\b|garden|playground|plaza|square|praça', 'parques'),
    (r'museum|art gallery|gallery|theater|theatre|cinema|movie|concert|cultural|library|performing arts|music venue', 'cultura'),
    (r'florist|flower', 'floriculturas'),
    (r'supermarket|grocery|convenience store|market|mercado|hortifruti|butcher|açougue|wine shop|liquor', 'mercados'),
    (r'restaurant|diner|bistro|food court|food truck|steak|seafood|italian|french|arab|lebanese|mexican|peruvian|vegan|vegetarian|brazilian|chinese|thai|korean|indian|portuguese|spanish|mediterranean|poke|salad|sandwich|snack|eatery|cantina|lanchonete|restaurante', 'restaurantes'),
    (r'clothing|shoe|jewelry|boutique|optical|eyewear|bookstore|book store|electronics|furniture|home decor|gift|toy|sporting goods|bicycle|cosmetics store|department store|shopping mall|\bstore\b|\bshop\b|loja', 'lojas'),
]
FSQ_IGNORA = r'office|coworking|residential|apartment|building|condo|parking|bus stop|metro station|train station|government|church|cemetery|real estate|corporate|factory|warehouse|lawyer|accountant|bus line'


def fsq_cat(cats, nome=''):
    t = ' | '.join(cats).lower()
    if re.search(FSQ_IGNORA, t) and not re.search(r'restaurant|bar|caf|store|shop', t):
        return None
    for pat, c in FSQ_MAP:
        if re.search(pat, t): return c
    n = (nome or '').lower()  # nome só ajuda em comida
    for pat, c in FSQ_MAP[:12]:
        if re.search(pat, n): return c
    return None


def fsq_get(url, key):
    tries = [
        (url.replace('{BASE}', 'https://places-api.foursquare.com/places'), {'Authorization': 'Bearer ' + key, 'X-Places-Api-Version': '2025-06-17', 'Accept': 'application/json'}),
        (url.replace('{BASE}', 'https://api.foursquare.com/v3/places'), {'Authorization': key, 'Accept': 'application/json'}),
    ]
    err = None
    for u, h in tries:
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=40) as r:
                return json.load(r), r.headers.get('Link', '')
        except Exception as e:
            err = e
    raise err


def fsq_fetch(key):
    s, w, n, e = BBOX
    out, seen = [], set()
    steps = 4
    for i in range(steps):
        for j in range(steps):
            lat = s + (n - s) * (i + .5) / steps
            lon = w + (e - w) * (j + .5) / steps
            q = urllib.parse.urlencode({'ll': f'{lat:.5f},{lon:.5f}', 'radius': 650, 'limit': 50})
            url = '{BASE}/search?' + q
            for _ in range(6):  # paginação
                try:
                    data, link = fsq_get(url, key)
                except Exception as ex:
                    print('foursquare falhou', ex, file=sys.stderr); break
                for p in data.get('results', []):
                    pid = p.get('fsq_place_id') or p.get('fsq_id')
                    if not pid or pid in seen: continue
                    seen.add(pid)
                    lat2 = p.get('latitude') or (p.get('geocodes', {}).get('main', {}) or {}).get('latitude')
                    lon2 = p.get('longitude') or (p.get('geocodes', {}).get('main', {}) or {}).get('longitude')
                    cats = [c.get('name', '') for c in p.get('categories', [])]
                    cat = fsq_cat(cats, p.get('name', ''))
                    if lat2 is None or not cat: continue
                    loc = p.get('location', {})
                    out.append({'id': 'f' + pid, 'nome': p.get('name'), 'cat': cat, 'lat': round(lat2, 6), 'lon': round(lon2, 6),
                                'horario': '', 'h24': False, 'end': loc.get('address', ''), 'tel': p.get('tel', ''), 'site': p.get('website', ''), 'insta': '', 'fonte': 'fsq'})
                m = re.search(r'<([^>]+)>;\s*rel="next"', link or '')
                if not m: break
                url = m.group(1).replace('https://places-api.foursquare.com/places', '{BASE}').replace('https://api.foursquare.com/v3/places', '{BASE}')
            time.sleep(.3)
    return out


def norm(t):
    t = unicodedata.normalize('NFD', (t or '').lower())
    return re.sub(r'[^a-z0-9]', '', ''.join(c for c in t if unicodedata.category(c) != 'Mn'))


def merge(base, extra):
    """Junta Foursquare ao OpenStreetMap: mesmo nome a menos de ~120 m completa telefone, site e endereço; o resto entra como novo."""
    idx = {}
    for l in base: idx.setdefault(norm(l['nome']), []).append(l)
    novos = 0
    for x in extra:
        hit = None
        for l in idx.get(norm(x['nome']), []):
            if abs(l['lat'] - x['lat']) < .0012 and abs(l['lon'] - x['lon']) < .0012: hit = l; break
        if hit:
            for k in ('tel', 'site', 'end'):
                if not hit.get(k) and x.get(k): hit[k] = x[k]
        else:
            base.append(x); novos += 1
    return novos


# ---------- horários no site do próprio estabelecimento ----------
DIAS = {'seg': 'Mo', 'segunda': 'Mo', 'ter': 'Tu', 'terça': 'Tu', 'terca': 'Tu', 'qua': 'We', 'quarta': 'We', 'qui': 'Th', 'quinta': 'Th',
        'sex': 'Fr', 'sexta': 'Fr', 'sáb': 'Sa', 'sab': 'Sa', 'sábado': 'Sa', 'sabado': 'Sa', 'dom': 'Su', 'domingo': 'Su'}
EN = {'monday': 'Mo', 'tuesday': 'Tu', 'wednesday': 'We', 'thursday': 'Th', 'friday': 'Fr', 'saturday': 'Sa', 'sunday': 'Su'}
D = r'(segunda|terça|terca|quarta|quinta|sexta|sábado|sabado|domingo|seg|ter|qua|qui|sex|sáb|sab|dom)(?:-feira)?\.?'
H = r'(\d{1,2})\s*(?:h|:)\s*(\d{2})?'
RX = re.compile(D + r'(?:\s*(?:a|à|até|-|–)\s*' + D + r')?\s*[:\-–,]?\s*(?:das\s*)?' + H + r'\s*(?:h)?\s*(?:às|as|a|até|-|–)\s*' + H, re.I)


def hh(h, m): return f"{int(h) % 24:02d}:{int(m or 0):02d}"


def horario_jsonld(html):
    for blk in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html, re.S | re.I):
        try: data = json.loads(blk.strip())
        except Exception: continue
        stack = data if isinstance(data, list) else [data]
        while stack:
            o = stack.pop()
            if isinstance(o, list): stack += o; continue
            if not isinstance(o, dict): continue
            stack += [v for v in o.values() if isinstance(v, (dict, list))]
            oh = o.get('openingHours')
            if isinstance(oh, list): oh = '; '.join(oh)
            if isinstance(oh, str) and re.search(r'\d{1,2}:\d{2}', oh): return oh.strip()
            sp = o.get('openingHoursSpecification')
            if sp:
                sp = sp if isinstance(sp, list) else [sp]
                parts = []
                for x in sp:
                    ds = x.get('dayOfWeek', [])
                    ds = ds if isinstance(ds, list) else [ds]
                    ds = [EN.get(str(d).split('/')[-1].lower()) for d in ds]
                    ds = [d for d in ds if d]
                    if ds and x.get('opens') and x.get('closes'):
                        parts.append(f"{','.join(ds)} {x['opens'][:5]}-{x['closes'][:5]}")
                if parts: return '; '.join(parts)
    return ''


def horario_texto(html):
    txt = re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', html, flags=re.S | re.I))
    txt = re.sub(r'\s+', ' ', txt)
    regras = []
    for m in RX.finditer(txt):
        d1, d2, h1, m1, h2, m2 = m.groups()
        a, b = DIAS.get(d1.lower().rstrip('.')), DIAS.get((d2 or '').lower().rstrip('.'))
        if not a: continue
        dia = f'{a}-{b}' if b else a
        r = f'{dia} {hh(h1, m1)}-{hh(h2, m2)}'
        if r not in regras: regras.append(r)
        if len(regras) >= 6: break
    return '; '.join(regras)


def abrir(url):
    """Testa variações do endereço (https/http, com e sem www). Devolve (url que abre, html) ou ('', '')."""
    u = re.sub(r'^https?://', '', url.strip()).rstrip('/')
    if not u: return '', ''
    host, _, path = u.partition('/')
    hosts = [host] + ([host[4:]] if host.startswith('www.') else ['www.' + host])
    for h in hosts:
        for sch in ('https://', 'http://'):
            cand = sch + h + ('/' + path if path else '')
            try:
                req = urllib.request.Request(cand, headers={'User-Agent': 'Mozilla/5.0 (compatible; ' + UA + ')', 'Accept': 'text/html'})
                with urllib.request.urlopen(req, timeout=8) as r:
                    if r.status >= 400: continue
                    ct = r.headers.get('Content-Type') or ''
                    html = r.read(600_000).decode('utf-8', 'ignore') if 'html' in ct else ''
                    return cand, html
            except urllib.error.HTTPError as e:
                if e.code in (401, 403, 405, 429): return cand, ''  # existe, só bloqueia robôs
            except Exception:
                continue
    return '', ''


def horario_site(url):
    ok, html = abrir(url)
    if not ok: return None, ''
    if not html or re.search(r'instagram|facebook|ifood|linktr', ok): return ok, ''
    return ok, horario_jsonld(html) or horario_texto(html)


ENFULL = {'monday': 'Mo', 'tuesday': 'Tu', 'wednesday': 'We', 'thursday': 'Th', 'friday': 'Fr', 'saturday': 'Sa', 'sunday': 'Su'}


def normaliza_horario(h):
    if not h: return ''
    h = h.strip()
    for k, v in ENFULL.items(): h = re.sub(k, v, h, flags=re.I)
    h = re.sub(r'(\d{1,2}:\d{2})\s*[-–]\s*(\d{1,2}:\d{2})', r'\1-\2', h)
    if re.fullmatch(r'00:00-23:59|00:00-24:00', h): h = '24/7'
    return h


def completar_horarios(locais):
    from concurrent.futures import ThreadPoolExecutor
    alvo = [l for l in locais if l.get('site')]
    mortos = [0]
    def job(l):
        if re.search(r'wa\.me|whatsapp', l['site']): return False
        ok, h = horario_site(l['site'])
        if ok is None:
            l['site'] = ''; mortos[0] += 1; return False  # site fora do ar: some o botão
        l['site'] = ok
        if h and not l.get('horario'):
            l['horario'] = h; l['h24'] = h.strip() == '24/7'; l['fonte_horario'] = 'site'; return True
        return False
    with ThreadPoolExecutor(24) as ex:
        n = sum(ex.map(job, alvo))
    # site de rede (mesmo domínio em 3+ lugares) costuma mostrar horário de escritório: descarta
    import collections
    dom = lambda u: re.sub(r'^https?://(www\.)?', '', u or '').split('/')[0]
    cont = collections.Counter(dom(l.get('site')) for l in locais if l.get('site'))
    for l in locais:
        if l.get('fonte_horario') == 'site' and cont[dom(l.get('site'))] >= 3:
            l['horario'] = ''; l['h24'] = False; l.pop('fonte_horario', None); n -= 1
    for l in locais:
        l['horario'] = normaliza_horario(l.get('horario')); l['h24'] = l['horario'] == '24/7'
    print('sites testados:', len(alvo), '| fora do ar removidos:', mortos[0], '| horários achados:', n)


# ---------- limpeza de duplicados ----------
STOP = {'restaurante', 'restaurant', 'parrillada', 'parrilla', 'unidade', 'moema', 'morma', 'loja', 'sp', 'sao', 'paulo', 'shopping', 'ibirapuera', 'filial', 'the', 'o', 'a', 'de', 'da', 'do', 'e', 'bar', 'cafe', 'cafeteria', 'pizzaria', 'lanchonete'}
GENERICAS = {'lojas', 'restaurantes', 'cultura', 'saude', 'mercados'}


def chave(nome):
    t = unicodedata.normalize('NFD', (nome or '').lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    toks = [w for w in re.split(r'[^a-z0-9]+', t) if w and w not in STOP]
    return ' '.join(toks)


def nota(l):
    return (4 if l.get('horario') else 0) + (1 if l.get('tel') else 0) + (1 if l.get('site') else 0) + (1 if l.get('end') else 0) + (3 if l.get('destaque') else 0)


def parecidos(a, b):
    ka, kb = chave(a['nome']), chave(b['nome'])
    if not ka or not kb: return False
    if ka == kb: return True
    if min(len(ka), len(kb)) >= 5 and (ka in kb or kb in ka): return True
    from difflib import SequenceMatcher
    return SequenceMatcher(None, ka, kb).ratio() >= .88


def deduplicar(locais):
    """Mesmo lugar (nome parecido a menos de ~150 m): fica o registro mais completo, de preferência o que tem horário."""
    locais.sort(key=nota, reverse=True)
    fic = []
    for l in locais:
        par = None
        for k in fic:
            if abs(k['lat'] - l['lat']) < .0014 and abs(k['lon'] - l['lon']) < .0014 and parecidos(k, l):
                par = k; break
        if par:
            for f in ('horario', 'tel', 'site', 'end', 'insta'):
                if not par.get(f) and l.get(f): par[f] = l[f]
            if par['cat'] in GENERICAS and l['cat'] not in GENERICAS: par['cat'] = l['cat']
            if len(chave(l['nome'])) and len(l['nome']) < len(par['nome']) and chave(l['nome']) in chave(par['nome']): par['nome'] = l['nome']
            par['h24'] = (par.get('horario') or '').strip() == '24/7'
        else:
            fic.append(l)
    # mesma marca, mesma categoria
    import collections
    marcas = collections.defaultdict(list)
    for l in fic: marcas[chave(l['nome'])].append(l)
    for k, ls in marcas.items():
        if len(ls) > 1 and k:
            cat = collections.Counter(x['cat'] for x in ls).most_common(1)[0][0]
            for x in ls: x['cat'] = cat
    print('duplicados removidos:', len(locais) - len(fic))
    return fic


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
    key = os.environ.get('FSQ_TOKEN')
    if key:
        try:
            extra = fsq_fetch(key)
            print('foursquare', len(extra), 'lugares;', merge(locais, extra), 'novos')
        except Exception as ex:
            print('foursquare indisponível', ex, file=sys.stderr)
    completar_horarios(locais)
    locais = deduplicar(locais)
    if os.path.exists(CUR):  # curadoria W3W tem prioridade
        cur = json.load(open(CUR, encoding='utf-8'))
        porid = {c['id']: c for c in cur if c.get('id')}
        for l in locais:
            if l['id'] in porid: l.update(porid.pop(l['id']))
        locais += [c for c in porid.values() if c.get('lat')]
        locais += [c for c in cur if not c.get('id') and c.get('lat')]
    locais.sort(key=lambda l: (not l.get('destaque'), l['cat'], l['nome']))
    # lista de trabalho da curadoria: lugares sem horário que têm telefone ou site
    pri = ['restaurantes','pizzarias','churrascarias','japoneses','hamburguerias','bares','cafes','docerias','sorveterias','padarias','farmacias','mercados','pet','lavanderias','chaveiros','cabeleireiros','estetica']
    pend = [l for l in locais if not l.get('horario') and (l.get('tel') or l.get('site'))]
    pend.sort(key=lambda l: (pri.index(l['cat']) if l['cat'] in pri else 99, l['nome'].lower()))
    import csv
    with open(os.path.join(ROOT, 'mapa', 'pendencias_horario.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['id', 'nome', 'categoria', 'endereco', 'telefone', 'site', 'horario_confirmado', 'nota_w3w'])
        for l in pend: w.writerow([l['id'], l['nome'], l['cat'], l.get('end', ''), l.get('tel', ''), l.get('site', ''), '', ''])
    out = {'atualizado': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).isoformat(timespec='minutes'),
           'fonte': '© colaboradores do OpenStreetMap' + (' · Foursquare' if os.environ.get('FSQ_TOKEN') else ''), 'total': len(locais), 'locais': locais}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('ok', len(locais), 'lugares')


if __name__ == '__main__':
    main()
