"""Páginas por categoria do Guia Moema (SEO): /moema/<categoria>/ e /moema/."""
import json, html

CAT_SLUG_SKIP = {'lojas', 'chaveiros', 'costureiras', 'floriculturas', 'lavarapido', 'bancos', 'lavanderias'}

TXT = {
 'pizzarias': ('As melhores pizzarias de Moema', 'De forno a lenha à napolitana de massa leve, Moema é um dos bairros com mais pizzarias por quarteirão em São Paulo. Reunimos as casas do bairro, com endereço, horário e como chegar, e destacamos as que a W3W indica.'),
 'padarias': ('Padarias em Moema', 'Pão na chapa, café coado e aquela fornada do fim da tarde: a padaria é parte da rotina de quem mora em Moema. Veja as padarias do bairro, com endereço, horário e as preferidas da W3W.'),
 'japoneses': ('Restaurantes japoneses em Moema', 'Moema tem uma das maiores concentrações de restaurantes japoneses da cidade, do sushi bar intimista ao izakaya e ao yakitori. Confira a lista completa do bairro e as casas que a W3W indica.'),
 'restaurantes': ('Restaurantes em Moema', 'Italianos, parrillas, cozinha brasileira, saudáveis e bistrôs: Moema concentra boa parte da gastronomia da Zona Sul. Veja todos os restaurantes do bairro e os que a W3W indica.'),
 'churrascarias': ('Churrascarias e casas de carne em Moema', 'Parrillas argentinas, steakhouses e churrascarias tradicionais. Os endereços de carne de Moema, com horário, como chegar e a seleção da W3W.'),
 'hamburguerias': ('Hamburguerias em Moema', 'Smash, artesanal ou clássico de lanchonete: as hamburguerias de Moema reunidas num só lugar, com endereço, horário e as indicações da W3W.'),
 'bares': ('Bares em Moema', 'Do boteco de esquina ao bar de vinhos e drinques autorais. Os bares de Moema, com endereço, horário e os que a W3W indica para a noite no bairro.'),
 'noite': ('Vida noturna em Moema', 'Música ao vivo, baladas e casas noturnas de Moema e arredores, com endereço e como chegar.'),
 'cafes': ('Cafés em Moema', 'Cafés especiais, confeitarias e lugares bons para trabalhar com calma. Os cafés de Moema, com horário, endereço e os favoritos da W3W.'),
 'docerias': ('Docerias e confeitarias em Moema', 'Bolos, chocolates, doces árabes e confeitaria fina: as docerias de Moema reunidas, com endereço, horário e as preferidas da W3W.'),
 'sorveterias': ('Sorveterias em Moema', 'Gelato italiano, sorvete artesanal e açaí. As sorveterias de Moema para os dias de calor, com endereço e como chegar.'),
 'mercados': ('Mercados e empórios em Moema', 'Supermercados, hortifrútis e empórios do bairro, com endereço, horário e como chegar.'),
 'pet': ('Pet shops e veterinários em Moema', 'Pet shops, banho e tosa e clínicas veterinárias de Moema, um dos bairros mais pet friendly de São Paulo.'),
 'farmacias': ('Farmácias em Moema', 'As farmácias de Moema, incluindo as que abrem 24 horas, com endereço, telefone e como chegar.'),
 'saude': ('Clínicas e serviços de saúde em Moema', 'Clínicas, consultórios, laboratórios e hospitais de Moema e arredores, com endereço e contato.'),
 'parques': ('Parques e praças em Moema', 'O Ibirapuera ao lado e dezenas de praças arborizadas: os espaços verdes de Moema para caminhar, levar as crianças e os pets.'),
 'cultura': ('Cultura em Moema', 'Teatros, museus, galerias e espaços culturais de Moema e do entorno do Ibirapuera.'),
 'academias': ('Academias em Moema', 'Academias, estúdios de pilates, crossfit e lutas em Moema, com endereço e contato.'),
 'escolas': ('Escolas em Moema', 'Escolas de educação infantil, ensino fundamental e médio e escolas de idiomas em Moema.'),
 'hoteis': ('Hotéis em Moema', 'Hotéis e flats em Moema e perto do Ibirapuera e do Aeroporto de Congonhas.'),
 'estetica': ('Manicure e estética em Moema', 'Esmalterias, clínicas de estética e spas de Moema, com endereço e contato.'),
 'cabeleireiros': ('Cabeleireiros e barbearias em Moema', 'Salões de beleza e barbearias de Moema, com endereço e contato.'),
}

