"""Apresentação web: Kit Boas-vindas Moema (W3W) — /deck/kit-boas-vindas-moema/"""
import sys

try:
    from deck_icons import svg as _svg
except Exception:  # fallback sem ícones
    _svg = lambda n, s=None, c='currentColor': ''

def ic(n):
    return _svg(n)

IMG = '../../../w3w-img/deck/kit/'
WA = 'https://wa.me/5511992460734?text=' + 'Ol%C3%A1%20Wilson!%20Vi%20a%20apresenta%C3%A7%C3%A3o%20do%20Kit%20Boas-vindas%20Moema%20e%20quero%20conversar%20sobre%20a%20parceria.'

CSS = r'''
:root{--n:#14213D;--n2:#1E2D4F;--c:#FBF6EE;--s:#F2E6D6;--g:#A88B5E;--gl:#D8C4A0;--t:#56607A;--p:#B6BFD0;--e:cubic-bezier(.16,1,.3,1)}
*{box-sizing:border-box;margin:0}
html{scroll-behavior:smooth}
body{background:var(--c);color:var(--n);font:300 18px/1.55 Poppins,system-ui,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{display:block;max-width:100%}
.sf{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-weight:400;letter-spacing:-.01em}
.ey{font:500 12px/1 Poppins;letter-spacing:.32em;text-transform:uppercase;color:var(--g);display:flex;align-items:center;gap:14px;margin-bottom:28px}
.ey::before{content:"";width:36px;height:1px;background:currentColor}
.dk .ey{color:var(--gl)}
h1,h2{font-weight:200;letter-spacing:-.04em;line-height:.98}
h2{font-size:clamp(42px,6vw,96px);max-width:16ch}
h2 .sf,h1 .sf{color:var(--g)}
.dk h2 .sf,.dk h1 .sf{color:var(--gl)}
h3{font-weight:400;font-size:22px;line-height:1.25;margin-bottom:6px}
.mut{color:var(--t)}
.dk .mut{color:var(--p)}
.in{width:min(1240px,calc(100% - 48px));margin:0 auto}
section{position:relative}
.pad{padding:clamp(100px,14vh,180px) 0}
.dk{background:var(--n);color:var(--c)}
.sand{background:var(--s)}
/* barra de progresso e topo */
.prog{position:fixed;left:0;top:0;height:2px;width:100%;background:var(--g);transform-origin:0 50%;transform:scaleX(0);z-index:50}
.top{position:fixed;left:0;right:0;top:0;z-index:40;display:flex;justify-content:space-between;align-items:center;padding:22px 28px;font:500 11px Poppins;letter-spacing:.24em;text-transform:uppercase;color:var(--c);mix-blend-mode:difference;pointer-events:none}
.top a{pointer-events:auto;color:inherit;text-decoration:none}
/* revelar */
.rv{opacity:0;transform:translateY(40px);transition:opacity 1.1s var(--e),transform 1.1s var(--e)}
.rv.on{opacity:1;transform:none}
.rv.d1{transition-delay:.08s}.rv.d2{transition-delay:.16s}.rv.d3{transition-delay:.24s}.rv.d4{transition-delay:.32s}.rv.d5{transition-delay:.4s}
.ln{display:block;overflow:hidden;padding-bottom:.08em}
.ln>span{display:block;transform:translateY(105%);transition:transform 1.2s var(--e)}
.on .ln>span,.ln.on>span{transform:none}
.on .ln:nth-child(2)>span{transition-delay:.1s}.on .ln:nth-child(3)>span{transition-delay:.2s}
/* hero */
.hero{height:100svh;min-height:680px;overflow:hidden;color:var(--c);display:flex;align-items:flex-start}
.hero .bg{position:absolute;inset:-8% 0;width:100%;height:116%;object-fit:cover;will-change:transform}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(100deg,rgba(20,33,61,.92) 0%,rgba(20,33,61,.6) 45%,rgba(20,33,61,.15) 100%)}
.hero .in{position:relative;z-index:2;padding-top:clamp(130px,20vh,220px)}
.hero h1{font-size:clamp(64px,11vw,184px);line-height:.88}
.hero .lead{font-size:clamp(18px,1.6vw,24px);max-width:34ch;margin-top:36px;color:#E3E6EA}
.cue{position:absolute;left:50%;bottom:34px;z-index:2;transform:translateX(-50%);font:500 10px Poppins;letter-spacing:.3em;text-transform:uppercase;color:var(--gl);display:flex;flex-direction:column;align-items:center;gap:12px}
.cue i{width:1px;height:46px;background:linear-gradient(var(--gl),transparent);animation:cue 2.2s var(--e) infinite}
@keyframes cue{0%{transform:scaleY(0);transform-origin:top}50%{transform:scaleY(1);transform-origin:top}51%{transform-origin:bottom}100%{transform:scaleY(0);transform-origin:bottom}}
/* contexto */
.ctx{display:grid;grid-template-columns:1fr 1fr;min-height:100vh}
.ctx .ph{position:relative;overflow:hidden}
.ctx .ph img{position:absolute;inset:-10% 0;width:100%;height:120%;object-fit:cover;will-change:transform}
.ctx .tx{padding:clamp(80px,12vh,160px) clamp(28px,6vw,96px);display:flex;flex-direction:column;justify-content:center}
.strike p{font-weight:200;font-size:clamp(28px,3vw,46px);line-height:1.35;letter-spacing:-.02em;color:var(--n);transition:color .8s var(--e)}
.strike p span{background:linear-gradient(var(--g),var(--g)) 0 60%/0% 2px no-repeat;-webkit-box-decoration-break:clone;box-decoration-break:clone;transition:background-size .9s var(--e)}
.strike.on p{color:var(--p)}
.strike.on p span{background-size:100% 2px}
.strike.on p:nth-child(2),.strike.on p:nth-child(2) span{transition-delay:.25s}
.strike.on p:nth-child(3),.strike.on p:nth-child(3) span{transition-delay:.5s}
.strike.on p:nth-child(4),.strike.on p:nth-child(4) span{transition-delay:.75s}
/* ideia */
.dia{margin-top:80px}
.dia svg{width:100%;height:auto;overflow:visible}
.dia .draw{stroke-dasharray:400;stroke-dashoffset:400;transition:stroke-dashoffset 1.6s var(--e)}
.dia.on .draw{stroke-dashoffset:0}
.dia .nd{opacity:0;transform:scale(.6);transform-box:fill-box;transform-origin:center;transition:all 1s var(--e)}
.dia.on .nd{opacity:1;transform:none}
.dia.on .nd2{transition-delay:.35s}.dia.on .nd3{transition-delay:.7s}
/* pilares */
.pil{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:64px}
.card{background:#FFFDF8;border-radius:28px;padding:36px 32px;box-shadow:0 24px 60px -40px rgba(20,33,61,.4);transition:transform .6s var(--e),box-shadow .6s var(--e)}
.card:hover{transform:translateY(-6px);box-shadow:0 40px 80px -40px rgba(20,33,61,.5)}
.dk .card{background:var(--n2);box-shadow:none;border:1px solid rgba(255,255,255,.08)}
.chip{width:56px;height:56px;border-radius:16px;background:var(--n);color:var(--c);display:grid;place-items:center;margin-bottom:26px}
.dk .chip{background:var(--gl);color:var(--n)}
.chip svg,.ico{width:26px;height:26px}
/* kit */
.kitg{display:grid;grid-template-columns:.9fr 1.1fr;gap:clamp(40px,6vw,100px);align-items:center}
.box{animation:flo 7s ease-in-out infinite}
@keyframes flo{50%{transform:translateY(-14px) rotate(-.6deg)}}
.row{display:grid;grid-template-columns:56px 1fr;gap:4px 22px;padding:24px 0;border-top:1px solid rgba(20,33,61,.12)}
.row .chip{margin:0;grid-row:span 2}
/* jornada horizontal */
.hz{height:340vh}
.hz .stick{position:sticky;top:0;height:100vh;overflow:hidden;display:flex;flex-direction:column;justify-content:center}
.hz .track{display:flex;gap:28px;padding:0 calc((100vw - min(1240px,100vw - 48px))/2);will-change:transform;margin-top:56px}
.jc{flex:none;width:min(420px,78vw);min-height:420px;border-radius:32px;padding:40px 36px;background:#FFFDF8;box-shadow:0 30px 70px -45px rgba(20,33,61,.45);display:flex;flex-direction:column}
.jc .d{font:500 12px Poppins;letter-spacing:.28em;text-transform:uppercase;color:var(--g);margin-bottom:auto}
.jc .big{font:200 120px/1 Poppins;letter-spacing:-.05em;color:var(--s);margin:20px 0 18px}
.jc h3{font-size:30px;font-weight:300;letter-spacing:-.02em}
.jc.hi{background:var(--n);color:var(--c)}
.jc.hi .big{color:var(--g)}.jc.hi .mut{color:var(--p)}
.hint{font:500 11px Poppins;letter-spacing:.24em;text-transform:uppercase;color:var(--t);margin-top:40px}
/* banda de imagem com parallax */
.band{height:min(70vh,640px);overflow:hidden;position:relative}
.band img{position:absolute;inset:-15% 0;width:100%;height:130%;object-fit:cover;will-change:transform}
.band .cap{position:absolute;left:0;right:0;bottom:0;padding:40px 0;background:linear-gradient(transparent,rgba(20,33,61,.75));color:var(--c)}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:64px}
.k{font:500 12px Poppins;letter-spacing:.26em;text-transform:uppercase;color:var(--g);margin-bottom:22px}
.qr{display:grid;grid-template-columns:repeat(7,1fr);gap:3px;width:96px;height:96px;margin-bottom:22px}
.qr span{background:var(--n);border-radius:2px}.qr span.o{background:transparent}
/* split com imagem fixa */
.split{display:grid;grid-template-columns:1fr 1fr;min-height:100vh}
.split .ph{position:sticky;top:0;height:100vh;overflow:hidden}
.split .ph img{width:100%;height:100%;object-fit:cover;transform:scale(1.08);transition:transform 2.4s var(--e)}
.split .ph.on img{transform:scale(1)}
.split .tx{padding:clamp(100px,14vh,180px) clamp(28px,6vw,96px)}
.menu .mi{display:grid;grid-template-columns:52px 1fr;gap:4px 18px;padding:26px 0;border-top:1px solid rgba(20,33,61,.12)}
.menu .mi .n{font-family:'Instrument Serif',serif;font-style:italic;font-size:36px;line-height:1.05}
.menu .mi svg{width:34px;height:34px;color:var(--g)}
.menu .mi p{grid-column:2;color:var(--t)}
.tag{display:inline-flex;gap:10px;align-items:center;margin-top:36px;padding:12px 20px;border-radius:999px;background:var(--s);font:500 12px Poppins;letter-spacing:.16em;text-transform:uppercase}
.gl{display:grid;grid-template-columns:1fr 1fr;gap:0 40px;margin-top:48px}
.gi{display:grid;grid-template-columns:44px 1fr;gap:4px 16px;padding:24px 0;border-top:1px solid rgba(255,255,255,.12)}
.gi svg{width:30px;height:30px;color:var(--gl)}
.gi p{grid-column:2;color:var(--p);font-size:16px}
/* conta */
.conta{display:grid;grid-template-columns:320px 1fr;gap:56px;align-items:end;margin-top:72px}
.one{background:var(--n);color:var(--c);border-radius:28px;padding:36px}
.one b{display:block;font:200 120px/1 Poppins;letter-spacing:-.05em;margin:18px 0 8px}
.bars{display:flex;align-items:flex-end;gap:5px;height:260px;border-bottom:1px solid var(--s)}
.bars i{flex:1;background:var(--g);border-radius:3px 3px 0 0;transform:scaleY(0);transform-origin:bottom;transition:transform 1s var(--e)}
.conta.on .bars i{transform:scaleY(1)}
.cnt{font:200 clamp(80px,9vw,140px)/1 Poppins;letter-spacing:-.05em}
/* vitrine */
.vit{min-height:110vh;color:var(--c);overflow:hidden;display:flex;align-items:flex-end}
.vit .bg{position:absolute;inset:-10% 0;width:100%;height:120%;object-fit:cover;will-change:transform}
.vit::before{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(0deg,rgba(20,33,61,.96) 10%,rgba(20,33,61,.55) 60%,rgba(20,33,61,.3))}
.vit .in{position:relative;z-index:2;padding-bottom:clamp(80px,12vh,140px)}
.c4{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:56px}
.glass{background:rgba(255,255,255,.07);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.14);border-radius:24px;padding:30px 28px}
.glass .chip{background:var(--gl);color:var(--n)}
.glass p{color:var(--p);font-size:16px}
/* regras */
.reg{display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(40px,6vw,100px);align-items:center}
.paper{background:#FFFDF8;border-radius:8px;padding:56px;box-shadow:0 50px 100px -50px rgba(20,33,61,.5);transform:rotate(-2.5deg)}
.paper .pl{height:9px;border-radius:5px;background:var(--s);margin:15px 0}
.paper .sig{display:flex;gap:30px;margin-top:50px}
.paper .sig div{flex:1;border-top:1.5px solid var(--n);padding-top:10px;font-size:14px;color:var(--t)}
.tl{display:grid;grid-template-columns:repeat(2,1fr);gap:0 40px}
.tl .row{grid-template-columns:44px 1fr}
.tl .row svg{width:30px;height:30px;color:var(--g);grid-row:span 2}.tl .row p{grid-column:2}
/* começar */
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:72px;position:relative}
.steps::before{content:"";position:absolute;left:36px;right:36px;top:35px;height:1px;background:var(--g);transform:scaleX(0);transform-origin:0 50%;transition:transform 1.6s var(--e)}
.steps.on::before{transform:scaleX(1)}
.st .dot{width:72px;height:72px;border-radius:50%;background:var(--n);color:var(--c);display:grid;place-items:center;position:relative;margin-bottom:28px}
.st.hi .dot{background:var(--g)}
.st .w{font:500 12px Poppins;letter-spacing:.24em;text-transform:uppercase;color:var(--g);margin-bottom:8px}
/* fim */
.fim{min-height:100svh;color:var(--c);overflow:hidden;display:flex;align-items:center}
.fim .bg{position:absolute;inset:-10% 0;width:100%;height:120%;object-fit:cover;will-change:transform}
.fim::before{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(100deg,rgba(20,33,61,.94),rgba(20,33,61,.55) 60%,rgba(20,33,61,.25))}
.fim .in{position:relative;z-index:2}
.fim h2{font-size:clamp(56px,8.5vw,140px);max-width:12ch}
.btn{display:inline-flex;align-items:center;gap:12px;margin-top:48px;padding:20px 32px;border-radius:999px;background:var(--c);color:var(--n);text-decoration:none;font:500 16px Poppins;transition:transform .5s var(--e),background .3s}
.btn:hover{transform:translateY(-3px);background:#fff}
.ct{display:flex;gap:64px;margin-top:56px;flex-wrap:wrap}
.ct small{display:block;font:500 11px Poppins;letter-spacing:.24em;text-transform:uppercase;color:var(--gl);margin-bottom:8px}
@media(max-width:900px){
.ctx,.split,.kitg,.reg{grid-template-columns:1fr}
.ctx .ph{height:60vh}.split .ph{position:relative;height:70vh}
.pil,.three,.c4,.steps,.gl,.tl{grid-template-columns:1fr}
.conta{grid-template-columns:1fr}
.steps::before{display:none}
.hz{height:auto}.hz .stick{position:relative;height:auto;padding:100px 0}
.hz .track{overflow-x:auto;scroll-snap-type:x mandatory;transform:none!important;padding:0 24px 20px}
.jc{scroll-snap-align:start}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.rv,.ln>span{opacity:1;transform:none}}
'''

