"""Índice /moema/ — layout editorial com fotos, ícones e grupos."""
import html
def esc(s): return html.escape(str(s or ''), quote=True)

P = {  # ícones de traço, viewBox 24
 'restaurantes':'M7 3v8M5 3v5a2 2 0 0 0 4 0V3M7 11v10M17 3c-2 2-3 4-3 7h3v11',
 'pizzarias':'M12 3 3 19c6 2.5 12 2.5 18 0L12 3zM10 11h.01M14 14h.01M9 16h.01',
 'churrascarias':'M4 10h16l-2 6H6l-2-6zM12 16v4M8 20h8M9 7c0-2 2-2 2-4M14 7c0-2 2-2 2-4',
 'japoneses':'M4 14h16a8 8 0 0 1-16 0zM14 4l-4 8M19 5l-7 7',
 'hamburguerias':'M4 11a8 6 0 0 1 16 0H4zM4 14h16M5 17h14a2 2 0 0 1-2 3H7a2 2 0 0 1-2-3z',
 'bares':'M5 4h14l-7 8-7-8zM12 12v8M8 20h8',
 'noite':'M20 14A8 8 0 1 1 10 4a6 6 0 0 0 10 10z',
 'cafes':'M4 9h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5V9zM17 10h2a2 2 0 0 1 0 4h-2M8 3v3M12 3v3',
 'docerias':'M4 12h16v8H4zM4 15h16M12 12V8M10 6a2 2 0 0 1 4 0c0 1-2 2-2 2s-2-1-2-2z',
 'sorveterias':'M8 10a4 4 0 0 1 8 0M7 10h10l-5 11-5-11z',
 'padarias':'M5 15c-2-4 1-9 7-9s9 5 7 9H5zM9 9l1 5M12 8v6M15 9l-1 5',
 'mercados':'M3 4h3l2 11h11l2-8H7M9 20h.01M18 20h.01',
 'pet':'M8 8h.01M16 8h.01M5 13h.01M19 13h.01M12 12c-3 0-5 3-5 5a2 2 0 0 0 3 2c1-.5 3-.5 4 0a2 2 0 0 0 3-2c0-2-2-5-5-5z',
 'farmacias':'M10 4h4v6h6v4h-6v6h-4v-6H4v-4h6z',
 'saude':'M12 20s-8-5-8-11a4 4 0 0 1 8-1 4 4 0 0 1 8 1c0 6-8 11-8 11z',
 'parques':'M12 3 6 13h12L12 3zM12 13v8M8 21h8',
 'cultura':'M3 9 12 4l9 5M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18',
 'academias':'M6 8v8M18 8v8M3 10v4M21 10v4M6 12h12',
 'escolas':'M2 9l10-5 10 5-10 5L2 9zM6 11v5c3 2 9 2 12 0v-5',
 'faculdades':'M2 9l10-5 10 5-10 5L2 9zM22 9v6',
 'hoteis':'M3 20V6M3 13h18v7M7 13V9h6v4M21 20v-7',
 'estetica':'M12 3c2 3 2 6 0 9-2-3-2-6 0-9zM5 9c3 0 5 2 7 5-3 0-5-2-7-5zM19 9c-3 0-5 2-7 5 3 0 5-2 7-5zM12 14v7',
 'cabeleireiros':'M6 6a2 2 0 1 0 0 .01M6 18a2 2 0 1 0 0 .01M8 7l12 10M8 17 20 7',
 'concessionarias':'M5 16l1.5-5h11l1.5 5M4 16h16v3H4zM7 19v2M17 19v2',
 'oficinas':'M14 6a4 4 0 0 0-5 5l-6 6 2 2 6-6a4 4 0 0 0 5-5l-2 2-2-2 2-2z',
 'postos':'M5 20V5h8v15M3 20h12M13 9h3l2 2v6a1 1 0 0 0 2 0V8',
}
GR = [('Comer bem', 'gastronomia', ['restaurantes','pizzarias','japoneses','churrascarias','hamburguerias','padarias','cafes','docerias','sorveterias']),
      ('A noite', 'noite', ['bares','noite']),
      ('Viver o bairro', 'vida', ['parques','cultura','academias','hoteis']),
      ('Dia a dia', 'servicos', ['mercados','farmacias','saude','pet','estetica','cabeleireiros','escolas','faculdades','concessionarias','oficinas','postos'])]
