"""Kit Boas-vindas Moema · v002 (enxuta e mais impactante)."""
from deck_icons import svg as ic

WA = 'https://wa.me/5511992460734?text=' + 'Ol%C3%A1%20Wilson!%20Vi%20a%20apresenta%C3%A7%C3%A3o%20do%20Kit%20Boas-vindas%20Moema%20e%20quero%20ser%20parceiro.'

CSS = r'''
:root{--n:#14213D;--n2:#1E2D4F;--c:#FBF6EE;--s:#F2E6D6;--g:#A88B5E;--gl:#D8C4A0;--t:#56607A;--p:#B6BFD0;--e:cubic-bezier(.16,1,.3,1)}
*{box-sizing:border-box;margin:0}
html{scroll-behavior:smooth}
body{background:var(--n);color:var(--c);font:300 18px/1.55 Poppins,system-ui,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{display:block;max-width:100%}
.sf{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-weight:400;letter-spacing:-.01em}
.ey{font:500 12px/1 Poppins;letter-spacing:.32em;text-transform:uppercase;color:var(--gl);display:flex;align-items:center;gap:14px;margin-bottom:28px}
.ey::before{content:"";width:36px;height:1px;background:currentColor}
.lt .ey{color:var(--g)}
h2{font-weight:200;font-size:clamp(44px,6.4vw,104px);letter-spacing:-.045em;line-height:.96}
h2 .sf{color:var(--gl)}.lt h2 .sf{color:var(--g)}
h3{font-weight:400;font-size:21px;line-height:1.25;margin-bottom:6px}
.in{width:min(1280px,calc(100% - 48px));margin:0 auto}
section{position:relative}
.lt{background:var(--c);color:var(--n)}
.mut{color:var(--p)}.lt .mut{color:var(--t)}
.prog{position:fixed;left:0;top:0;height:2px;width:100%;background:var(--g);transform-origin:0 50%;transform:scaleX(0);z-index:60}
.top{position:fixed;left:0;right:0;top:0;z-index:50;display:flex;justify-content:space-between;padding:22px 28px;font:500 11px Poppins;letter-spacing:.24em;text-transform:uppercase;color:#fff;mix-blend-mode:difference;pointer-events:none}
.rv{opacity:0;transform:translateY(46px);transition:opacity 1.2s var(--e),transform 1.2s var(--e)}
.rv.on{opacity:1;transform:none}
.d1{transition-delay:.1s!important}.d2{transition-delay:.2s!important}.d3{transition-delay:.3s!important}.d4{transition-delay:.4s!important}
.ln{display:block;overflow:hidden;padding-bottom:.06em}
.ln>span{display:block;transform:translateY(108%) rotate(2deg);transform-origin:0 100%;transition:transform 1.4s var(--e)}
.on .ln>span{transform:none}
.on .ln:nth-child(2)>span{transition-delay:.12s}.on .ln:nth-child(3)>span{transition-delay:.24s}
/* 1 hero */
.hero{height:100svh;min-height:700px;overflow:hidden}
.hero .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transform-origin:center;will-change:transform}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,33,61,.15) 0%,rgba(20,33,61,.2) 40%,rgba(20,33,61,.92) 100%),linear-gradient(90deg,rgba(20,33,61,.7),transparent 70%)}
.hero .in{position:relative;z-index:2;padding-top:clamp(120px,18vh,200px)}
.hero h1{font-weight:200;font-size:clamp(72px,13vw,230px);line-height:.84;letter-spacing:-.06em}
.hero h1 .sf{color:var(--gl)}
.hero .sub{display:flex;justify-content:space-between;align-items:flex-end;gap:40px;position:absolute;left:0;right:0;bottom:48px;z-index:2}
.hero .sub p{max-width:30ch;font-size:clamp(17px,1.4vw,21px);color:#E6E8EC}
.cue{font:500 10px Poppins;letter-spacing:.3em;text-transform:uppercase;color:var(--gl);display:flex;align-items:center;gap:14px}
.cue i{width:60px;height:1px;background:var(--gl);transform-origin:0 50%;animation:cue 2.4s var(--e) infinite}
@keyframes cue{0%{transform:scaleX(0)}60%{transform:scaleX(1)}100%{transform:scaleX(1);opacity:0}}
/* 2 manifesto */
.man{height:260vh}
.man .mst{position:sticky;top:0;height:100vh;display:flex;align-items:center}
.man p.big{font-weight:200;font-size:clamp(34px,4.6vw,76px);line-height:1.12;letter-spacing:-.035em;max-width:22ch}
.man .w{opacity:.14;transition:opacity .35s linear}
.man .w.on{opacity:1}
.man .w.sf{color:var(--gl)}
/* 3 chegada */
.arr{display:grid;grid-template-columns:1.05fr .95fr;min-height:100vh}
.arr .ph{position:relative;overflow:hidden}
.arr .ph img{position:absolute;inset:-8% 0;width:100%;height:116%;object-fit:cover;will-change:transform}
.arr .tx{padding:clamp(90px,13vh,170px) clamp(28px,5vw,88px);display:flex;flex-direction:column;justify-content:center}
.kit4{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:44px}
.kc{border-radius:22px;padding:24px;background:#FFFDF8;box-shadow:0 20px 50px -36px rgba(20,33,61,.5);transition:transform .6s var(--e)}
.kc:hover{transform:translateY(-5px)}
.kc svg{width:28px;height:28px;color:var(--g);margin-bottom:18px}
.kc p{font-size:15px;color:var(--t)}
/* 4 jornada */
.hz{height:360vh}
.hz .stick{position:sticky;top:0;height:100vh;overflow:hidden;display:flex;flex-direction:column;justify-content:center}
.hz .track{display:flex;gap:24px;padding:0 max(24px,calc((100vw - 1280px)/2));margin-top:52px;will-change:transform}
.jc{flex:none;width:min(400px,80vw);height:min(480px,58vh);border-radius:30px;overflow:hidden;position:relative;background:var(--n2);border:1px solid rgba(255,255,255,.08);display:flex;flex-direction:column;justify-content:flex-end;padding:34px}
.jc img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.55}
.jc::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 30%,rgba(20,33,61,.95))}
.jc>*:not(img){position:relative;z-index:1}
.jc .num{position:absolute;top:22px;right:28px;font:200 110px/1 Poppins;letter-spacing:-.05em;color:rgba(216,196,160,.22);z-index:1}
.jc .d{font:500 11px Poppins;letter-spacing:.28em;text-transform:uppercase;color:var(--gl);margin-bottom:12px}
.jc h3{font-size:32px;font-weight:300;letter-spacing:-.02em}
.jc.hi{background:var(--g);border:0}.jc.hi::after{background:linear-gradient(180deg,transparent 20%,rgba(20,33,61,.9))}
.hint{margin-top:36px;font:500 11px Poppins;letter-spacing:.24em;text-transform:uppercase;color:var(--p)}
/* 5 acordo */
.deal{display:grid;grid-template-columns:1fr 1fr;min-height:100vh}
.deal .ph{position:sticky;top:0;height:100vh;overflow:hidden}
.deal .ph img{width:100%;height:100%;object-fit:cover;transform:scale(1.1);transition:transform 2.6s var(--e)}
.deal .ph.on img{transform:scale(1)}
.deal .ph .lbl{position:absolute;left:32px;bottom:32px;padding:14px 20px;border-radius:999px;background:rgba(20,33,61,.7);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);font:500 12px Poppins;letter-spacing:.18em;text-transform:uppercase;color:var(--gl)}
.deal .tx{padding:clamp(100px,14vh,170px) clamp(28px,5vw,88px)}
.col h4{font:500 12px Poppins;letter-spacing:.28em;text-transform:uppercase;color:var(--g);margin:56px 0 8px}
.li{display:grid;grid-template-columns:40px 1fr;gap:2px 16px;padding:18px 0;border-top:1px solid rgba(20,33,61,.12)}
.li svg{width:26px;height:26px;color:var(--g);grid-row:span 2}
.li p{grid-column:2;font-size:15px;color:var(--t)}
.li .n{font-family:'Instrument Serif',serif;font-style:italic;font-size:30px;line-height:1.1}
/* 6 conta */
.conta{padding:clamp(110px,16vh,190px) 0}
.cg{display:grid;grid-template-columns:auto 1fr;gap:clamp(30px,5vw,80px);align-items:end;margin-top:72px}
.n1{font:200 clamp(160px,20vw,320px)/.8 Poppins;letter-spacing:-.07em;color:var(--gl)}
.n52{font:200 clamp(160px,20vw,320px)/.8 Poppins;letter-spacing:-.07em}
.bars{display:flex;align-items:flex-end;gap:4px;height:120px;margin-top:28px}
.bars i{flex:1;background:var(--g);border-radius:2px 2px 0 0;transform:scaleY(0);transform-origin:bottom;transition:transform .9s var(--e)}
.cg.on .bars i{transform:scaleY(1)}
.cap{font-size:14px;color:var(--p);margin-top:44px}
/* 7 como */
.como{padding:clamp(110px,16vh,190px) 0}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:72px;position:relative}
.steps::before{content:"";position:absolute;left:32px;right:32px;top:31px;height:1px;background:var(--g);transform:scaleX(0);transform-origin:0 50%;transition:transform 1.8s var(--e)}
.steps.on::before{transform:scaleX(1)}
.st .dot{width:64px;height:64px;border-radius:50%;background:var(--n);color:var(--c);display:grid;place-items:center;margin-bottom:26px;position:relative}
.st .dot svg{width:26px;height:26px}
.st.hi .dot{background:var(--g)}
.st .w{font:500 11px Poppins;letter-spacing:.26em;text-transform:uppercase;color:var(--g);margin-bottom:8px}
.chips{display:flex;flex-wrap:wrap;gap:12px;margin-top:64px}
.chips span{display:inline-flex;align-items:center;gap:10px;padding:14px 22px;border-radius:999px;background:var(--s);font-size:15px}
.chips svg{width:20px;height:20px;color:var(--g)}
/* 8 fim */
.fim{min-height:100svh;overflow:hidden;display:flex;align-items:center}
.fim .bg{position:absolute;inset:-8% 0;width:100%;height:116%;object-fit:cover;will-change:transform}
.fim::before{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(20,33,61,.95),rgba(20,33,61,.6) 55%,rgba(20,33,61,.2))}
.fim .in{position:relative;z-index:2}
.fim h2{font-size:clamp(58px,9vw,150px)}
.btn{display:inline-flex;align-items:center;gap:14px;margin-top:52px;padding:22px 34px;border-radius:999px;background:var(--c);color:var(--n);text-decoration:none;font:500 17px Poppins;transition:transform .5s var(--e),gap .5s var(--e)}
.btn:hover{transform:translateY(-3px);gap:22px}
.ct{display:flex;gap:64px;flex-wrap:wrap;margin-top:56px;font-size:16px}
.ct small{display:block;font:500 11px Poppins;letter-spacing:.24em;text-transform:uppercase;color:var(--gl);margin-bottom:8px}
@media(max-width:900px){
.hero .sub{flex-direction:column;align-items:flex-start;bottom:32px;gap:20px}
.man{height:200vh}
.arr,.deal{grid-template-columns:1fr}
.arr .ph{height:62vh}
.deal .ph{position:relative;height:62vh}
.kit4{grid-template-columns:1fr 1fr}
.hz{height:auto}.hz .stick{position:relative;height:auto;padding:110px 0}
.hz .track{overflow-x:auto;scroll-snap-type:x mandatory;transform:none!important;padding:0 24px 16px}
.jc{scroll-snap-align:start;height:440px}
.cg{grid-template-columns:1fr}
.steps{grid-template-columns:1fr 1fr;gap:40px 20px}.steps::before{display:none}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.rv,.ln>span{opacity:1;transform:none}.man .w{opacity:1}}
'''