JS = r'''
(()=>{
const R=matchMedia('(prefers-reduced-motion: reduce)').matches;
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{threshold:.18});
document.querySelectorAll('.rv,.strike,.dia,.conta,.steps,.split .ph,.lnw').forEach(el=>io.observe(el));
const prog=document.querySelector('.prog'),par=[...document.querySelectorAll('[data-par]')],hz=document.querySelector('.hz'),track=hz&&hz.querySelector('.track');
let cnt=document.querySelector('.cnt'),done=false;
function f(){const y=scrollY,h=innerHeight;
prog.style.transform=`scaleX(${y/(document.documentElement.scrollHeight-h)})`;
if(!R){par.forEach(el=>{const r=el.parentElement.getBoundingClientRect();if(r.bottom<0||r.top>h)return;const k=+el.dataset.par;const p=(r.top+r.height/2-h/2)/h;el.style.transform=`translate3d(0,${p*k*100}px,0) scale(1.02)`});}
if(track&&innerWidth>900){const r=hz.getBoundingClientRect();const tot=hz.offsetHeight-h;const p=Math.min(1,Math.max(0,-r.top/tot));const max=track.scrollWidth-innerWidth;track.style.transform=`translate3d(${-p*max}px,0,0)`;}
if(cnt&&!done){const r=cnt.getBoundingClientRect();if(r.top<h*.85){done=true;let t0=null;const run=t=>{t0=t0||t;const k=Math.min(1,(t-t0)/1400);cnt.textContent=Math.round(52*(1-Math.pow(1-k,3)));if(k<1)requestAnimationFrame(run)};R?cnt.textContent='52':requestAnimationFrame(run)}}
}
let tk=false;addEventListener('scroll',()=>{if(!tk){tk=true;requestAnimationFrame(()=>{f();tk=false})}},{passive:true});addEventListener('resize',f);f();
document.querySelectorAll('.bars i').forEach((b,i)=>{b.style.transitionDelay=(i*0.018)+'s'});
})();
'''

