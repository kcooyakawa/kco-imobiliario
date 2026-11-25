"""Página de serviços da W3W — versão 4: palco preto, escultura metálica, provas em placas e planos em faixa clara. Chamado por build.py."""
import json

IMG = 'https://kcooyakawa.github.io/kco-imobiliario/w3w-img'

CSS = r"""
<style>
body:has(.a4){background:#000}
.a4{--d:"SF Pro Display","Inter","Helvetica Neue",Helvetica,Arial,sans-serif;--t:"SF Pro Text","Inter","Helvetica Neue",Helvetica,Arial,sans-serif;--blue:#0071e3;--lk:#2997ff;--lk2:#0066cc;--ch:#1d1d1f;--pn:#161617;--g:#86868b;--g2:#6e6e73;--edge:#333336;--soft:#f5f5f7;background:#000;color:var(--soft);font-family:var(--t);overflow-x:clip;-webkit-font-smoothing:antialiased}
.a4 a{color:inherit}
.a4 .box{max-width:1260px;margin:0 auto;padding:0 clamp(20px,6vw,90px)}
.a4 .cp{max-width:840px;margin:0 auto;text-align:center}
.a4 .ey{font:600 21px/1 var(--d);letter-spacing:.011em;color:var(--g);margin:0 0 20px}
.a4 .dp{font:600 clamp(48px,6.7vw,96px)/1.04 var(--d);letter-spacing:-.015em;margin:0}
.a4 .h2{font:600 clamp(34px,3.4vw,48px)/1.08 var(--d);letter-spacing:-.003em;margin:0}
.a4 .ld{font:600 clamp(18px,1.5vw,21px)/1.381 var(--d);letter-spacing:.011em;color:var(--g);margin:24px 0 0}
.a4 .ld b{color:var(--soft);font-weight:600}
.a4-btn{display:inline-flex;align-items:center;height:44px;padding:0 21px;border-radius:980px;background:var(--blue);color:#fff!important;font:400 17px/1 var(--t);letter-spacing:-.022em;text-decoration:none;transition:background .1s linear}
.a4-btn:hover{background:#0076df}.a4-btn:active{background:#006edb}
.a4-btn:focus-visible,.a4-lk:focus-visible{outline:2px solid var(--blue);outline-offset:3px}
.a4-lk{color:var(--lk)!important;font:400 17px/1.235 var(--t);letter-spacing:-.022em;text-decoration:none}
.a4-lk:hover{text-decoration:underline}
.a4 section{padding:144px 0}
/* palco */
.a4-hero{padding:120px 0 72px!important;text-align:center;overflow:hidden}
.a4-name{font:600 clamp(22px,2.2vw,32px)/1.125 var(--d);letter-spacing:.004em;margin:0 0 10px}
.a4-prom{font:600 clamp(44px,5.6vw,80px)/1.05 var(--d);letter-spacing:-.015em;margin:0 auto;max-width:18ch}
.a4-prom span{background:linear-gradient(90deg,#f5f5f7 0%,#bfe3ff 30%,#fff 45%,#9fd1ff 60%,#f5f5f7 100%);background-size:300% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:a4sw 3.5s linear 1 .4s both}
@keyframes a4sw{from{background-position:100% 0}to{background-position:0 0}}
.a4-stage{position:relative;height:clamp(380px,48vw,640px);margin-top:40px}
.a4-sc{position:absolute;left:50%;top:0;width:min(1260px,130vw);transform:translateX(-50%);will-change:transform}
.a4-sc svg{width:100%;height:auto;display:block}
.a4-plane{position:absolute;left:50%;top:18%;width:min(440px,84vw);transform:translateX(-50%) perspective(1400px) rotateX(10deg);background:rgba(22,22,23,.86);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-radius:28px;box-shadow:0 0 0 1px #333336,0 60px 120px -30px #000;padding:26px 26px 22px;text-align:left;will-change:transform}
.a4-plane .a4hd{display:flex;justify-content:space-between;font:600 13px var(--t);color:var(--g);padding-bottom:14px;border-bottom:1px solid var(--edge)}
.a4-plane .a4hd b{color:#30d158;font-weight:600}
.a4-plane dl{margin:0;display:grid;grid-template-columns:96px 1fr}
.a4-plane dt,.a4-plane dd{margin:0;padding:10px 0;border-bottom:1px solid #232325;font:400 15px/1.3 var(--t);letter-spacing:-.016em}
.a4-plane dt{color:var(--g)}
.a4-plane .sc{display:flex;align-items:center;gap:14px;margin-top:16px}
.a4-plane .sc strong{font:600 44px/1 var(--d);background:linear-gradient(90deg,#c9f0e0,#9fd1ff,#fff);-webkit-background-clip:text;background-clip:text;color:transparent}
.a4-plane .sc span{font:400 14px/1.3 var(--t);color:var(--g)}
.a4-plat{display:flex;justify-content:center;align-items:center;gap:22px;flex-wrap:wrap;margin-top:28px}
.a4-plat .pr{font:600 14px/1.286 var(--t);letter-spacing:-.016em;color:var(--g);text-align:left}
.a4-plat .pr b{display:block;color:var(--soft);font-weight:600}
/* destaques */
.a4-hl{background:var(--ch)}
.a4-hlh{display:flex;justify-content:space-between;align-items:end;gap:20px;margin-bottom:48px}
.a4-gal{display:flex;gap:20px;overflow-x:auto;scroll-snap-type:x mandatory;padding:0 clamp(20px,6vw,90px);scrollbar-width:none;max-width:none}
.a4-gal::-webkit-scrollbar{display:none}
.a4-gal figure{flex:0 0 min(84vw,696px);margin:0;scroll-snap-align:start}
.a4-gal figure:nth-child(even){flex-basis:min(70vw,420px)}
.a4-gal .im{height:clamp(300px,32vw,452px);border-radius:28px;overflow:hidden;border:1px solid var(--edge)}
.a4-gal img{width:100%;height:100%;object-fit:cover;transition:transform .8s cubic-bezier(0,0,.5,1)}
.a4-gal figure:hover img{transform:scale(1.03)}
.a4-gal figcaption{padding:28px 16px 0;font:400 17px/1.235 var(--t);letter-spacing:-.022em;color:var(--g);max-width:52ch}
.a4-gal figcaption b{color:var(--soft);font-weight:600}
.a4-pad{display:flex;justify-content:flex-end;gap:18px;margin-top:28px}
.a4-pad button{width:36px;height:36px;border-radius:50%;border:0;background:rgba(66,66,69,.72);color:rgba(255,255,255,.8);cursor:pointer;display:grid;place-items:center;transition:background .1s linear,opacity .1s linear}
.a4-pad button:hover{background:rgba(73,73,76,.73)}
.a4-pad button:disabled{opacity:.36;cursor:default}
.a4-pad button:focus-visible{outline:2px solid var(--blue);outline-offset:3px}
/* macro */
.a4-mac{position:relative;padding:0!important;height:min(92vh,860px);overflow:hidden}
.a4-mac img{position:absolute;inset:-10% 0;width:100%;height:120%;object-fit:cover;filter:brightness(.55) contrast(1.1);will-change:transform}
.a4-mac::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,#000 0%,transparent 30%,transparent 55%,#000 100%)}
.a4-mac .cp{position:relative;z-index:2;padding-top:120px}
.a4-cr{position:absolute;right:24px;bottom:20px;z-index:2;font:400 12px/1.333 var(--t);color:#d2d2d7}
/* prova */
.a4-pf{background:#000}
.a4-panel{background:var(--ch);border-radius:28px;padding:72px clamp(20px,4vw,72px) 120px;max-width:1260px;margin:0 auto}
.a4-panelh{display:flex;justify-content:space-between;align-items:end;gap:24px;flex-wrap:wrap;margin-bottom:48px}
.a4-panelh h2{font:600 clamp(36px,3.9vw,56px)/1.07 var(--d);letter-spacing:-.005em;margin:0;max-width:16ch}
.a4-sel{display:grid;gap:8px;font:400 14px var(--t);color:var(--g)}
.a4-sel select{appearance:none;-webkit-appearance:none;height:44px;padding:0 45px 0 24px;border-radius:980px;border:1px solid var(--g2);background:rgba(255,255,255,.04) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M1 1l5 5 5-5' fill='none' stroke='%23f5f5f7' stroke-width='1.6'/%3E%3C/svg%3E") no-repeat right 20px center;color:var(--soft);font:400 17px var(--t)}
.a4-sel select:focus-visible{outline:2px solid var(--blue);outline-offset:3px}
.a4-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;max-width:1050px;margin:0 auto}
.a4-tile{background:#000;border-radius:28px;height:300px;overflow:clip;display:grid;place-content:center;text-align:center;padding:32px;position:relative}
.a4-tile strong{display:block;font:600 48px/52px var(--d);letter-spacing:-.003em;transition:opacity .3s}
.a4-tile span{display:block;margin-top:10px;font:400 17px/1.3 var(--t);color:var(--g);max-width:24ch;margin-inline:auto}
.a4-tile.im{padding:0;display:block}
.a4-tile.im img{width:100%;height:100%;object-fit:cover;opacity:.8}
.a4-tile.im span{position:absolute;left:24px;bottom:22px;margin:0;color:var(--soft);text-align:left}
.a4-tile .ic{width:56px;height:56px;margin:0 auto 18px;color:#9fd1ff}
.a4-tile .glow{position:absolute;inset:auto;width:160px;height:160px;border-radius:50%;filter:blur(40px);opacity:.35;background:#2997ff;left:50%;top:50%;transform:translate(-50%,-50%);pointer-events:none}
.a4-fine{max-width:1050px;margin:24px auto 0;font:400 12px/1.4 var(--t);color:var(--g2)}
/* faixa clara */
.a4-light{background:var(--soft);color:var(--ch)}
.a4-light .ey{color:var(--g2)}
.a4-light .ld{color:var(--g2)}
.a4-light .a4-lk{color:var(--lk2)!important}
.a4-tg{display:inline-flex;gap:4px;padding:4px;border-radius:980px;background:#e8e8ed;margin-top:32px}
.a4-tg button{border:0;background:none;padding:9px 18px;border-radius:980px;font:400 15px var(--t);color:var(--ch);cursor:pointer;transition:background .2s,box-shadow .2s}
.a4-tg button[aria-pressed=true]{background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.12)}
.a4-tg button:focus-visible{outline:2px solid var(--blue);outline-offset:2px}
.a4-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:48px}
.a4-card{background:#fff;border-radius:28px;padding:40px 32px 36px;display:flex;flex-direction:column;transition:transform .3s cubic-bezier(0,0,.5,1)}
.a4-card:hover{transform:scale(1.012)}
.a4-card .lb{font:600 14px var(--t);color:var(--g2)}
.a4-card h3{font:600 28px/1.143 var(--d);letter-spacing:.007em;margin:8px 0 22px}
.a4-card .pc{font:600 40px/1 var(--d);letter-spacing:-.01em}
.a4-card .pc small{font:400 15px var(--t);color:var(--g2)}
.a4-card ul{list-style:none;padding:0;margin:24px 0 32px;display:grid;gap:12px;font:400 17px/1.3 var(--t);letter-spacing:-.022em;color:#424245}
.a4-card .a4f{margin-top:auto;display:flex;justify-content:space-between;align-items:center}
.a4-card.hot{box-shadow:0 0 0 2px var(--blue)}
.a4-sm{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:20px}
.a4-sm div{background:#fff;border-radius:28px;padding:28px}
.a4-sm b{display:block;font:600 21px/1.2 var(--d);margin-top:6px}
.a4-sm span{font:400 14px var(--t);color:var(--g2)}
.a4-own{display:grid;grid-template-columns:1.2fr 1fr;gap:20px;margin-top:20px}
.a4-own>div{border-radius:28px;padding:40px 32px}
.a4-own .d{background:var(--ch);color:var(--soft)}
.a4-own .d h3,.a4-own .w h3{font:600 28px/1.143 var(--d);margin:0 0 12px}
.a4-own .d p{color:var(--g);font:400 17px/1.4 var(--t);margin:0 0 24px}
.a4-own .w{background:#fff}
.a4-own .w details{border-top:1px solid #d2d2d7;padding:14px 0}
.a4-own .w summary{cursor:pointer;font:600 17px var(--t);list-style:none;display:flex;justify-content:space-between}
.a4-own .w summary::after{content:"+";color:var(--g2)}
.a4-own .w details[open] summary::after{content:"–"}
.a4-own .w p{font:400 15px/1.45 var(--t);color:var(--g2);margin:10px 0 0}
/* diretório */
.a4-dir{background:#fafafc;color:var(--ch);padding:144px 0!important}
.a4-dir .cols{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:40px;margin-top:48px}
.a4-dir .lb{font:400 12px var(--t);color:var(--g2);margin-bottom:14px}
.a4-dir .c1 a{display:block;font:600 28px/1.5 var(--d);text-decoration:none;color:var(--ch)}
.a4-dir .cn a{display:block;font:400 17px/2 var(--t);color:#333336;text-decoration:none}
.a4-dir a:hover{color:var(--lk2)}
@media (max-width:1068px){.a4-grid,.a4-cards{grid-template-columns:1fr 1fr}.a4-sm{grid-template-columns:1fr 1fr}}
@media (max-width:734px){
.a4 section{padding:96px 0}
.a4-grid,.a4-cards,.a4-sm,.a4-own,.a4-dir .cols{grid-template-columns:1fr}
.a4-hlh{flex-direction:column;align-items:start}
.a4-plane{top:14%}
.a4-panel{border-radius:0}
}
@media (prefers-reduced-motion:reduce){.a4 *{animation:none!important;transition:none!important}.a4-prom span{background-position:0 0}}
</style>
"""

