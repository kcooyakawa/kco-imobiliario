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
.mc{background:#F4F2EF;color:#16191E;padding:clamp(96px,12vw,140px) 0 80px}
.mc .in{width:min(1180px,calc(100% - 40px));margin:0 auto}
.mc-bc{font:500 11px var(--mono,monospace);letter-spacing:.12em;text-transform:uppercase;color:#757E8D;display:flex;gap:8px;flex-wrap:wrap}
.mc-bc a{color:#757E8D;text-decoration:none}.mc-bc a:hover{color:#16191E}
.mc h1{font:300 clamp(44px,7vw,92px)/.95 var(--sans,sans-serif);letter-spacing:-.045em;margin:22px 0 22px;max-width:14ch}
.mc h1 em{font-family:var(--serif,serif);font-style:italic;color:#4A5568}
.mc .lead{font-size:clamp(17px,1.6vw,20px);line-height:1.55;color:#4A5160;max-width:62ch;margin:0}
.mc-st{display:flex;gap:36px;flex-wrap:wrap;margin:34px 0 30px}
.mc-st dt{font:300 40px/1 var(--sans,sans-serif);letter-spacing:-.03em}.mc-st dd{margin:6px 0 0;font:500 10.5px var(--mono,monospace);letter-spacing:.12em;text-transform:uppercase;color:#757E8D}
.mc-cta{display:inline-flex;align-items:center;gap:10px;padding:16px 26px;border-radius:999px;background:linear-gradient(160deg,#3A424F,#222831);color:#F3F2EF;text-decoration:none;font:500 15px var(--sans,sans-serif);box-shadow:inset 0 1px 0 rgba(255,255,255,.14),0 20px 40px -20px rgba(14,17,22,.5)}
.mc h2{font:300 clamp(30px,3.6vw,46px)/1 var(--sans,sans-serif);letter-spacing:-.035em;margin:72px 0 22px}
.mc h2 em{font-family:var(--serif,serif);font-style:italic;color:#4A5568}
.mc-ind{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
.mc-ind article{padding:24px;border-radius:24px;color:#F3F2EF;background:linear-gradient(160deg,#3A424F,#222831);box-shadow:inset 0 1px 0 rgba(255,255,255,.12)}
.mc-ind .tg{font:500 10px var(--mono,monospace);letter-spacing:.12em;text-transform:uppercase;color:#1C2129;background:#F3F2EF;padding:4px 9px;border-radius:999px}
.mc-ind h3{font:300 28px/1.05 var(--sans,sans-serif);letter-spacing:-.03em;margin:18px 0 8px}
.mc-ind p{margin:0 0 4px;font-size:14px;color:#C5CBD4;line-height:1.5}
.mc-ind .h{font:12px/1.6 var(--mono,monospace);color:#8F98A6;margin-top:10px}
.mc-ac{display:flex;gap:8px;margin-top:18px;flex-wrap:wrap}
.mc-ac a{font:500 13px var(--sans,sans-serif);padding:10px 15px;border-radius:999px;text-decoration:none;background:rgba(255,255,255,.1);color:#F3F2EF}
.mc-ac a.p{background:#F3F2EF;color:#1C2129}
.mc-ls{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px}
.mc-ls article{padding:20px;border-radius:20px;background:#fff;box-shadow:0 1px 0 rgba(22,25,30,.05),0 14px 30px -24px rgba(22,25,30,.25)}
.mc-ls h3{font:400 18px/1.2 var(--sans,sans-serif);letter-spacing:-.01em;margin:0 0 6px}
.mc-ls p{margin:0;font-size:13.5px;color:#5B6372;line-height:1.5}
.mc-ls .h{font:11.5px/1.6 var(--mono,monospace);color:#757E8D;margin-top:8px}
.mc-ls .mc-ac a{background:#EEEBE5;color:#16191E;padding:8px 13px;font-size:12.5px}
.mc-ls .mc-ac a.p{background:#2A313B;color:#F3F2EF}
.mc-ot{display:flex;flex-wrap:wrap;gap:8px}
.mc-ot a{padding:12px 18px;border-radius:999px;background:#fff;color:#16191E;text-decoration:none;font:500 14px var(--sans,sans-serif);box-shadow:0 10px 24px -18px rgba(22,25,30,.3)}
.mc-ot a small{color:#757E8D;font:500 11px var(--mono,monospace);margin-left:6px}
.mc-fq details{border-top:1px solid rgba(22,25,30,.1);padding:20px 0}
.mc-fq summary{cursor:pointer;font:400 19px var(--sans,sans-serif);letter-spacing:-.01em;list-style:none}
.mc-fq p{color:#4A5160;line-height:1.6;margin:10px 0 0;max-width:70ch}
.mc-end{margin-top:80px;padding:clamp(28px,5vw,56px);border-radius:32px;background:linear-gradient(160deg,#3A424F,#222831);color:#F3F2EF;display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.mc-end h2{margin:0;color:#F3F2EF}.mc-end h2 em{color:#8DB8FF}
.mc-end a{padding:16px 26px;border-radius:999px;background:#F3F2EF;color:#1C2129;text-decoration:none;font:500 15px var(--sans,sans-serif)}
</style>'''

def card(l, CM, dark=False):
    acts = f'<a class="p" href="https://www.google.com/maps/dir/?api=1&destination={l["lat"]},{l["lon"]}" target="_blank" rel="noopener">Como chegar</a>'
    if l.get('site'): acts += f'<a href="{esc(l["site"])}" target="_blank" rel="noopener nofollow">Site</a>'
    if l.get('tel'): acts += f'<a href="tel:{esc("".join(c for c in l["tel"] if c.isdigit() or c=="+"))}">Ligar</a>'
    h = hum(l.get('horario'))
    if dark:
        return f'<article><span class="tg">W3W indica</span><h3>{esc(l["nome"])}</h3>{f"<p>{esc(l.get('nota'))}</p>" if l.get("nota") else ""}<p>{esc(l.get("end") or "Moema, São Paulo")}</p>{f"<div class=h>{esc(h)}</div>" if h else ""}<div class="mc-ac">{acts}</div></article>'
    return f'<article><h3>{esc(l["nome"])}</h3><p>{esc(l.get("end") or "Moema, São Paulo")}</p>{f"<div class=h>{esc(h)}</div>" if h else ""}<div class="mc-ac">{acts}</div></article>'

def cats_validas(L, CATS):
    from collections import Counter
    n = Counter(l['cat'] for l in L)
    return [(c, n[c[0]]) for c in CATS if c[0] not in CAT_SLUG_SKIP and n[c[0]] >= 8]

def render(cat, L, CATS, u, wa):
    CM = {c[0]: c for c in CATS}
    key, label = cat[0], cat[1]
    itens = [l for l in L if l['cat'] == key]
    itens.sort(key=lambda l: (not l.get('destaque'), not l.get('horario'), l['nome'].lower()))
    ind = [l for l in itens if l.get('destaque')]
    resto = [l for l in itens if not l.get('destaque')]
    titulo, intro = TXT.get(key, (f'{label} em Moema', f'{label} de Moema reunidos pela W3W Imóveis, com endereço, horário e como chegar.'))
    pal = label.lower()
    h1 = f'{label} em <em>Moema.</em>'
    outros = ''.join(f'<a href="{u("moema/" + c[0])}">{esc(c[1])}<small>{n}</small></a>' for c, n in cats_validas(L, CATS) if c[0] != key)
    faq = [(f'Quantos lugares de {pal} existem em Moema?', f'O Guia Moema da W3W lista {len(itens)} lugares na categoria {pal} em Moema e arredores, atualizados duas vezes por semana.'),
           (f'Quais {pal} a W3W indica em Moema?', (', '.join(l['nome'] for l in ind[:6]) + '.') if ind else f'A curadoria W3W de {pal} está em andamento. Enquanto isso, veja a lista completa nesta página.'),
           ('Como saber o que está aberto agora?', 'No Mapa de Moema da W3W você filtra pelo que está aberto neste momento, busca pelo nome e salva seus favoritos.')]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "ItemList", "name": titulo, "numberOfItems": len(itens), "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "item": {"@type": "LocalBusiness", "name": l['nome'], "address": {"@type": "PostalAddress", "streetAddress": l.get('end') or '', "addressLocality": "São Paulo", "addressRegion": "SP", "addressCountry": "BR"}, "geo": {"@type": "GeoCoordinates", "latitude": l['lat'], "longitude": l['lon']}, **({"telephone": l['tel']} if l.get('tel') else {}), **({"url": l['site']} if l.get('site') else {})}}
            for i, l in enumerate(itens[:60])]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Guia Moema", "item": u('guia-moema')}, {"@type": "ListItem", "position": 2, "name": "Moema por categoria", "item": u('moema')}, {"@type": "ListItem", "position": 3, "name": label}]}]}
    return CSS + f'''<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<main class="mc"><div class="in">
<nav class="mc-bc" aria-label="Você está em"><a href="{u('guia-moema')}">Guia Moema</a><span>/</span><a href="{u('moema')}">Moema por categoria</a><span>/</span><span>{esc(label)}</span></nav>
<h1>{h1}</h1>
<p class="lead">{esc(intro)}</p>
<dl class="mc-st"><div><dt>{len(itens)}</dt><dd>lugares</dd></div><div><dt>{len(ind)}</dt><dd>W3W indica</dd></div><div><dt>2×</dt><dd>atualizado por semana</dd></div></dl>
<a class="mc-cta" href="{u('mapa-moema')}?cat={key}">Ver {esc(pal)} no mapa →</a>
{f'<h2>A W3W <em>indica.</em></h2><div class="mc-ind">' + ''.join(card(l, CM, True) for l in ind) + '</div>' if ind else ''}
<h2>Todos os lugares <em>do bairro.</em></h2>
<div class="mc-ls">{''.join(card(l, CM) for l in resto)}</div>
<h2>Perguntas <em>frequentes.</em></h2>
<div class="mc-fq">{''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faq)}</div>
<h2>Mais de <em>Moema.</em></h2>
<div class="mc-ot">{outros}</div>
<div class="mc-end"><h2>Pensando em morar <em>em Moema?</em></h2><a href="{wa}" target="_blank" rel="noopener">Fale com a W3W</a></div>
</div></main>'''

def render_index(L, CATS, u, wa):
    cs = cats_validas(L, CATS)
    return CSS + f'''<main class="mc"><div class="in">
<nav class="mc-bc"><a href="{u('guia-moema')}">Guia Moema</a><span>/</span><span>Moema por categoria</span></nav>
<h1>Moema, <em>por categoria.</em></h1>
<p class="lead">Restaurantes, cafés, padarias, bares, serviços e lazer: tudo o que existe em Moema, organizado pela W3W Imóveis. Escolha uma categoria ou abra o mapa vivo do bairro.</p>
<dl class="mc-st"><div><dt>{len(L)}</dt><dd>lugares</dd></div><div><dt>{len(cs)}</dt><dd>categorias</dd></div></dl>
<a class="mc-cta" href="{u('mapa-moema')}">Abrir o Mapa de Moema →</a>
<h2>Escolha <em>uma categoria.</em></h2>
<div class="mc-ot">{''.join(f'<a href="{u("moema/" + c[0])}">{esc(c[1])}<small>{n}</small></a>' for c, n in cs)}</div>
<div class="mc-end"><h2>Pensando em morar <em>em Moema?</em></h2><a href="{wa}" target="_blank" rel="noopener">Fale com a W3W</a></div>
</div></main>'''
