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
FOTO = {'pizzarias':'moema/pizzarias.jpg','japoneses':'moema/japoneses.jpg','padarias':'moema/padarias.jpg','parques':'guia/alameda-parque.jpg','cultura':'guia/auditorio-ibirapuera.jpg'}

def ico(k): return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{P.get(k, "M12 4v16M4 12h16")}"/></svg>'

CSS = r'''<style>
.mx{--ink:#14171C;--ink2:#5A616D;--pp:#F4F1EB;--ac:#2F5FA8;--ln:rgba(20,23,28,.1);--e:cubic-bezier(.16,1,.3,1);background:var(--pp);color:var(--ink);overflow:clip}
.mx .in{width:min(1280px,calc(100% - 40px));margin:0 auto}
.mx-h{position:relative;min-height:min(88svh,820px);color:#fff;isolation:isolate;display:flex}
.mx-h>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;animation:mxk 18s var(--e) both}
@keyframes mxk{from{transform:scale(1.14)}to{transform:scale(1)}}
.mx-h::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(12,14,18,.62),rgba(12,14,18,.15) 45%,rgba(12,14,18,.75))}
.mx-h .in{padding:clamp(120px,14vw,170px) 0 60px;display:flex;flex-direction:column}
.mx-ey{font:500 11px var(--mono,monospace);letter-spacing:.18em;text-transform:uppercase;opacity:.8;display:flex;gap:10px}
.mx-ey a{color:inherit;text-decoration:none}
.mx h1{margin:26px 0 0;font:200 clamp(64px,11vw,180px)/.84 var(--sans,sans-serif);letter-spacing:-.06em}
.mx h1 em{display:block;font-family:var(--serif,serif);font-style:italic;font-weight:200;letter-spacing:-.035em}
.mx h1 span{display:block;overflow:hidden}.mx h1 span>i{display:block;font-style:inherit;animation:mxu 1.2s var(--e) both}.mx h1 span:nth-child(2)>i{animation-delay:.12s}
@keyframes mxu{from{transform:translateY(105%)}}
.mx-lead{max-width:46ch;font-size:clamp(17px,1.4vw,20px);line-height:1.55;margin:28px 0 0;opacity:.9;animation:mxf 1.2s .35s var(--e) both}
@keyframes mxf{from{opacity:0;transform:translateY(16px)}}
.mx-nums{margin-top:auto;padding-top:60px;display:flex;gap:clamp(28px,5vw,72px);border-top:1px solid rgba(255,255,255,.25);animation:mxf 1.2s .5s var(--e) both}
.mx-nums div{padding-top:18px}.mx-nums b{display:block;font:200 clamp(38px,4vw,56px)/1 var(--sans,sans-serif);letter-spacing:-.04em}
.mx-nums small{font:500 10.5px var(--mono,monospace);letter-spacing:.16em;text-transform:uppercase;opacity:.75}
.mx-nums a{margin-left:auto;align-self:flex-end;color:#fff;text-decoration:none;font:500 14px var(--sans,sans-serif);padding:15px 24px;border:1px solid rgba(255,255,255,.5);border-radius:999px;transition:background .3s,color .3s}
.mx-nums a:hover{background:#fff;color:var(--ink)}
.mx-gr{padding:clamp(80px,10vw,140px) 0 0}
.mx-gh{display:grid;grid-template-columns:auto 1fr auto;gap:24px;align-items:end;border-bottom:1px solid var(--ln);padding-bottom:20px;margin-bottom:28px}
.mx-gh .n{font:500 11px var(--mono,monospace);letter-spacing:.16em;color:var(--ac)}
.mx-gh h2{margin:0;font:200 clamp(40px,5.5vw,80px)/.9 var(--sans,sans-serif);letter-spacing:-.05em}
.mx-gh h2 em{font-family:var(--serif,serif);font-style:italic;color:var(--ac)}
.mx-gh small{font:500 11px var(--mono,monospace);letter-spacing:.14em;text-transform:uppercase;color:var(--ink2)}
.mx-fe{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin-bottom:14px}
.mx-ph{position:relative;aspect-ratio:4/5;overflow:hidden;color:#fff;text-decoration:none;isolation:isolate;border-radius:4px}
.mx-ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;transition:transform 1.4s var(--e)}
.mx-ph::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(10,10,12,.1),transparent 40%,rgba(10,10,12,.8))}
.mx-ph:hover img{transform:scale(1.06)}
.mx-ph .top{position:absolute;top:18px;left:18px;right:18px;display:flex;justify-content:space-between;align-items:center}
.mx-ph svg{width:22px;height:22px}
.mx-ph .top small{font:500 10px var(--mono,monospace);letter-spacing:.16em;text-transform:uppercase}
.mx-ph h3{position:absolute;left:20px;right:20px;bottom:20px;margin:0;font:200 clamp(34px,3vw,46px)/.95 var(--sans,sans-serif);letter-spacing:-.04em;display:flex;justify-content:space-between;align-items:flex-end}
.mx-ph h3 i{font:500 18px var(--sans,sans-serif);font-style:normal;transform:translateX(-6px);opacity:0;transition:all .5s var(--e)}
.mx-ph:hover h3 i{transform:none;opacity:1}
.mx-ic{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:0;border-top:1px solid var(--ln);border-left:1px solid var(--ln)}
.mx-ic a{border-right:1px solid var(--ln);border-bottom:1px solid var(--ln);position:relative;display:flex;flex-direction:column;gap:38px;padding:22px;background:var(--pp);color:var(--ink);text-decoration:none;overflow:hidden;transition:color .45s var(--e)}
.mx-ic a::before{content:"";position:absolute;inset:0;background:var(--ink);transform:translateY(101%);transition:transform .55s var(--e);z-index:0}
.mx-ic a:hover{color:#fff}.mx-ic a:hover::before{transform:none}
.mx-ic a>*{position:relative;z-index:1}
.mx-ic .r{display:flex;justify-content:space-between;align-items:flex-start}
.mx-ic svg{width:30px;height:30px;color:var(--ac);transition:color .45s,transform .6s var(--e)}
.mx-ic a:hover svg{color:#fff;transform:rotate(-8deg) scale(1.1)}
.mx svg path{fill:none;stroke:currentColor;stroke-width:1.3;stroke-linecap:round;stroke-linejoin:round}
.mx-ic small{font:500 11px var(--mono,monospace);color:var(--ink2);transition:color .45s}.mx-ic a:hover small{color:rgba(255,255,255,.6)}
.mx-ic b{font:300 22px/1.1 var(--sans,sans-serif);letter-spacing:-.02em}
.mx-rv{opacity:0;transform:translateY(30px);transition:opacity 1s var(--e),transform 1s var(--e)}
.mx-rv.on{opacity:1;transform:none}
.mx-end{margin:clamp(90px,11vw,150px) 0 clamp(60px,8vw,100px);display:grid;grid-template-columns:1fr auto;gap:30px;align-items:end;border-top:1px solid var(--ink);padding-top:30px}
.mx-end h2{margin:0;font:200 clamp(40px,5.5vw,84px)/.92 var(--sans,sans-serif);letter-spacing:-.05em}.mx-end h2 em{font-family:var(--serif,serif);font-style:italic;color:var(--ac)}
.mx-end a{background:var(--ink);color:#fff;text-decoration:none;padding:18px 28px;border-radius:999px;font:500 15px var(--sans,sans-serif)}
@media(max-width:700px){.mx-gh{grid-template-columns:1fr}.mx-nums{flex-wrap:wrap}.mx-nums a{margin-left:0}.mx-end{grid-template-columns:1fr}.mx-ic{grid-template-columns:1fr 1fr}.mx-ic a{gap:26px;padding:18px}}
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
        out += f'<section class="mx-gr"><div class="in"><div class="mx-gh mx-rv"><span class="n">0{gi+1}</span><h2>{esc(a)} <em>{esc(b)}.</em></h2><small>{sum(n[k][1] for k in ks)} lugares</small></div>'
        if fe:
            out += '<div class="mx-fe">' + ''.join(f'<a class="mx-ph mx-rv" data-d="{i*90}" href="{u("moema/"+k)}"><img src="{img_base}{FOTO[k]}" alt="{esc(n[k][0][1])} em Moema" loading="lazy"><div class="top">{ico(k)}<small>Seleção W3W</small></div><h3>{esc(n[k][0][1])}<i>→</i></h3></a>' for i, k in enumerate(fe)) + '</div>'
        if ic:
            out += '<div class="mx-ic mx-rv">' + ''.join(f'<a href="{u("moema/"+k)}"><div class="r">{ico(k)}<small>{n[k][1]:02d}</small></div><b>{esc(n[k][0][1])}</b></a>' for k in ic) + '</div>'
        out += '</div></section>'
    return (CSS + '<main class="mx">'
        f'<section class="mx-h"><img src="{img_base}guia/skyline-ibirapuera.jpg" alt="Moema vista do alto, com o Ibirapuera"><div class="in">'
        f'<nav class="mx-ey"><a href="{u("guia-moema")}">Guia Moema</a><span>/</span><span>Moema por categoria</span></nav>'
        f'<h1><span><i>Moema,</i></span><span><i><em>de perto.</em></i></span></h1>'
        f'<p class="mx-lead">Onde comer, tomar um café, passear e resolver a vida no bairro. Cada lugar mapeado, e os melhores escolhidos pela W3W.</p>'
        f'<div class="mx-nums"><div><b>{len(L)}</b><small>lugares</small></div><div><b>{len(cs)}</b><small>categorias</small></div><div><b>2×</b><small>atualizado por semana</small></div><a href="{u("mapa-moema")}">Abrir o mapa →</a></div>'
        f'</div></section>{out}'
        f'<div class="in"><div class="mx-end mx-rv"><h2>Gostou do bairro?<br><em>Venha morar nele.</em></h2><a href="{wa}" target="_blank" rel="noopener">Fale com a W3W →</a></div></div></main>' + JS)
