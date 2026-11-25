"""Guia Moema — versão 2: linguagem da página de serviços (v3), em versão clara. Chamado por build.py."""
import html

esc = lambda s: html.escape(str(s or ''))

CSS = r"""
<style>
body:has(.g2){background:#F6F5F2}
.g2{--bg:#F6F5F2;--bg2:#FFFFFF;--tx:#0E1116;--tx2:#4C5563;--tx3:#8A93A1;--ln:rgba(14,17,22,.1);--ac:#2F6FD0;--ok:#1E9E6A;--mono:ui-monospace,'SF Mono',Menlo,monospace;--e:cubic-bezier(.16,1,.3,1);background:var(--bg);color:var(--tx);overflow-x:clip;position:relative}
.g2 ::selection{background:var(--ac);color:#fff}
.g2 em{font-family:var(--serif);font-style:italic;font-weight:200;color:var(--ac)}
.g2 .mono{font:500 11px/1.3 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--tx2)}
.g2-in{padding:0 clamp(20px,5vw,72px)}
.g2-ey{display:block;color:var(--ac)!important;margin-bottom:14px}
/* liquid glass claro */
.g2-btn{position:relative;display:inline-flex;align-items:center;gap:10px;height:54px;padding:0 26px;border-radius:999px;font:500 15px/1 var(--sans);text-decoration:none;color:var(--tx);overflow:hidden;isolation:isolate;
background:linear-gradient(135deg,rgba(255,255,255,.75),rgba(255,255,255,.35) 50%,rgba(255,255,255,.6));backdrop-filter:blur(20px) saturate(1.8);-webkit-backdrop-filter:blur(20px) saturate(1.8);
box-shadow:inset 0 1.5px 0 #fff,inset 0 -1px 1px rgba(255,255,255,.7),inset 0 0 0 1px rgba(14,17,22,.08),inset 0 -12px 22px -14px rgba(47,111,208,.35),0 14px 34px -16px rgba(14,17,22,.35);transition:transform .5s var(--e),box-shadow .4s}
.g2-btn.p{color:#fff;background:linear-gradient(135deg,rgba(47,111,208,.92),rgba(30,70,150,.85) 50%,rgba(70,140,230,.9));box-shadow:inset 0 1.5px 0 rgba(255,255,255,.6),inset 0 -1px 1px rgba(255,255,255,.25),inset 0 0 0 1px rgba(255,255,255,.18),0 18px 40px -14px rgba(47,111,208,.6)}
.g2-btn::after{content:"";position:absolute;top:0;left:-60%;width:40%;height:100%;z-index:-1;background:linear-gradient(100deg,transparent,rgba(255,255,255,.7),transparent);transform:skewX(-20deg);animation:g2sh 5s 2s infinite}
@keyframes g2sh{0%,70%{left:-60%}100%{left:130%}}
.g2-btn:hover{transform:translateY(-2px) scale(1.02)}
.g2-btn:active{transform:scale(.97)}
.g2-btn:focus-visible{outline:2px solid var(--ac);outline-offset:4px}
/* manchas de luz */
.g2-blob{position:absolute;border-radius:50%;filter:blur(80px);pointer-events:none;animation:g2bl 16s ease-in-out infinite alternate}
@keyframes g2bl{50%{transform:translate(-5vw,4vh) scale(1.12)}100%{transform:translate(4vw,-3vh) scale(.95)}}
/* abertura */
.g2-hero{position:relative;padding:150px 0 70px;overflow:hidden}
.g2-hero .g2-blob.a{width:44vw;height:44vw;right:-10vw;top:-10vw;background:radial-gradient(circle,rgba(47,111,208,.28),transparent 65%)}
.g2-hero .g2-blob.b{width:30vw;height:30vw;left:30vw;top:20vh;background:radial-gradient(circle,rgba(30,158,106,.18),transparent 65%);animation-duration:20s}
.g2-top{position:relative;display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;margin-bottom:6vh}
.g2-live{display:inline-flex;align-items:center;gap:10px}
.g2-live i{width:7px;height:7px;border-radius:50%;background:var(--ok);animation:g2p 2s infinite}
@keyframes g2p{0%{box-shadow:0 0 0 0 rgba(30,158,106,.5)}70%{box-shadow:0 0 0 9px rgba(30,158,106,0)}}
.g2 h1{position:relative;font:300 clamp(52px,10vw,180px)/.88 var(--sans);letter-spacing:-.055em;margin:0;max-width:12ch}
.g2-sub{position:relative;display:flex;justify-content:space-between;align-items:end;gap:32px;flex-wrap:wrap;margin-top:5vh}
.g2-sub p{max-width:46ch;font-size:clamp(17px,1.4vw,21px);line-height:1.5;color:var(--tx2);margin:0}
.g2-cta{display:flex;gap:10px;flex-wrap:wrap}
.g2-meta{position:relative;display:flex;gap:28px;flex-wrap:wrap;margin-top:5vh;padding-top:20px;border-top:1px solid var(--ln)}
.g2-meta span{font:13px var(--sans);color:var(--tx2)}.g2-meta b{color:var(--tx);font-weight:400}
/* capa */
.g2-cover{padding:0 clamp(20px,5vw,72px)}
.g2-cover figure{margin:0;border-radius:28px;overflow:hidden;height:min(78vh,760px);position:relative;box-shadow:0 40px 90px -50px rgba(14,17,22,.6)}
.g2-cover img{width:100%;height:118%;object-fit:cover;display:block;will-change:transform}
.g2-cover figcaption{position:absolute;left:20px;bottom:18px;padding:9px 14px;border-radius:999px;font:500 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--tx);background:rgba(255,255,255,.6);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);box-shadow:inset 0 1px 0 #fff}
/* citação */
.g2-man{padding:22vh clamp(20px,5vw,72px)}
.g2-mg{display:grid;grid-template-columns:1fr 3fr;gap:4vw}
.g2-mg aside{border-top:1px solid var(--ln);padding-top:18px}
.g2-mg aside p{color:var(--tx3);font-size:13px;line-height:1.6;margin:18px 0 0;max-width:24ch}
.g2-mt{margin:0;font:300 clamp(34px,5vw,92px)/1.05 var(--sans);letter-spacing:-.05em}
.g2-mt .w{font-style:inherit;opacity:.12;transition:opacity .3s}
.g2-mt .w.on{opacity:1}
/* matéria */
.g2-art{padding:4vh 0 16vh;border-top:1px solid var(--ln)}
.g2-ag{display:grid;grid-template-columns:280px 1fr;gap:6vw;padding:12vh clamp(20px,5vw,72px) 0}
.g2-idx{position:sticky;top:120px;align-self:start}
.g2-idx ol{list-style:none;padding:0;margin:18px 0 0;border-left:1px solid var(--ln)}
.g2-idx a{display:block;padding:10px 0 10px 18px;margin-left:-1px;border-left:1px solid transparent;font:15px/1.35 var(--sans);color:var(--tx3);text-decoration:none;transition:color .3s,border-color .3s}
.g2-idx a.on{color:var(--tx);border-left-color:var(--ac)}
.g2-idx .prog{height:2px;background:var(--ln);margin-top:24px;border-radius:2px;overflow:hidden}
.g2-idx .prog i{display:block;height:100%;width:0;background:var(--ac);transition:width .2s}
.g2-body{max-width:720px}
.g2-sec{padding:0 0 9vh}
.g2-sec h2{font:300 clamp(32px,3.4vw,54px)/1.02 var(--sans);letter-spacing:-.04em;margin:0 0 22px}
.g2-sec h2 small{display:block;font:500 11px var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--ac);margin-bottom:14px}
.g2-sec p{font-size:19px;line-height:1.7;color:var(--tx2);margin:0}
.g2-sec p::first-letter{}
.g2-fig{margin:40px 0 0;border-radius:22px;overflow:hidden;position:relative}
.g2-fig img{width:100%;aspect-ratio:16/10;object-fit:cover;display:block;transform:scale(1.08);transition:transform 1.6s var(--e)}
.g2-fig.on img{transform:scale(1)}
.g2-fig figcaption{font:12px var(--mono);color:var(--tx3);padding:12px 4px 0;letter-spacing:.04em}
.g2-q{margin:0 0 9vh;padding:34px 0 34px 30px;border-left:2px solid var(--ac);font:300 clamp(26px,2.6vw,40px)/1.2 var(--sans);letter-spacing:-.03em}
/* concierge */
.g2-con{padding:16vh 0;border-top:1px solid var(--ln);position:relative;overflow:hidden}
.g2-con .g2-blob{width:50vw;height:50vw;left:-15vw;top:10vh;background:radial-gradient(circle,rgba(47,111,208,.16),transparent 65%)}
.g2-sh h2{position:relative;font:300 clamp(40px,5.2vw,88px)/.98 var(--sans);letter-spacing:-.045em;margin:0}
.g2-sh h2 em{display:block}
.g2-sh p{position:relative;color:var(--tx2);font-size:18px;line-height:1.55;max-width:56ch;margin:24px 0 0}
.g2-pins{position:relative;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:64px}
.g2-pin{padding:26px;border-radius:22px;background:rgba(255,255,255,.62);backdrop-filter:blur(16px) saturate(1.6);-webkit-backdrop-filter:blur(16px) saturate(1.6);box-shadow:inset 0 1px 0 #fff,inset 0 0 0 1px rgba(14,17,22,.06),0 20px 40px -28px rgba(14,17,22,.35);transition:transform .5s var(--e),box-shadow .4s;position:relative;overflow:hidden}
.g2-pin:hover{transform:translateY(-4px);box-shadow:inset 0 1px 0 #fff,inset 0 0 0 1px rgba(47,111,208,.25),0 30px 50px -28px rgba(47,111,208,.45)}
.g2-pin::after{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(300px circle at var(--sx,50%) var(--sy,50%),rgba(47,111,208,.10),transparent 60%);opacity:0;transition:opacity .4s}
.g2-pin:hover::after{opacity:1}
.g2-pin .n{font:200 44px/1 var(--serif);font-style:italic;color:var(--ac)}
.g2-pin b{display:block;font:400 22px/1.15 var(--sans);letter-spacing:-.02em;margin:16px 0 8px}
.g2-pin p{color:var(--tx2);font-size:15px;line-height:1.5;margin:0}
.g2-pin .t{position:absolute;top:22px;right:22px;font:500 10px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--tx2);padding:6px 10px;border-radius:999px;background:rgba(255,255,255,.7);box-shadow:inset 0 0 0 1px var(--ln)}
.g2-con .g2-cta{margin-top:40px;position:relative}
/* imóveis */
.g2-near{padding:14vh 0;border-top:1px solid var(--ln)}
.g2-near .grid{margin-top:56px}
/* próximas */
.g2-next{padding:12vh 0;border-top:1px solid var(--ln)}
.g2-next ul{list-style:none;padding:0;margin:40px 0 0;border-top:1px solid var(--ln)}
.g2-next li{display:flex;justify-content:space-between;align-items:baseline;padding:24px 0;border-bottom:1px solid var(--ln);font:300 clamp(26px,3vw,46px)/1 var(--sans);letter-spacing:-.03em;transition:padding .5s var(--e),color .3s}
.g2-next li:hover{padding-left:16px;color:var(--ac)}
.g2-next small{font:500 11px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--tx3)}
/* final */
.g2-end{padding:16vh clamp(20px,5vw,72px);border-top:1px solid var(--ln);display:grid;grid-template-columns:1.4fr 1fr;gap:6vw;align-items:end;position:relative;overflow:hidden}
.g2-end .g2-blob{width:50vw;height:50vw;right:-15vw;top:-20vh;background:radial-gradient(circle,rgba(47,111,208,.2),transparent 65%)}
.g2-end h2{position:relative;font:300 clamp(52px,8vw,140px)/.9 var(--sans);letter-spacing:-.05em;margin:0}
.g2-end h2 em{display:block}
.g2-end p{position:relative;color:var(--tx2);font-size:17px;line-height:1.55;margin:0 0 28px}
/* animações */
.g2 .rv{opacity:0;transform:translateY(40px);transition:opacity 1s var(--e),transform 1s var(--e)}
.g2 .rv.on{opacity:1;transform:none}
.g2-sp .wd{display:inline-block;overflow:hidden;vertical-align:top;padding-bottom:.08em}
.g2-sp .wd>i{display:inline-block;font-style:inherit;transform:translateY(110%) rotate(4deg);transition:transform 1.1s var(--e)}
.g2-sp.on .wd>i{transform:none}
.g2-pbar{position:fixed;left:0;top:0;height:2px;width:100%;z-index:60;transform-origin:left;transform:scaleX(0);background:linear-gradient(90deg,var(--ac),#7FB2FF)}
@media (max-width:900px){
.g2-mg,.g2-ag,.g2-end{grid-template-columns:1fr}
.g2-idx{position:static}.g2-idx ol{display:none}
.g2-pins{grid-template-columns:1fr}
.g2-cover figure{height:60vh;border-radius:20px}
.g2-sec p{font-size:17px}
}
@media (prefers-reduced-motion:reduce){.g2 *{animation:none!important;transition:none!important}.g2 .rv,.g2-sp .wd>i{opacity:1;transform:none}.g2-mt .w{opacity:1}}
</style>
"""

