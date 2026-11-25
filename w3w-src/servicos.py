"""Página de serviços da W3W (marketing imobiliário) — versão high tech, escura. Chamado por build.py."""
import json

CSS = r"""
<style>
body:has(.sx){background:#070B12}
.sx{--bg:#070B12;--bg2:#0C121D;--bg3:#111A28;--tx:#E8EEF6;--tx2:#9AA8BA;--tx3:#5F6D80;--ln:rgba(232,238,246,.09);--ln2:rgba(232,238,246,.18);--ac:#8FC2FF;--ac2:#3D7DD8;--ok:#7BE0B3;--mono:ui-monospace,'SF Mono','JetBrains Mono',Menlo,monospace;background:var(--bg);color:var(--tx);overflow:hidden}
.sx ::selection{background:var(--ac);color:#06101E}
.sx a{color:inherit}
.sx .wrap{position:relative}
.sx section{position:relative;padding:120px 0;border-top:1px solid var(--ln)}
.sx .grid-bg{position:absolute;inset:0;pointer-events:none;background-image:linear-gradient(var(--ln) 1px,transparent 1px),linear-gradient(90deg,var(--ln) 1px,transparent 1px);background-size:80px 80px;mask-image:radial-gradient(ellipse 80% 70% at 50% 30%,#000 30%,transparent 80%);-webkit-mask-image:radial-gradient(ellipse 80% 70% at 50% 30%,#000 30%,transparent 80%);opacity:.7}
.sx h1,.sx h2{font-family:var(--sans);font-weight:300;letter-spacing:-.035em;margin:0;text-wrap:balance}
.sx h1{font-size:clamp(46px,7.2vw,112px);line-height:.95;max-width:14ch}
.sx h2{font-size:clamp(36px,4.6vw,68px);line-height:1;max-width:17ch}
.sx h1 em,.sx h2 em{font-family:var(--serif);font-style:italic;font-weight:200;color:var(--ac)}
.sx .lead{font-size:19px;line-height:1.55;color:var(--tx2);max-width:54ch;margin-top:24px}
.sx .tag{display:inline-flex;align-items:center;gap:8px;font:500 12px/1 var(--mono);letter-spacing:.06em;color:var(--tx2);padding:8px 12px;border:1px solid var(--ln2);border-radius:999px;background:rgba(143,194,255,.04)}
.sx .tag i{width:7px;height:7px;border-radius:50%;background:var(--ok);box-shadow:0 0 0 4px rgba(123,224,179,.15);animation:sxp 2s infinite}
@keyframes sxp{50%{box-shadow:0 0 0 7px rgba(123,224,179,0)}}
.sx-btn{display:inline-flex;align-items:center;gap:10px;height:52px;padding:0 24px;border-radius:12px;font:500 15px/1 var(--sans);text-decoration:none;transition:transform .2s var(--ease),background .25s,border-color .25s,box-shadow .3s}
.sx-btn.pri{background:var(--ac);color:#06101E;box-shadow:0 10px 30px -10px rgba(143,194,255,.6)}
.sx-btn.pri:hover{background:#B5D7FF;transform:translateY(-1px)}
.sx-btn.sec{border:1px solid var(--ln2);color:var(--tx)}
.sx-btn.sec:hover{border-color:var(--tx2)}
.sx-btn:focus-visible{outline:2px solid var(--ac);outline-offset:3px}
.sx-btn svg{width:16px;height:16px}
/* hero */
.sx-hero{padding:150px 0 90px!important;border-top:0!important}
.sx-hero .tag{margin-bottom:34px}
.sx-hgrid{display:grid;grid-template-columns:1.05fr 1fr;gap:56px;align-items:start}
.sx-cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:40px}
.sx-console{position:relative;background:linear-gradient(180deg,var(--bg2),var(--bg));border:1px solid var(--ln2);border-radius:20px;padding:0;overflow:hidden;box-shadow:0 40px 80px -40px rgba(0,0,0,.8),0 0 0 1px rgba(143,194,255,.04) inset}
.sx-console .bar{display:flex;align-items:center;gap:8px;padding:14px 18px;border-bottom:1px solid var(--ln);font:12px var(--mono);color:var(--tx3)}
.sx-console .bar b{width:9px;height:9px;border-radius:50%;background:var(--ln2)}
.sx-console .bar span{margin-left:auto;color:var(--ok)}
.sx-pipe{padding:22px 18px 8px}
.sx-pipe svg{width:100%;height:auto;display:block}
.sx-pipe .nd rect{fill:var(--bg3);stroke:var(--ln2)}
.sx-pipe .nd text{fill:var(--tx);font:500 12px var(--sans)}
.sx-pipe .nd .s{fill:var(--tx3);font:10px var(--mono)}
.sx-pipe path.l{stroke:var(--ln2);fill:none;stroke-width:1.2}
.sx-pipe circle.d{fill:var(--ac);filter:drop-shadow(0 0 6px rgba(143,194,255,.9))}
.sx-feed{border-top:1px solid var(--ln);font:12.5px/1.5 var(--mono);height:178px;overflow:hidden;position:relative}
.sx-feed::after{content:"";position:absolute;left:0;right:0;bottom:0;height:60px;background:linear-gradient(transparent,var(--bg))}
.sx-feed div{display:grid;grid-template-columns:62px 1fr auto;gap:12px;padding:9px 18px;border-bottom:1px solid var(--ln);color:var(--tx2);animation:sxin .6s var(--ease)}
.sx-feed div b{color:var(--tx);font-weight:500}
.sx-feed .sc{color:#06101E;background:var(--ok);border-radius:5px;padding:0 7px;font-weight:600}
.sx-feed .sc.b{background:var(--ac)}.sx-feed .sc.c{background:var(--tx3);color:var(--tx)}
@keyframes sxin{from{opacity:0;transform:translateY(-8px);filter:blur(3px)}}
.sx-console .ft{display:flex;justify-content:space-between;padding:12px 18px;border-top:1px solid var(--ln);font:11px var(--mono);color:var(--tx3)}
.sx-kpis{display:grid;grid-template-columns:repeat(4,1fr);margin-top:80px;border-top:1px solid var(--ln2)}
.sx-kpis div{padding:24px 24px 0 0}
.sx-kpis div+div{padding-left:24px;border-left:1px solid var(--ln)}
.sx-kpis b{display:block;font:300 30px/1.1 var(--sans);letter-spacing:-.02em;margin-bottom:8px}
.sx-kpis span{font-size:14px;color:var(--tx2);line-height:1.45}
/* vs */
.sx-vs{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:64px}
.sx-vs>div{border:1px solid var(--ln);border-radius:18px;padding:30px;background:var(--bg2)}
.sx-vs .us{border-color:rgba(143,194,255,.35);background:linear-gradient(180deg,rgba(143,194,255,.07),var(--bg2) 60%)}
.sx-vs h3{font:500 12px var(--mono);letter-spacing:.08em;color:var(--tx3);margin:0 0 18px;text-transform:uppercase}
.sx-vs .us h3{color:var(--ac)}
.sx-vs ul{list-style:none;margin:0;padding:0}
.sx-vs li{display:flex;gap:12px;align-items:baseline;padding:13px 0;border-top:1px solid var(--ln);font-size:17px;line-height:1.4;color:var(--tx3)}
.sx-vs .us li{color:var(--tx)}
.sx-vs li svg{flex:none;width:14px;height:14px;transform:translateY(2px)}
/* who */
.sx-who{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;margin-top:64px;background:var(--ln);border:1px solid var(--ln);border-radius:18px;overflow:hidden}
.sx-who>div{background:var(--bg);padding:34px 30px 30px;transition:background .3s}
.sx-who>div:hover{background:var(--bg2)}
.sx-who h3{font:300 30px/1.05 var(--sans);letter-spacing:-.02em;margin:0 0 14px}
.sx-who p{margin:0 0 22px;font-size:16px;line-height:1.55;color:var(--tx2)}
.sx-who li{list-style:none;font:13px var(--mono);color:var(--tx2);padding:9px 0;border-top:1px solid var(--ln)}
.sx-who li::before{content:"→ ";color:var(--ac)}
.sx-who ul{margin:0;padding:0}
/* dossie */
.sx-dos{display:grid;grid-template-columns:1fr 1.05fr;gap:72px;align-items:center}
.sx-doc{border:1px solid rgba(143,194,255,.3);border-radius:20px;background:var(--bg2);overflow:hidden;box-shadow:0 50px 90px -50px rgba(61,125,216,.55)}
.sx-doc header{display:flex;justify-content:space-between;align-items:center;padding:18px 22px;border-bottom:1px solid var(--ln)}
.sx-doc header b{font:400 20px var(--sans)}
.sx-doc header span{font:11px var(--mono);color:var(--tx3)}
.sx-doc dl{margin:0;padding:6px 22px}
.sx-doc dl div{display:grid;grid-template-columns:130px 1fr;gap:12px;padding:12px 0;border-bottom:1px solid var(--ln);font-size:15px}
.sx-doc dt{font:12px var(--mono);color:var(--tx3);padding-top:2px}
.sx-doc dd{margin:0}
.sx-meter{display:flex;align-items:center;gap:12px}
.sx-meter i{flex:1;height:6px;border-radius:3px;background:var(--ln);overflow:hidden;position:relative}
.sx-meter i::after{content:"";position:absolute;inset:0;width:var(--v,0%);background:linear-gradient(90deg,var(--ac2),var(--ok));border-radius:3px;transition:width 1.6s var(--ease)}
.sx-meter b{font:600 13px var(--mono);color:#06101E;background:var(--ok);padding:3px 8px;border-radius:6px}
.sx-doc .msg{margin:16px 22px 22px;padding:16px 18px;border-radius:14px 14px 14px 4px;background:#12324F;color:#EAF4FF;font-size:16px;line-height:1.45}
.sx-doc .msg small{display:block;margin-top:8px;font:11px var(--mono);color:rgba(234,244,255,.55)}
.sx-dos ul{list-style:none;margin:36px 0 0;padding:0}
.sx-dos li{display:grid;grid-template-columns:36px 1fr;gap:14px;padding:16px 0;border-top:1px solid var(--ln);font-size:16.5px;line-height:1.5;color:var(--tx2)}
.sx-dos li b{color:var(--tx);font-weight:500}
.sx-dos li svg{width:20px;height:20px;color:var(--ac);margin-top:2px}
/* flow */
.sx-flow{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:64px}
.sx-flow div{border:1px solid var(--ln);border-radius:16px;padding:22px;background:var(--bg2);position:relative}
.sx-flow code{font:12px var(--mono);color:var(--ac)}
.sx-flow b{display:block;font:400 22px var(--sans);margin:14px 0 10px;letter-spacing:-.01em}
.sx-flow p{margin:0;font-size:14.5px;line-height:1.5;color:var(--tx2)}
/* art */
.sx-art{display:grid;grid-template-columns:1.15fr 1fr;gap:72px;align-items:center}
.sx-art .cred{font:300 clamp(26px,2.8vw,40px)/1.2 var(--sans);letter-spacing:-.02em;margin-top:28px;color:var(--tx2)}
.sx-art .cred b{color:var(--tx);font-weight:300}
.sx-logos{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--ln);border:1px solid var(--ln);border-radius:18px;overflow:hidden}
.sx-logos div{background:var(--bg);padding:28px 24px;font:300 26px var(--sans);letter-spacing:-.01em}
.sx-logos div span{display:block;font:11px var(--mono);color:var(--tx3);margin-top:8px;letter-spacing:.06em}
.sx-svc{display:flex;flex-wrap:wrap;gap:8px;margin-top:30px}
.sx-svc span{font:13px var(--mono);color:var(--tx2);border:1px solid var(--ln2);border-radius:999px;padding:8px 14px}
/* planos */
.sx-seg{display:inline-flex;gap:4px;padding:4px;border-radius:12px;border:1px solid var(--ln2);background:var(--bg2);margin-top:44px}
.sx-seg button{border:0;background:transparent;font:500 14px/1 var(--sans);color:var(--tx2);padding:12px 18px;border-radius:9px;cursor:pointer;transition:background .25s var(--ease),color .2s}
.sx-seg button[aria-pressed=true]{background:var(--ac);color:#06101E}
.sx-seg button:focus-visible{outline:2px solid var(--ac);outline-offset:2px}
.sx-seg em{font-style:normal;font:11px var(--mono);margin-left:6px;opacity:.75}
.sx-plans{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:28px}
.sx-plan{border:1px solid var(--ln);border-radius:20px;padding:30px;background:var(--bg2);display:flex;flex-direction:column}
.sx-plan.hot{border-color:rgba(143,194,255,.5);background:linear-gradient(180deg,rgba(143,194,255,.09),var(--bg2) 55%);box-shadow:0 40px 80px -50px rgba(61,125,216,.6)}
.sx-plan h3{font:500 13px var(--mono);letter-spacing:.06em;color:var(--tx2);margin:0;text-transform:uppercase}
.sx-plan.hot h3{color:var(--ac)}
.sx-plan .pr{font:300 54px/1 var(--sans);letter-spacing:-.04em;margin:22px 0 4px;font-variant-numeric:tabular-nums}
.sx-plan .pr small{font:14px var(--sans);color:var(--tx3);letter-spacing:0;margin-left:4px}
.sx-plan .un{font:12px var(--mono);color:var(--tx3)}
.sx-plan ul{list-style:none;margin:24px 0 28px;padding:0;flex:1}
.sx-plan li{padding:10px 0;border-top:1px solid var(--ln);font-size:15px;color:var(--tx2)}
.sx-plan li::before{content:"✓";display:none}
.sx-plan .sx-btn{justify-content:center}
.sx-addon{display:grid;grid-template-columns:auto 1fr auto;gap:28px;align-items:center;margin-top:16px;border:1px dashed rgba(143,194,255,.4);border-radius:18px;padding:24px 28px;background:rgba(143,194,255,.04)}
.sx-addon b{font:400 22px var(--sans)}
.sx-addon p{margin:0;color:var(--tx2);font-size:15px;line-height:1.5}
.sx-addon .pr{font:300 32px var(--sans);white-space:nowrap}
.sx-addon .pr small{font:13px var(--sans);color:var(--tx3)}
.sx-proj{margin-top:56px;border-top:1px solid var(--ln2)}
.sx-proj div{display:grid;grid-template-columns:1fr 1.4fr auto;gap:28px;align-items:baseline;padding:22px 0;border-bottom:1px solid var(--ln)}
.sx-proj b{font:400 20px var(--sans)}
.sx-proj p{margin:0;color:var(--tx2);font-size:15px}
.sx-proj span{font:300 22px var(--sans);white-space:nowrap;font-variant-numeric:tabular-nums}
.sx-note{margin-top:20px;font:12.5px/1.6 var(--mono);color:var(--tx3);max-width:90ch}
.sx-own{margin-top:56px;display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;border-radius:20px;padding:40px;background:linear-gradient(120deg,#0F2238,#0B1626);border:1px solid rgba(143,194,255,.25)}
.sx-own h3{font:300 36px/1.05 var(--sans);letter-spacing:-.02em;margin:0}
.sx-own p{margin:0 0 20px;color:var(--tx2);font-size:16.5px;line-height:1.55}
/* faq */
.sx-faq{margin-top:48px;border-top:1px solid var(--ln2);max-width:900px}
.sx-faq details{border-bottom:1px solid var(--ln)}
.sx-faq summary{cursor:pointer;list-style:none;padding:24px 44px 24px 0;font:400 21px var(--sans);position:relative}
.sx-faq summary::-webkit-details-marker{display:none}
.sx-faq summary::after{content:"+";position:absolute;right:4px;top:50%;transform:translateY(-50%);font:300 26px var(--sans);color:var(--ac);transition:transform .3s var(--ease)}
.sx-faq details[open] summary::after{transform:translateY(-50%) rotate(45deg)}
.sx-faq summary:focus-visible{outline:2px solid var(--ac);outline-offset:3px}
.sx-faq details p{margin:0 0 24px;max-width:68ch;font-size:16.5px;line-height:1.6;color:var(--tx2)}
.sx-end{text-align:center}
.sx-end h2{margin:0 auto;max-width:16ch}
.sx-end .sx-cta{justify-content:center}
.sx .rv{opacity:0;transform:translateY(18px);filter:blur(6px);transition:opacity .9s var(--ease),transform .9s var(--ease),filter .9s var(--ease)}
.sx .rv.in{opacity:1;transform:none;filter:none}
@media(prefers-reduced-motion:reduce){.sx .rv{opacity:1;transform:none;filter:none}.sx-feed div{animation:none}}
/* header escuro nesta página */
body:has(.sx) .hd{background:rgba(7,11,18,.72)!important;border-bottom-color:rgba(232,238,246,.08)!important;color:#E8EEF6}
body:has(.sx) .hd .brand svg,body:has(.sx) .hd .burger{color:#E8EEF6}
body:has(.sx) .hd .creci{color:rgba(232,238,246,.55)}
body:has(.sx) .hd .nav .btn{border-color:rgba(232,238,246,.4);color:#E8EEF6}
@media(max-width:900px){body:has(.sx) .hd .nav{background:#0C121D;color:#E8EEF6}}
@media(max-width:900px){.sx section{padding:84px 0}.sx-hero{padding-top:118px!important}.sx-hgrid,.sx-dos,.sx-art,.sx-own,.sx-vs{grid-template-columns:1fr;gap:36px}.sx-kpis{grid-template-columns:1fr 1fr;row-gap:24px}.sx-kpis div:nth-child(3){border-left:0;padding-left:0}.sx-who,.sx-plans{grid-template-columns:1fr}.sx-flow{grid-template-columns:1fr 1fr}.sx-addon,.sx-proj div{grid-template-columns:1fr;gap:8px}.sx-own{padding:28px}.sx-doc dl div{grid-template-columns:100px 1fr}}
</style>"""

