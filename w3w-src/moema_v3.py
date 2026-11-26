"""Páginas /moema/<cat>/ v3 — branco, tipo grande, fotos reais, 'aberto agora' ao vivo.
Ideia: em Moema as ruas têm nome de pássaro; o endereço de cada casa vira o elemento gráfico."""
import json, html, os
from moema_idx import P, FOTO, ico, GR
def esc(s): return html.escape(str(s or ''), quote=True)
try: FOTOS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'locais_fotos.json')))
except Exception: FOTOS = {}
LB = 'moema/locais/'

CSS = r'''<style>
body:has(.v3){background:#fff}
.v3{--ink:#111316;--i2:#4A505A;--g1:#F1F3F6;--g2:#E5E9EF;--ac:#1F4FA0;--e:cubic-bezier(.16,1,.3,1);background:#fff;color:var(--ink);overflow:clip}
.v3 .in{width:calc(100% - clamp(32px,5vw,96px));margin:0 auto;max-width:1600px}
.v3 h1,.v3 h2,.v3 h3{font-family:var(--sans,sans-serif);font-weight:300;margin:0}
.v3-h{padding:clamp(110px,11vw,150px) 0 0}
.v3-bc{display:flex;gap:10px;font-size:14px;color:var(--i2)}.v3-bc a{color:inherit}
.v3-h h1{font-size:clamp(76px,15.5vw,270px);line-height:.9;letter-spacing:-.035em;margin:18px 0 0;overflow:hidden;padding-bottom:.04em}
.v3-h h1 span{display:inline-block;animation:v3u 1.3s var(--e) both}
@keyframes v3u{from{transform:translateY(100%)}}
.v3-hg{display:grid;grid-template-columns:5fr 7fr;gap:clamp(24px,4vw,72px);margin-top:clamp(28px,3vw,48px);align-items:start}
.v3-ld{font-size:clamp(18px,1.4vw,21px);line-height:1.75;max-width:40ch;margin:0;animation:v3f 1.1s .3s var(--e) both}
.v3-live{margin:28px 0 0;font-size:clamp(26px,2.4vw,36px);line-height:1.1;letter-spacing:-.03em;animation:v3f 1.1s .45s var(--e) both}
.v3-live b{font-weight:500;color:var(--k)}
.v3-live i{display:inline-block;width:.38em;height:.38em;border-radius:50%;background:var(--k);margin-right:.3em;vertical-align:.12em;animation:v3p 2s infinite}
@keyframes v3p{50%{opacity:.35}}
.v3-bt{display:flex;gap:10px;margin-top:30px;flex-wrap:wrap;animation:v3f 1.1s .55s var(--e) both}
.v3-bt a,.v3-bt button{font:500 15px var(--sans,sans-serif);padding:17px 26px;border:0;cursor:pointer;text-decoration:none;background:var(--ink);color:#fff;transition:transform .35s var(--e),background .3s}
.v3-bt a.s{background:var(--g1);color:var(--ink)}
.v3-bt a:hover,.v3-bt button:hover{transform:translateY(-3px)}.v3-bt a:active{transform:scale(.97)}
@keyframes v3f{from{opacity:0;transform:translateY(22px)}}
.v3-bd{position:relative;height:clamp(380px,72vh,820px);margin-top:clamp(40px,5vw,80px);overflow:hidden;background:var(--g1)}
.v3-bd img{position:absolute;inset:-8% 0;width:100%;height:116%;object-fit:cover;animation:v3z 2.2s var(--e) both;will-change:transform}
.v3-bd .ph{position:absolute;inset:0;display:grid;place-items:center;background:var(--k);color:#fff}.v3-bd .ph svg{width:22%;height:40%}
.v3-mo{display:grid;grid-template-columns:2fr 1fr;grid-template-rows:1fr 1fr;gap:10px;height:clamp(360px,40vw,640px)}
.v3-mo figure{margin:0;position:relative;overflow:hidden;background:var(--g1)}
.v3-mo figure:first-child{grid-row:span 2}
.v3-mo img{width:100%;height:118%;object-fit:cover;display:block;will-change:transform;animation:v3z 1.8s var(--e) both}
.v3-mo figure:nth-child(2) img{animation-delay:.12s}.v3-mo figure:nth-child(3) img{animation-delay:.24s}
@keyframes v3z{from{transform:scale(1.18);opacity:0}}
.v3-mo.one{grid-template-columns:1fr;grid-template-rows:1fr}
.v3-mo .ph{display:grid;place-items:center;color:var(--ink);background:var(--g1)}.v3-mo .ph svg{width:34%;height:34%}
.v3 svg path{fill:none;stroke:currentColor;stroke-width:1.2;stroke-linecap:round;stroke-linejoin:round}
.v3-sec{padding:clamp(150px,16vw,260px) 0 0}
.v3-sec>.in>h2,.v3-hd{font-size:clamp(52px,7.4vw,124px);line-height:1;letter-spacing:-.03em;margin-bottom:clamp(40px,5vw,80px)}
.v3-it{display:grid;grid-template-columns:7fr 5fr;gap:clamp(24px,4vw,72px);align-items:end;margin-bottom:clamp(120px,13vw,220px)}
.v3-it:nth-of-type(even){grid-template-columns:5fr 7fr}.v3-it:nth-of-type(even) .v3-pi{order:2}
.v3-pi{position:relative;aspect-ratio:4/3;overflow:hidden;background:var(--g1)}
.v3-pi img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.6s var(--e),opacity .9s var(--e)}
.v3-pi img.pb{filter:grayscale(1) contrast(1.06);transition:filter 1s var(--e),transform 1.6s var(--e),opacity .9s var(--e)}.v3-pi:hover img.pb{filter:none}.v3-pi img+img{opacity:0}.v3-pi:hover img+img{opacity:1}.v3-pi:hover img{transform:scale(1.04)}
.v3-st{font-size:clamp(36px,4vw,64px);line-height:1.02;letter-spacing:-.025em;font-weight:300;margin:0 0 22px}
.v3-it h3{font-size:clamp(22px,1.8vw,27px);font-weight:500;letter-spacing:0;margin-top:6px}
.v3-it p{margin:14px 0 0;font-size:17px;line-height:1.75;max-width:40ch}
.v3-it .hr{margin-top:14px;font-size:15px;color:var(--i2)}
.v3-op{display:inline-flex;align-items:center;gap:8px;margin-top:16px;font-size:15px;font-weight:500}
.v3-op i{width:8px;height:8px;border-radius:50%;background:#B9BCC2}.v3-op.on i{background:#1E9E6A}
.v3-ac{display:flex;gap:8px;margin-top:24px;flex-wrap:wrap}
.v3-ac a{font:500 14px var(--sans,sans-serif);padding:13px 20px;text-decoration:none;background:var(--g1);color:var(--ink);transition:background .3s,color .3s,transform .3s var(--e)}
.v3-ac a:first-child,.v3-ac a:hover{background:var(--ink);color:#fff}.v3-ac a:active{transform:scale(.97)}
.v3-dk{background:var(--k);color:#fff;padding:clamp(100px,11vw,180px) 0;margin-top:clamp(40px,5vw,80px)}
.v3-dk h2{font-size:clamp(52px,7.4vw,124px);line-height:1;letter-spacing:-.03em;margin-bottom:clamp(40px,5vw,72px)}
.v3-tb{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:4px}
.v3-tb a{display:flex;flex-direction:column;justify-content:space-between;min-height:220px;padding:26px;background:rgba(0,0,0,.18);color:#fff;text-decoration:none;transition:background .45s var(--e),color .45s}
.v3-tb a:hover{background:#fff;color:var(--ink)}
.v3-tb svg{width:34px;height:34px;transition:transform .6s var(--e)}.v3-tb a:hover svg{transform:rotate(-10deg) scale(1.12)}
.v3-tb b{font-size:28px;font-weight:300;letter-spacing:-.03em;line-height:1.05}
.v3-tb span{font-size:15px;opacity:.7;margin-top:6px}
.v3-fl{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:22px}
.v3-fl button{font:500 15px var(--sans,sans-serif);padding:14px 22px;border:0;background:var(--g1);color:var(--ink);cursor:pointer;transition:background .3s,color .3s}
.v3-fl button[aria-pressed=true]{background:var(--ink);color:#fff}
.v3-fl input{flex:1;min-width:220px;height:52px;border:0;background:var(--g1);padding:0 20px;font:17px var(--sans,sans-serif);color:var(--ink);outline-offset:2px}
.v3-ls a{display:grid;grid-template-columns:1.4fr 1.4fr 1fr 28px;gap:18px;align-items:center;padding:28px 24px;color:var(--ink);text-decoration:none;transition:background .3s,padding .5s var(--e)}
.v3-ls a:nth-child(odd){background:var(--g1)}
.v3-ls a:hover{background:var(--ink);color:#fff;padding-left:30px}
.v3-ls b{font-size:21px;font-weight:400;letter-spacing:-.015em}
.v3-ls span{font-size:15px}
.v3-ls .op{display:flex;gap:8px;align-items:center}.v3-ls .op i{width:7px;height:7px;border-radius:50%;background:#B9BCC2}.v3-ls .op.on i{background:#1E9E6A}
.v3-ls .ar{opacity:0;transform:translateX(-8px);transition:all .45s var(--e)}.v3-ls a:hover .ar{opacity:1;transform:none}
.v3-mr{margin-top:20px}
.v3-ot{display:flex;flex-wrap:wrap;gap:8px}
.v3-ot a{display:inline-flex;gap:10px;align-items:center;padding:16px 22px;background:var(--g1);color:var(--ink);text-decoration:none;font-size:17px;transition:background .3s,color .3s,transform .3s var(--e)}
.v3-ot svg{width:22px;height:22px}.v3-ot a:hover{background:var(--ink);color:#fff;transform:translateY(-3px)}
.v3-mm{margin-top:clamp(120px,13vw,220px);background:var(--g1);color:var(--ink)}.v3-mm .v3-ot a{background:#fff;color:var(--ink)}.v3-mm .v3-ot a:hover{background:#fff;color:var(--ink)}
.v3-end{display:grid;grid-template-columns:1fr auto;align-items:end;gap:30px;padding:clamp(120px,13vw,220px) 0 clamp(80px,9vw,140px)}
.v3-end h2{font-size:clamp(52px,7.4vw,124px);line-height:1;letter-spacing:-.03em}
.v3-end a{background:var(--k);color:#fff;text-decoration:none;padding:20px 30px;font:500 16px var(--sans,sans-serif);transition:transform .35s var(--e)}.v3-end a:hover{transform:translateY(-3px)}
.v3-rv>*{opacity:0;transform:translateY(26px);transition:opacity 1s var(--e),transform 1s var(--e)}
.v3-rv.on>*{opacity:1;transform:none}
.v3-rv.on>*:nth-child(2){transition-delay:.08s}.v3-rv.on>*:nth-child(3){transition-delay:.16s}.v3-rv.on>*:nth-child(4){transition-delay:.24s}
.v3-pi.v3-zz img:first-child{transform:scale(1.12)}.v3-it.on .v3-pi img:first-child{transform:scale(1)}
@media(max-width:860px){.v3-hg,.v3-it,.v3-it:nth-of-type(even),.v3-end{grid-template-columns:1fr}.v3-it:nth-of-type(even) .v3-pi{order:0}.v3-mo{height:auto;grid-template-columns:1fr 1fr;grid-template-rows:auto}.v3-mo figure:first-child{grid-column:span 2;grid-row:auto;aspect-ratio:4/3}.v3-mo figure{aspect-ratio:1}.v3-ls a{grid-template-columns:1fr auto}.v3-ls .ad{display:none}}
@media(prefers-reduced-motion:reduce){.v3 *{animation:none!important;transition:none!important}.v3-rv>*{opacity:1;transform:none}}
</style>'''