JS = r'''
(()=>{
const R=matchMedia('(prefers-reduced-motion: reduce)').matches;
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{threshold:.2});
document.querySelectorAll('.rv,.lnw,.cg,.steps,.deal .ph').forEach(el=>io.observe(el));
const prog=document.querySelector('.prog'),hero=document.querySelector('.hero .bg'),par=[...document.querySelectorAll('[data-par]')];
const man=document.querySelector('.man'),words=[...document.querySelectorAll('.man .w')];
const hz=document.querySelector('.hz'),track=hz.querySelector('.track');
const n52=document.querySelector('.n52');let go=false;
document.querySelectorAll('.bars i').forEach((b,i)=>b.style.transitionDelay=(i*.02)+'s');
function f(){const y=scrollY,h=innerHeight;
prog.style.transform=`scaleX(${y/(document.documentElement.scrollHeight-h)})`;
if(!R){hero.style.transform=`scale(${1.12-Math.min(y/h,1)*.12}) translateY(${y*.25}px)`;
par.forEach(el=>{const r=el.parentElement.getBoundingClientRect();if(r.bottom<0||r.top>h)return;const p=(r.top+r.height/2-h/2)/h;el.style.transform=`translate3d(0,${p*(+el.dataset.par)*90}px,0)`});}
{const r=man.getBoundingClientRect();const p=Math.min(1,Math.max(0,(-r.top+h*.35)/(man.offsetHeight-h*.6)));const k=Math.round(p*words.length);words.forEach((w,i)=>w.classList.toggle('on',R||i<k));}
if(innerWidth>900){const r=hz.getBoundingClientRect();const p=Math.min(1,Math.max(0,-r.top/(hz.offsetHeight-h)));track.style.transform=`translate3d(${-p*(track.scrollWidth-innerWidth)}px,0,0)`;}
if(!go&&n52.getBoundingClientRect().top<h*.8){go=true;let t0;const run=t=>{t0=t0||t;const k=Math.min(1,(t-t0)/1600);n52.textContent=Math.round(52*(1-Math.pow(1-k,4)));k<1&&requestAnimationFrame(run)};R?n52.textContent='52':requestAnimationFrame(run)}
}
let tk;addEventListener('scroll',()=>{if(!tk){tk=requestAnimationFrame(()=>{f();tk=0})}},{passive:true});addEventListener('resize',f);f();
})();
'''