def render():
    qr = ''.join(f'<span class="{"" if c=="1" else "o"}"></span>' for c in "1110111100101110111011010001101110110100111101111")
    bars = ''.join(f'<i style="height:{58+((i*53+i*i*7)%41)}%"></i>' for i in range(52))
    box = '''<svg class="box" viewBox="0 0 760 760" aria-label="Ilustração do kit: caixa aberta com carta, mapa e cartão de cortesia"><ellipse cx="380" cy="690" rx="300" ry="34" fill="#14213D" opacity=".08"/><path d="M120 380 L380 470 L640 380 L640 640 L380 730 L120 640 Z" fill="#1E2D4F"/><path d="M380 470 L380 730 L640 640 L640 380 Z" fill="#14213D"/><g transform="rotate(-8 300 300)"><rect x="170" y="150" width="300" height="380" rx="10" fill="#FFFDF8" stroke="#F2E6D6" stroke-width="2"/><text x="200" y="215" font-family="Poppins" font-size="22" letter-spacing="4" fill="#A88B5E">BEM-VINDO</text><text x="200" y="270" font-family="Instrument Serif" font-style="italic" font-size="52" fill="#14213D">a Moema.</text></g><g transform="rotate(6 470 300)"><rect x="360" y="170" width="250" height="330" rx="10" fill="#F2E6D6"/><path d="M380 210 L590 250 M380 300 L590 260 M420 190 L460 490 M520 190 L500 490" stroke="#FBF6EE" stroke-width="10"/><circle cx="455" cy="300" r="12" fill="#14213D"/><circle cx="530" cy="380" r="12" fill="#A88B5E"/></g><path d="M120 380 L380 470 L380 520 L120 430 Z" fill="#2A3A5E"/><path d="M380 470 L640 380 L640 430 L380 520 Z" fill="#1E2D4F"/><g transform="translate(-20,-120)"><rect x="230" y="420" width="360" height="170" rx="14" fill="#A88B5E"/><text x="256" y="470" font-family="Poppins" font-size="20" letter-spacing="3" fill="#14213D">CORTESIA</text><text x="256" y="530" font-family="Poppins" font-weight="300" font-size="28" fill="#14213D">Café da manhã</text><rect x="500" y="440" width="64" height="64" fill="#14213D"/><rect x="512" y="452" width="16" height="16" fill="#A88B5E"/><rect x="536" y="476" width="16" height="16" fill="#A88B5E"/></g></svg>'''
    dia = '''<svg viewBox="0 0 1240 360" aria-label="A W3W entrega o kit ao novo morador, que vem conhecer o seu negócio"><g font-family="Poppins">
<g class="nd"><circle cx="160" cy="170" r="140" fill="#1E2D4F" stroke="#A88B5E" stroke-width="2"/><text x="160" y="164" fill="#FBF6EE" font-size="42" font-weight="200" text-anchor="middle">W3W</text><text x="160" y="204" fill="#B6BFD0" font-size="18" letter-spacing="4" text-anchor="middle">IMÓVEIS</text></g>
<path class="draw" d="M310 170 L460 170" stroke="#A88B5E" stroke-width="2"/><text x="385" y="146" fill="#D8C4A0" font-size="18" text-anchor="middle">entrega o kit</text>
<g class="nd nd2"><circle cx="620" cy="170" r="140" fill="#FBF6EE"/><text x="620" y="162" fill="#14213D" font-size="34" font-weight="300" text-anchor="middle">Novo</text><text x="620" y="202" fill="#14213D" font-size="34" font-weight="300" text-anchor="middle">morador</text></g>
<path class="draw" d="M770 170 L920 170" stroke="#A88B5E" stroke-width="2"/><text x="845" y="146" fill="#D8C4A0" font-size="18" text-anchor="middle">vem conhecer</text>
<g class="nd nd3"><circle cx="1080" cy="170" r="140" fill="#A88B5E"/><text x="1080" y="162" fill="#14213D" font-size="34" font-weight="300" text-anchor="middle">O seu</text><text x="1080" y="202" fill="#14213D" font-size="34" font-weight="300" text-anchor="middle">negócio</text></g>
</g></svg>'''
    jor = [('Dia 0','Recebe as chaves','e, junto, o kit da W3W.','01'),('Dia 1','Abre o mapa','e descobre os parceiros do bairro.','02'),('Dia 4','Visita você','mostra o QR e usa a cortesia.','03'),('Semana 3','Volta sozinha','agora pagando, porque gostou.','04'),('Mês 6','Cliente da casa','e indica aos vizinhos.','05')]
    jcards = ''.join(f'<article class="jc{" hi" if i==2 else ""}"><p class="d">{d}</p><p class="big">{n}</p><h3>{t}</h3><p class="mut">{s}</p></article>' for i,(d,t,s,n) in enumerate(jor))
    menu = [('Coffee','Padarias e cafés','Café com pão na chapa ou um doce da casa.'),('UtensilsCrossed','Restaurantes','Sobremesa, entrada ou bebida na primeira visita.'),('Wine','Bares','Um drinque de boas-vindas.'),('PawPrint','Pet','Primeiro banho ou avaliação.'),('Sparkles','Beleza e bem-estar','Aula experimental ou avaliação.'),('Wrench','Serviços da casa','Desconto no primeiro serviço.')]
    gains = [('UserPlus','Clientes novos','Moradores que ainda não têm seus lugares de cada dia.'),('Repeat','Frequência por anos','Quem mora a poucas quadras volta toda semana.'),('Gem','Público de alto padrão','Clientes de uma boutique imobiliária de Moema.'),('Megaphone','Divulgação sem custo','Mapa de Moema, Guia, páginas do bairro e Instagram W3W.'),('BadgeCheck','Selo de parceiro','“Parceiro W3W Moema” na porta ou no balcão.'),('Gauge','Custo previsível','Poucas cortesias por mês, sempre sob controle.')]
    regras = [('Gift','A cortesia','Você define o que oferece.'),('Ticket','Uso único','Uma vez por cliente.'),('QrCode','Validação','QR no nome do cliente.'),('CalendarDays','Validade','90 dias após a entrega do kit.'),('RefreshCw','Prazo','12 meses, saída com 60 dias de aviso.'),('ShieldCheck','Sem custo','Nada a pagar entre as partes.')]
    steps = [('Handshake','Semana 1','Adesão','Conversa, cortesia e termo.'),('Camera','Semana 2','Fotos e selo','Entrada no mapa e selo na porta.'),('Megaphone','Semana 3','Divulgação','Post e páginas do bairro.'),('Users','Todo mês','Novos moradores','Kits entregues e resumo do mês.')]
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Kit Boas-vindas Moema · W3W Imóveis</title><meta name="description" content="Proposta de parceria da W3W Imóveis para estabelecimentos de Moema.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500&family=Instrument+Serif:ital@0;1&display=swap">
<style>{CSS}</style></head><body>
<div class="prog"></div>
<div class="top"><span>W3W Imóveis</span><span>Proposta de parceria · 2026</span></div>

