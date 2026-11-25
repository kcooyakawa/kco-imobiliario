"""Página de serviços da W3W — versão 3: imersiva, escura, parallax e rolagem horizontal. Chamado por build.py."""
import json

IMG = 'https://kcooyakawa.github.io/kco-imobiliario/w3w-img'

CSS = r"""
<style>
body:has(.z3){background:#05070B}
.z3{--bg:#05070B;--bg2:#0B0F17;--tx:#EEF2F8;--tx2:#9AA6B8;--tx3:#5C677A;--ln:rgba(238,242,248,.1);--ac:#9CCBFF;--ok:#7BE0B3;--mono:ui-monospace,'SF Mono',Menlo,monospace;--e:cubic-bezier(.16,1,.3,1);background:var(--bg);color:var(--tx);overflow-x:clip}
.z3 ::selection{background:var(--ac);color:#05070B}
.z3 a{color:inherit}
.z3 em{font-family:var(--serif);font-style:italic;font-weight:200;color:var(--ac)}
.z3 .mono{font:500 11px/1.2 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--tx2)}
.z3-btn{display:inline-flex;align-items:center;gap:12px;height:56px;padding:0 28px;border-radius:999px;font:500 15px/1 var(--sans);text-decoration:none;transition:transform .4s var(--e),background .3s,color .3s,border-color .3s}
.z3-btn.p{background:var(--tx);color:#05070B}
.z3-btn.p:hover{background:var(--ac)}
.z3-btn.s{border:1px solid rgba(238,242,248,.25)}
.z3-btn.s:hover{border-color:var(--tx)}
.z3-btn:focus-visible{outline:2px solid var(--ac);outline-offset:4px}
/* cursor glow */
.z3-glow{position:fixed;left:0;top:0;width:520px;height:520px;margin:-260px 0 0 -260px;border-radius:50%;pointer-events:none;z-index:1;background:radial-gradient(circle,rgba(156,203,255,.13),transparent 60%);transform:translate3d(-999px,-999px,0);mix-blend-mode:screen}
/* hero */
.z3-hero{position:relative;height:150svh}
.z3-stick{position:sticky;top:0;height:100svh;overflow:hidden}
.z3-bg{position:absolute;inset:-6%;background:url("%I/agami-park-residences/voo.jpg") center/cover;transform:scale(1.15);will-change:transform;filter:saturate(.75) brightness(.55)}
.z3-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,7,11,.85) 0%,rgba(5,7,11,.2) 45%,#05070B 98%)}
.z3-grid{position:absolute;inset:0;background-image:linear-gradient(var(--ln) 1px,transparent 1px),linear-gradient(90deg,var(--ln) 1px,transparent 1px);background-size:96px 96px;mask-image:linear-gradient(180deg,#000,transparent 75%);-webkit-mask-image:linear-gradient(180deg,#000,transparent 75%);opacity:.5}
.z3-hin{position:relative;z-index:2;padding:132px clamp(20px,5vw,72px) 0;will-change:transform,opacity}
.z3-top{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;margin-bottom:5vh}
.z3-live{display:inline-flex;align-items:center;gap:10px}
.z3-live i{width:7px;height:7px;border-radius:50%;background:var(--ok);box-shadow:0 0 0 0 rgba(123,224,179,.6);animation:z3p 2s infinite}
@keyframes z3p{70%{box-shadow:0 0 0 9px rgba(123,224,179,0)}}
.z3 h1{font-family:var(--sans);font-weight:300;font-size:clamp(54px,11.5vw,210px);line-height:.86;letter-spacing:-.055em;margin:0}
.z3 h1 .ln{display:block;overflow:hidden;padding-bottom:.06em}
.z3 h1 .ln>span{display:inline-block;transform:translateY(105%);animation:z3up 1.3s var(--e) forwards}
.z3 h1 .ln:nth-child(2)>span{animation-delay:.12s}
.z3 h1 .ln:nth-child(3)>span{animation-delay:.24s}
@keyframes z3up{to{transform:none}}
.z3-hsub{display:flex;justify-content:space-between;align-items:end;gap:32px;flex-wrap:wrap;margin-top:5vh;opacity:0;animation:z3f 1s .7s var(--e) forwards}
@keyframes z3f{to{opacity:1}}
.z3-hsub p{max-width:44ch;font-size:clamp(16px,1.4vw,20px);line-height:1.5;color:var(--tx2);margin:0}
.z3-cta{display:flex;gap:10px;flex-wrap:wrap}
.z3-hud{position:absolute;z-index:3;right:clamp(20px,5vw,72px);top:30vh;display:grid;gap:10px;will-change:transform}
.z3-chip{display:flex;align-items:center;gap:12px;padding:12px 16px;border-radius:14px;background:rgba(11,15,23,.6);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border:1px solid var(--ln);font:13px var(--sans);min-width:250px;opacity:0;transform:translateY(16px);transition:opacity .6s var(--e),transform .6s var(--e)}
.z3-chip.on{opacity:1;transform:none}
.z3-chip b{font:600 11px var(--mono);padding:4px 7px;border-radius:6px;background:rgba(123,224,179,.14);color:var(--ok)}
.z3-chip b.b{background:rgba(156,203,255,.14);color:var(--ac)}
.z3-chip span{color:var(--tx2);margin-left:auto;font:11px var(--mono)}
.z3-scroll{position:absolute;left:50%;bottom:28px;z-index:3;transform:translateX(-50%);display:grid;justify-items:center;gap:10px}
.z3-scroll i{width:1px;height:46px;background:linear-gradient(var(--tx),transparent);animation:z3s 2s infinite var(--e);transform-origin:top}
@keyframes z3s{0%{transform:scaleY(0)}50%{transform:scaleY(1)}100%{transform:scaleY(1);opacity:0}}
/* marquee */
.z3-mq{border-block:1px solid var(--ln);overflow:hidden;padding:26px 0;white-space:nowrap}
.z3-mq div{display:inline-flex;gap:56px;animation:z3m 38s linear infinite;font:300 clamp(28px,3.4vw,52px)/1 var(--sans);letter-spacing:-.03em}
.z3-mq div span:nth-child(even){font-family:var(--serif);font-style:italic;font-weight:200;color:var(--ac)}
@keyframes z3m{to{transform:translateX(-50%)}}
/* manifesto */
.z3-man{padding:22vh clamp(20px,5vw,72px)}
.z3-man p{font:300 clamp(32px,5vw,84px)/1.06 var(--sans);letter-spacing:-.04em;margin:0;max-width:20ch}
.z3-man .w{opacity:.14;transition:opacity .25s}
.z3-man .w.on{opacity:1}
.z3-man .w.a.on{color:var(--ac)}
/* horizontal */
.z3-hz{position:relative}
.z3-hz .z3-stick{display:flex;flex-direction:column;justify-content:center;padding-top:72px}
.z3-hzh{padding:0 clamp(20px,5vw,72px);display:flex;justify-content:space-between;align-items:end;margin-bottom:4vh}
.z3-hzh h2{font:300 clamp(36px,4.4vw,72px)/1 var(--sans);letter-spacing:-.04em;margin:0}
.z3-prog{width:200px;height:1px;background:var(--ln);position:relative}
.z3-prog i{position:absolute;inset:0;background:var(--tx);transform-origin:left;transform:scaleX(0)}
.z3-track{display:flex;gap:2vw;padding:0 clamp(20px,5vw,72px);will-change:transform}
.z3-card{position:relative;flex:0 0 min(78vw,620px);height:min(64svh,620px);border-radius:24px;overflow:hidden;background:var(--bg2);border:1px solid var(--ln)}
.z3-card img{position:absolute;inset:0;width:120%;height:100%;object-fit:cover;filter:saturate(.7) brightness(.5);transition:filter .8s var(--e),transform .8s var(--e);will-change:transform}
.z3-card:hover img{filter:saturate(1) brightness(.62)}
.z3-card::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 30%,rgba(5,7,11,.95))}
.z3-cin{position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;justify-content:space-between;padding:clamp(22px,3vw,40px)}
.z3-cin .n{font:200 clamp(80px,10vw,150px)/.8 var(--serif);font-style:italic;color:var(--ac);opacity:.85}
.z3-cin h3{font:400 clamp(28px,3vw,44px)/1.02 var(--sans);letter-spacing:-.03em;margin:0 0 12px}
.z3-cin p{color:var(--tx2);max-width:40ch;margin:0 0 18px;line-height:1.5}
.z3-tags{display:flex;gap:6px;flex-wrap:wrap}
.z3-tags span{font:500 10px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;padding:7px 10px;border:1px solid rgba(238,242,248,.2);border-radius:999px}
/* dossiê */
.z3-dos{padding:20vh clamp(20px,5vw,72px);display:grid;grid-template-columns:1fr 1fr;gap:6vw;align-items:center;perspective:1400px}
.z3-dos h2,.z3-pl h2,.z3-end h2{font:300 clamp(40px,5.2vw,88px)/.98 var(--sans);letter-spacing:-.045em;margin:18px 0 0}
.z3-dos .t{color:var(--tx2);font-size:18px;line-height:1.55;max-width:44ch;margin-top:24px}
.z3-dcard{position:relative;border-radius:22px;padding:28px;background:linear-gradient(160deg,rgba(156,203,255,.09),rgba(11,15,23,.9) 40%);border:1px solid rgba(156,203,255,.22);box-shadow:0 60px 120px -50px rgba(0,0,0,.9),0 0 80px -30px rgba(156,203,255,.35);transform-style:preserve-3d;transition:transform .2s ease-out;overflow:hidden}
.z3-dcard::before{content:"";position:absolute;left:0;right:0;height:120px;top:-120px;background:linear-gradient(180deg,transparent,rgba(156,203,255,.14),transparent);animation:z3scan 3.6s infinite linear}
@keyframes z3scan{to{top:110%}}
.z3-dh{display:flex;justify-content:space-between;align-items:center;padding-bottom:16px;border-bottom:1px solid var(--ln)}
.z3-row{display:grid;grid-template-columns:110px 1fr;gap:14px;padding:12px 0;border-bottom:1px solid var(--ln);font-size:15px;opacity:0;transform:translateX(-10px);transition:opacity .5s var(--e),transform .5s var(--e)}
.z3-row.on{opacity:1;transform:none}
.z3-row span{color:var(--tx3)}
.z3-score{display:flex;align-items:center;gap:22px;margin-top:22px;transform:translateZ(40px)}
.z3-ring{width:96px;height:96px;flex:none}
.z3-ring circle{fill:none;stroke-width:6}
.z3-ring .bgc{stroke:var(--ln)}
.z3-ring .fg{stroke:var(--ac);stroke-linecap:round;stroke-dasharray:264;stroke-dashoffset:264;transition:stroke-dashoffset 1.8s var(--e);transform:rotate(-90deg);transform-origin:center}
.z3-ring text{fill:var(--tx);font:300 28px var(--sans);text-anchor:middle;dominant-baseline:central}
.z3-quote{margin-top:20px;padding:16px;border-radius:14px;background:rgba(238,242,248,.04);color:var(--tx2);font-size:15px;line-height:1.5;transform:translateZ(24px)}
.z3-fict{margin-top:14px;color:var(--tx3)}
/* números */
.z3-num{display:grid;grid-template-columns:repeat(4,1fr);border-block:1px solid var(--ln)}
.z3-num div{padding:7vh clamp(20px,3vw,40px);border-right:1px solid var(--ln)}
.z3-num div:last-child{border:0}
.z3-num b{display:block;font:200 clamp(52px,7vw,120px)/.9 var(--sans);letter-spacing:-.05em;margin-top:18px;font-variant-numeric:tabular-nums}
/* planos */
.z3-pl{padding:20vh clamp(20px,5vw,72px)}
.z3-plh{display:flex;justify-content:space-between;align-items:end;gap:30px;flex-wrap:wrap;margin-bottom:56px}
.z3-tg{display:inline-flex;padding:5px;border:1px solid var(--ln);border-radius:999px;position:relative}
.z3-tg button{position:relative;z-index:1;background:none;border:0;color:var(--tx2);font:500 13px var(--sans);padding:11px 18px;border-radius:999px;cursor:pointer;transition:color .3s}
.z3-tg button[aria-pressed=true]{color:#05070B}
.z3-tg i{position:absolute;top:5px;bottom:5px;left:5px;border-radius:999px;background:var(--tx);transition:transform .5s var(--e),width .5s var(--e)}
.z3-plans{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.z3-plan{position:relative;padding:36px 30px;border-radius:24px;border:1px solid var(--ln);background:var(--bg2);overflow:hidden;transition:transform .5s var(--e),border-color .4s}
.z3-plan:hover{transform:translateY(-6px);border-color:rgba(238,242,248,.3)}
.z3-plan.hot{background:linear-gradient(170deg,rgba(156,203,255,.16),var(--bg2) 55%);border-color:rgba(156,203,255,.4)}
.z3-plan h3{font:400 22px var(--sans);margin:0 0 30px}
.z3-pr{font:200 clamp(48px,4.6vw,72px)/1 var(--sans);letter-spacing:-.04em}
.z3-pr small{font-size:15px;color:var(--tx2);letter-spacing:0}
.z3-plan ul{list-style:none;padding:0;margin:26px 0 30px;display:grid;gap:10px;color:var(--tx2);font-size:15px}
.z3-plan li::before{content:"→ ";color:var(--ac)}
.z3-extra{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:16px}
.z3-extra div{padding:22px;border-radius:18px;border:1px solid var(--ln)}
.z3-extra b{display:block;font:300 24px var(--sans);margin-top:12px}
.z3-note{margin-top:22px;color:var(--tx3);font-size:13px}
/* final */
.z3-end{position:relative;padding:24vh clamp(20px,5vw,72px);overflow:hidden;text-align:center}
.z3-end .big{font:300 clamp(64px,15vw,260px)/.82 var(--sans);letter-spacing:-.06em;background:url("%I/la-galerie-moema/voo.jpg") center/cover;-webkit-background-clip:text;background-clip:text;color:transparent;margin:0;will-change:background-position}
.z3-end p{color:var(--tx2);font-size:19px;margin:34px auto 38px;max-width:46ch}
.z3-end .z3-cta{justify-content:center}
.rv{opacity:0;transform:translateY(40px);transition:opacity 1s var(--e),transform 1s var(--e)}
.rv.on{opacity:1;transform:none}
@media (max-width:900px){
.z3-hud{display:none}
.z3-dos{grid-template-columns:1fr}
.z3-num{grid-template-columns:1fr 1fr}.z3-num div:nth-child(2){border-right:0}.z3-num div:nth-child(-n+2){border-bottom:1px solid var(--ln)}
.z3-plans,.z3-extra{grid-template-columns:1fr}
.z3-prog{display:none}
.z3-glow{display:none}
}
@media (prefers-reduced-motion:reduce){
.z3 *{animation:none!important;transition:none!important}
.z3 h1 .ln>span,.z3-hsub,.rv,.z3-row,.z3-chip{transform:none;opacity:1}
.z3-man .w{opacity:1}
}
</style>
"""