PT = {'Mo': 'Seg', 'Tu': 'Ter', 'We': 'Qua', 'Th': 'Qui', 'Fr': 'Sex', 'Sa': 'Sáb', 'Su': 'Dom', 'PH': 'Feriados', 'off': 'fechado'}

def hum(h):
    if not h: return ''
    if h.strip() == '24/7': return 'Aberto 24 horas'
    s = h
    for k, v in PT.items(): s = s.replace(k, v)
    return s.replace(';', ' ·').replace(',', ', ')

def esc(s): return html.escape(str(s or ''), quote=True)

CSS = '''<style>
.mc{--k:#C2553D;--kd:color-mix(in srgb,var(--k) 62%,#140f0c);--kl:color-mix(in srgb,var(--k) 14%,#FBF7F1);--cr:#FBF6EE;background:var(--cr);color:#1A1612;overflow:clip}
.mc .in{width:min(1240px,calc(100% - 40px));margin:0 auto}
.mc-hero{position:relative;background:radial-gradient(120% 90% at 85% 10%,color-mix(in srgb,var(--k) 80%,#fff 20%),var(--k) 45%,var(--kd));color:var(--cr);padding:clamp(108px,12vw,150px) 0 clamp(70px,8vw,110px);isolation:isolate}
.mc-hero::before{content:"";position:absolute;inset:0;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)' opacity='.09'/%3E%3C/svg%3E");mix-blend-mode:overlay;z-index:-1}
.mc-hg{display:grid;grid-template-columns:1.15fr .85fr;gap:clamp(30px,5vw,80px);align-items:center}
.mc-bc{font:500 11px var(--mono,monospace);letter-spacing:.14em;text-transform:uppercase;opacity:.75;display:flex;gap:8px;flex-wrap:wrap}
.mc-bc a{color:inherit;text-decoration:none}.mc-bc a:hover{opacity:1;text-decoration:underline}
.mc h1{margin:22px 0 24px;line-height:.86;letter-spacing:-.055em}
.mc h1 .a{display:block;font:300 clamp(64px,10.5vw,168px)/.86 var(--sans,sans-serif)}
.mc h1 .b{display:block;font:200 clamp(54px,8.5vw,138px)/.9 var(--serif,serif);font-style:italic;letter-spacing:-.03em;color:color-mix(in srgb,var(--cr) 82%,var(--k))}
.mc .lead{font-size:clamp(17px,1.5vw,20px);line-height:1.55;max-width:52ch;margin:0;opacity:.9}
.mc-st{display:flex;gap:10px;flex-wrap:wrap;margin:30px 0 32px;padding:0}
.mc-st div{padding:12px 18px;border-radius:999px;background:rgba(255,255,255,.14);backdrop-filter:blur(10px);box-shadow:inset 0 1px 0 rgba(255,255,255,.25)}
.mc-st dt{display:inline;font:500 18px var(--sans,sans-serif)}.mc-st dd{display:inline;margin:0 0 0 6px;font:500 10.5px var(--mono,monospace);letter-spacing:.12em;text-transform:uppercase;opacity:.8}
.mc-bt{display:flex;gap:10px;flex-wrap:wrap}
.mc-cta{display:inline-flex;align-items:center;gap:10px;padding:17px 28px;border-radius:999px;background:var(--cr);color:var(--kd);text-decoration:none;font:500 15px var(--sans,sans-serif);box-shadow:0 20px 40px -18px rgba(0,0,0,.45);transition:transform .4s cubic-bezier(.16,1,.3,1)}
.mc-cta:hover{transform:translateY(-3px)}
.mc-cta.g{background:transparent;color:var(--cr);box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.45)}
.mc-art{position:relative;aspect-ratio:4/5;max-height:600px}
.mc-ph{position:absolute;inset:0;border-radius:36px;overflow:hidden;transform:rotate(2.5deg);box-shadow:0 50px 90px -40px rgba(0,0,0,.6);background:var(--kd)}
.mc-ph img{width:100%;height:100%;object-fit:cover;transform:scale(1.06);animation:mczoom 14s ease-in-out infinite alternate}
@keyframes mczoom{to{transform:scale(1.16)}}
.mc-pl{position:absolute;inset:0;display:grid;place-items:center}
.mc-pl i{position:absolute;border-radius:50%;border:1.5px solid rgba(255,255,255,.28)}
.mc-pl i:nth-child(1){width:86%;aspect-ratio:1;background:radial-gradient(circle,rgba(255,255,255,.16),rgba(255,255,255,.04) 70%)}
.mc-pl i:nth-child(2){width:62%;aspect-ratio:1;border-style:dashed;animation:mcspin 40s linear infinite}
.mc-pl i:nth-child(3){width:36%;aspect-ratio:1;background:var(--cr);border:0;box-shadow:0 30px 60px -20px rgba(0,0,0,.5)}
@keyframes mcspin{to{transform:rotate(360deg)}}
.mc-pl b{position:relative;z-index:1;font:200 clamp(70px,9vw,140px)/1 var(--serif,serif);font-style:italic;color:var(--k)}
.mc-tag{position:absolute;z-index:2;padding:12px 16px;border-radius:16px;background:rgba(251,246,238,.94);color:#1A1612;font:500 14px var(--sans,sans-serif);box-shadow:0 20px 40px -18px rgba(0,0,0,.45);animation:mcfl 6s ease-in-out infinite}
.mc-tag small{display:block;font:500 9.5px var(--mono,monospace);letter-spacing:.12em;text-transform:uppercase;color:var(--k);margin-bottom:3px}
.mc-tag:nth-of-type(1){left:-8%;top:12%}.mc-tag:nth-of-type(2){right:-6%;top:46%;animation-delay:-2s}.mc-tag:nth-of-type(3){left:4%;bottom:6%;animation-delay:-4s}
@keyframes mcfl{50%{transform:translateY(-10px)}}
.mc-mq{background:var(--kd);color:var(--cr);overflow:hidden;white-space:nowrap;padding:18px 0;border-block:1px solid rgba(255,255,255,.1)}
.mc-mq div{display:inline-flex;gap:28px;animation:mcmq 60s linear infinite;font:300 clamp(22px,2.4vw,32px) var(--sans,sans-serif);letter-spacing:-.02em}
.mc-mq span::after{content:"✦";margin-left:28px;color:color-mix(in srgb,var(--k) 60%,#fff);font-size:.6em;vertical-align:middle}
@keyframes mcmq{to{transform:translateX(-50%)}}
.mc-sec{padding:clamp(70px,9vw,120px) 0 0}
.mc h2{font:300 clamp(38px,5vw,72px)/.95 var(--sans,sans-serif);letter-spacing:-.045em;margin:0 0 30px;display:flex;align-items:flex-end;justify-content:space-between;gap:20px;flex-wrap:wrap}
.mc h2 em{font-family:var(--serif,serif);font-style:italic;font-weight:200;color:var(--k)}
.mc h2 small{font:500 11px var(--mono,monospace);letter-spacing:.14em;text-transform:uppercase;color:#8A7F74}
.mc-ind{display:grid;grid-auto-flow:column;grid-auto-columns:min(340px,82vw);gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;padding:6px 20px 30px;margin:0 -20px;scrollbar-width:none}
.mc-ind::-webkit-scrollbar{display:none}
.mc-ind article{scroll-snap-align:start;position:relative;min-height:440px;display:flex;flex-direction:column;justify-content:flex-end;padding:28px;border-radius:30px;color:var(--cr);background:linear-gradient(170deg,color-mix(in srgb,var(--k) 88%,#fff 12%),var(--kd));overflow:hidden;box-shadow:0 30px 60px -34px color-mix(in srgb,var(--k) 70%,#000);transition:transform .5s cubic-bezier(.16,1,.3,1)}
.mc-ind article:hover{transform:translateY(-6px) rotate(-.6deg)}
.mc-ind article::before{content:attr(data-n);position:absolute;top:10px;right:18px;font:200 150px/1 var(--serif,serif);font-style:italic;color:rgba(255,255,255,.14)}
.mc-ind article.f{background:var(--kd)}
.mc-ind article.f img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;transition:opacity .8s cubic-bezier(.16,1,.3,1),transform 1.2s cubic-bezier(.16,1,.3,1)}
.mc-ind article.f{isolation:isolate}
.mc-ind article.f::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(15,11,8,0) 30%,rgba(15,11,8,.55) 62%,rgba(15,11,8,.88))}
.mc-ind article.f::before{color:rgba(255,255,255,.22);z-index:0}
.mc-ind article.f2 img+img{opacity:0}
.mc-ind article.f:hover img{transform:scale(1.05)}
.mc-ind article.f2:hover img+img{opacity:1}
.mc-ind .tg{align-self:flex-start;font:500 10px var(--mono,monospace);letter-spacing:.12em;text-transform:uppercase;color:var(--kd);background:var(--cr);padding:5px 10px;border-radius:999px}
.mc-ind h3{font:300 36px/1 var(--sans,sans-serif);letter-spacing:-.035em;margin:16px 0 10px}
.mc-ind p{margin:0 0 3px;font-size:14px;opacity:.85;line-height:1.5}
.mc-ind .h{font:11.5px/1.6 var(--mono,monospace);opacity:.7;margin-top:10px}
.mc-ac{display:flex;gap:8px;margin-top:20px;flex-wrap:wrap}
.mc-ac a{font:500 13px var(--sans,sans-serif);padding:10px 15px;border-radius:999px;text-decoration:none;background:rgba(255,255,255,.14);color:inherit;transition:background .25s}
.mc-ac a.p{background:var(--cr);color:var(--kd)}
.mc-fl{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:0 0 22px}
.mc-fl input{flex:1;min-width:220px;height:52px;border-radius:999px;border:0;padding:0 22px;font:16px var(--sans,sans-serif);background:#fff;box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--k) 25%,transparent),0 14px 30px -24px rgba(0,0,0,.4);color:#1A1612}
.mc-fl input:focus{outline:0;box-shadow:inset 0 0 0 2px var(--k)}
.mc-fl span{font:500 11px var(--mono,monospace);letter-spacing:.12em;text-transform:uppercase;color:#8A7F74}
.mc-ls{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:12px}
.mc-ls article{display:grid;grid-template-columns:58px 1fr;gap:4px 16px;padding:18px;border-radius:24px;background:#fff;box-shadow:0 1px 0 rgba(26,22,18,.04),0 18px 36px -30px rgba(26,22,18,.35);transition:transform .4s cubic-bezier(.16,1,.3,1),box-shadow .4s}
.mc-ls article:hover{transform:translateY(-4px);box-shadow:0 0 0 1.5px color-mix(in srgb,var(--k) 40%,transparent),0 28px 50px -30px color-mix(in srgb,var(--k) 60%,#000)}
.mc-ls .mo{grid-row:span 3;width:58px;height:58px;border-radius:18px;display:grid;place-items:center;font:200 32px/1 var(--serif,serif);font-style:italic;color:var(--k);background:var(--kl)}
.mc-ls h3{font:500 17px/1.2 var(--sans,sans-serif);letter-spacing:-.01em;margin:4px 0 2px}
.mc-ls p{margin:0;font-size:13.5px;color:#6B6157;line-height:1.45}
.mc-ls .h{font:11px/1.6 var(--mono,monospace);color:#8A7F74;margin-top:6px}
.mc-ls .mc-ac{grid-column:2;margin-top:12px}
.mc-ls .mc-ac a{background:var(--kl);color:var(--kd);padding:8px 13px;font-size:12.5px}
.mc-ls .mc-ac a.p{background:var(--k);color:#fff}
.mc-ot{display:flex;flex-wrap:wrap;gap:10px}
.mc-ot a{display:inline-flex;align-items:center;gap:10px;padding:14px 20px;border-radius:999px;background:#fff;color:#1A1612;text-decoration:none;font:500 15px var(--sans,sans-serif);box-shadow:0 14px 30px -24px rgba(0,0,0,.4);transition:transform .3s cubic-bezier(.16,1,.3,1),background .3s,color .3s}
.mc-ot a i{width:10px;height:10px;border-radius:50%;background:var(--c)}
.mc-ot a:hover{transform:translateY(-3px);background:var(--c);color:#fff}
.mc-ot a:hover i{background:#fff}
.mc-ot a small{opacity:.55;font:500 11px var(--mono,monospace)}
.mc-fq details{border-top:1px solid rgba(26,22,18,.1);padding:22px 0}
.mc-fq summary{cursor:pointer;font:400 clamp(18px,1.8vw,22px) var(--sans,sans-serif);letter-spacing:-.015em;list-style:none;display:flex;justify-content:space-between;gap:16px}
.mc-fq summary::after{content:"+";color:var(--k);font-size:26px;line-height:1;transition:transform .3s}
.mc-fq details[open] summary::after{transform:rotate(45deg)}
.mc-fq p{color:#5B5249;line-height:1.6;margin:12px 0 0;max-width:70ch}
.mc-end{margin:clamp(70px,9vw,120px) 0 clamp(60px,8vw,100px);padding:clamp(34px,6vw,72px);border-radius:40px;background:radial-gradient(120% 120% at 100% 0%,color-mix(in srgb,var(--k) 75%,#fff 25%),var(--kd));color:var(--cr);display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.mc-end h2{margin:0;color:var(--cr)}.mc-end h2 em{color:var(--cr)}
.mc-rv{opacity:0;transform:translateY(28px);transition:opacity .9s cubic-bezier(.16,1,.3,1),transform .9s cubic-bezier(.16,1,.3,1)}
.mc-rv.on{opacity:1;transform:none}
@media(max-width:900px){.mc-hg{grid-template-columns:1fr}.mc-art{max-width:420px;width:86%;margin:10px auto 0}.mc-tag:nth-of-type(1){left:-4%}.mc-tag:nth-of-type(2){right:-4%}}
@media(prefers-reduced-motion:reduce){.mc *{animation:none!important}.mc-rv{opacity:1;transform:none}}
</style>'''

