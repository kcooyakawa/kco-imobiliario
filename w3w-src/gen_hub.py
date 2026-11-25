"""Gera hub-w3w/produtos.js a partir de empreendimentos.json.
Rode: python3 gen_hub.py (depois de editar o JSON)."""
import json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, '..', 'hub-w3w', 'produtos.js')
SITE = 'https://kcooyakawa.github.io/kco-imobiliario/w3w'

E = json.load(open(os.path.join(ROOT, 'empreendimentos.json'), encoding='utf-8'))
E = [e for e in E if not e['slug'].startswith('on-') and not e.get('esgotado')]


def nums(t):
    return [float(x.replace('.', '').replace(',', '.')) for x in re.findall(r'\d[\d.]*(?:,\d+)?', t or '')]


def cats(e):
    pl = (e.get('ficha') or {}).get('plantas') or []
    st = [r for r in pl if 'studio' in (r[0] + ' ' + r[2]).lower()]
    ap = [r for r in pl if r not in st]
    if not pl:
        return e['categorias']
    c = []
    if ap:
        ns = [n for r in ap for n in nums(r[1])]
        c.append('alto-padrao' if ns and min(ns) >= 145 else 'apartamentos')
    if st:
        c.append('studios')
    return c


out = []
for e in E:
    f = e.get('ficha') or {}
    I = f.get('img') or {}
    imgs = []
    for k, lab in (('capa', 'Capa'), ('fachada', 'Fachada'), ('conceito', 'Conceito'), ('voo', 'Lazer'), ('terraco', 'Terraço')):
        if I.get(k):
            imgs.append([I[k], I.get(k + '_cap', lab)])
    for k in ('par', 'lazer'):
        for src, cap in I.get(k) or []:
            imgs.append([src, cap])
    if not imgs:
        imgs.append([e['img'], 'Fachada'])
    out.append({
        'id': e['slug'], 'nome': e['nome'], 'bairro': e['bairro'], 'status': e['status'],
        'cat': cats(e), 'resumo': e['resumo'], 'frase': e.get('frase', ''),
        'img': I.get('capa') or e['img'], 'url': f"{SITE}/empreendimentos/{e['slug']}/",
        'tagline': f.get('tagline', ''), 'conceito': f.get('conceito', ''),
        'endereco': f.get('endereco', ''), 'entrega': f.get('entrega', ''),
        'assinaturas': f.get('assinaturas', []), 'destaques': f.get('destaques', []),
        'plantas': f.get('plantas', []), 'lazer': f.get('lazer', []), 'local': f.get('local', []),
        'tecnica': f.get('tecnica', []), 'imgs': imgs,
    })

ordem = {'moema': 0}
out.sort(key=lambda p: (p['bairro'] != 'Moema', p['nome']))
with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write('/* gerado por w3w-src/gen_hub.py a partir de empreendimentos.json; não editar à mão */\n')
    fh.write('const W3W=' + json.dumps(out, ensure_ascii=False) + ';\n')
print('ok', len(out), 'produtos ->', OUT)