JS = r"""
<script>
(()=>{const R=matchMedia('(prefers-reduced-motion: reduce)').matches,$=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{threshold:.2});
$$('.z3 .rv').forEach(el=>io.observe(el));
/* chips do hero */
$$('.z3-chip').forEach((c,i)=>setTimeout(()=>c.classList.add('on'),1100+i*450));
/* dossiê */
const dc=$('.z3-dcard');
if(dc){new IntersectionObserver((es,o)=>{if(es[0].isIntersecting){$$('.z3-row').forEach((r,i)=>setTimeout(()=>r.classList.add('on'),i*140));
setTimeout(()=>{const f=$('.z3-ring .fg');f.style.strokeDashoffset=264*(1-.92);let n=0,t=$('.z3-ring text');const it=setInterval(()=>{n+=2;t.textContent=Math.min(n,92);if(n>=92)clearInterval(it)},30)},700);o.disconnect()}},{threshold:.35}).observe(dc);
if(!R&&matchMedia('(hover:hover)').matches){dc.addEventListener('mousemove',e=>{const r=dc.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;dc.style.transform=`rotateY(${x*10}deg) rotateX(${-y*10}deg)`});dc.addEventListener('mouseleave',()=>dc.style.transform='')}}
/* números */
$$('.z3-num b').forEach(b=>{new IntersectionObserver((es,o)=>{if(!es[0].isIntersecting)return;o.disconnect();const to=+b.dataset.n,suf=b.dataset.s||'',st=performance.now(),fr=to>1000?to-40:0;
const k=t=>{const p=Math.min((t-st)/1600,1),v=Math.round(fr+(to-fr)*(1-Math.pow(1-p,4)));b.textContent=v+suf;if(p<1)requestAnimationFrame(k)};R?b.textContent=to+suf:requestAnimationFrame(k)},{threshold:.5}).observe(b)});
/* manifesto */
const ws=$$('.z3-man .w');
/* planos */
const P=JSON.parse($('.z3-pl').dataset.p),tg=$('.z3-tg'),pill=tg.querySelector('i');
const mv=b=>{pill.style.width=b.offsetWidth+'px';pill.style.transform=`translateX(${b.offsetLeft-5}px)`};
tg.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{tg.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b));mv(b);
$$('.z3-pr span').forEach(s=>s.textContent=P[b.dataset.k][+s.dataset.i].toLocaleString('pt-BR'))}));
requestAnimationFrame(()=>mv(tg.querySelector('[aria-pressed=true]')));addEventListener('resize',()=>mv(tg.querySelector('[aria-pressed=true]')));
if(R){ws.forEach(w=>w.classList.add('on'));return}
/* cursor */
const g=$('.z3-glow');let gx=-999,gy=-999,cx=-999,cy=-999;
if(matchMedia('(hover:hover)').matches)addEventListener('pointermove',e=>{gx=e.clientX;gy=e.clientY});
/* scroll loop */
const hero=$('.z3-hero'),bg=$('.z3-bg'),hin=$('.z3-hin'),hud=$('.z3-hud'),hz=$('.z3-hz'),tr=$('.z3-track'),pg=$('.z3-prog i'),man=$('.z3-man'),end=$('.z3-end .big'),imgs=$$('.z3-card img');
const size=()=>{hz.style.height=(tr.scrollWidth-innerWidth+innerHeight)+'px'};size();addEventListener('resize',size);
const loop=()=>{const vh=innerHeight;
let r=hero.getBoundingClientRect(),p=Math.min(Math.max(-r.top/(r.height-vh),0),1);
bg.style.transform=`scale(${1.15-p*.12}) translateY(${p*6}%)`;hin.style.transform=`translateY(${-p*120}px)`;hin.style.opacity=1-p*1.1;hud.style.transform=`translateY(${-p*260}px)`;
r=hz.getBoundingClientRect();p=Math.min(Math.max(-r.top/(r.height-vh),0),1);const d=tr.scrollWidth-innerWidth;tr.style.transform=`translateX(${-p*d}px)`;pg.style.transform=`scaleX(${p})`;
imgs.forEach((im,i)=>{const b=im.parentNode.getBoundingClientRect(),q=(b.left+b.width/2)/innerWidth-.5;im.style.transform=`translateX(${-q*12-8}%)`});
r=man.getBoundingClientRect();p=Math.min(Math.max((vh*.85-r.top)/(r.height*.8),0),1);const n=Math.floor(p*ws.length);ws.forEach((w,i)=>w.classList.toggle('on',i<n));
r=end.getBoundingClientRect();end.style.backgroundPosition=`center ${50+(r.top/vh-.5)*40}%`;
cx+=(gx-cx)*.12;cy+=(gy-cy)*.12;g.style.transform=`translate3d(${cx}px,${cy}px,0)`;
requestAnimationFrame(loop)};requestAnimationFrame(loop);
})();
</script>
"""