CHK = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 8.5l3.2 3L13 4.5"/></svg>'
XX = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M4 4l8 8M12 4l-8 8"/></svg>'
ARW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
IC = {
    'user': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>',
    'gauge': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 15a9 9 0 0118 0"/><path d="M12 15l4-5"/></svg>',
    'msg': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 5h16v11H9l-5 4z"/></svg>',
    'card': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 10h18"/></svg>',
}


def render(wa, way, BASE, u):
    contato = wa('Olá! Vi a página de serviços da W3W e quero conversar sobre uma campanha.')
    prop = wa('Olá! Tenho um imóvel de alto padrão e quero saber como funciona a venda assistida da W3W.')
    planos = {'mensal': (1500, 1400, 1300), 'trimestral': (1350, 1250, 1150), 'semestral': (1200, 1100, 1000)}
    P = json.dumps(planos)
    fm = lambda n: f"{n:,.0f}".replace(',', '.')
    m = planos['mensal']
    plan = lambda i, nome, txt, itens, hot=False: f'''<div class="sx-plan{' hot' if hot else ''} rv"><h3>{nome}</h3><div class="pr">R$ <span data-i="{i}">{fm(m[i])}</span><small>/mês</small></div><div class="un">por campanha · mídia à parte</div><ul>{''.join(f'<li>{x}</li>' for x in itens)}</ul><a class="sx-btn {'pri' if hot else 'sec'}" href="{wa('Olá! Quero contratar o plano ' + nome + ' da W3W.')}" target="_blank" rel="noopener">{txt}</a></div>'''
    pipe = '''<svg viewBox="0 0 520 210" role="img" aria-label="Fluxo: campanha, lead, dossiê e corretor">
<path class="l" id="p1" d="M100 52 C160 52 160 105 210 105"/><path class="l" id="p2" d="M100 158 C160 158 160 105 210 105"/><path class="l" id="p3" d="M310 105 L360 105"/><path class="l" id="p4" d="M460 105 L470 105"/>
<g class="nd"><rect x="8" y="30" width="92" height="44" rx="10"/><text x="20" y="50">Meta Ads</text><text class="s" x="20" y="64">campanha 01</text></g>
<g class="nd"><rect x="8" y="136" width="92" height="44" rx="10"/><text x="20" y="156">Google Ads</text><text class="s" x="20" y="170">campanha 02</text></g>
<g class="nd"><rect x="210" y="80" width="100" height="50" rx="10"/><text x="222" y="102">Triagem</text><text class="s" x="222" y="117">site + WhatsApp</text></g>
<g class="nd"><rect x="360" y="80" width="100" height="50" rx="10" style="stroke:rgba(143,194,255,.6)"/><text x="372" y="102">Lead Dossiê</text><text class="s" x="372" y="117">score · roteiro</text></g>
<circle class="d" r="3.5"><animateMotion dur="2.4s" repeatCount="indefinite"><mpath href="#p1"/></animateMotion></circle>
<circle class="d" r="3.5"><animateMotion dur="2.4s" begin="1.2s" repeatCount="indefinite"><mpath href="#p2"/></animateMotion></circle>
<circle class="d" r="3.5"><animateMotion dur="1.2s" repeatCount="indefinite"><mpath href="#p3"/></animateMotion></circle>
</svg>'''
    return CSS + f'''
<main class="sx">
<section class="sx-hero"><div class="grid-bg"></div><div class="wrap">
<div class="sx-hgrid">
<div><h1>Do anúncio à chave, <em>com inteligência.</em></h1>
<p class="lead">Campanha dedicada para cada produto, criação assinada por Head of Art e o Lead Dossiê: cada contato chega ao corretor com perfil, prioridade e o roteiro da primeira conversa.</p>
<div class="sx-cta"><a class="sx-btn pri" href="{contato}" target="_blank" rel="noopener">Falar com a W3W {ARW}</a><a class="sx-btn sec" href="#planos">Ver planos</a></div></div>
<div class="sx-console rv" aria-label="Simulação do fluxo de leads da W3W"><div class="bar"><b></b><b></b><b></b>w3w · operação de leads<span>● simulação ao vivo</span></div>
<div class="sx-pipe">{pipe}</div>
<div class="sx-feed" id="sxFeed" aria-hidden="true"></div>
<div class="ft"><span>dados ilustrativos</span><span id="sxClock">--:--</span></div></div>
</div>
<div class="sx-kpis rv"><div><b>1 produto, 1 campanha</b><span>Estratégia, verba, público e criativos próprios.</span></div><div><b>Criação de agência</b><span>Padrão FIFA™, Rio 2016, Coca-Cola e Itaú.</span></div><div><b>Lead Dossiê</b><span>Score e roteiro no WhatsApp do corretor.</span></div><div><b>Desde 2004</b><span>Imobiliária que conhece Moema rua a rua.</span></div></div>
</div></section>

<section><div class="wrap">
<h2 class="rv">Agências entregam contatos. <em>Nós entregamos compradores.</em></h2>
<div class="sx-vs"><div class="rv"><h3>Agência de tráfego comum</h3><ul>
<li>{XX}Criativo de banco de imagem</li><li>{XX}Lead frio, sem contexto</li><li>{XX}Relatório de cliques</li><li>{XX}Não conhece produto nem bairro</li><li>{XX}Para no formulário</li></ul></div>
<div class="us rv"><h3>W3W</h3><ul>
<li>{CHK}Direção de arte, imagem tratada e vídeo</li><li>{CHK}Lead com dossiê e roteiro de abordagem</li><li>{CHK}Relatório de visitas e propostas</li><li>{CHK}Corretores de Moema desde 2004</li><li>{CHK}Vai até a assinatura</li></ul></div></div>
</div></section>

<section class="sx-dark2"><div class="grid-bg" style="opacity:.4"></div><div class="wrap sx-dos">
<div class="rv"><h2>Lead Dossiê <em>W3W.</em></h2>
<p class="lead">Antes do primeiro "olá", o corretor já sabe o que a pessoa procura, quanto pretende investir, quando quer comprar e por onde começar.</p>
<ul><li>{IC['user']}<span><b>Dados do próprio lead.</b> Faixa de investimento, objetivo e prazo, coletados na triagem. Sem compra de base, dentro da LGPD.</span></li>
<li>{IC['gauge']}<span><b>Score A, B ou C</b> e prazo de retorno sugerido.</span></li>
<li>{IC['msg']}<span><b>Roteiro de abordagem</b> com o texto certo do hub, pronto para copiar.</span></li>
<li>{IC['card']}<span><b>Card do imóvel</b> e campanha de origem no mesmo WhatsApp.</span></li></ul></div>
<div class="sx-doc rv" id="sxDoc"><header><b>Lead Dossiê</b><span>exemplo · dados fictícios</span></header>
<dl><div><dt>lead</dt><dd>Mariana, 41</dd></div><div><dt>imóvel</dt><dd>Cobertura 1.184 m² · Moema</dd></div><div><dt>origem</dt><dd>Instagram · campanha Coberturas</dd></div><div><dt>investimento</dt><dd>Acima de R$ 20 milhões</dd></div><div><dt>objetivo</dt><dd>Morar · família com 2 filhos</dd></div><div><dt>prazo</dt><dd>Até 6 meses</dd></div>
<div><dt>score</dt><dd><span class="sx-meter"><i style="--v:0%" data-v="92%"></i><b>A · 92</b></span></dd></div><div><dt>retorno</dt><dd>Em até 15 minutos</dd></div></dl>
<div class="msg">"Mariana, vi que você quer morar perto do Ibirapuera com a família. Posso te mostrar a planta da cobertura e marcar uma visita privativa?"<small>roteiro sugerido · enviado ao corretor</small></div></div>
</div></section>

<section><div class="wrap">
<h2 class="rv">Três formas de <em>trabalhar com a W3W.</em></h2>
<div class="sx-who rv">
<div><h3>Incorporadoras</h3><p>Lançamento e estoque com campanha por produto, landing page própria, criativos e hub de vendas para o time comercial.</p><ul><li>Campanha por empreendimento</li><li>Landing page e book</li><li>Lead Dossiê para o plantão</li></ul></div>
<div><h3>Imobiliárias e corretores</h3><p>Leads do produto que você vende, com texto pronto para o primeiro contato e o card do imóvel direto no WhatsApp.</p><ul><li>Tráfego por produto</li><li>Triagem no WhatsApp</li><li>Textos e fichas no hub</li></ul></div>
<div><h3>Proprietários</h3><p>Venda assistida: produção de imagem, campanha exclusiva e atendimento W3W, com o investimento abatido da comissão.</p><ul><li>Imagem tratada e vídeo</li><li>Campanha só do seu imóvel</li><li>Atendimento e negociação</li></ul></div>
</div></div></section>

<section><div class="wrap">
<h2 class="rv">Do produto <em>à proposta.</em></h2>
<div class="sx-flow">
<div class="rv"><code>01 · produto</code><b>Diagnóstico</b><p>Público, praça, concorrência e o que torna o imóvel único.</p></div>
<div class="rv"><code>02 · criação</code><b>Direção de arte</b><p>Identidade, imagens tratadas, carrosséis, vídeo e landing page.</p></div>
<div class="rv"><code>03 · mídia</code><b>Campanha</b><p>Meta e Google Ads com verba, público e otimização próprios.</p></div>
<div class="rv"><code>04 · dados</code><b>Dossiê</b><p>Triagem, score e roteiro de cada lead em tempo real.</p></div>
<div class="rv"><code>05 · venda</code><b>Atendimento</b><p>Corretor W3W ou do seu time, com o hub de materiais.</p></div>
</div></div></section>

<section><div class="wrap sx-art">
<div class="rv"><h2>Criação de agência, <em>não de template.</em></h2>
<p class="cred"><b>Direção de arte de Kco Oyakawa</b>, Head of Art com mais de 20 anos em agências de publicidade.</p>
<div class="sx-svc"><span>identidade e naming</span><span>book e ficha técnica</span><span>tratamento de imagem</span><span>carrosséis e reels</span><span>vídeo</span><span>landing page</span></div>
<div class="sx-cta"><a class="sx-btn sec" href="https://kcooyakawa.github.io/kco-imobiliario/" target="_blank" rel="noopener">Ver portfólio imobiliário {ARW}</a></div></div>
<div class="sx-logos rv"><div>FIFA™<span>COPA DO MUNDO 2014</span></div><div>Rio 2016<span>JOGOS OLÍMPICOS</span></div><div>Coca-Cola<span>CAMPANHAS</span></div><div>Itaú<span>CAMPANHAS</span></div></div>
</div></section>

<section id="planos"><div class="grid-bg" style="opacity:.35"></div><div class="wrap">
<h2 class="rv">Planos <em>transparentes.</em></h2>
<p class="lead rv">Preço por campanha por mês. Mais produtos e mais tempo, menor o valor. A verba de mídia é paga direto ao Meta e ao Google.</p>
<div class="sx-seg" role="group" aria-label="Período"><button type="button" data-p="mensal" aria-pressed="true">Mensal</button><button type="button" data-p="trimestral" aria-pressed="false">Trimestral<em>−10%</em></button><button type="button" data-p="semestral" aria-pressed="false">Semestral<em>−20%</em></button></div>
<div class="sx-plans">
{plan(0, '1 campanha', 'Começar com 1 produto', ['Estratégia e diagnóstico do produto', 'Meta e Google Ads', 'Públicos e otimização semanal', 'Relatório de leads e visitas'])}
{plan(1, '2 campanhas', 'Escolher 2 campanhas', ['Tudo do plano 1 campanha', 'Verba e criativos por produto', 'Comparativo entre produtos', 'Reunião quinzenal de performance'], True)}
{plan(2, '3 campanhas', 'Escolher 3 campanhas', ['Tudo do plano 2 campanhas', 'Prioridade de criação', 'Dashboard consolidado', 'A partir de 4: plano sob medida'])}
</div>
<div class="sx-addon rv"><b>+ Lead Dossiê</b><p>Triagem do lead, score A/B/C, roteiro de abordagem e entrega no WhatsApp do corretor. Opcional em qualquer plano.</p><div class="pr">R$ 390<small> /campanha/mês</small></div></div>
<div class="sx-proj rv">
<div><b>Criativos da campanha</b><p>Carrosséis, estáticos e reels com direção de arte, por ciclo mensal.</p><span>a partir de R$ 1.200/mês</span></div>
<div><b>Landing page do produto</b><p>Página rápida, com card para WhatsApp e triagem do lead.</p><span>a partir de R$ 2.500</span></div>
<div><b>Identidade e book</b><p>Marca, naming, book de vendas, ficha técnica e cards.</p><span>a partir de R$ 6.000</span></div>
<div><b>Hub de vendas</b><p>Textos prontos, fichas, tabelas e imagens de cada produto para o time.</p><span>R$ 1.900 + R$ 290/mês</span></div>
</div>
<p class="sx-note">Trimestral e semestral contratados pelo período completo, em até 3x ou 6x. Valores por campanha/mês, sem a verba de mídia.</p>
<div class="sx-own rv"><h3>Proprietário? <em style="font-family:var(--serif);font-style:italic;font-weight:200;color:var(--ac)">Venda assistida.</em></h3><div><p>Você investe antes na produção e na campanha do seu imóvel. Se vender com a W3W, o valor é descontado da comissão, que cai de até 6% para 5%.</p><a class="sx-btn pri" href="{prop}" target="_blank" rel="noopener">Quero saber mais {ARW}</a></div></div>
</div></section>

<section><div class="wrap">
<h2 class="rv">Perguntas <em>frequentes.</em></h2>
<div class="sx-faq">
<details><summary>O valor da mídia está incluído?</summary><p>Não. A verba de anúncios é paga direto ao Meta e ao Google, no cartão do cliente. A W3W recomenda o valor ideal para cada produto.</p></details>
<details><summary>Preciso ter corretor próprio?</summary><p>Não. Os leads podem ser atendidos pela equipe da W3W ou pela sua, que recebe o Lead Dossiê e o hub de textos para o primeiro contato.</p></details>
<details><summary>O Lead Dossiê usa dados de terceiros?</summary><p>Não. Usamos o que o próprio lead informa na triagem e os dados da campanha de origem. Nada de compra de base ou estimativa de renda por fontes externas.</p></details>
<details><summary>Atendem fora de Moema?</summary><p>Sim. Moema é a nossa especialidade, e também trabalhamos com Vila Nova Conceição, Itaim, Paraíso e Brooklin, sob consulta.</p></details>
<details><summary>Existe fidelidade?</summary><p>No plano mensal, não. Os planos trimestral e semestral têm desconto e são contratados pelo período completo.</p></details>
</div></div></section>

<section class="sx-end"><div class="grid-bg"></div><div class="wrap">
<h2 class="rv">Vamos colocar o seu produto <em>em movimento?</em></h2>
<div class="sx-cta"><a class="sx-btn pri" href="{contato}" target="_blank" rel="noopener">Falar com a W3W no WhatsApp {ARW}</a><a class="sx-btn sec" href="{BASE}/">Ver a vitrine W3W</a></div>
</div></section>
</main>
<script>(function(){{
var P={P};document.querySelectorAll('.sx-seg button').forEach(function(b){{b.onclick=function(){{document.querySelectorAll('.sx-seg button').forEach(function(x){{x.setAttribute('aria-pressed',x===b)}});var v=P[b.dataset.p];document.querySelectorAll('.sx-plan [data-i]').forEach(function(s){{s.textContent=v[+s.dataset.i].toLocaleString('pt-BR')}})}}}});
var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);if(e.target.id==='sxDoc'){{var m=e.target.querySelector('[data-v]');setTimeout(function(){{m.style.setProperty('--v',m.dataset.v)}},300)}}}}}})}},{{threshold:.15}});document.querySelectorAll('.sx .rv').forEach(function(el){{io.observe(el)}});
var F=document.getElementById('sxFeed'),C=document.getElementById('sxClock'),L=[['Cobertura · Moema','A'],['Studio · Moema','B'],['Apto 258 m² · Moema','A'],['Casa · Brooklin','A'],['Apto 147 m² · Moema','B'],['Studio · investimento','C'],['Duplex 625 m² · Moema','A'],['Apto 170 m² · Moema','B']],N=['Mariana','Rafael','Helena','Pedro','Camila','Bruno','Lúcia','André'],k=0;
function t(){{var d=new Date();return ('0'+d.getHours()).slice(-2)+':'+('0'+d.getMinutes()).slice(-2)+':'+('0'+d.getSeconds()).slice(-2)}}
function add(){{var x=L[k%L.length],n=N[(k*3)%N.length],r=document.createElement('div');r.innerHTML='<span>'+t()+'</span><span><b>'+n+'</b> · '+x[0]+'</span><span class="sc '+(x[1]==='A'?'':x[1]==='B'?'b':'c')+'">'+x[1]+'</span>';F.insertBefore(r,F.firstChild);while(F.children.length>6)F.removeChild(F.lastChild);k++}}
if(F){{for(var i=0;i<4;i++)add();if(!matchMedia('(prefers-reduced-motion: reduce)').matches)setInterval(add,2600);setInterval(function(){{C.textContent=t()}},1000);C.textContent=t()}}
}})();</script>
'''