JS = '''<script>(()=>{const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});document.querySelectorAll('.mc-rv').forEach(el=>io.observe(el));
const q=document.getElementById('mcQ');if(q){const it=[...document.querySelectorAll('.mc-ls article')],n=document.getElementById('mcN');const nm=s=>s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();q.oninput=()=>{const t=nm(q.value);let c=0;it.forEach(a=>{const ok=!t||nm(a.textContent).includes(t);a.style.display=ok?'':'none';ok&&c++});n.textContent=c+' lugares'}}})()</script>'''

import os as _os
try: FOTOS = json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'locais_fotos.json')))
except Exception: FOTOS = {}
IMGB = 'https://kcooyakawa.github.io/kco-imobiliario/w3w-img/moema/locais/'

IMG = {'parques': 'guia/alameda-parque.jpg', 'cultura': 'guia/auditorio-ibirapuera.jpg'}

def card(l, CM, dark=False, n=0):
    acts = f'<a class="p" href="https://www.google.com/maps/dir/?api=1&destination={l["lat"]},{l["lon"]}" target="_blank" rel="noopener">Como chegar</a>'
    if l.get('site'): acts += f'<a href="{esc(l["site"])}" target="_blank" rel="noopener nofollow">Site</a>'
    if l.get('tel'): acts += f'<a href="tel:{esc("".join(c for c in l["tel"] if c.isdigit() or c=="+"))}">Ligar</a>'
    h = hum(l.get('horario'))
    hh = f'<div class="h">{esc(h)}</div>' if h else ''
    nota = f'<p>{esc(l.get("nota"))}</p>' if l.get('nota') else ''
    if dark:
        fs = FOTOS.get(l['nome'], [])
        ph = ''.join(f'<img src="{IMGB}{f}.jpg" alt="{esc(l["nome"])}, Moema" loading="lazy">' for f in fs[:2])
        return f'<article data-n="{n:02d}"{" class=\"f" + (" f2" if len(fs) > 1 else "") + "\"" if fs else ""}>{ph}<span class="tg">W3W indica</span><h3>{esc(l["nome"])}</h3>{nota}<p>{esc(l.get("end") or "Moema, São Paulo")}</p>{hh}<div class="mc-ac">{acts}</div></article>'
    ini = (l['nome'].strip()[:1] or '·').upper()
    return f'<article><span class="mo">{esc(ini)}</span><h3>{esc(l["nome"])}</h3><p>{esc(l.get("end") or "Moema, São Paulo")}</p>{hh}<div class="mc-ac">{acts}</div></article>'