JS = r'''<script>(()=>{
const D={Mo:1,Tu:2,We:3,Th:4,Fr:5,Sa:6,Su:0};
function open(h){if(!h)return null;h=h.trim();if(h==='24/7')return true;const n=new Date(),d=n.getDay(),m=n.getHours()*60+n.getMinutes();let known=false,ok=false;
for(const part of h.split(';')){const p=part.trim();const mm=p.match(/^([A-Za-z,\- ]*?)\s*(\d{1,2}:\d{2}.*)$/);if(!mm)continue;known=true;let days=mm[1].replace('PH','').trim(),on=!days;
if(days){for(const t of days.split(',')){const r=t.trim().split('-');if(r.length===2&&r[0] in D&&r[1] in D){let a=D[r[0]],b=D[r[1]];for(let i=a;;i=(i+1)%7){if(i===d)on=true;if(i===b)break}}else if(t.trim() in D&&D[t.trim()]===d)on=true}}
if(!on)continue;for(const r of mm[2].split(',')){const x=r.trim().match(/(\d{1,2}):(\d{2})\s*-\s*(\d{1,2}):(\d{2})/);if(!x)continue;let a=+x[1]*60+ +x[2],b=+x[3]*60+ +x[4];if(b<=a)b+=1440;if((m>=a&&m<b)||(m+1440>=a&&m+1440<b))ok=true}}
return known?ok:null}
let tot=0,ab=0;document.querySelectorAll('[data-h]').forEach(el=>{const o=open(el.dataset.h);el.dataset.o=o===true?'1':'0';const s=el.querySelector('.op,.v3-op');if(o!==null&&s){s.classList.toggle('on',o);s.querySelector('em').textContent=o?'Aberto agora':'Fechado agora'}if(el.closest('.v3-ls')||el.classList.contains('v3-it')){tot++;if(o)ab++}});
const lv=document.getElementById('v3Live');if(lv)lv.innerHTML=`<i></i>Agora, <b>${ab}</b> de ${tot} estão abertos.`;
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{rootMargin:'0px 0px -10% 0px'});document.querySelectorAll('.v3-rv').forEach(el=>io.observe(el));
const mo=[...document.querySelectorAll('.v3-bd img')];if(mo.length&&!matchMedia('(prefers-reduced-motion: reduce)').matches){let t=0;addEventListener('scroll',()=>{if(t)return;t=requestAnimationFrame(()=>{t=0;const y=scrollY;mo.forEach((im,i)=>im.style.transform=`translateY(${y*.12}px)`)})},{passive:true})}
const q=document.getElementById('v3Q'),it=[...document.querySelectorAll('.v3-ls a')],n=document.getElementById('v3N'),more=document.getElementById('v3More');let f='t',all=false;const nm=s=>s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase();
function run(){const t=nm(q?q.value:'');let c=0,shown=0;it.forEach(a=>{const ok=(!t||nm(a.textContent).includes(t))&&(f==='t'||a.dataset.o==='1');if(ok)c++;const vis=ok&&(all||t||shown<14);if(vis)shown++;a.style.display=vis?'':'none'});if(n)n.textContent=c+(c===1?' lugar':' lugares');if(more)more.hidden=all||!!t||c<=14}
document.querySelectorAll('.v3-fl button').forEach(b=>b.onclick=()=>{f=b.dataset.f;document.querySelectorAll('.v3-fl button').forEach(x=>x.setAttribute('aria-pressed',x===b));run()});
if(q)q.oninput=run;if(more)more.onclick=()=>{all=true;run()};run()})()</script>'''

