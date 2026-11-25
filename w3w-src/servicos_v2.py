"""Serviços W3W — versão 2, na linguagem visual do site KCO Studio (suíço, grotesca condensada, branco)."""
import json

F = '/kco-imobiliario/w3w-fonts/kco'
IMG = 'https://kcooyakawa.github.io/kco-imobiliario/w3w-img'

CSS = r"""
<style>
@font-face{font-family:"KCO Grotesk";src:url("%F/grotesk-300.woff") format("woff");font-weight:300;font-display:swap}
@font-face{font-family:"KCO Grotesk";src:url("%F/grotesk-500.woff") format("woff");font-weight:500;font-display:swap}
@font-face{font-family:"KCO Text";src:url("%F/text-400.woff") format("woff");font-weight:400;font-display:swap}
@font-face{font-family:"KCO Label";src:url("%F/label-500.woff") format("woff");font-weight:500;font-display:swap}
body:has(.k2){background:#FAFAFA}
.k2{--k:#111;--k2:#555;--k3:#8A8A8A;--ln:#111;--ln2:rgba(17,17,17,.14);--g:'KCO Grotesk',sans-serif;--t:'KCO Text','Helvetica Neue',Helvetica,Arial,sans-serif;--l:'KCO Label',sans-serif;background:#FAFAFA;color:var(--k);font-family:var(--t)}
.k2 ::selection{background:#111;color:#fff}
.k2 .wrap{max-width:1360px}
.k2 .lb{font:500 10.5px/1.4 var(--l);letter-spacing:.14em;text-transform:uppercase}
.k2 section{position:relative}
.k2-meta{display:grid;grid-template-columns:1.4fr 1.4fr 1fr auto;gap:24px;border-top:1px solid var(--ln);padding-top:12px;margin-top:118px}
.k2-meta .on::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:#D93A2B;margin-right:8px;vertical-align:1px}
.k2-hero{min-height:calc(100vh - 84px);display:flex;flex-direction:column}
.k2-hero .intro{margin-top:auto;padding-top:120px;max-width:600px;font:300 clamp(20px,1.7vw,25px)/1.35 var(--g);color:var(--k)}
.k2-word{display:flex;justify-content:space-between;align-items:flex-end;margin:40px -1vw 0;font:500 clamp(120px,24vw,380px)/.78 var(--g);letter-spacing:-.06em;user-select:none}
.k2-word span{display:block;transform:translateY(var(--y,0));transition:transform 1.2s cubic-bezier(.2,.7,.2,1)}
.k2-scroll{text-align:center;margin:18px 0 22px;color:var(--k3)}
.k2-band{position:relative;height:78vh;min-height:520px;overflow:hidden;background:#111}
.k2-band img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.62;transform:scale(1.08);transition:transform .1s linear}
.k2-band .ln{position:absolute;left:0;right:0;font:300 clamp(48px,7vw,110px)/1 var(--g);letter-spacing:-.03em;color:#fff;white-space:nowrap}
.k2-band .l1{top:36%;transform:translateX(var(--x1,-4%))}.k2-band .l2{top:52%;transform:translateX(var(--x2,18%))}
.k2-cta{background:#111;color:#fff;padding:34px 0}
.k2-cta .wrap{display:flex;justify-content:space-between;align-items:center;gap:32px}
.k2-cta p{margin:0;max-width:58ch;font-size:16px;line-height:1.55;color:rgba(255,255,255,.82)}
.k2-btn{display:inline-flex;align-items:center;gap:8px;height:46px;padding:0 18px;font:500 13px var(--t);text-decoration:none;border:1px solid currentColor;white-space:nowrap;transition:background .2s,color .2s}
.k2-btn.w{background:#fff;color:#111;border-color:#fff}.k2-btn.w:hover{background:transparent;color:#fff}
.k2-btn.o{color:#fff}.k2-btn.o:hover{background:#fff;color:#111}
.k2-btn.k{background:#111;color:#fff;border-color:#111}.k2-btn.k:hover{background:transparent;color:#111}
.k2-btn.ko{color:#111}.k2-btn.ko:hover{background:#111;color:#fff}
.k2-btn:focus-visible{outline:2px solid #111;outline-offset:3px}
.k2-sec{padding:120px 0;border-bottom:1px solid var(--ln2)}
.k2-hd{display:grid;grid-template-columns:1fr 2fr;gap:32px;border-top:1px solid var(--ln);padding-top:12px}
.k2-hd h2{font:500 clamp(36px,4vw,56px)/1.02 var(--g);letter-spacing:-.03em;margin:0;max-width:18ch}
.k2-hd p{margin:16px 0 0;max-width:56ch;font-size:16.5px;line-height:1.6;color:var(--k2)}
.k2-big{display:flex;justify-content:space-between;align-items:baseline;gap:32px;border-top:1px solid var(--ln);padding-top:12px;margin-bottom:40px}
.k2-big h2{font:300 clamp(44px,6.4vw,104px)/.95 var(--g);letter-spacing:-.035em;text-transform:uppercase;margin:0}
.k2-vs{display:grid;grid-template-columns:1fr 1fr;margin-top:48px}
.k2-vs>div{padding-right:40px}.k2-vs>div+div{padding:0 0 0 40px;border-left:1px solid var(--ln2)}
.k2-vs .lb{display:block;padding-bottom:12px;border-bottom:1px solid var(--ln);color:var(--k3)}
.k2-vs .us .lb{color:var(--k)}
.k2-vs li{list-style:none;padding:15px 0;border-bottom:1px solid var(--ln2);font:300 22px/1.25 var(--g);letter-spacing:-.01em}
.k2-vs .them li{color:var(--k3);text-decoration:line-through;text-decoration-thickness:1px;text-decoration-color:rgba(17,17,17,.3)}
.k2-vs ul{margin:0;padding:0}
.k2-boxes{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:56px}
.k2-box{border:1px solid var(--ln);background:#fff;min-height:260px;display:flex;flex-direction:column;padding:20px 22px 24px;position:relative;transition:background .3s,color .3s}
.k2-box:hover{background:#111;color:#fff}
.k2-box:hover p,.k2-box:hover li{color:rgba(255,255,255,.75)}
.k2-box .top{display:flex;justify-content:space-between}
.k2-box h3{margin:auto 0 10px;font:500 30px/1.05 var(--g);letter-spacing:-.02em}
.k2-box p{margin:0;font-size:15px;line-height:1.55;color:var(--k2);max-width:46ch}
.k2-box ul{margin:16px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:6px}
.k2-box li{list-style:none;font:500 10.5px var(--l);letter-spacing:.12em;text-transform:uppercase;border:1px solid currentColor;padding:6px 9px;color:var(--k2)}
.k2-tl{margin-top:56px;border-top:1px solid var(--ln)}
.k2-tl div{display:grid;grid-template-columns:140px 1fr 1.2fr;gap:24px;padding:16px 0;border-bottom:1px solid var(--ln2);font-size:15px;align-items:baseline}
.k2-tl b{font:500 18px var(--g)}
.k2-tl span{color:var(--k2)}
.k2-dos{display:grid;grid-template-columns:1fr 1fr;gap:56px;margin-top:56px;align-items:start}
.k2-doc{border:1px solid var(--ln);background:#fff}
.k2-doc .h{display:flex;justify-content:space-between;padding:14px 18px;border-bottom:1px solid var(--ln)}
.k2-doc dl{margin:0;padding:0 18px}
.k2-doc dl div{display:grid;grid-template-columns:130px 1fr;padding:12px 0;border-bottom:1px solid var(--ln2);font-size:15px}
.k2-doc dt{color:var(--k3)}
.k2-doc dd{margin:0}
.k2-doc .k2sc{display:inline-block;background:#111;color:#fff;font:500 11px var(--l);letter-spacing:.1em;padding:4px 8px;margin-right:8px}
.k2-doc blockquote{margin:0;padding:18px;font:300 20px/1.35 var(--g);border-top:1px solid var(--ln)}
.k2-photo{position:relative;overflow:hidden;aspect-ratio:4/5;background:#ddd}
.k2-photo img{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.05)}
.k2-photo span{position:absolute;left:14px;bottom:12px;color:#fff}
.k2-nums{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:56px}
.k2-nums div{border-top:1px solid var(--ln);padding-top:10px}
.k2-nums b{display:block;font:500 clamp(48px,5.4vw,84px)/1 var(--g);letter-spacing:-.04em;margin-top:16px}
.k2-seg{display:inline-flex;border:1px solid var(--ln);margin-top:40px}
.k2-seg button{border:0;background:transparent;font:500 11px var(--l);letter-spacing:.12em;text-transform:uppercase;padding:13px 18px;cursor:pointer;color:var(--k)}
.k2-seg button+button{border-left:1px solid var(--ln)}
.k2-seg button[aria-pressed=true]{background:#111;color:#fff}
.k2-seg button:focus-visible{outline:2px solid #111;outline-offset:2px}
.k2-tb{width:100%;border-collapse:collapse;margin-top:24px;font-variant-numeric:tabular-nums}
.k2-tb th{text-align:left;font:500 10.5px var(--l);letter-spacing:.14em;text-transform:uppercase;padding:0 12px 12px 0;border-bottom:1px solid var(--ln);color:var(--k3)}
.k2-tb td{padding:20px 12px 20px 0;border-bottom:1px solid var(--ln2);vertical-align:top}
.k2-tb td:first-child{font:500 22px var(--g);letter-spacing:-.01em;width:36%}
.k2-tb td small{display:block;font:400 14px/1.5 var(--t);color:var(--k2);margin-top:6px;letter-spacing:0}
.k2-tb .pr{font:300 34px var(--g);letter-spacing:-.02em;white-space:nowrap}
.k2-tb .pr small{display:inline;font-size:13px;color:var(--k3);margin-left:4px}
.k2-note{margin-top:16px;font-size:13px;color:var(--k3);max-width:90ch}
.k2-own{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;margin-top:56px;background:#111;color:#fff;padding:40px}
.k2-own h3{font:500 34px/1.05 var(--g);letter-spacing:-.02em;margin:0}
.k2-own p{margin:0 0 20px;color:rgba(255,255,255,.78);font-size:16px;line-height:1.55}
.k2-faq{margin-top:40px;border-top:1px solid var(--ln)}
.k2-faq details{border-bottom:1px solid var(--ln)}
.k2-faq summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;padding:20px 0;font:500 22px var(--g);letter-spacing:-.01em}
.k2-faq summary::-webkit-details-marker{display:none}
.k2-faq summary::after{content:"+";font:300 26px var(--g);transition:transform .3s}
.k2-faq details[open] summary::after{transform:rotate(45deg)}
.k2-faq summary:focus-visible{outline:2px solid #111;outline-offset:3px}
.k2-faq p{margin:0 0 22px;max-width:70ch;font-size:16px;line-height:1.6;color:var(--k2)}
.k2-end{padding:140px 0 120px}
.k2-end h2{font:300 clamp(48px,8vw,140px)/.9 var(--g);letter-spacing:-.04em;text-transform:uppercase;margin:0}
.k2-end .row{display:flex;justify-content:space-between;align-items:end;gap:32px;margin-top:40px;border-top:1px solid var(--ln);padding-top:16px}
.k2 .rv{opacity:0;transform:translateY(24px);transition:opacity .9s cubic-bezier(.2,.7,.2,1),transform .9s cubic-bezier(.2,.7,.2,1)}
.k2 .rv.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.k2 .rv{opacity:1;transform:none}.k2-word span{transition:none}}
@media(max-width:900px){.k2-meta{grid-template-columns:1fr 1fr;row-gap:6px;margin-top:96px}.k2-hero{min-height:auto}.k2-hero .intro{padding-top:80px}.k2-word{font-size:30vw}.k2-cta .wrap,.k2-end .row{flex-direction:column;align-items:flex-start}.k2-hd,.k2-vs,.k2-boxes,.k2-dos,.k2-own{grid-template-columns:1fr}.k2-vs>div+div{padding:24px 0 0;border-left:0}.k2-big{flex-direction:column;gap:8px}.k2-nums{grid-template-columns:1fr 1fr}.k2-tl div{grid-template-columns:1fr;gap:4px}.k2-sec{padding:84px 0}.k2-tb thead{display:none}.k2-tb tr{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px 14px;padding:16px 0;border-bottom:1px solid var(--ln2)}.k2-tb td{border:0;padding:0}.k2-tb td:first-child{grid-column:1/-1;width:auto}.k2-tb .pr{font-size:22px}.k2-own{padding:28px}.k2-band .ln{font-size:13vw}}
</style>""".replace('%F', F)