<section class="hero"><img class="bg" data-par=".6" src="{IMG}cidade.jpg" alt="Moema vista do alto">
<div class="in"><p class="ey rv">Para estabelecimentos de Moema</p>
<h1 class="lnw"><span class="ln"><span>Kit</span></span><span class="ln"><span class="sf">Boas-vindas</span></span><span class="ln"><span>Moema.</span></span></h1>
<p class="lead rv d3">Quem se muda para Moema com a W3W conhece o seu negócio na primeira semana.</p></div>
<div class="cue"><span>Role</span><i></i></div></section>

<section class="ctx"><div class="ph"><img data-par=".5" src="{IMG}lar.jpg" alt="Sala de um apartamento novo em Moema"></div>
<div class="tx"><p class="ey rv">01 · O contexto</p><h2 class="rv d1">Endereço novo. <span class="sf">Nenhum hábito ainda.</span></h2>
<div class="strike" style="margin-top:48px"><p><span>A padaria do café da manhã</span></p><p><span>O restaurante de domingo</span></p><p><span>O pet shop de confiança</span></p><p><span>O bar de sexta-feira</span></p></div>
<p class="mut rv" style="margin-top:44px;max-width:44ch;font-size:20px">Quem acaba de se mudar ainda vai escolher tudo isso. É a melhor hora para conhecer o seu negócio.</p></div></section>