JS = r"""
<script>
(()=>{const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)],R=matchMedia('(prefers-reduced-motion: reduce)').matches;
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{threshold:.18});
$$('.g2 .rv,.g2-fig').forEach(el=>io.observe(el));
/* títulos palavra por palavra */
$$('.g2 h1,.g2-sh h2,.g2-end h2,.g2-sec h2').forEach(h=>{const walk=n=>{[...n.childNodes].forEach(c=>{if(c.nodeType===3){const f=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(t=>{if(!t)return;if(/^\s+$/.test(t)){f.append(t);return}const w=document.createElement('span');w.className='wd';const i=document.createElement('i');i.textContent=t;w.append(i);f.append(w)});c.replaceWith(f)}else if(c.nodeType===1&&c.tagName!=='BR'&&c.tagName!=='SMALL')walk(c)})};walk(h);h.classList.add('g2-sp');h.querySelectorAll('.wd>i').forEach((i,k)=>i.style.transitionDelay=k*.05+'s');io.observe(h)});
/* barra de progresso */
const pb=document.createElement('div');pb.className='g2-pbar';document.body.appendChild(pb);
/* índice ativo */
const secs=$$('.g2-sec'),links=$$('.g2-idx a'),pr=$('.g2-idx .prog i'),art=$('.g2-body');
const sio=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id))}}),{rootMargin:'-40% 0px -55% 0px'});secs.forEach(s=>sio.observe(s));
/* holofote */
if(matchMedia('(hover:hover)').matches)$$('.g2-pin').forEach(c=>c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect();c.style.setProperty('--sx',e.clientX-r.left+'px');c.style.setProperty('--sy',e.clientY-r.top+'px')}));
const ws=$$('.g2-mt .w'),man=$('.g2-man'),cov=$('.g2-cover img');
if(R){ws.forEach(w=>w.classList.add('on'));return}
const loop=()=>{const vh=innerHeight,h=document.documentElement;pb.style.transform=`scaleX(${h.scrollTop/(h.scrollHeight-vh)})`;
if(cov){const r=cov.parentNode.getBoundingClientRect();if(r.bottom>0&&r.top<vh)cov.style.transform=`translateY(${(r.top/vh)*-8-4}%)`}
if(man){const r=man.getBoundingClientRect(),p=Math.min(Math.max((vh*.8-r.top)/(r.height*.7),0),1),n=Math.floor(p*ws.length*1.05);ws.forEach((w,i)=>w.classList.toggle('on',i<n))}
if(art&&pr){const r=art.getBoundingClientRect();pr.style.width=Math.min(Math.max(-r.top/(r.height-vh),0),1)*100+'%'}
requestAnimationFrame(loop)};requestAnimationFrame(loop);
})();
</script>
"""