def render(wa, way, BASE, u):
    contato = wa('Olá! Vi a página de serviços da W3W e quero conversar sobre uma campanha.')
    prop = wa('Olá! Tenho um imóvel de alto padrão e quero saber como funciona a venda assistida da W3W.')
    planos = {'mensal': (1500, 1400, 1300), 'trimestral': (1350, 1250, 1150), 'semestral': (1200, 1100, 1000)}
    P = json.dumps(planos)
    fm = lambda n: f"R$ {n:,.0f}".replace(',', '.')
    m = planos['mensal']
    return CSS + f'''
<main class="k2">
<section class="k2-hero"><div class="wrap" style="display:flex;flex-direction:column;flex:1">
<div class="k2-meta lb"><span>W3W Serviços</span><span>Marketing imobiliário · Criação · Leads</span><span>Moema — São Paulo</span><span class="on">Agenda aberta — 2026</span></div>
<p class="intro">Campanha dedicada para cada imóvel, criação assinada por Head of Art e um dossiê de cada lead antes do primeiro contato. A W3W cria, anuncia e atende.</p>
<div class="k2-word" aria-label="W3W"><span>W</span><span>3</span><span>W</span></div>
<div class="k2-scroll lb">↓ Role para ver o método</div>
</div></section>

<section class="k2-band" id="k2band"><img src="{IMG}/vista-parque-ibirapuera/fachada.jpg" alt="" loading="lazy"><div class="ln l1">Do anúncio à chave,</div><div class="ln l2">com inteligência.</div></section>
<div class="k2-cta"><div class="wrap"><p>Imóvel de alto padrão não se vende como lead. Unimos mídia, criação e corretores que conhecem Moema rua a rua, desde 2004.</p><div style="display:flex;gap:10px;flex-wrap:wrap"><a class="k2-btn w" href="{contato}" target="_blank" rel="noopener">Falar com a W3W →</a><a class="k2-btn o" href="#k2planos">Ver planos</a></div></div></div>

<section class="k2-sec"><div class="wrap">
<div class="k2-big rv"><h2>Agências entregam<br>contatos.</h2><h2 style="text-align:right">Nós, compradores.</h2></div>
<div class="k2-vs rv"><div class="them"><span class="lb">Agência de tráfego comum</span><ul><li>Criativo de banco de imagem</li><li>Lead frio, sem contexto</li><li>Relatório de cliques</li><li>Não conhece o bairro</li><li>Para no formulário</li></ul></div>
<div class="us"><span class="lb">W3W</span><ul><li>Direção de arte, imagem tratada e vídeo</li><li>Lead com dossiê e roteiro</li><li>Relatório de visitas e propostas</li><li>Corretores de Moema desde 2004</li><li>Vai até a assinatura</li></ul></div></div>
</div></section>

<section class="k2-sec"><div class="wrap">
<div class="k2-hd rv"><span class="lb">Serviços</span><div><h2>Da campanha ao contrato, com o mesmo olhar.</h2><p>Quatro frentes que funcionam juntas ou separadas, sempre com uma campanha por produto.</p></div></div>
<div class="k2-boxes">
<div class="k2-box rv"><div class="top lb"><span>01 — Mídia</span><span>+</span></div><h3>Tráfego por produto</h3><p>Meta e Google Ads com estratégia, públicos, verba e otimização próprios para cada empreendimento.</p><ul><li>Meta Ads</li><li>Google Ads</li><li>Relatório de visitas</li></ul></div>
<div class="k2-box rv"><div class="top lb"><span>02 — Dados</span><span>+</span></div><h3>Lead Dossiê</h3><p>Triagem, score e roteiro de abordagem de cada lead, entregues no WhatsApp do corretor com o card do imóvel.</p><ul><li>Score A/B/C</li><li>Roteiro</li><li>LGPD</li></ul></div>
<div class="k2-box rv"><div class="top lb"><span>03 — Criação</span><span>+</span></div><h3>Direção de arte</h3><p>Identidade, naming, book, tratamento de imagem, carrosséis, reels e vídeo com padrão de agência.</p><ul><li>Identidade</li><li>Book</li><li>Vídeo</li></ul></div>
<div class="k2-box rv"><div class="top lb"><span>04 — Plataforma</span><span>+</span></div><h3>Landing page e hub</h3><p>Página do produto com triagem e card para WhatsApp, e o hub com textos, fichas e imagens para o time.</p><ul><li>Landing page</li><li>Triagem</li><li>Hub de vendas</li></ul></div>
</div></div></section>

<section class="k2-sec"><div class="wrap">
<div class="k2-hd rv"><span class="lb">Lead Dossiê</span><div><h2>O corretor sabe quem é antes do primeiro "olá".</h2><p>Dados informados pelo próprio lead na triagem, cruzados com a campanha de origem. Sem compra de base, dentro da LGPD.</p></div></div>
<div class="k2-dos">
<div class="k2-doc rv"><div class="h lb"><span>Lead Dossiê W3W</span><span>Exemplo · dados fictícios</span></div>
<dl><div><dt>Lead</dt><dd>Mariana, 41</dd></div><div><dt>Imóvel</dt><dd>Cobertura 1.184 m² · Moema</dd></div><div><dt>Origem</dt><dd>Instagram · campanha Coberturas</dd></div><div><dt>Investimento</dt><dd>Acima de R$ 20 milhões</dd></div><div><dt>Objetivo</dt><dd>Morar · família com 2 filhos</dd></div><div><dt>Prazo</dt><dd>Até 6 meses</dd></div><div><dt>Prioridade</dt><dd><span class="k2sc">A</span>Retornar em até 15 min</dd></div></dl>
<blockquote>"Mariana, vi que você quer morar perto do Ibirapuera com a família. Posso mostrar a planta da cobertura e marcar uma visita privativa?"</blockquote></div>
<div class="k2-photo rv"><img src="{IMG}/park-lane/par-1.jpg" alt="Interior de cobertura em Moema" loading="lazy"><span class="lb">Park Lane Ibirapuera · cobertura</span></div>
</div></div></section>

<section class="k2-sec"><div class="wrap">
<div class="k2-hd rv"><span class="lb">Método</span><div><h2>Do produto à proposta.</h2></div></div>
<div class="k2-tl rv">
<div><span class="lb">01 — Produto</span><b>Diagnóstico</b><span>Público, praça, concorrência e o que torna o imóvel único.</span></div>
<div><span class="lb">02 — Criação</span><b>Direção de arte</b><span>Identidade, imagens tratadas, carrosséis, vídeo e landing page.</span></div>
<div><span class="lb">03 — Mídia</span><b>Campanha</b><span>Meta e Google Ads com verba, público e otimização próprios.</span></div>
<div><span class="lb">04 — Dados</span><b>Dossiê</b><span>Triagem, score e roteiro de cada lead.</span></div>
<div><span class="lb">05 — Venda</span><b>Atendimento</b><span>Corretor W3W ou do seu time, com o hub de materiais.</span></div>
</div>
<div class="k2-nums rv"><div><span class="lb">Mercado</span><b>2004</b></div><div><span class="lb">Copa do Mundo</span><b>2014</b></div><div><span class="lb">Jogos Olímpicos</span><b>2016</b></div><div><span class="lb">Anos de criação</span><b>20+</b></div></div>
</div></section>

<section class="k2-sec" id="k2planos"><div class="wrap">
<div class="k2-hd rv"><span class="lb">Planos</span><div><h2>Preço claro, por campanha.</h2><p>Mais produtos e mais tempo, menor o valor. A verba de mídia é paga direto ao Meta e ao Google.</p>
<div class="k2-seg" role="group" aria-label="Período"><button type="button" data-p="mensal" aria-pressed="true">Mensal</button><button type="button" data-p="trimestral" aria-pressed="false">Trimestral</button><button type="button" data-p="semestral" aria-pressed="false">Semestral</button></div></div></div>
<table class="k2-tb rv"><thead><tr><th>Serviço</th><th>1 campanha</th><th>2 campanhas</th><th>3 campanhas</th></tr></thead><tbody>
<tr><td>Tráfego por produto<small>Estratégia, Meta e Google Ads, otimização e relatório de visitas.</small></td><td class="pr" data-i="0">{fm(m[0])}<small>/mês</small></td><td class="pr" data-i="1">{fm(m[1])}<small>/mês</small></td><td class="pr" data-i="2">{fm(m[2])}<small>/mês</small></td></tr>
<tr><td>+ Lead Dossiê<small>Triagem, score e roteiro no WhatsApp. Opcional.</small></td><td class="pr" colspan="3">R$ 390<small>/campanha/mês</small></td></tr>
<tr><td>Criativos da campanha<small>Carrosséis, estáticos e reels com direção de arte.</small></td><td class="pr" colspan="3">a partir de R$ 1.200<small>/mês</small></td></tr>
<tr><td>Landing page do produto<small>Com triagem e card para WhatsApp.</small></td><td class="pr" colspan="3">a partir de R$ 2.500</td></tr>
<tr><td>Identidade e book<small>Marca, naming, book, ficha técnica e cards.</small></td><td class="pr" colspan="3">a partir de R$ 6.000</td></tr>
<tr><td>Hub de vendas<small>Textos, fichas, tabelas e imagens para o time.</small></td><td class="pr" colspan="3">R$ 1.900 + R$ 290<small>/mês</small></td></tr>
</tbody></table>
<p class="k2-note">Trimestral e semestral pelo período completo, em até 3x ou 6x. A partir de 4 campanhas, plano sob medida.</p>
<div class="k2-own rv"><h3>Proprietário: venda assistida.</h3><div><p>Você investe antes na produção e na campanha do seu imóvel. Se vender com a W3W, o valor é descontado da comissão, que cai de até 6% para 5%.</p><a class="k2-btn w" href="{prop}" target="_blank" rel="noopener">Quero saber mais →</a></div></div>
</div></section>

<section class="k2-sec"><div class="wrap">
<div class="k2-hd rv"><span class="lb">Dúvidas</span><div><h2>Perguntas frequentes.</h2></div></div>
<div class="k2-faq">
<details><summary>O valor da mídia está incluído?</summary><p>Não. A verba é paga direto ao Meta e ao Google, no cartão do cliente. A W3W recomenda o valor ideal para cada produto.</p></details>
<details><summary>Preciso ter corretor próprio?</summary><p>Não. Os leads podem ser atendidos pela equipe da W3W ou pela sua, que recebe o Lead Dossiê e o hub de textos.</p></details>
<details><summary>O Lead Dossiê usa dados de terceiros?</summary><p>Não. Usamos o que o próprio lead informa na triagem e os dados da campanha de origem.</p></details>
<details><summary>Atendem fora de Moema?</summary><p>Sim. Moema é a nossa especialidade, e também trabalhamos com Vila Nova Conceição, Itaim, Paraíso e Brooklin, sob consulta.</p></details>
<details><summary>Existe fidelidade?</summary><p>No plano mensal, não. Trimestral e semestral têm desconto e são contratados pelo período completo.</p></details>
</div></div></section>

<section class="k2-end"><div class="wrap">
<h2 class="rv">Vamos vender<br>do jeito certo.</h2>
<div class="row"><span class="lb">W3W Imóveis · Inteligência imobiliária · Desde 2004</span><div style="display:flex;gap:10px;flex-wrap:wrap"><a class="k2-btn k" href="{contato}" target="_blank" rel="noopener">Falar com a W3W →</a><a class="k2-btn ko" href="{BASE}/">Ver a vitrine</a></div></div>
</div></section>
</main>
<script>(function(){{
var P={P},f=function(n){{return 'R$ '+n.toLocaleString('pt-BR')}};
document.querySelectorAll('.k2-seg button').forEach(function(b){{b.onclick=function(){{document.querySelectorAll('.k2-seg button').forEach(function(x){{x.setAttribute('aria-pressed',x===b)}});var v=P[b.dataset.p];document.querySelectorAll('.k2-tb .pr[data-i]').forEach(function(td){{td.innerHTML=f(v[+td.dataset.i])+'<small>/mês</small>'}})}}}});
var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:.12}});document.querySelectorAll('.k2 .rv').forEach(function(el){{io.observe(el)}});
if(!matchMedia('(prefers-reduced-motion: reduce)').matches){{var w=document.querySelectorAll('.k2-word span'),band=document.getElementById('k2band'),tk=0;
function run(){{tk=0;var y=scrollY;w.forEach(function(s,i){{s.style.setProperty('--y',(-y*(.08+i*.05)).toFixed(1)+'px')}});var r=band.getBoundingClientRect(),p=(innerHeight-r.top)/(innerHeight+r.height);if(p>-0.2&&p<1.2){{band.style.setProperty('--x1',(-4-p*14)+'%');band.style.setProperty('--x2',(18-p*24)+'%');band.querySelector('img').style.transform='scale('+(1.08+p*.06)+')'}}}}
addEventListener('scroll',function(){{if(!tk)tk=requestAnimationFrame(run)}},{{passive:true}});run()}}
}})();</script>
'''