<section class="dk pad"><div class="in"><p class="ey rv">02 · A ideia</p><h2 class="rv d1" style="max-width:20ch">A W3W entrega as chaves <span class="sf">e apresenta o bairro.</span></h2>
<div class="dia">{dia}</div></div></section>

<section class="pad"><div class="in"><p class="ey rv">03 · Quem está por trás</p><h2 class="rv d1">W3W, a boutique imobiliária <span class="sf">que vive Moema.</span></h2>
<div class="pil"><div class="card rv d1"><div class="chip">{ic('Home')}</div><h3>Curadoria imobiliária</h3><p class="mut">Imóveis de alto padrão, com foco total em Moema.</p></div>
<div class="card rv d2"><div class="chip">{ic('MapPin')}</div><h3>Mapa de Moema</h3><p class="mut">O guia vivo do bairro, com o que está aberto agora.</p></div>
<div class="card rv d3"><div class="chip">{ic('BookOpen')}</div><h3>Guia Moema</h3><p class="mut">Conteúdo do bairro no site e nas redes da W3W.</p></div></div></div></section>

<section class="sand pad"><div class="in kitg"><div class="rv">{box}</div>
<div><p class="ey rv">04 · O kit</p><h2 class="rv d1">Um presente na <span class="sf">entrega das chaves.</span></h2><div style="margin-top:40px">
<div class="row rv d1"><div class="chip">{ic('Mail')}</div><h3>Carta de boas-vindas</h3><p class="mut">Assinada pelos sócios da W3W.</p></div>
<div class="row rv d2"><div class="chip">{ic('Map')}</div><h3>Mapa ilustrado de Moema</h3><p class="mut">Com cada parceiro marcado.</p></div>
<div class="row rv d3"><div class="chip">{ic('Ticket')}</div><h3>Cartões de cortesia</h3><p class="mut">Um por parceiro, com QR no nome do cliente.</p></div>
<div class="row rv d4"><div class="chip">{ic('Smartphone')}</div><h3>Versão digital</h3><p class="mut">Tudo no celular, com validade de 90 dias.</p></div></div></div></div></section>