def render(G, p0, near_html, wa, u, dt, BASE=''):
    ed = G.get('edicao', {"numero": "01", "mes": ""})
    ims = p0.get('imagens') or []
    idx, body = '', ''
    for i, (t, x) in enumerate(p0['secoes']):
        k = t.split(' · ')
        sid = f's{i+1}'
        h = f'<h2><small>{esc(k[0])}</small>{esc(k[1][:1].upper()+k[1][1:])}</h2>' if len(k) == 2 else f'<h2>{esc(t)}</h2>'
        idx += f'<li><a href="#{sid}">{esc(t)}</a></li>'
        im = ims[i] if i < len(ims) else None
        fig = f'<figure class="g2-fig"><img src="{im[0]}" alt="{esc(im[1])}" loading="lazy" decoding="async"><figcaption>{esc(im[1])}</figcaption></figure>' if im else ''
        body += f'<section class="g2-sec" id="{sid}">{h}<p>{esc(x)}</p>{fig}</section>'
        if i == 1 and p0.get('citacao'):
            body += f'<blockquote class="g2-q">“{esc(p0["citacao"])}”</blockquote>'
    pins = p0.get('concierge', [])
    pins_html = ''.join(f'<div class="g2-pin rv" style="transition-delay:{(j%3)*.08}s"><span class="t">{esc(c["tempo"])}</span><span class="n">{c.get("n", j+1):02d}</span><b>{esc(c["nome"])}</b><p>{esc(c["nota"])}</p></div>' for j, c in enumerate(pins))
    W = lambda t: ' '.join(f'<i class="w">{w}</i>' for w in t.split())
    q = 'Moema não é só um endereço. É um jeito de viver a cidade a pé, entre o parque, a mesa e a noite.'
    concierge = wa('Olá! Vi o Guia Moema e quero uma indicação do concierge W3W.')
    nxt = ''.join(f'<li>{esc(c)}<small>Em breve</small></li>' for c in G['categorias'] if c != p0['categoria'])
    return CSS + f'''
<main class="g2">
<section class="g2-hero"><i class="g2-blob a"></i><i class="g2-blob b"></i><div class="g2-in">
<div class="g2-top"><span class="mono g2-live"><i></i>Guia Moema · Edição nº {ed["numero"]} · {esc(ed["mes"])}</span><span class="mono">Matéria de capa · {esc(p0["categoria"])}</span></div>
<h1>{esc(p0["titulo"])}</h1>
<div class="g2-sub"><p>{esc(p0["sub"])}</p><div class="g2-cta"><a class="g2-btn p" href="#materia">Ler a matéria ↓</a><a class="g2-btn" href="{concierge}" target="_blank" rel="noopener">Falar com o concierge</a></div></div>
<div class="g2-meta"><span><b>{dt(p0["data"])}</b></span><span>Leitura · <b>{p0["leitura"]}</b></span><span>Por <b>W3W Imóveis</b></span><span>{len(pins)} endereços do concierge</span></div>
</div></section>

<div class="g2-cover rv"><figure><img src="{p0["capa"]}" alt="Moema vista do alto" decoding="async"><figcaption>Moema · São Paulo</figcaption></figure></div>

<section class="g2-man" aria-label="Abertura"><div class="g2-mg"><aside><span class="mono g2-ey">Concierge W3W</span><p>A visão de quem trabalha no bairro há mais de vinte anos.</p></aside><p class="g2-mt">{W(q)}</p></div></section>

<section class="g2-art" id="materia"><div class="g2-ag">
<aside class="g2-idx"><span class="mono g2-ey">Nesta matéria</span><ol>{idx}</ol><div class="prog"><i></i></div></aside>
<article class="g2-body">{body}</article>
</div></section>

<section class="g2-con"><i class="g2-blob"></i><div class="g2-in">
<div class="g2-sh rv"><span class="mono g2-ey">Carnet do concierge</span><h2>Do parque pela manhã <em>ao jazz da noite.</em></h2><p>Os endereços desta edição, na ordem do dia. Peça pelo WhatsApp e o concierge W3W indica o resto: reserva, horário e o melhor lugar da casa.</p></div>
<div class="g2-pins">{pins_html}</div>
<div class="g2-cta"><a class="g2-btn p" href="{concierge}" target="_blank" rel="noopener">Pedir uma indicação →</a></div>
</div></section>

<section class="g2-near"><div class="g2-in"><div class="g2-sh rv"><span class="mono g2-ey">Morar perto daqui</span><h2>Endereços para <em>viver Moema.</em></h2></div>
<div class="grid">{near_html}</div></div></section>

<section class="g2-next"><div class="g2-in"><div class="g2-sh rv"><span class="mono g2-ey">Próximas edições</span><h2>O bairro, <em>uma página por vez.</em></h2></div><ul>{nxt}</ul></div></section>

<section class="g2-end"><i class="g2-blob"></i><h2 class="rv">Quer morar <em>em Moema?</em></h2>
<div class="rv"><p>A W3W conhece o bairro rua a rua. Conte o que procura e receba uma seleção sob medida.</p><div class="g2-cta"><a class="g2-btn p" href="{wa('Olá! Li o Guia Moema e quero conhecer imóveis no bairro.')}" target="_blank" rel="noopener">Falar com a W3W →</a><a class="g2-btn" href="{BASE}/#imoveis">Ver a vitrine</a></div></div></section>
</main>
''' + JS