MAN = ("Todo mês, novos vizinhos chegam a Moema. Eles ainda não têm a padaria, o restaurante, o pet shop de confiança. "
       "A W3W entrega as chaves *e apresenta o bairro.*")

def manifesto():
    out, it = [], False
    for w in MAN.split(' '):
        s = w
        if s.startswith('*'): it, s = True, s[1:]
        end = s.endswith('*')
        if end: s = s[:-1]
        out.append(f'<span class="w{" sf" if it else ""}">{s}</span>')
        if end: it = False
    return ' '.join(out)

def render(IMG):
    bars = ''.join(f'<i style="height:{55+((i*53+i*i*7)%45)}%"></i>' for i in range(52))
    jor = [('Dia 0','Recebe as chaves','e, junto, o kit da W3W.',None),('Dia 1','Abre o mapa','e descobre os parceiros do bairro.',None),('Dia 4','Visita você','mostra o QR e usa a cortesia.','padaria'),('Semana 3','Volta sozinha','agora pagando, porque gostou.','mesa'),('Mês 6','Cliente da casa','e indica aos vizinhos.','casal')]
    jc = ''.join(f'<article class="jc{" hi" if i==2 else ""}">' + (f'<img src="{IMG}{im}.jpg" alt="" loading="lazy">' if im else '') + f'<span class="num">0{i+1}</span><p class="d">{d}</p><h3>{t}</h3><p class="mut">{s}</p></article>' for i,(d,t,s,im) in enumerate(jor))
    oferece = [('Coffee','Padarias e cafés','Café com pão na chapa ou um doce.'),('UtensilsCrossed','Restaurantes','Sobremesa, entrada ou bebida.'),('Wine','Bares','Um drinque de boas-vindas.'),('PawPrint','Pet, beleza e serviços','Primeiro banho, aula ou desconto.')]
    recebe = [('UserPlus','Clientes novos e locais','Moradores que ainda vão escolher seus lugares.'),('Repeat','Frequência por anos','Quem mora perto volta toda semana.'),('Megaphone','Divulgação sem custo','Mapa de Moema, Guia e Instagram W3W.'),('BadgeCheck','Selo de parceiro','“Parceiro W3W Moema” na porta.')]
    steps = [('Handshake','Semana 1','Adesão','Conversa, cortesia e termo de uma página.'),('Camera','Semana 2','Fotos e selo','Entrada no mapa e selo na porta.'),('Megaphone','Semana 3','Divulgação','Post e páginas do bairro.'),('Users','Todo mês','Novos moradores','Kits entregues e resumo do mês.')]
    li = lambda a,b,c: f'<div class="li rv">{ic(a)}<p class="n">{b}</p><p>{c}</p></div>'
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Kit Boas-vindas Moema · W3W Imóveis</title><meta name="description" content="Proposta de parceria da W3W Imóveis para estabelecimentos de Moema.">
<meta property="og:title" content="Kit Boas-vindas Moema · W3W Imóveis"><meta property="og:description" content="Quem se muda para Moema com a W3W conhece o seu negócio na primeira semana."><meta property="og:image" content="{IMG}capa.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500&family=Instrument+Serif:ital@0;1&display=swap">
<style>{CSS}</style></head><body>
<div class="prog"></div><div class="top"><span>W3W Imóveis</span><span>Proposta de parceria</span></div>