<section class="hz"><div class="stick"><div class="in"><p class="ey rv">05 · A mecânica, na prática</p><h2 class="rv d1" style="max-width:20ch">Um exemplo: a Ana compra um apê <span class="sf">com a W3W.</span></h2></div>
<div class="track">{jcards}</div><div class="in"><p class="hint">A cortesia acontece uma vez, no dia 4. O resto são visitas pagas.</p></div></div></section>

<section class="pad" style="padding-bottom:0"><div class="in"><p class="ey rv">06 · O que muda no seu dia a dia</p><h2 class="rv d1">Do seu lado, <span class="sf">três momentos simples.</span></h2>
<div class="three"><div class="card rv d1"><p class="k">Antes</p><div class="chip">{ic('Handshake')}</div><h3>Você escolhe a cortesia</h3><p class="mut">Define o que oferece, em quais dias e horários. Assina um termo de uma página.</p></div>
<div class="card rv d2"><p class="k">Na visita</p><div class="qr">{qr}</div><h3>O cliente mostra o QR</h3><p class="mut">O atendente confere e entrega a cortesia. Leva segundos.</p></div>
<div class="card rv d3"><p class="k">Todo mês</p><div class="chip">{ic('Chart')}</div><h3>Você recebe o resumo</h3><p class="mut">Quantos novos moradores vieram pelo kit, e quando.</p></div></div></div>
<div class="band" style="margin-top:100px"><img data-par=".7" src="{IMG}padaria.jpg" alt="Balcão de padaria com atendente entregando café"></div></section>