FOTO_EXTRA = {"churrascarias": "moema/locais/gm-29b554724b.jpg", "hamburguerias": "moema/locais/k-chico1.jpg", "cafes": "moema/locais/k-cafe.jpg", "docerias": "moema/locais/gm-5e5dcc50f4.jpg", "bares": "moema/locais/gm-5654ef8c06.jpg", "noite": "moema/locais/gm-89cc7cf948.jpg", "restaurantes": "moema/locais/gm-c71d70184b.jpg", "sorveterias": "moema/locais/k-gelato.jpg", "padarias": "moema/locais/boston-2.jpg", "concessionarias": "moema/u-concessionarias.jpg", "hoteis": "moema/u-hoteis.jpg", "cabeleireiros": "moema/u-cabeleireiros.jpg", "mercados": "moema/u-mercados.jpg", "estetica": "moema/u-estetica.jpg", "faculdades": "moema/u-faculdades.jpg", "academias": "moema/u-academias.jpg", "pet": "moema/u-pet.jpg", "oficinas": "moema/u-oficinas.jpg", "escolas": "moema/u-escolas.jpg", "postos": "moema/u-postos.jpg", "saude": "moema/u-saude.jpg", "farmacias": "moema/u-farmacias.jpg"}
FOTO = {'pizzarias':'moema/pizzarias.jpg','japoneses':'moema/japoneses.jpg','padarias':'moema/padarias.jpg','parques':'guia/alameda-parque.jpg','cultura':'guia/auditorio-ibirapuera.jpg'}
import os as _o
for _c in ('academias','hoteis','mercados','farmacias','cabeleireiros','pet','escolas','concessionarias','estetica','faculdades','oficinas','postos','saude'):
    if _o.path.exists(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),'..','w3w-img','moema',_c+'.jpg')): FOTO.setdefault(_c,'moema/'+_c+'.jpg')
FOTO.update(FOTO_EXTRA)

def ico(k): return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{P.get(k, "M12 4v16M4 12h16")}"/></svg>'

