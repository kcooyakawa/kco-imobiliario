"""Página de serviços da W3W (marketing imobiliário). Chamado por build.py."""

CSS = r"""
<style>
.sv{--gold:#8C7B62}
.sv ::selection{background:var(--ink);color:var(--paper-2)}
.sv section{padding:112px 0;border-bottom:1px solid var(--line)}
.sv h2{font-family:var(--serif);font-weight:200;font-size:clamp(40px,5.2vw,76px);line-height:.98;letter-spacing:-.03em;margin:0;text-wrap:balance;max-width:16ch}
.sv h2 em{font-style:italic}
.sv p.lead{font-size:19px;line-height:1.55;color:var(--ink-2);max-width:56ch;margin-top:22px}
.sv-hero{padding:150px 0 0!important;border-bottom:0!important}
.sv-hero h1{font-family:var(--serif);font-weight:200;font-size:clamp(52px,8.4vw,128px);line-height:.92;letter-spacing:-.035em;margin:0;max-width:13ch;text-wrap:balance}
.sv-hero h1 em{font-style:italic}
.sv-hero .sub{display:grid;grid-template-columns:1.1fr 1fr;gap:56px;align-items:end;margin-top:56px;padding-bottom:56px;border-bottom:1px solid var(--ink)}
.sv-hero .sub p{font-size:20px;line-height:1.5;color:var(--ink-2);max-width:44ch;margin:0}
.sv-cta{display:flex;gap:12px;flex-wrap:wrap;justify-content:flex-end}
.sv-strip{display:grid;grid-template-columns:repeat(4,1fr);border-bottom:1px solid var(--line)}
.sv-strip div{padding:26px 20px 30px 0;font-size:15px;line-height:1.45;color:var(--ink-2)}
.sv-strip div+div{padding-left:20px;border-left:1px solid var(--line)}
.sv-strip b{display:block;font-family:var(--serif);font-weight:300;font-size:26px;color:var(--ink);margin-bottom:6px;letter-spacing:-.01em}
.sv-vs{display:grid;grid-template-columns:1fr 1fr;margin-top:64px;border-top:1px solid var(--ink)}
.sv-vs>div{padding:32px 32px 8px 0}
.sv-vs>div+div{padding-left:32px;border-left:1px solid var(--line)}
.sv-vs h3{font-size:12px;letter-spacing:.2em;text-transform:uppercase;font-weight:500;color:var(--slate);margin:0 0 18px}
.sv-vs .us h3{color:var(--ink)}
.sv-vs li{list-style:none;padding:14px 0;border-bottom:1px solid var(--line);font-size:17px;line-height:1.4}
.sv-vs .them li{color:var(--slate)}
.sv-vs .us li{font-family:var(--serif);font-weight:300;font-size:22px}
.sv-who{margin-top:56px;border-top:1px solid var(--ink)}
.sv-who>div{display:grid;grid-template-columns:.9fr 1.4fr 1fr;gap:40px;padding:36px 0;border-bottom:1px solid var(--line);align-items:start}
.sv-who h3{font-family:var(--serif);font-weight:300;font-size:34px;line-height:1.05;margin:0}
.sv-who p{margin:0;font-size:17px;line-height:1.55;color:var(--ink-2)}
.sv-who ul{list-style:none;margin:0;padding:0;font-size:15px}
.sv-who li{padding:6px 0;border-bottom:1px solid var(--line)}
.sv-flow{display:grid;grid-template-columns:repeat(5,1fr);margin-top:64px;position:relative}
.sv-flow::before{content:"";position:absolute;left:0;right:0;top:9px;height:1px;background:var(--ink)}
.sv-flow div{position:relative;padding:36px 20px 0 0}
.sv-flow div::before{content:"";position:absolute;top:4px;left:0;width:11px;height:11px;border-radius:50%;background:var(--paper);border:1px solid var(--ink)}
.sv-flow div:last-child::before{background:var(--ink)}
.sv-flow b{display:block;font-family:var(--serif);font-weight:300;font-size:28px;margin-bottom:10px}
.sv-flow p{margin:0;font-size:15px;line-height:1.5;color:var(--ink-2)}
.sv-dark{background:var(--ink);color:#F1F2F4;border-bottom:0!important}
.sv-dark h2{color:#F6F7F9}
.sv-dark p.lead{color:rgba(241,242,244,.72)}
.sv-dos{display:grid;grid-template-columns:1fr 1.05fr;gap:72px;align-items:start}
.sv-doc{background:#F6F7F9;color:var(--ink);border-radius:18px;padding:30px 30px 26px;box-shadow:0 30px 60px -30px rgba(0,0,0,.6);font-size:15px}
.sv-doc header{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--ink);padding-bottom:14px;margin-bottom:6px}
.sv-doc header b{font-family:var(--serif);font-weight:300;font-size:24px}
.sv-doc header span{font-size:12px;color:var(--slate)}
.sv-doc dl{margin:0;display:grid;grid-template-columns:150px 1fr}
.sv-doc dt,.sv-doc dd{padding:11px 0;border-bottom:1px solid var(--line);margin:0}
.sv-doc dt{color:var(--slate);font-size:13px}
.sv-doc .score{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--ink);color:#fff;font-weight:500;margin-right:8px}
.sv-doc blockquote{margin:16px 0 0;padding:16px 18px;background:var(--paper);border-radius:12px;font-family:var(--serif);font-weight:300;font-size:18px;line-height:1.4}
.sv-doc small{display:block;margin-top:12px;color:var(--slate);font-size:12px}
.sv-dos ul{list-style:none;padding:0;margin:36px 0 0;border-top:1px solid rgba(241,242,244,.25)}
.sv-dos li{padding:16px 0;border-bottom:1px solid rgba(241,242,244,.18);font-size:17px;line-height:1.45;color:rgba(241,242,244,.86)}
.sv-dos li b{color:#fff;font-weight:500}
.sv-art{display:grid;grid-template-columns:1.2fr 1fr;gap:72px;align-items:end}
.sv-art .cred{font-family:var(--serif);font-weight:200;font-size:clamp(30px,3.4vw,48px);line-height:1.12;letter-spacing:-.02em}
.sv-art .cred em{font-style:italic}
.sv-art ul{list-style:none;padding:0;margin:0;border-top:1px solid var(--ink)}
.sv-art li{display:flex;justify-content:space-between;gap:20px;padding:14px 0;border-bottom:1px solid var(--line);font-size:16px}
.sv-art li span{color:var(--slate)}
.sv-pl{margin-top:56px}
.sv-seg{display:inline-flex;gap:2px;padding:3px;border-radius:11px;background:rgba(26,24,23,.07);margin-bottom:28px}
.sv-seg button{border:0;background:transparent;font:500 14px/1 var(--sans);color:var(--ink-2);padding:11px 16px;border-radius:8px;cursor:pointer;transition:background .25s var(--ease),color .2s}
.sv-seg button[aria-pressed=true]{background:#fff;color:var(--ink);box-shadow:0 1px 2px rgba(0,0,0,.08),0 3px 10px rgba(0,0,0,.06)}
.sv-tb{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums}
.sv-tb th{text-align:left;font-size:12px;letter-spacing:.16em;text-transform:uppercase;font-weight:500;color:var(--slate);padding:0 12px 14px 0;border-bottom:1px solid var(--ink)}
.sv-tb td{padding:22px 12px 22px 0;border-bottom:1px solid var(--line);font-size:16px;vertical-align:top}
.sv-tb td:first-child{font-family:var(--serif);font-weight:300;font-size:24px;width:34%}
.sv-tb td small{display:block;font-family:var(--sans);font-size:14px;color:var(--ink-2);margin-top:6px;line-height:1.45}
.sv-tb .pr{font-family:var(--serif);font-weight:300;font-size:30px;white-space:nowrap}
.sv-tb .pr span{font-family:var(--sans);font-size:13px;color:var(--slate);margin-left:4px}
.sv-note{margin-top:22px;font-size:14px;color:var(--ink-2);max-width:80ch;line-height:1.55}
.sv-own{margin-top:64px;display:grid;grid-template-columns:1fr 1fr;gap:56px;padding:40px;background:var(--paper-2);border:1px solid var(--line);border-radius:18px}
.sv-own h3{font-family:var(--serif);font-weight:300;font-size:36px;line-height:1.05;margin:0}
.sv-own p{margin:0;font-size:17px;line-height:1.55;color:var(--ink-2)}
.sv-faq{margin-top:48px;border-top:1px solid var(--ink)}
.sv-faq details{border-bottom:1px solid var(--line)}
.sv-faq summary{cursor:pointer;list-style:none;padding:22px 40px 22px 0;font-family:var(--serif);font-weight:300;font-size:24px;position:relative}
.sv-faq summary::-webkit-details-marker{display:none}
.sv-faq summary::after{content:"";position:absolute;right:6px;top:50%;width:12px;height:12px;border-right:1px solid var(--ink);border-bottom:1px solid var(--ink);transform:translateY(-70%) rotate(45deg);transition:transform .3s var(--ease)}
.sv-faq details[open] summary::after{transform:translateY(-30%) rotate(225deg)}
.sv-faq details p{margin:0 0 24px;max-width:70ch;font-size:17px;line-height:1.6;color:var(--ink-2)}
.sv-end{text-align:left}
.sv-end h2{max-width:18ch}
.sv .btn:focus-visible,.sv-seg button:focus-visible,.sv-faq summary:focus-visible{outline:2px solid var(--ink);outline-offset:3px}
@media(max-width:900px){.sv section{padding:80px 0}.sv-hero{padding-top:118px!important}.sv-hero .sub,.sv-dos,.sv-art,.sv-own,.sv-vs{grid-template-columns:1fr;gap:32px}.sv-cta{justify-content:flex-start}.sv-strip{grid-template-columns:1fr 1fr}.sv-strip div:nth-child(3){border-left:0;padding-left:0}.sv-who>div{grid-template-columns:1fr;gap:14px}.sv-flow{grid-template-columns:1fr;gap:0}.sv-flow::before{left:5px;right:auto;top:0;bottom:0;width:1px;height:auto}.sv-flow div{padding:0 0 30px 34px}.sv-vs>div+div{padding-left:0;border-left:0;border-top:1px solid var(--line)}.sv-tb thead{display:none}.sv-tb tr{display:grid;grid-template-columns:1fr 1fr;gap:6px 16px;padding:18px 0;border-bottom:1px solid var(--line)}.sv-tb td{border:0;padding:0}.sv-tb td:first-child{grid-column:1/-1;width:auto}.sv-own{padding:28px}.sv-doc dl{grid-template-columns:120px 1fr}}
</style>"""