<section class="split"><div class="ph"><img src="{IMG}mesa.jpg" alt="Mesa com café, croissant, sobremesa e drinque"></div>
<div class="tx"><p class="ey rv">07 · O que pedimos</p><h2 class="rv d1">Um cardápio de cortesias <span class="sf">simples.</span></h2>
<div class="menu" style="margin-top:40px">{''.join(f'<div class="mi rv d{(i%3)+1}">{ic(a)}<p class="n">{b}</p><p>{c}</p></div>' for i,(a,b,c) in enumerate(menu))}</div>
<p class="tag rv">Nada de prato grátis · você escolhe dias e horários</p></div></section>

<section class="split dk"><div class="tx"><p class="ey rv">08 · O que você ganha</p><h2 class="rv d1">O que entra <span class="sf">de fato</span> no caixa e na marca.</h2>
<div class="gl">{''.join(f'<div class="gi rv d{(i%3)+1}">{ic(a)}<h3>{b}</h3><p>{c}</p></div>' for i,(a,b,c) in enumerate(gains))}</div></div>
<div class="ph"><img src="{IMG}casal.jpg" alt="Casal de moradores em café de rua arborizada"></div></section>

<section class="pad"><div class="in"><p class="ey rv">09 · A conta</p><h2 class="rv d1" style="max-width:22ch">Uma cortesia hoje. <span class="sf">Um cliente por anos.</span></h2>
<div class="conta"><div class="one"><p class="k" style="color:var(--gl)">Visita 1</p><b>1</b><p style="color:var(--p)">cortesia, uma única vez</p></div>
<div><div style="display:flex;align-items:flex-end;gap:24px;margin-bottom:28px;flex-wrap:wrap"><span class="cnt">0</span><div><h3>visitas pagas no ano</h3><p class="mut">se o novo morador voltar uma vez por semana</p></div></div>
<div class="bars">{bars}</div><div style="display:flex;justify-content:space-between;margin-top:12px" class="mut"><small>Semana 1</small><small>Semana 52</small></div></div></div>
<p class="mut rv" style="margin-top:40px;font-size:15px">Exemplo ilustrativo. Multiplique pelo seu gasto médio por visita para ver o valor de um cliente novo no ano.</p></div></section>