CSS = r'''<style>
body:has(.mx){background:#fff}
.mx{--ink:#111316;--ink2:#5A616D;--pp:#fff;--g1:#F1F3F6;--ac:#1F4FA0;--ln:#E5E9EF;--e:cubic-bezier(.16,1,.3,1);background:#fff;color:var(--ink);overflow:clip;font-family:var(--sans,sans-serif)}
.mx .in{width:calc(100% - clamp(32px,5vw,96px));max-width:1600px;margin:0 auto}
.mx h1,.mx h2,.mx h3{font-family:var(--sans,sans-serif);font-weight:300;margin:0}
.mx-h{padding:clamp(110px,11vw,150px) 0 0}
.mx-ey{display:flex;gap:10px;font-size:14px;color:var(--ink2)}.mx-ey a{color:inherit}
.mx h1{font-size:clamp(76px,13vw,230px);line-height:.9;letter-spacing:-.035em;margin-top:18px;overflow:hidden}
.mx h1 span{display:inline-block;animation:mxu 1.3s var(--e) both}
@keyframes mxu{from{transform:translateY(100%)}}
.mx-hg{display:grid;grid-template-columns:5fr 7fr;gap:clamp(24px,4vw,72px);margin-top:clamp(28px,3vw,48px);align-items:end}
.mx-lead{font-size:clamp(18px,1.4vw,21px);line-height:1.75;max-width:40ch;margin:0;animation:mxf 1.1s .3s var(--e) both}
@keyframes mxf{from{opacity:0;transform:translateY(22px)}}
.mx-nums{display:flex;gap:clamp(24px,4vw,60px);align-items:flex-end;flex-wrap:wrap;animation:mxf 1.1s .45s var(--e) both}
.mx-nums b{display:block;font-size:clamp(40px,4vw,60px);font-weight:300;letter-spacing:-.03em;line-height:1}
.mx-nums small{font-size:14px;color:var(--ink2)}
.mx-nums a{margin-left:auto;background:var(--ink);color:#fff;text-decoration:none;padding:17px 26px;font-size:15px;font-weight:500;transition:transform .35s var(--e)}.mx-nums a:hover{transform:translateY(-3px)}
.mx-bd{position:relative;height:clamp(380px,70vh,800px);margin-top:clamp(40px,5vw,80px);overflow:hidden;background:var(--g1)}
.mx-bd img{position:absolute;inset:-6% 0;width:100%;height:112%;object-fit:cover;animation:mxz 2.2s var(--e) both}
@keyframes mxz{from{transform:scale(1.15);opacity:0}}
.mx-gr{padding:clamp(150px,16vw,260px) 0 0}
.mx-gh{margin-bottom:clamp(40px,5vw,72px);display:flex;justify-content:space-between;align-items:flex-end;gap:20px}
.mx-gh h2{font-size:clamp(52px,7vw,118px);line-height:1;letter-spacing:-.03em}
.mx-gh small{font-size:15px;color:var(--ink2)}
.mx-fe{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px;margin-bottom:12px}
.mx-ph{position:relative;aspect-ratio:4/5;overflow:hidden;color:#fff;text-decoration:none;isolation:isolate}
.mx-ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;transition:transform 1.4s var(--e)}
.mx-ph::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,transparent 50%,rgba(10,10,12,.7))}
.mx-ph:hover img{transform:scale(1.05)}
.mx-ph .top{position:absolute;top:18px;left:18px}.mx-ph .top small{display:none}
.mx-ph svg{width:24px;height:24px}
.mx-ph h3{position:absolute;left:22px;right:22px;bottom:20px;font-size:clamp(32px,2.8vw,44px);letter-spacing:-.025em;display:flex;justify-content:space-between;align-items:flex-end}
.mx-ph h3 i{font-style:normal;font-size:20px;opacity:0;transform:translateX(-6px);transition:all .5s var(--e)}.mx-ph:hover h3 i{opacity:1;transform:none}
.mx-ic{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:4px}
.mx-ic a{display:flex;flex-direction:column;gap:40px;padding:24px;background:var(--g1);color:var(--ink);text-decoration:none;transition:background .4s var(--e),color .4s}
.mx-ic a:hover{background:var(--ink);color:#fff}
.mx-ic .r{display:flex;justify-content:space-between}
.mx-ic svg{width:30px;height:30px;transition:transform .6s var(--e)}.mx-ic a:hover svg{transform:rotate(-8deg) scale(1.1)}
.mx svg path{fill:none;stroke:currentColor;stroke-width:1.3;stroke-linecap:round;stroke-linejoin:round}
.mx-ic small{font-size:14px;opacity:.6}
.mx-ic b{font-size:23px;font-weight:300;letter-spacing:-.015em}
.mx-rv{opacity:0;transform:translateY(28px);transition:opacity 1s var(--e),transform 1s var(--e)}.mx-rv.on{opacity:1;transform:none}
.mx-end{margin:clamp(150px,16vw,260px) 0 clamp(80px,9vw,140px);display:grid;grid-template-columns:1fr auto;gap:30px;align-items:end}
.mx-end h2{font-size:clamp(52px,7vw,118px);line-height:1;letter-spacing:-.03em}
.mx-end a{background:var(--ac);color:#fff;text-decoration:none;padding:20px 30px;font-size:16px;font-weight:500}
@media(max-width:860px){.mx-fe{grid-template-columns:1fr 1fr;gap:8px}.mx-ph h3{font-size:22px;left:14px;bottom:12px}.mx-hg,.mx-end{grid-template-columns:1fr}.mx-gh{flex-direction:column;align-items:flex-start}.mx-nums a{margin-left:0}.mx-ic{grid-template-columns:1fr 1fr}.mx-ic a{gap:26px;padding:18px}}
@media(prefers-reduced-motion:reduce){.mx *{animation:none!important;transition:none!important}.mx-rv{opacity:1;transform:none}}
</style>'''
JS = '''<script>(()=>{const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});document.querySelectorAll('.mx-rv').forEach((el,i)=>{el.style.transitionDelay=(el.dataset.d||0)+'ms';io.observe(el)})})()</script>'''