CK = {'japoneses':'#B3262D','pizzarias':'#C8442B','padarias':'#B07A1E','restaurantes':'#2F4A36','bares':'#6B1E2E','noite':'#2A2350','cafes':'#6A4630','docerias':'#B0476F','sorveterias':'#2C7FA8','churrascarias':'#7A2A1C','hamburguerias':'#B5551E','parques':'#2E5E44','cultura':'#22407A'}
FAC = {'speranza-1','casale-1','djapa-1','hito-1','kinoshita-1','yakitori-1','pingo-1','padoca-1','padoca-2','boston-1'}
def gm(l): return f'https://www.google.com/maps/dir/?api=1&destination={l["lat"]},{l["lon"]}'
def rua(l):
    e = (l.get('end') or '').strip()
    if e[:1].isdigit():  # "567 Alameda dos X" -> "Alameda dos X, 567"
        p = e.split(' ', 1); e = f'{p[1]}, {p[0]}' if len(p) == 2 else e
    return e or 'Moema'

def render_cat(cat, L, cs, u, wa, img_base, titulo, intro, ld):
    key, label = cat[0], cat[1]
    it = [l for l in L if l['cat'] == key]
    ind = [l for l in it if l.get('destaque')]
    com = [l for l in ind if FOTOS.get(l['nome'])]; sem = [l for l in ind if not FOTOS.get(l['nome'])]
    resto = sorted([l for l in it if not l.get('destaque')], key=lambda l: l['nome'].lower())
    fotos = ([FOTO[key]] if key in FOTO else []) + [LB + FOTOS[l['nome']][0] + '.jpg' for l in com]
    fotos = fotos[:3]
    bd = f'<div class="v3-bd"><img src="{img_base}{fotos[0]}" alt="{esc(label)} em Moema" loading="eager"></div>' if fotos else f'<div class="v3-bd"><div class="ph">{ico(key)}</div></div>'
    if len(fotos) >= 3: mo = '<div class="v3-mo">' + ''.join(f'<figure><img src="{img_base}{f}" alt="{esc(label)} em Moema" loading="eager"></figure>' for f in fotos) + '</div>'
    elif fotos: mo = f'<div class="v3-mo one"><figure><img src="{img_base}{fotos[0]}" alt="{esc(label)} em Moema" loading="eager"></figure></div>'
    else: mo = f'<div class="v3-mo one"><figure class="ph">{ico(key)}</figure></div>'
    def acts(l):
        return (f'<a href="{gm(l)}" target="_blank" rel="noopener">Como chegar</a>' + (f'<a href="{esc(l["site"])}" target="_blank" rel="noopener nofollow">Site</a>' if l.get('site') else '')
                + (f'<a href="tel:{esc("".join(c for c in l["tel"] if c.isdigit() or c=="+"))}">Ligar</a>' if l.get('tel') else ''))
    from moema_idx import hum
    fe = ''.join(f'<article class="v3-it v3-rv" data-h="{esc(l.get("horario"))}"><div class="v3-pi v3-zz">' + ''.join(f'<img{" class=\"pb\"" if f in FAC else ""} src="{img_base}{LB}{f}.jpg" alt="{esc(l["nome"])}, Moema" loading="lazy">' for f in FOTOS[l['nome']][:2])
                 + f'</div><div><p class="v3-st">{esc(rua(l))}</p><h3>{esc(l["nome"])}</h3>' + (f'<p>{esc(l["nota"])}</p>' if l.get('nota') else '')
                 + (f'<div class="hr">{esc(hum(l.get("horario")))}</div>' if l.get('horario') else '') + f'<div class="v3-op"><i></i><em>Horário não informado</em></div><div class="v3-ac">{acts(l)}</div></div></article>' for l in com)
    tb = ''.join(f'<a href="{gm(l)}" target="_blank" rel="noopener" data-h="{esc(l.get("horario"))}">{ico(key)}<div><b>{esc(l["nome"])}</b><span>{esc(rua(l))}</span></div></a>' for l in sem)
    ls = ''.join(f'<a href="{gm(l)}" target="_blank" rel="noopener" data-h="{esc(l.get("horario"))}"><b>{esc(l["nome"])}</b><span class="ad">{esc(rua(l))}</span><span class="op"><i></i><em>Sem horário</em></span><span class="ar">→</span></a>' for l in resto)
    ot = ''.join(f'<a href="{u("moema/"+c[0])}">{ico(c[0])}{esc(c[1])}</a>' for c, n in cs if c[0] != key)
    return (CSS + f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script><main class="v3" style="--k:{CK.get(key, chr(35)+"1F4FA0")}">'
        f'<section class="v3-h"><div class="in"><nav class="v3-bc" aria-label="Você está em"><a href="{u("guia-moema")}">Guia Moema</a><span>/</span><a href="{u("moema")}">Moema por categoria</a></nav>'
        f'<h1><span>{esc(label)}</span></h1><div class="v3-hg"><div><p class="v3-ld">{esc(intro)}</p><p class="v3-live" id="v3Live">{len(it)} lugares em Moema.</p>'
        f'</div><div><div class="v3-bt" style="margin-top:0"><a href="{u("mapa-moema")}?cat={key}">Ver no mapa</a><a class="s" href="#lista">Ver a lista</a></div></div></div></div>{bd}</section>'
        + (f'<section class="v3-sec"><div class="in"><h2 class="v3-hd v3-rv"><span>A W3W indica</span></h2>{fe}</div></section>' if com else '')
        + (f'<section class="v3-dk"><div class="in"><h2 class="v3-rv"><span>{"Também indicamos" if com else "A W3W indica"}</span></h2><div class="v3-tb v3-rv">{tb}</div></div></section>' if sem else '')
        + f'<section class="v3-sec" id="lista"><div class="in"><h2 class="v3-rv"><span>Todos de Moema</span></h2>'
        f'<div class="v3-fl"><button data-f="t" aria-pressed="true">Todos</button><button data-f="a" aria-pressed="false">Aberto agora</button><input id="v3Q" type="search" placeholder="Buscar pelo nome ou rua" aria-label="Buscar na lista"><span id="v3N"></span></div>'
        f'<div class="v3-ls">{ls}</div><div class="v3-bt v3-mr"><button id="v3More" class="s" style="background:var(--g1);color:var(--ink)">Ver todos</button></div></div></section>'
        f'<section class="v3-dk v3-mm"><div class="in"><h2 class="v3-rv"><span>Mais de Moema</span></h2><div class="v3-ot v3-rv">{ot}</div></div></section>'
        f'<div class="in v3-end v3-rv"><h2>Gostou do bairro? Venha morar nele.</h2><a href="{wa}" target="_blank" rel="noopener">Fale com a W3W</a></div></main>' + JS)