<section class="hero"><img class="bg" src="{IMG}capa.jpg" alt="Rua arborizada de Moema com cafés na calçada ao entardecer">
<div class="in"><p class="ey rv on">Kit Boas-vindas · para estabelecimentos de Moema</p>
<h1 class="lnw"><span class="ln"><span>Bem-vindo</span></span><span class="ln"><span class="sf">ao bairro.</span></span></h1></div>
<div class="sub in"><p class="rv d3">Quem se muda para Moema com a W3W conhece o seu negócio na primeira semana.</p><div class="cue rv d4"><i></i>Role para conhecer</div></div></section>

<section class="man"><div class="mst"><div class="in"><p class="ey">A ideia</p><p class="big">{manifesto()}</p></div></div></section>

<section class="arr lt"><div class="ph"><img data-par=".5" src="{IMG}chegada.jpg" alt="Nova moradora chegando ao apartamento com uma caixa de presente"></div>
<div class="tx"><p class="ey rv">O kit</p><h2 class="rv d1">Um presente na <span class="sf">entrega das chaves.</span></h2>
<div class="kit4"><div class="kc rv d1">{ic('Mail')}<h3>Carta</h3><p>Boas-vindas assinada pelos sócios.</p></div><div class="kc rv d2">{ic('Map')}<h3>Mapa ilustrado</h3><p>Moema com cada parceiro marcado.</p></div><div class="kc rv d3">{ic('Ticket')}<h3>Cortesias</h3><p>Uma por parceiro, com QR no nome.</p></div><div class="kc rv d4">{ic('Smartphone')}<h3>No celular</h3><p>Versão digital, válida por 90 dias.</p></div></div></div></section>