def render(L, cs, u, wa, img_base):
    n = dict((c[0], (c, k)) for c, k in cs)
    out = ''
    for gi, (tit, slug, ks) in enumerate(GR):
        ks = [k for k in ks if k in n]
        if not ks: continue
        fe = [k for k in ks if k in FOTO]; ic = [k for k in ks if k not in FOTO]
        a, b = tit.split(' ', 1)
        out += f'<section class="mx-gr"><div class="in"><div class="mx-gh mx-rv"><h2>{esc(tit)}</h2><small>{sum(n[k][1] for k in ks)} lugares</small></div>'
        if fe:
            out += '<div class="mx-fe">' + ''.join(f'<a class="mx-ph mx-rv" data-d="{i*90}" href="{u("moema/"+k)}"><img src="{img_base}{FOTO[k]}" alt="{esc(n[k][0][1])} em Moema" loading="lazy"><div class="top">{ico(k)}<small>Seleção W3W</small></div><h3>{esc(n[k][0][1])}<i>→</i></h3></a>' for i, k in enumerate(fe)) + '</div>'
        if ic:
            out += '<div class="mx-ic mx-rv">' + ''.join(f'<a href="{u("moema/"+k)}"><div class="r">{ico(k)}<small>{n[k][1]:02d}</small></div><b>{esc(n[k][0][1])}</b></a>' for k in ic) + '</div>'
        out += '</div></section>'
    return (CSS + '<main class="mx">'
        f'<section class="mx-h"><div class="in"><nav class="mx-ey"><a href="{u("guia-moema")}">Guia Moema</a><span>/</span><span>Moema por categoria</span></nav>'
        f'<h1><span>Moema, de perto</span></h1><div class="mx-hg"><p class="mx-lead">Onde comer, tomar um café, passear e resolver a vida no bairro. Cada lugar mapeado, e os melhores escolhidos pela W3W.</p>'
        f'<div class="mx-nums"><div><b>{len(L)}</b><small>lugares</small></div><div><b>{len(cs)}</b><small>categorias</small></div><a href="{u("mapa-moema")}">Abrir o mapa</a></div></div></div>'
        f'<div class="mx-bd"><img src="{img_base}guia/avenida-arborizada.jpg" alt="Avenida arborizada em Moema, fim de tarde"></div>'
        f'</section>{out}'
        f'<div class="in"><div class="mx-end mx-rv"><h2>Gostou do bairro? Venha morar nele.</h2><a href="{wa}" target="_blank" rel="noopener">Fale com a W3W</a></div></div></main>' + JS)


# ---------- página de cada categoria ----------
import json as _json, os as _os
try: FOTOS = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'locais_fotos.json')))
except Exception: FOTOS = {}
LB = 'moema/locais/'

CSS2 = r'''<style>
.mx-h2{min-height:min(92svh,860px)}
.mx-h2 .in{padding-bottom:50px}
.mx-ft{padding:clamp(80px,10vw,140px) 0 0}
.mx-it{display:grid;grid-template-columns:1.25fr 1fr;gap:clamp(30px,5vw,90px);align-items:center;margin-bottom:clamp(70px,9vw,130px)}
.mx-it:nth-child(even){grid-template-columns:1fr 1.25fr}.mx-it:nth-child(even) .mx-ig{order:2}
.mx-ig{position:relative;aspect-ratio:5/4;overflow:hidden;border-radius:4px;background:#1c1f25}
.mx-ig img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transform:scale(1.12);transition:transform 1.8s var(--e),opacity 1s var(--e)}
.mx-it.on .mx-ig img{transform:scale(1)}
.mx-ig img+img{opacity:0}.mx-ig:hover img+img{opacity:1}
.mx-ig .nn{position:absolute;left:18px;bottom:12px;color:#fff;font:200 clamp(70px,8vw,120px)/1 var(--serif,serif);font-style:italic;text-shadow:0 10px 40px rgba(0,0,0,.4)}
.mx-ig.no{display:grid;place-items:center;color:rgba(255,255,255,.12)}
.mx-ig.no svg{width:40%;height:40%}
.mx-tx .tg{font:500 10.5px var(--mono,monospace);letter-spacing:.18em;text-transform:uppercase;color:var(--ac)}
.mx-tx h3{margin:16px 0 18px;font:200 clamp(44px,5vw,78px)/.92 var(--sans,sans-serif);letter-spacing:-.05em}
.mx-tx p{margin:0 0 6px;color:var(--ink2);font-size:16px;line-height:1.55;max-width:42ch}
.mx-tx .hr{margin-top:18px;padding-top:16px;border-top:1px solid var(--ln);font:12px/1.7 var(--mono,monospace);color:var(--ink2)}
.mx-tx .ac{display:flex;gap:10px;margin-top:26px;flex-wrap:wrap}
.mx-tx .ac a{text-decoration:none;font:500 14px var(--sans,sans-serif);padding:14px 22px;border-radius:999px;border:1px solid var(--ink);color:var(--ink);transition:background .3s,color .3s}
.mx-tx .ac a:first-child,.mx-tx .ac a:hover{background:var(--ink);color:#fff}
.mx-ls{border-top:1px solid var(--ink)}
.mx-ls a{display:grid;grid-template-columns:56px 1.3fr 1.4fr 1fr 30px;gap:16px;align-items:center;padding:20px 4px;border-bottom:1px solid var(--ln);color:var(--ink);text-decoration:none;position:relative;transition:padding .5s var(--e)}
.mx-ls a::before{content:"";position:absolute;left:0;top:0;bottom:0;width:0;background:var(--ink);transition:width .6s var(--e);z-index:0}
.mx-ls a:hover{color:#fff;padding-left:18px}.mx-ls a:hover::before{width:100%}
.mx-ls a>*{position:relative;z-index:1}
.mx-ls .i{font:11px var(--mono,monospace);color:var(--ink2)}.mx-ls a:hover .i,.mx-ls a:hover .s{color:rgba(255,255,255,.65)}
.mx-ls b{font:300 22px/1.15 var(--sans,sans-serif);letter-spacing:-.02em}
.mx-ls .s{font-size:14px;color:var(--ink2)}
.mx-ls .ar{font-size:20px;transform:translateX(-8px);opacity:0;transition:all .5s var(--e)}.mx-ls a:hover .ar{transform:none;opacity:1}
.mx-q{width:100%;height:58px;border:0;border-bottom:1px solid var(--ink);background:transparent;font:300 24px var(--sans,sans-serif);letter-spacing:-.02em;color:var(--ink);margin-bottom:10px;outline:0}
.mx-ot{display:flex;flex-wrap:wrap;gap:10px}
.mx-ot a{display:inline-flex;gap:10px;align-items:center;padding:12px 18px;border:1px solid var(--ln);border-radius:999px;color:var(--ink);text-decoration:none;font:400 15px var(--sans,sans-serif);transition:all .3s}
.mx-ot a svg{width:18px;height:18px;color:var(--ac)}.mx-ot a:hover{background:var(--ink);color:#fff}.mx-ot a:hover svg{color:#fff}
@media(max-width:800px){.mx-it,.mx-it:nth-child(even){grid-template-columns:1fr}.mx-it:nth-child(even) .mx-ig{order:0}.mx-ls a{grid-template-columns:40px 1fr 24px}.mx-ls .s{display:none}}
</style>'''