<section class="vit"><img class="bg" data-par=".6" src="{IMG}avenida.jpg" alt="Avenida arborizada de Moema">
<div class="in"><p class="ey rv">10 · Visibilidade</p><h2 class="rv d1">Seu negócio na vitrine <span class="sf" style="color:var(--gl)">da W3W.</span></h2>
<div class="c4"><div class="glass rv d1"><div class="chip">{ic('MapPin')}</div><h3>Mapa de Moema</h3><p>Destaque de parceiro no mapa vivo.</p></div>
<div class="glass rv d2"><div class="chip">{ic('BookOpen')}</div><h3>Guia do bairro</h3><p>Páginas como “Cafés em Moema”.</p></div>
<div class="glass rv d3"><div class="chip">{ic('Camera')}</div><h3>Instagram W3W</h3><p>Post de apresentação e roteiros.</p></div>
<div class="glass rv d4"><div class="chip">{ic('BadgeCheck')}</div><h3>Selo na porta</h3><p>“Parceiro W3W Moema”.</p></div></div></div></section>

<section class="pad"><div class="in reg"><div class="paper rv"><p class="ey" style="margin-bottom:14px">Termo de parceria</p><p class="sf" style="font-size:44px;line-height:1.1">Kit Boas-vindas Moema</p><div class="pl" style="width:90%;margin-top:34px"></div><div class="pl" style="width:76%"></div><div class="pl" style="width:84%"></div><div class="pl" style="width:60%"></div><div class="pl" style="width:88%"></div><div class="sig"><div>W3W Imóveis</div><div>Parceiro</div></div></div>
<div><p class="ey rv">11 · Regras simples</p><h2 class="rv d1">Um termo <span class="sf">de uma página.</span></h2><div class="tl" style="margin-top:36px">{''.join(f'<div class="row rv d{(i%3)+1}">{ic(a)}<h3>{b}</h3><p class="mut">{c}</p></div>' for i,(a,b,c) in enumerate(regras))}</div></div></div></section>

<section class="sand pad" style="padding-bottom:0"><div class="in"><p class="ey rv">12 · Como começar</p><h2 class="rv d1" style="max-width:20ch">Do aperto de mão <span class="sf">ao primeiro cliente.</span></h2>
<div class="steps">{''.join(f'<div class="st rv d{i+1}{" hi" if i==2 else ""}"><div class="dot">{ic(a)}</div><p class="w">{b}</p><h3>{c}</h3><p class="mut">{d}</p></div>' for i,(a,b,c,d) in enumerate(steps))}</div>
<p class="tag rv" style="background:var(--n);color:var(--c);margin-top:56px">Exclusivo: um parceiro por categoria em cada kit</p></div>
<div class="band" style="margin-top:100px"><img data-par=".7" src="{IMG}aperto.jpg" alt="Aperto de mão na porta de um restaurante"></div></section>

<section class="fim"><img class="bg" data-par=".5" src="{IMG}jantar.jpg" alt="Mesa posta ao ar livre">
<div class="in"><p class="ey rv">Vamos conversar</p><h2 class="lnw"><span class="ln"><span>Seja o primeiro</span></span><span class="ln"><span class="sf">endereço deles.</span></span></h2>
<a class="btn rv d2" href="{WA}" target="_blank" rel="noopener">Quero ser parceiro →</a>
<div class="ct rv d3"><div><small>Comercial</small>Wilson Rodrigues<br><span style="color:var(--p)">WhatsApp +55 11 99246-0734</span></div><div><small>W3W Imóveis</small>Curadoria imobiliária em Moema<br><span style="color:var(--p)">Guia Moema · Mapa de Moema</span></div></div></div></section>
<script>{JS}</script></body></html>'''