def render(wa, way, BASE, u):
    contato = wa('Olá! Vi a página de serviços da W3W e quero conversar sobre uma campanha.')
    prop = wa('Olá! Tenho um imóvel de alto padrão e quero saber como funciona a venda assistida da W3W.')
    planos = {
        'mensal': (1500, 1400, 1300),
        'trimestral': (1350, 1250, 1150),
        'semestral': (1200, 1100, 1000),
    }
    import json
    P = json.dumps(planos)
    fm = lambda n: f"R$ {n:,.0f}".replace(',', '.')
    m = planos['mensal']
    return CSS + f'''
<main class="sv">
<section class="sv-hero"><div class="wrap">
<h1>Imóvel de alto padrão <em>não se vende</em> como lead.</h1>
<div class="sub"><p>A W3W cria, anuncia e atende. Uma campanha para cada produto, criação assinada por Head of Art e um dossiê de cada lead antes do primeiro contato. Com mais de 20 anos de mercado em Moema.</p>
<div class="sv-cta"><a class="btn solid" href="{contato}" target="_blank" rel="noopener">Falar com a W3W</a><a class="btn" href="#planos">Ver planos e preços</a></div></div>
<div class="sv-strip"><div><b>1 produto, 1 campanha</b>Estratégia, verba e criativos próprios.</div><div><b>Criação de agência</b>O mesmo padrão de FIFA™, Rio 2016 e Itaú.</div><div><b>Lead Dossiê</b>Perfil, prioridade e abordagem no WhatsApp.</div><div><b>Quem vende, anuncia</b>Corretores que conhecem o bairro.</div></div>
</div></section>

<section><div class="wrap">
<h2>Agências entregam contatos. <em>Nós entregamos compradores.</em></h2>
<p class="lead">A maioria das operações para no formulário. A W3W é uma imobiliária que domina mídia e criação, então a campanha continua até a visita e a proposta.</p>
<div class="sv-vs"><div class="them"><h3>Agência de tráfego</h3><ul><li>Criativos de banco de imagem</li><li>Lead entregue frio, sem contexto</li><li>Relatório de cliques</li><li>Não conhece o produto nem o bairro</li><li>Termina no formulário</li></ul></div>
<div class="us"><h3>W3W</h3><ul><li>Direção de arte, imagens tratadas, vídeo</li><li>Lead com dossiê e roteiro de abordagem</li><li>Relatório de visitas e propostas</li><li>Corretores de Moema desde 2004</li><li>Vai até a chave</li></ul></div></div>
</div></section>

<section><div class="wrap">
<h2>Três formas de <em>trabalhar com a W3W.</em></h2>
<div class="sv-who">
<div><h3>Incorporadoras</h3><p>Lançamento e estoque com campanha por produto, landing page própria, criativos e o hub de vendas para a equipe comercial.</p><ul><li>Campanha por empreendimento</li><li>Landing page e book</li><li>Lead Dossiê para o plantão</li></ul></div>
<div><h3>Imobiliárias e corretores</h3><p>Leads qualificados do produto que você vende, com texto pronto para o primeiro contato e card do imóvel direto no WhatsApp.</p><ul><li>Tráfego por produto</li><li>Triagem no WhatsApp</li><li>Textos e fichas prontos</li></ul></div>
<div><h3>Proprietários</h3><p>Venda assistida do seu imóvel: produção de imagens, campanha dedicada e atendimento da W3W, com o investimento abatido da comissão.</p><ul><li>Tratamento de imagem e vídeo</li><li>Campanha exclusiva do imóvel</li><li>Atendimento e negociação</li></ul></div>
</div></div></section>

<section><div class="wrap">
<h2>Do produto <em>à proposta.</em></h2>
<div class="sv-flow">
<div><b>Produto</b><p>Entendemos público, praça, concorrência e o que torna o imóvel único.</p></div>
<div><b>Criação</b><p>Identidade, imagens tratadas, carrosséis, vídeos e landing page.</p></div>
<div><b>Campanha</b><p>Meta e Google Ads com verba, público e otimização próprios.</p></div>
<div><b>Dossiê</b><p>Cada lead chega com perfil, prioridade e abordagem sugerida.</p></div>
<div><b>Atendimento</b><p>Corretor W3W ou da sua equipe, com hub de textos e materiais.</p></div>
</div></div></section>

<section class="sv-dark"><div class="wrap sv-dos">
<div><h2>Lead Dossiê <em>W3W.</em></h2>
<p class="lead">Antes do primeiro "olá", o corretor já sabe quem está do outro lado: o que a pessoa procura, quanto pretende investir, quando quer comprar e por onde começar a conversa.</p>
<ul><li><b>Dados declarados pelo próprio lead</b> na triagem: faixa de investimento, objetivo e prazo. Sem compra de base, dentro da LGPD.</li><li><b>Score A, B ou C</b> e prioridade de retorno.</li><li><b>Abordagem sugerida</b> com o texto certo do hub, pronto para copiar.</li><li><b>Card do produto</b> e origem da campanha no mesmo WhatsApp.</li></ul></div>
<div class="sv-doc" aria-label="Exemplo de Lead Dossiê com dados fictícios"><header><b>Lead Dossiê</b><span>exemplo · dados fictícios</span></header>
<dl><dt>Lead</dt><dd>Mariana, 41</dd><dt>Produto</dt><dd>Cobertura 1.184 m² · Moema</dd><dt>Origem</dt><dd>Instagram · campanha Coberturas</dd><dt>Investimento</dt><dd>Acima de R$ 20 milhões</dd><dt>Objetivo</dt><dd>Morar, família com dois filhos</dd><dt>Prazo</dt><dd>Até 6 meses</dd><dt>Prioridade</dt><dd><span class="score">A</span>Retornar em até 15 min</dd></dl>
<blockquote>"Mariana, vi que você quer morar perto do Ibirapuera com a família. Posso te mostrar a planta da cobertura e agendar uma visita privativa?"</blockquote>
<small>O dossiê chega no WhatsApp do corretor junto com o card do imóvel.</small></div>
</div></section>

<section><div class="wrap sv-art">
<div><h2>Criação de <em>agência</em>, não de template.</h2>
<p class="cred" style="margin-top:28px">Direção de arte de Kco Oyakawa, Head of Art com trabalhos para <em>FIFA™, Jogos Olímpicos 2016, Coca-Cola</em> e <em>Itaú.</em></p></div>
<ul><li>Identidade e naming do empreendimento<span>marca</span></li><li>Book, ficha técnica e cards<span>vendas</span></li><li>Tratamento de imagem e perspectivas<span>visual</span></li><li>Carrosséis, reels e vídeo<span>mídia</span></li><li>Landing page e site<span>web</span></li><li><a href="https://kcooyakawa.github.io/kco-imobiliario/" target="_blank" rel="noopener" style="border-bottom:1px solid">Ver portfólio imobiliário</a><span>cases</span></li></ul>
</div></section>

<section id="planos"><div class="wrap">
<h2>Planos <em>claros.</em></h2>
<p class="lead">Preço por campanha por mês. Quanto mais produtos e mais tempo, menor o valor. O investimento em mídia é pago direto às plataformas.</p>
<div class="sv-pl">
<div class="sv-seg" role="group" aria-label="Período"><button type="button" data-p="mensal" aria-pressed="true">Mensal</button><button type="button" data-p="trimestral" aria-pressed="false">Trimestral</button><button type="button" data-p="semestral" aria-pressed="false">Semestral</button></div>
<table class="sv-tb"><thead><tr><th>Serviço</th><th>1 campanha</th><th>2 campanhas</th><th>3 campanhas</th></tr></thead><tbody>
<tr><td>Tráfego por produto<small>Estratégia, Meta e Google Ads, públicos, otimização e relatório de visitas.</small></td><td class="pr" data-i="0">{fm(m[0])}<span>/mês</span></td><td class="pr" data-i="1">{fm(m[1])}<span>/mês</span></td><td class="pr" data-i="2">{fm(m[2])}<span>/mês</span></td></tr>
<tr><td>Lead Dossiê W3W<small>Triagem, score, abordagem sugerida e entrega no WhatsApp. Opcional.</small></td><td class="pr" colspan="3">+ R$ 390<span>por campanha/mês</span></td></tr>
</tbody></table>
<p class="sv-note">Trimestral e semestral com pagamento do período completo, em até 3x ou 6x. A partir de 4 campanhas, plano sob medida.</p>

<table class="sv-tb" style="margin-top:56px"><thead><tr><th>Projetos</th><th colspan="3">Investimento</th></tr></thead><tbody>
<tr><td>Criativos da campanha<small>Carrosséis, estáticos e reels com direção de arte, por ciclo mensal.</small></td><td class="pr" colspan="3">a partir de R$ 1.200<span>/mês</span></td></tr>
<tr><td>Landing page do produto<small>Página rápida, com card para WhatsApp e triagem do lead.</small></td><td class="pr" colspan="3">a partir de R$ 2.500</td></tr>
<tr><td>Identidade e book<small>Marca, naming, book de vendas, ficha técnica e cards.</small></td><td class="pr" colspan="3">a partir de R$ 6.000</td></tr>
<tr><td>Hub de vendas<small>Textos prontos, fichas, tabelas e imagens de cada produto para a equipe.</small></td><td class="pr" colspan="3">R$ 1.900 + R$ 290<span>/mês</span></td></tr>
</tbody></table>

<div class="sv-own"><h3>Proprietário: venda assistida.</h3><p>Você investe antes na produção e na campanha do seu imóvel. Se vender com a W3W, o valor pago é descontado da comissão, que cai de até 6% para 5%. <a href="{prop}" target="_blank" rel="noopener" style="border-bottom:1px solid">Quero saber mais</a></p></div>
</div></div></section>

<section><div class="wrap">
<h2>Perguntas <em>frequentes.</em></h2>
<div class="sv-faq">
<details><summary>O valor da mídia está incluído?</summary><p>Não. A verba de anúncios é paga direto ao Meta e ao Google, no cartão do cliente. A W3W recomenda o valor ideal para cada produto.</p></details>
<details><summary>Preciso ter corretor próprio?</summary><p>Não. Os leads podem ser atendidos pela equipe da W3W ou pela sua, que recebe o Lead Dossiê e o hub de textos para o primeiro contato.</p></details>
<details><summary>O Lead Dossiê usa dados de terceiros?</summary><p>Não. Usamos o que o próprio lead informa na triagem e os dados da campanha de origem. Nada de compra de base ou estimativa de renda por fontes externas.</p></details>
<details><summary>Atendem fora de Moema?</summary><p>Sim. Moema é a nossa especialidade, e também trabalhamos com Vila Nova Conceição, Itaim, Paraíso e Brooklin, sob consulta.</p></details>
<details><summary>Existe fidelidade?</summary><p>No plano mensal, não. Os planos trimestral e semestral têm desconto e são contratados pelo período completo.</p></details>
</div></div></section>

<section class="sv-end"><div class="wrap">
<h2>Vamos vender o seu produto <em>do jeito certo?</em></h2>
<div class="sv-cta" style="justify-content:flex-start;margin-top:36px"><a class="btn solid" href="{contato}" target="_blank" rel="noopener">Falar com a W3W no WhatsApp</a><a class="btn" href="{BASE}/">Ver a vitrine da W3W</a></div>
</div></section>
</main>
<script>(function(){{var P={P},f=function(n){{return 'R$ '+n.toLocaleString('pt-BR')}};document.querySelectorAll('.sv-seg button').forEach(function(b){{b.onclick=function(){{document.querySelectorAll('.sv-seg button').forEach(function(x){{x.setAttribute('aria-pressed',x===b)}});var v=P[b.dataset.p];document.querySelectorAll('.sv-tb .pr[data-i]').forEach(function(td){{td.innerHTML=f(v[+td.dataset.i])+'<span>/mês</span>'}})}}}})}})();</script>
'''