PT = {'Mo':'Seg','Tu':'Ter','We':'Qua','Th':'Qui','Fr':'Sex','Sa':'Sáb','Su':'Dom','PH':'Feriados'}
def hum(h):
    if not h: return ''
    if h.strip()=='24/7': return 'Aberto 24 horas'
    for k,v in PT.items(): h=h.replace(k,v)
    return h.replace(';',' ·')

def render_cat(cat, L, cs, u, wa, img_base, titulo, intro, ld):
    key, label = cat[0], cat[1]
    it = [l for l in L if l['cat']==key]
    ind = sorted([l for l in it if l.get('destaque')], key=lambda l: (not FOTOS.get(l['nome']), l['nome']))
    resto = sorted([l for l in it if not l.get('destaque')], key=lambda l: l['nome'].lower())
    hero = FOTO.get(key) or next((LB+FOTOS[l['nome']][0]+'.jpg' for l in ind if FOTOS.get(l['nome'])), None) or 'guia/skyline-ibirapuera.jpg'
    def gm(l): return f'https://www.google.com/maps/dir/?api=1&destination={l["lat"]},{l["lon"]}'
    fe = ''
    sem = [l for l in ind if not FOTOS.get(l['nome'])]
    for i, l in enumerate([l for l in ind if FOTOS.get(l['nome'])]):
        fs = FOTOS.get(l['nome'], [])
        ig = (f'<div class="mx-ig">' + ''.join(f'<img src="{img_base}{LB}{f}.jpg" alt="{esc(l["nome"])}, Moema" loading="lazy">' for f in fs[:2]) + f'<span class="nn">{i+1:02d}</span></div>') if fs else f'<div class="mx-ig no">{ico(key)}<span class="nn">{i+1:02d}</span></div>'
        ac = f'<a href="{gm(l)}" target="_blank" rel="noopener">Como chegar</a>' + (f'<a href="{esc(l["site"])}" target="_blank" rel="noopener nofollow">Site</a>' if l.get('site') else '') + (f'<a href="tel:{esc("".join(c for c in l["tel"] if c.isdigit() or c=="+"))}">Ligar</a>' if l.get('tel') else '')
        h = hum(l.get('horario'))
        fe += (f'<article class="mx-it mx-rv">{ig}<div class="mx-tx"><span class="tg">W3W indica · {esc(label)}</span><h3>{esc(l["nome"])}</h3>'
               + (f'<p>{esc(l["nota"])}</p>' if l.get('nota') else '') + f'<p>{esc(l.get("end") or "Moema, São Paulo")}</p>'
               + (f'<div class="hr">{esc(h)}</div>' if h else '') + f'<div class="ac">{ac}</div></div></article>')
    if sem:
        fe += ('<div class="mx-gh mx-rv" style="margin-top:10px"><span class="n">+</span><h2 style="font-size:clamp(30px,3.4vw,48px)">Também <em>indicamos.</em></h2><small>' + str(len(sem)) + ' lugares</small></div><div class="mx-ic mx-rv">'
               + ''.join(f'<a href="{gm(l)}" target="_blank" rel="noopener"><div class="r">{ico(key)}<small>W3W</small></div><b>{esc(l["nome"])}</b><small>{esc(l.get("end") or "Moema")}</small></a>' for l in sem) + '</div>')
    ls = ''.join(f'<a href="{gm(l)}" target="_blank" rel="noopener"><span class="i">{i+1:03d}</span><b>{esc(l["nome"])}</b><span class="s">{esc(l.get("end") or "Moema")}</span><span class="s">{esc(hum(l.get("horario"))[:34])}</span><span class="ar">→</span></a>' for i, l in enumerate(resto))
    ot = ''.join(f'<a href="{u("moema/"+c[0])}">{ico(c[0])}{esc(c[1])}</a>' for c, n in cs if c[0]!=key)
    a, b = (titulo.rsplit(' em ', 1) + [''])[:2] if ' em ' in titulo else (label, 'Moema')
    return (CSS + CSS2 + f'<script type="application/ld+json">{_json.dumps(ld, ensure_ascii=False)}</script><main class="mx">'
        f'<section class="mx-h mx-h2"><img src="{img_base}{hero}" alt="{esc(label)} em Moema"><div class="in">'
        f'<nav class="mx-ey"><a href="{u("guia-moema")}">Guia Moema</a><span>/</span><a href="{u("moema")}">Moema por categoria</a><span>/</span><span>{esc(label)}</span></nav>'
        f'<h1><span><i>{esc(label)}</i></span><span><i><em>em Moema.</em></i></span></h1><p class="mx-lead">{esc(intro)}</p>'
        f'<div class="mx-nums"><div><b>{len(it)}</b><small>lugares</small></div>' + (f'<div><b>{len(ind)}</b><small>W3W indica</small></div>' if ind else '') + f'<div><b>2×</b><small>atualizado por semana</small></div><a href="{u("mapa-moema")}?cat={key}">Ver no mapa →</a></div></div></section>'
        + (f'<section class="mx-ft"><div class="in"><div class="mx-gh mx-rv"><span class="n">01</span><h2>A W3W <em>indica.</em></h2><small>{len(ind)} escolhidos</small></div>{fe}</div></section>' if ind else '')
        + f'<section class="mx-gr" id="lista"><div class="in"><div class="mx-gh mx-rv"><span class="n">0{2 if ind else 1}</span><h2>Todos de <em>Moema.</em></h2><small id="mxN">{len(resto)} lugares</small></div>'
        f'<input class="mx-q" id="mxQ" type="search" placeholder="Buscar pelo nome ou rua" aria-label="Buscar na lista"><div class="mx-ls">{ls}</div></div></section>'
        f'<section class="mx-gr"><div class="in"><div class="mx-gh mx-rv"><span class="n">→</span><h2>Mais de <em>Moema.</em></h2><small></small></div><div class="mx-ot mx-rv">{ot}</div></div></section>'
        f'<div class="in"><div class="mx-end mx-rv"><h2>Gostou do bairro? Venha morar nele.</h2><a href="{wa}" target="_blank" rel="noopener">Fale com a W3W</a></div></div></main>'
        + JS + '''<script>(()=>{const q=document.getElementById('mxQ');if(!q)return;const it=[...document.querySelectorAll('.mx-ls a')],n=document.getElementById('mxN'),nm=s=>s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();q.oninput=()=>{const t=nm(q.value);let c=0;it.forEach(a=>{const ok=!t||nm(a.textContent).includes(t);a.style.display=ok?'':'none';ok&&c++});n.textContent=c+' lugares'}})()</script>''')