SCULPT = r"""<svg viewBox="0 0 1260 520" aria-hidden="true">
<defs>
<linearGradient id="a4m" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".18" stop-color="#d8dde4"/><stop offset=".5" stop-color="#3a3d42"/><stop offset=".72" stop-color="#9aa3ad"/><stop offset="1" stop-color="#1a1b1d"/></linearGradient>
<linearGradient id="a4x" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a2c30"/><stop offset="1" stop-color="#050506"/></linearGradient>
<linearGradient id="a4e" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset=".08" stop-color="#fff" stop-opacity="0"/></linearGradient>
<filter id="a4r" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="14"/></filter>
</defs>
<g font-family="'SF Pro Display','Inter','Helvetica Neue',Arial,sans-serif" font-weight="800" font-size="470" text-anchor="middle" letter-spacing="-28">
<text x="630" y="452" fill="#7fc8ff" opacity=".22" filter="url(#a4r)">W3W</text>
<text x="630" y="470" fill="url(#a4x)">W3W</text>
<text x="630" y="462" fill="url(#a4x)">W3W</text>
<text x="630" y="452" fill="url(#a4m)">W3W</text>
<text x="630" y="452" fill="url(#a4e)">W3W</text>
</g></svg>"""

JS = r"""
<script>
(()=>{const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)],R=matchMedia('(prefers-reduced-motion: reduce)').matches;
/* galeria */
const g=$('.a4-gal'),[pv,nx]=$$('.a4-pad button');
const st=()=>{pv.disabled=g.scrollLeft<8;nx.disabled=g.scrollLeft+g.clientWidth>g.scrollWidth-8};
g.addEventListener('scroll',st,{passive:true});st();
const step=()=>g.querySelector('figure').offsetWidth+20;
pv.onclick=()=>g.scrollBy({left:-step(),behavior:R?'auto':'smooth'});nx.onclick=()=>g.scrollBy({left:step(),behavior:R?'auto':'smooth'});
/* comparação */
const D=JSON.parse($('.a4-panel').dataset.d),sel=$('.a4-sel select');
sel.onchange=()=>{const v=D[sel.value];$$('[data-k]').forEach(el=>{el.style.opacity=0;setTimeout(()=>{el.textContent=v[el.dataset.k];el.style.opacity=1},200)})};
/* planos */
const P=JSON.parse($('.a4-cards').dataset.p);
$$('.a4-tg button').forEach(b=>b.onclick=()=>{$$('.a4-tg button').forEach(x=>x.setAttribute('aria-pressed',x===b));$$('.a4-card [data-i]').forEach(s=>s.textContent=P[b.dataset.k][+s.dataset.i].toLocaleString('pt-BR'))});
if(R)return;
/* palco e macro */
const sc=$('.a4-sc'),pl=$('.a4-plane'),mac=$('.a4-mac img'),mw=$('.a4-mac');
const loop=()=>{const y=scrollY,vh=innerHeight;
if(y<vh*1.3){sc.style.transform=`translateX(-50%) translateY(${y*.25}px) scale(${1+y*.0002})`;pl.style.transform=`translateX(-50%) perspective(1400px) rotateX(${Math.max(10-y*.03,0)}deg) translateY(${-y*.08}px)`}
const r=mw.getBoundingClientRect();if(r.bottom>0&&r.top<vh)mac.style.transform=`translateY(${(r.top/vh)*-8}%) scale(1.05)`;
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
    comp = {
        'agencia': {'a': 'Seu imóvel', 'a2': 'uma campanha só dele, nunca um pacote', 'b': 'Moema', 'b2': 'rua a rua, desde 2004', 'c': '15 min', 'c2': 'meta de retorno ao lead, em horário comercial', 'd': 'Head of Art', 'd2': 'assinando cada peça, de FIFA™ a Rio 2016'},
        'portal': {'a': '1 imóvel', 'a2': 'em destaque, sem disputar a página com outros', 'b': 'Público', 'b2': 'escolhido por perfil, não por quem passou no portal', 'c': 'Dossiê', 'c2': 'em cada lead, no lugar de nome e telefone', 'd': 'Marca', 'd2': 'própria do produto, em vez de anúncio padrão'},
    }
    C = comp['agencia']
    gal = [
        ('agami-park-residences/fachada.jpg', 'Tráfego por produto.', 'Meta e Google Ads com públicos, verba e otimização próprios para cada empreendimento.'),
        ('agami-park-residences/lobby.jpg', 'Lead Dossiê.', 'Triagem, score e roteiro de cada lead, no WhatsApp do corretor.'),
        ('la-galerie-moema/lazer-1.jpg', 'Direção de arte.', 'Identidade, book, imagem tratada, carrosséis, reels e vídeo.'),
        ('agami-park-residences/terraco.jpg', 'Landing page e hub.', 'Página do produto com triagem e o hub de materiais para o time.'),
    ]
    gal_html = ''.join(f'<figure><div class="im"><img src="{IMG}/{i}" alt="" loading="lazy" decoding="async"></div><figcaption><b>{t}</b> {d}</figcaption></figure>' for i, t, d in gal)
    card = lambda i, lb, nome, itens, hot=False: f'''<div class="a4-card{' hot' if hot else ''}"><span class="lb">{lb}</span><h3>{nome}</h3><div class="pc">R$ <span data-i="{i}">{fm(m[i])}</span><small> /mês por campanha</small></div><ul>{''.join(f'<li>{x}</li>' for x in itens)}</ul><div class="a4f"><a class="a4-btn" href="{wa('Olá! Quero contratar o plano ' + nome + ' da W3W.')}" target="_blank" rel="noopener">Contratar</a><a class="a4-lk" href="{contato}" target="_blank" rel="noopener">Tirar dúvidas ›</a></div></div>'''
    ic = '<svg class="ic" viewBox="0 0 56 56" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M10 46V22l18-12 18 12v24"/><path d="M22 46V32h12v14"/></svg>'
    return CSS + f'''
<main class="a4">
<section class="a4-hero"><div class="box">
<p class="a4-name">W3W Serviços</p>
<h1 class="a4-prom"><span>Seu imóvel. Em cartaz.</span></h1>
<div class="a4-plat"><div class="pr">Campanhas a partir de<b>R$ 1.300/mês</b></div><a class="a4-btn" href="{contato}" target="_blank" rel="noopener">Falar com a W3W</a><a class="a4-lk" href="#planos">Ver planos ›</a></div>
</div>
<div class="a4-stage"><div class="a4-sc">{SCULPT}</div>
<div class="a4-plane" aria-label="Exemplo de Lead Dossiê com dados fictícios"><div class="a4hd"><span>Lead Dossiê · exemplo</span><b>● Prioridade A</b></div>
<dl><dt>Lead</dt><dd>Mariana, 41</dd><dt>Imóvel</dt><dd>Cobertura 1.184 m² · Moema</dd><dt>Origem</dt><dd>Instagram · Coberturas</dd><dt>Objetivo</dt><dd>Morar · família</dd><dt>Prazo</dt><dd>Até 6 meses</dd></dl>
<div class="sc"><strong>92</strong><span>Score de compra.<br>Retornar em até 15 min.</span></div></div>
</div></section>

<section style="padding-top:72px"><div class="box cp"><p class="ey">Por que a W3W</p><h2 class="dp">Anúncio atrai. Inteligência vende.</h2>
<p class="ld">Agências entregam contatos. <b>Nós entregamos compradores.</b> Cada imóvel ganha campanha própria, criação assinada por Head of Art e corretores que conhecem Moema há mais de vinte anos. <b>Do primeiro clique à assinatura.</b></p></div></section>

<section class="a4-hl"><div class="box a4-hlh"><h2 class="h2">Quatro frentes. Um só olhar.</h2><a class="a4-lk" href="{contato}" target="_blank" rel="noopener">Montar minha campanha ›</a></div>
<div class="a4-gal">{gal_html}</div>
<div class="box a4-pad"><button type="button" aria-label="Anterior"><svg width="10" height="16" viewBox="0 0 10 16"><path d="M8 2 2 8l6 6" fill="none" stroke="currentColor" stroke-width="2"/></svg></button><button type="button" aria-label="Próximo"><svg width="10" height="16" viewBox="0 0 10 16"><path d="m2 2 6 6-6 6" fill="none" stroke="currentColor" stroke-width="2"/></svg></button></div>
</section>

<section class="a4-mac"><img src="{IMG}/agami-park-residences/par-1.jpg" alt="" loading="lazy" decoding="async"><div class="box cp"><p class="ey">Direção de arte</p><h2 class="dp">Cada detalhe, à altura do metro quadrado.</h2>
<p class="ld">Imagem tratada, luz corrigida, texto revisado. <b>Seu imóvel aparece como ele merece.</b></p></div><span class="a4-cr">Agami Park Residences · Moema</span></section>

<section class="a4-pf"><div class="a4-panel" data-d='{json.dumps(comp)}'>
<div class="a4-panelh"><h2>O que muda com a W3W.</h2><label class="a4-sel">Comparar com<select><option value="agencia">Agência de tráfego comum</option><option value="portal">Anúncio em portal</option></select></label></div>
<div class="a4-grid">
<div class="a4-tile"><strong data-k="a">{C['a']}</strong><span data-k="a2">{C['a2']}</span></div>
<div class="a4-tile im"><img src="{IMG}/la-galerie-moema/voo.jpg" alt="" loading="lazy"><span>Campanha com imagem do próprio produto</span></div>
<div class="a4-tile"><div class="glow"></div>{ic}<strong data-k="b" style="position:relative">{C['b']}</strong><span data-k="b2" style="position:relative">{C['b2']}</span></div>
<div class="a4-tile"><strong data-k="c">{C['c']}</strong><span data-k="c2">{C['c2']}</span></div>
<div class="a4-tile"><strong data-k="d">{C['d']}</strong><span data-k="d2">{C['d2']}</span></div>
<div class="a4-tile im"><img src="{IMG}/agami-park-residences/lazer-1.jpg" alt="" loading="lazy"><span>Hub com fichas e imagens para o time</span></div>
</div>
<p class="a4-fine">Os 15 minutos são a meta de retorno em horário comercial. Dados do dossiê informados pelo próprio lead, dentro da LGPD.</p>
</div></section>

<section class="a4-light" id="planos"><div class="box">
<div class="cp"><p class="ey">Planos</p><h2 class="dp" style="font-size:clamp(44px,5vw,72px)">Escolha o seu ritmo.</h2><p class="ld">Mais campanhas e mais tempo, menor o valor. A verba de mídia é paga direto ao Meta e ao Google.</p>
<div class="a4-tg" role="group" aria-label="Período"><button data-k="mensal" aria-pressed="true">Mensal</button><button data-k="trimestral" aria-pressed="false">Trimestral</button><button data-k="semestral" aria-pressed="false">Semestral</button></div></div>
<div class="a4-cards" data-p='{json.dumps(planos)}'>
{card(0, 'Para um lançamento', '1 campanha', ['Estratégia e públicos', 'Meta e Google Ads', 'Otimização semanal', 'Relatório de visitas'])}
{card(1, 'Mais escolhido', '2 campanhas', ['Tudo do plano anterior', 'Testes cruzados', 'Reunião quinzenal', 'Relatório comparativo'], True)}
{card(2, 'Para carteiras', '3 campanhas', ['Tudo do plano anterior', 'Prioridade de criação', 'Reunião semanal', 'Painel de resultados'])}
</div>
<div class="a4-sm">
<div><span>Adicional</span><b>Lead Dossiê · R$ 390/mês</b></div>
<div><span>Criativos</span><b>a partir de R$ 1.200</b></div>
<div><span>Landing page</span><b>a partir de R$ 2.500</b></div>
<div><span>Identidade e book</span><b>a partir de R$ 6.000</b></div>
</div>
<div class="a4-own">
<div class="d"><h3>Proprietário? Venda assistida.</h3><p>Você investe na produção e na campanha do seu imóvel. Se vender com a W3W, o valor é descontado da comissão, que cai de até 6% para 5%.</p><a class="a4-btn" href="{prop}" target="_blank" rel="noopener">Quero saber mais</a></div>
<div class="w"><h3>Perguntas rápidas.</h3>
<details><summary>A mídia está incluída?</summary><p>Não. A verba é paga direto ao Meta e ao Google, com total transparência.</p></details>
<details><summary>Preciso ter corretor?</summary><p>Não. O atendimento pode ser da W3W ou do seu time, com o hub de materiais.</p></details>
<details><summary>Existe fidelidade?</summary><p>O plano mensal pode ser cancelado a qualquer momento. Trimestral e semestral valem pelo período contratado.</p></details>
<details><summary>Atendem fora de Moema?</summary><p>Sim, sob consulta: Vila Nova Conceição, Itaim, Paraíso e Brooklin.</p></details>
</div></div>
</div></section>

<section class="a4-dir"><div class="box"><h2 class="h2">Continue explorando.</h2>
<div class="cols"><div class="c1"><p class="lb">Conheça</p><a href="{BASE}/#imoveis">Vitrine de imóveis</a><a href="{u('moema')}">Moema</a><a href="{u('guia-moema')}">Guia Moema</a></div>
<div class="cn"><p class="lb">Serviços</p><a href="#planos">Planos</a><a href="{contato}" target="_blank" rel="noopener">Montar campanha</a><a href="{prop}" target="_blank" rel="noopener">Venda assistida</a></div>
<div class="cn"><p class="lb">W3W</p><a href="{BASE}/#socios">Quem somos</a><a href="{u('contato')}">Contato</a><a href="{u('politica-de-privacidade')}">Privacidade</a></div></div>
</div></section>
</main>
''' + JS