<section class="hz"><div class="stick"><div class="in"><p class="ey rv">Na prática</p><h2 class="rv d1">A jornada <span class="sf">de um novo vizinho.</span></h2></div>
<div class="track">{jc}</div><div class="in"><p class="hint">A cortesia acontece uma vez. O resto são visitas pagas.</p></div></div></section>

<section class="deal lt"><div class="ph"><img src="{IMG}mesa.jpg" alt="Mesa com café, croissant, sobremesa e drinque"><span class="lbl">O acordo</span></div>
<div class="tx"><p class="ey rv">O acordo</p><h2 class="rv d1">Você oferece pouco. <span class="sf">Recebe muito.</span></h2>
<div class="col"><h4 class="rv">Você oferece · uma cortesia simples</h4>{''.join(li(*x) for x in oferece)}
<h4 class="rv">Você recebe</h4>{''.join(li(*x) for x in recebe)}</div></div></section>

<section class="conta"><div class="in"><p class="ey rv">A conta</p><h2 class="rv d1">Uma cortesia hoje. <span class="sf">Um cliente por anos.</span></h2>
<div class="cg"><div><p class="n1">1</p><p class="mut" style="margin-top:18px">cortesia, uma única vez</p></div>
<div><div style="display:flex;align-items:flex-end;gap:28px;flex-wrap:wrap"><p class="n52">0</p><div style="padding-bottom:14px"><h3>visitas pagas no ano</h3><p class="mut">se o novo morador voltar uma vez por semana</p></div></div><div class="bars">{bars}</div></div></div>
<p class="cap rv">Exemplo ilustrativo. Multiplique pelo seu gasto médio por visita.</p></div></section>

<section class="como lt"><div class="in"><p class="ey rv">Como começar</p><h2 class="rv d1">Do aperto de mão <span class="sf">ao primeiro cliente.</span></h2>
<div class="steps">{''.join(f'<div class="st rv d{i+1}{" hi" if i==2 else ""}"><div class="dot">{ic(a)}</div><p class="w">{b}</p><h3>{c}</h3><p class="mut">{d}</p></div>' for i,(a,b,c,d) in enumerate(steps))}</div>
<div class="chips rv"><span>{ic('ShieldCheck')}Sem custo para entrar</span><span>{ic('CalendarDays')}Cortesia válida por 90 dias</span><span>{ic('RefreshCw')}12 meses, saída com 60 dias de aviso</span><span>{ic('Star')}Um parceiro por categoria</span></div></div></section>

<section class="fim"><img class="bg" data-par=".5" src="{IMG}final.jpg" alt="Mesa de restaurante à noite em Moema">
<div class="in"><p class="ey rv">Vamos conversar</p><h2 class="lnw"><span class="ln"><span>Seja o primeiro</span></span><span class="ln"><span class="sf">endereço deles.</span></span></h2>
<a class="btn rv d2" href="{WA}" target="_blank" rel="noopener">Quero ser parceiro <span>→</span></a>
<div class="ct rv d3"><div><small>Comercial</small>Wilson Rodrigues<br><span class="mut">WhatsApp +55 11 99246-0734</span></div><div><small>W3W Imóveis</small>Curadoria imobiliária em Moema<br><span class="mut">Guia Moema · Mapa de Moema</span></div></div></div></section>
<script>{JS}</script></body></html>'''