def cats_validas(L, CATS):
    from collections import Counter
    n = Counter(l['cat'] for l in L)
    return [(c, n[c[0]]) for c in CATS if c[0] not in CAT_SLUG_SKIP and n[c[0]] >= 8]

def render(cat, L, CATS, u, wa, img_base='', img_ok=None):
    CM = {c[0]: c for c in CATS}
    key, label, cor = cat[0], cat[1], cat[2]
    itens = [l for l in L if l['cat'] == key]
    itens.sort(key=lambda l: (not l.get('destaque'), not l.get('horario'), l['nome'].lower()))
    ind = [l for l in itens if l.get('destaque')]
    resto = sorted([l for l in itens if not l.get('destaque')], key=lambda l: l['nome'].lower())
    titulo, intro = TXT.get(key, (f'{label} em Moema', f'{label} de Moema reunidos pela W3W Imóveis, com endereço, horário e como chegar.'))
    pal = label.lower()
    foto = (img_ok or {}).get(key) or IMG.get(key)
    tags = ''.join(f'<span class="mc-tag"><small>{"W3W indica" if ind else esc(label)}</small>{esc(l["nome"])}</span>' for l in (ind or itens)[:3])
    if foto:
        art = f'<div class="mc-ph"><img src="{img_base}{foto}" alt="{esc(label)} em Moema" loading="eager"></div>'
    else:
        art = f'<div class="mc-ph"><div class="mc-pl"><i></i><i></i><i></i><b>{esc(label[:1])}</b></div></div>'
    mq = ''.join(f'<span>{esc(l["nome"])}</span>' for l in itens[:24]) * 2
    outros = ''.join(f'<a href="{u("moema/" + c[0])}" style="--c:{c[2]}"><i></i>{esc(c[1])}<small>{n}</small></a>' for c, n in cats_validas(L, CATS) if c[0] != key)
    faq = [(f'Quantos lugares de {pal} existem em Moema?', f'O Guia Moema da W3W lista {len(itens)} lugares na categoria {pal} em Moema e arredores, atualizados duas vezes por semana.'),
           (f'Quais {pal} a W3W indica em Moema?', (', '.join(l['nome'] for l in ind[:6]) + '.') if ind else f'A curadoria W3W de {pal} está em andamento. Enquanto isso, veja a lista completa nesta página.'),
           ('Como saber o que está aberto agora?', 'No Mapa de Moema da W3W você filtra pelo que está aberto neste momento, busca pelo nome e salva seus favoritos.')]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "ItemList", "name": titulo, "numberOfItems": len(itens), "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "item": {"@type": "LocalBusiness", "name": l['nome'], "address": {"@type": "PostalAddress", "streetAddress": l.get('end') or '', "addressLocality": "São Paulo", "addressRegion": "SP", "addressCountry": "BR"}, "geo": {"@type": "GeoCoordinates", "latitude": l['lat'], "longitude": l['lon']}, **({"telephone": l['tel']} if l.get('tel') else {}), **({"url": l['site']} if l.get('site') else {})}}
            for i, l in enumerate(itens[:60])]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Guia Moema", "item": u('guia-moema')}, {"@type": "ListItem", "position": 2, "name": "Moema por categoria", "item": u('moema')}, {"@type": "ListItem", "position": 3, "name": label}]}]}
    st_ind = f'<div><dt>{len(ind)}</dt><dd>W3W indica</dd></div>' if ind else ''
    sec_ind = ('<section class="mc-sec mc-rv"><h2><span>A W3W <em>indica.</em></span><small>Arraste para o lado →</small></h2><div class="mc-ind">'
               + ''.join(card(l, CM, True, i + 1) for i, l in enumerate(ind)) + '</div></section>') if ind else ''
    fq = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faq)
    lista = ''.join(card(l, CM) for l in resto)
    return (CSS + f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
        f'<main class="mc" style="--k:{cor}">'
        f'<section class="mc-hero"><div class="in mc-hg"><div>'
        f'<nav class="mc-bc" aria-label="Você está em"><a href="{u("guia-moema")}">Guia Moema</a><span>/</span><a href="{u("moema")}">Moema por categoria</a><span>/</span><span>{esc(label)}</span></nav>'
        f'<h1><span class="a">{esc(label)}</span><span class="b">em Moema.</span></h1>'
        f'<p class="lead">{esc(intro)}</p>'
        f'<dl class="mc-st"><div><dt>{len(itens)}</dt><dd>lugares</dd></div>{st_ind}<div><dt>2×</dt><dd>atualizado por semana</dd></div></dl>'
        f'<div class="mc-bt"><a class="mc-cta" href="{u("mapa-moema")}?cat={key}">Ver no mapa →</a><a class="mc-cta g" href="#lista">Ver a lista</a></div>'
        f'</div><div class="mc-art">{art}{tags}</div></div></section>'
        f'<div class="mc-mq" aria-hidden="true"><div>{mq}</div></div>'
        f'<div class="in">{sec_ind}'
        f'<section class="mc-sec" id="lista"><h2 class="mc-rv"><span>Todos de <em>Moema.</em></span><small id="mcN">{len(resto)} lugares</small></h2>'
        f'<div class="mc-fl"><input id="mcQ" type="search" placeholder="Buscar {esc(pal)} pelo nome ou rua" aria-label="Buscar na lista"></div>'
        f'<div class="mc-ls">{lista}</div></section>'
        f'<section class="mc-sec mc-rv"><h2><span>Perguntas <em>frequentes.</em></span></h2><div class="mc-fq">{fq}</div></section>'
        f'<section class="mc-sec mc-rv"><h2><span>Mais de <em>Moema.</em></span></h2><div class="mc-ot">{outros}</div></section>'
        f'<div class="mc-end mc-rv"><h2>Pensando em morar <em>em Moema?</em></h2><a class="mc-cta" href="{wa}" target="_blank" rel="noopener">Fale com a W3W →</a></div>'
        f'</div></main>' + JS)