def render(wa, way, BASE, u):
    contato = wa('Olá! Vi a página de serviços da W3W e quero conversar sobre uma campanha.')
    prop = wa('Olá! Tenho um imóvel de alto padrão e quero saber como funciona a venda assistida da W3W.')
    planos = {'mensal': (1500, 1400, 1300), 'trimestral': (1350, 1250, 1150), 'semestral': (1200, 1100, 1000)}
    fm = lambda n: f"{n:,.0f}".replace(',', '.')
    m = planos['mensal']
    man = ('Agências entregam *contatos.* Nós entregamos *compradores,* com campanha própria para cada imóvel, '
           'criação assinada e corretores que conhecem Moema *rua a rua.*')
    words = []
    for w in man.split(' '):
        a = w.startswith('*')
        words.append(f'<span class="w{" a" if a else ""}">{w.strip("*")}</span>')
    man_html = ' '.join(words)
    cards = [
        ('01', 'Tráfego por produto', 'Meta e Google Ads com estratégia, públicos, verba e otimização próprios para cada empreendimento.', ['Meta Ads', 'Google Ads', 'Relatório de visitas'], 'agami-park-residences/fachada.jpg'),
        ('02', 'Lead Dossiê', 'Triagem, score e roteiro de abordagem de cada lead, entregues no WhatsApp do corretor com o card do imóvel.', ['Score A/B/C', 'Roteiro', 'LGPD'], 'agami-park-residences/lobby.jpg'),
        ('03', 'Direção de arte', 'Identidade, naming, book, tratamento de imagem, carrosséis, reels e vídeo com padrão de agência.', ['Identidade', 'Book', 'Vídeo'], 'la-galerie-moema/lazer-1.jpg'),
        ('04', 'Landing page e hub', 'Página do produto com triagem e card para WhatsApp, e o hub com textos, fichas e imagens para o time.', ['Landing page', 'Triagem', 'Hub de vendas'], 'agami-park-residences/terraco.jpg'),
    ]
    cards_html = ''.join(f'''<article class="z3-card"><img src="{IMG}/{img}" alt="" loading="lazy" decoding="async"><div class="z3-cin"><div class="n">{n}</div><div><h3>{t}</h3><p>{d}</p><div class="z3-tags">{''.join(f'<span>{x}</span>' for x in tg)}</div></div></div></article>''' for n, t, d, tg, img in cards)
    plan = lambda i, nome, itens, hot=False: f'''<div class="z3-plan{' hot' if hot else ''} rv"><h3>{nome}</h3><div class="z3-pr">R$ <span data-i="{i}">{fm(m[i])}</span><small> /mês por campanha</small></div><ul>{''.join(f'<li>{x}</li>' for x in itens)}</ul><a class="z3-btn {'p' if hot else 's'}" href="{wa('Olá! Quero contratar o plano ' + nome + ' da W3W.')}" target="_blank" rel="noopener">Quero este plano</a></div>'''
    mq = ''.join(f'<span>{x}</span>' for x in ['Tráfego', 'por produto', 'Direção de arte', 'assinada', 'Lead Dossiê', 'antes do olá', 'Moema', 'desde 2004'] * 2)
    css = CSS.replace('%I', IMG)
    return css + f'''
<main class="z3">
<div class="z3-glow" aria-hidden="true"></div>
<section class="z3-hero"><div class="z3-stick"><div class="z3-bg"></div><div class="z3-grid"></div>
<div class="z3-hin">
<div class="z3-top"><span class="mono z3-live"><i></i>Agenda aberta · 2026</span><span class="mono">W3W Serviços · Marketing imobiliário de alto padrão</span></div>
<h1><span class="ln"><span>Do anúncio</span></span><span class="ln"><span>à chave, <em>com</em></span></span><span class="ln"><span><em>inteligência.</em></span></span></h1>
<div class="z3-hsub"><p>Campanha dedicada para cada imóvel, criação assinada por Head of Art e um dossiê de cada lead antes do primeiro contato.</p>
<div class="z3-cta"><a class="z3-btn p" href="{contato}" target="_blank" rel="noopener">Falar com a W3W →</a><a class="z3-btn s" href="#planos">Ver planos</a></div></div>
</div>
<div class="z3-hud" aria-hidden="true"><div class="z3-chip"><b>A</b>Lead · Cobertura 1.184 m²<span>agora</span></div><div class="z3-chip"><b class="b">B</b>Lead · Studio Moema<span>2 min</span></div><div class="z3-chip"><b>A</b>Visita agendada · sábado<span>5 min</span></div></div>
<div class="z3-scroll mono" aria-hidden="true">Role<i></i></div>
</div></section>

<div class="z3-mq" aria-hidden="true"><div>{mq}</div></div>

<section class="z3-man"><p class="mono" style="font-size:11px;margin-bottom:40px;letter-spacing:.14em">Manifesto</p><p>{man_html}</p></section>

<section class="z3-hz" aria-label="Serviços"><div class="z3-stick">
<div class="z3-hzh"><h2>Quatro frentes,<br><em>um só olhar.</em></h2><div class="z3-prog"><i></i></div></div>
<div class="z3-track">{cards_html}</div>
</div></section>

<section class="z3-dos">
<div class="rv"><span class="mono">Lead Dossiê W3W</span><h2>O corretor sabe quem é <em>antes do primeiro olá.</em></h2>
<p class="t">Dados informados pelo próprio lead na triagem, cruzados com a campanha de origem. Sem compra de base, dentro da LGPD.</p></div>
<div><div class="z3-dcard">
<div class="z3-dh"><span class="mono">Dossiê #0412</span><span class="mono" style="color:var(--ok)">● Prioridade A</span></div>
<div class="z3-row"><span>Lead</span>Mariana, 41</div>
<div class="z3-row"><span>Imóvel</span>Cobertura 1.184 m² · Moema</div>
<div class="z3-row"><span>Origem</span>Instagram · campanha Coberturas</div>
<div class="z3-row"><span>Investimento</span>Acima de R$ 20 milhões</div>
<div class="z3-row"><span>Objetivo</span>Morar · família com 2 filhos</div>
<div class="z3-row"><span>Prazo</span>Até 6 meses</div>
<div class="z3-score"><svg class="z3-ring" viewBox="0 0 96 96"><circle class="bgc" cx="48" cy="48" r="42"/><circle class="fg" cx="48" cy="48" r="42"/><text x="48" y="48">0</text></svg><div><span class="mono">Score de compra</span><div style="margin-top:8px;font-size:15px">Retornar em até 15 min</div></div></div>
<div class="z3-quote">"Mariana, vi que você quer morar perto do Ibirapuera com a família. Posso mostrar a planta da cobertura e marcar uma visita privativa?"</div>
</div><p class="mono z3-fict">Exemplo com dados fictícios</p></div>
</section>

<div class="z3-num">
<div><span class="mono">No mercado desde</span><b data-n="2004">2004</b></div>
<div><span class="mono">Copa do Mundo</span><b data-n="2014">2014</b></div>
<div><span class="mono">Jogos Olímpicos</span><b data-n="2016">2016</b></div>
<div><span class="mono">Anos de criação</span><b data-n="20" data-s="+">20+</b></div>
</div>

<section class="z3-pl" id="planos" data-p='{json.dumps(planos)}'>
<div class="z3-plh"><div><span class="mono">Planos</span><h2>Preço claro, <em>por campanha.</em></h2></div>
<div class="z3-tg" role="group" aria-label="Período"><i></i><button data-k="mensal" aria-pressed="true">Mensal</button><button data-k="trimestral" aria-pressed="false">Trimestral</button><button data-k="semestral" aria-pressed="false">Semestral</button></div></div>
<div class="z3-plans">
{plan(0, '1 campanha', ['Estratégia e públicos', 'Meta e Google Ads', 'Otimização semanal', 'Relatório de visitas'])}
{plan(1, '2 campanhas', ['Tudo do plano anterior', 'Testes cruzados entre produtos', 'Reunião quinzenal', 'Relatório comparativo'], True)}
{plan(2, '3 campanhas', ['Tudo do plano anterior', 'Prioridade de criação', 'Reunião semanal', 'Painel de resultados'])}
</div>
<div class="z3-extra rv">
<div><span class="mono">+ Lead Dossiê</span><b>R$ 390/mês</b></div>
<div><span class="mono">Criativos</span><b>a partir de R$ 1.200</b></div>
<div><span class="mono">Landing page</span><b>a partir de R$ 2.500</b></div>
<div><span class="mono">Identidade e book</span><b>a partir de R$ 6.000</b></div>
</div>
<p class="z3-note">Verba de mídia paga direto ao Meta e ao Google. Proprietário: invista na campanha e, se vender com a W3W, o valor é descontado da comissão. <a href="{prop}" target="_blank" rel="noopener" style="color:var(--ac)">Saiba mais →</a></p>
</section>

<section class="z3-end"><h2 class="big">Vamos<br>vender.</h2><p>Do jeito certo: campanha própria, criação assinada e atendimento de quem conhece Moema.</p>
<div class="z3-cta"><a class="z3-btn p" href="{contato}" target="_blank" rel="noopener">Falar com a W3W →</a><a class="z3-btn s" href="{BASE}/#imoveis">Ver a vitrine</a></div></section>
</main>
''' + JS