def render_index(L, CATS, u, wa, img_base='', img_ok=None):
    import moema_idx
    return moema_idx.render(L, cats_validas(L, CATS), u, wa, img_base)
    cs = cats_validas(L, CATS)
    tiles = ''.join(f'<a href="{u("moema/" + c[0])}" style="--c:{c[2]}"><i></i>{esc(c[1])}<small>{n}</small></a>' for c, n in cs)
    mq = ''.join(f'<span>{esc(c[1])}</span>' for c, n in cs) * 2
    return (CSS + '<main class="mc" style="--k:#3A424F">'
        f'<section class="mc-hero"><div class="in mc-hg"><div>'
        f'<nav class="mc-bc"><a href="{u("guia-moema")}">Guia Moema</a><span>/</span><span>Moema por categoria</span></nav>'
        f'<h1><span class="a">Moema,</span><span class="b">por categoria.</span></h1>'
        f'<p class="lead">Restaurantes, cafés, padarias, bares, serviços e lazer: tudo o que existe em Moema, organizado pela W3W Imóveis.</p>'
        f'<dl class="mc-st"><div><dt>{len(L)}</dt><dd>lugares</dd></div><div><dt>{len(cs)}</dt><dd>categorias</dd></div></dl>'
        f'<div class="mc-bt"><a class="mc-cta" href="{u("mapa-moema")}">Abrir o mapa →</a><a class="mc-cta g" href="#cats">Ver categorias</a></div>'
        f'</div><div class="mc-art"><div class="mc-ph"><img src="{img_base}guia/skyline-ibirapuera.jpg" alt="Moema"></div></div></div></section>'
        f'<div class="mc-mq" aria-hidden="true"><div>{mq}</div></div>'
        f'<div class="in"><section class="mc-sec" id="cats"><h2 class="mc-rv"><span>Escolha <em>uma categoria.</em></span></h2><div class="mc-ot">{tiles}</div></section>'
        f'<div class="mc-end mc-rv"><h2>Pensando em morar <em>em Moema?</em></h2><a class="mc-cta" href="{wa}" target="_blank" rel="noopener">Fale com a W3W →</a></div></div></main>' + JS)
