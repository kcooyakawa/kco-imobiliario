"""Páginas /moema/<cat>/ v4 — editorial branco, nível revista. Serifa PP Editorial nos títulos, Neue Montreal no texto."""
import json, html
from moema_idx import ico, FOTO, hum
from moema_v3 import FOTOS, LB, CK, gm, rua, JS as JS3
def esc(s): return html.escape(str(s or ''), quote=True)

CSS = r'''<style>
body:has(.v4){background:#fff}
.v4{--ink:#17181A;--i2:#6B6F76;--g1:#F5F5F4;--e:cubic-bezier(.22,1,.36,1);position:relative;background:#fff;color:var(--ink);font-family:var(--sans,sans-serif);overflow:clip}
.v4::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:60;opacity:.035;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23n)'/%3E%3C/svg%3E")}
.v4 .in{width:calc(100% - clamp(40px,8vw,160px));max-width:1440px;margin:0 auto}
.v4 h1,.v4 h2,.v4 h3{font-family:var(--serif,serif);font-weight:200;margin:0;letter-spacing:-.025em}
.v4-h{padding:clamp(130px,13vw,190px) 0 0}
.v4-hg{display:grid;grid-template-columns:7fr 4fr;gap:clamp(30px,6vw,120px);align-items:end}
.v4-bc{font-size:14px;color:var(--i2);margin-bottom:clamp(28px,3vw,44px);display:flex;gap:10px}.v4-bc a{color:inherit;text-decoration:none}.v4-bc a:hover{color:var(--ink)}
.v4-h h1{font-size:clamp(72px,10.5vw,184px);line-height:.9;overflow:hidden}
.v4-h h1 span{display:block;animation:v4u 1.6s var(--e) both}.v4-h h1 span+span{animation-delay:.1s}
@keyframes v4u{from{transform:translateY(105%)}}
.v4-ld{font-size:clamp(17px,1.25vw,19px);line-height:1.75;margin:0;max-width:34ch;animation:v4f 1.4s .4s var(--e) both}
.v4-lv{margin:26px 0 0;font-size:16px;display:flex;align-items:center;gap:10px;animation:v4f 1.4s .5s var(--e) both}
.v4-lv i{width:7px;height:7px;border-radius:50%;background:var(--k);animation:v4p 2.4s infinite}
@keyframes v4p{50%{opacity:.3}}
.v4-lk{display:flex;gap:28px;margin-top:30px;animation:v4f 1.4s .6s var(--e) both}
.v4-lk a{color:var(--ink);text-decoration:none;font-size:16px;padding-bottom:6px;background:linear-gradient(var(--ink),var(--ink)) 0 100%/100% 1px no-repeat;transition:background-size .5s var(--e)}
.v4-lk a:hover{background-size:0 1px;background-position:100% 100%}
@keyframes v4f{from{opacity:0;transform:translateY(18px)}}
.v4-bd{margin-top:clamp(70px,8vw,130px)}
.v4-bd figure{margin:0;position:relative;overflow:hidden;aspect-ratio:21/9;background:var(--g1)}
.v4-bd img{position:absolute;inset:-6% 0;width:100%;height:112%;object-fit:cover;animation:v4z 2.6s var(--e) both}
@keyframes v4z{from{transform:scale(1.12);opacity:0}}
.v4-bd figcaption,.v4-it figcaption{display:flex;justify-content:space-between;margin-top:14px;font-size:13.5px;color:var(--i2)}
.v4-bd .ph{position:absolute;inset:0;display:grid;place-items:center;color:var(--i2)}.v4-bd .ph svg{width:10%;height:30%}
.v4 svg path{fill:none;stroke:currentColor;stroke-width:1;stroke-linecap:round;stroke-linejoin:round}
.v4-sec{padding:clamp(150px,16vw,260px) 0 0}
.v4-sh{display:grid;grid-template-columns:7fr 4fr;gap:clamp(30px,6vw,120px);align-items:end;margin-bottom:clamp(70px,8vw,130px)}
.v4-sh h2{font-size:clamp(52px,6.4vw,112px);line-height:.95}
.v4-sh p{margin:0;font-size:17px;line-height:1.75;color:var(--i2);max-width:34ch}
.v4-it{display:grid;grid-template-columns:repeat(12,1fr);gap:0 clamp(16px,2vw,32px);margin-bottom:clamp(120px,13vw,220px);align-items:end}
.v4-it figure{margin:0;grid-column:1/8}
.v4-it .tx{grid-column:9/13;padding-bottom:30px}
.v4-it:nth-of-type(even) figure{grid-column:6/13;order:2}.v4-it:nth-of-type(even) .tx{grid-column:1/5}
.v4-it:nth-of-type(3n) figure{grid-column:2/9;order:0}.v4-it:nth-of-type(3n) .v4-pi{aspect-ratio:4/5}.v4-it:nth-of-type(3n) .tx{grid-column:10/13}
.v4-pi{position:relative;aspect-ratio:4/5;overflow:hidden;background:var(--g1)}
.v4-it:nth-of-type(even) .v4-pi{aspect-ratio:3/2}
.v4-pi img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transform:scale(1.1);transition:transform 2s var(--e),opacity 1.1s var(--e)}
.v4-it.on .v4-pi img{transform:scale(1)}
.v4-pi img+img{opacity:0}.v4-pi:hover img+img{opacity:1}
.v4-it h3{font-size:clamp(40px,3.8vw,64px);line-height:.98}
.v4-it .ad{margin:18px 0 0;font-size:16px}
.v4-it .ds{margin:22px 0 0;font-size:16px;line-height:1.75;color:var(--i2);max-width:32ch}
.v4-op{display:flex;align-items:center;gap:9px;margin-top:22px;font-size:14.5px}
.v4-op i{width:6px;height:6px;border-radius:50%;background:#C9CBCF}.v4-op.on i{background:var(--k)}
.v4-op em{font-style:normal}
.v4-ac{display:flex;gap:22px;margin-top:28px;flex-wrap:wrap}
.v4-ac a{color:var(--ink);text-decoration:none;font-size:15px;padding-bottom:5px;background:linear-gradient(var(--ink),var(--ink)) 0 100%/100% 1px no-repeat;transition:background-size .5s var(--e)}
.v4-ac a:hover{background-size:0 1px;background-position:100% 100%}
.v4-tb{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(40px,5vw,80px) clamp(24px,3vw,56px)}
.v4-tb a{color:var(--ink);text-decoration:none;display:block}
.v4-tb b{display:block;font:200 clamp(30px,2.6vw,42px)/1 var(--serif,serif);letter-spacing:-.02em;transition:transform .6s var(--e)}
.v4-tb span{display:block;margin-top:10px;font-size:15px;color:var(--i2)}
.v4-tb a:hover b{transform:translateX(8px)}
.v4-fl{display:flex;gap:26px;align-items:baseline;flex-wrap:wrap;margin-bottom:clamp(40px,4vw,60px)}
.v4-fl button{font:400 16px var(--sans,sans-serif);border:0;background:none;padding:0 0 6px;color:var(--i2);cursor:pointer;transition:color .3s}
.v4-fl button[aria-pressed=true]{color:var(--ink);background:linear-gradient(var(--ink),var(--ink)) 0 100%/100% 1px no-repeat}
.v4-fl input{margin-left:auto;width:min(340px,100%);border:0;border-bottom:1px solid #D9DADC;background:none;padding:8px 0;font:16px var(--sans,sans-serif);color:var(--ink);outline:0}
.v4-fl input:focus{border-color:var(--ink)}
.v4-fl span{font-size:14px;color:var(--i2)}
.v4-ls{columns:2;column-gap:clamp(40px,6vw,120px)}
.v4-ls a{break-inside:avoid;display:grid;grid-template-columns:1fr auto;gap:4px 16px;padding:18px 0;color:var(--ink);text-decoration:none}
.v4-ls b{font:300 clamp(22px,1.7vw,27px)/1.15 var(--serif,serif);letter-spacing:-.01em;transition:transform .5s var(--e)}
.v4-ls a:hover b{transform:translateX(6px)}
.v4-ls .ad{grid-column:1;font-size:14px;color:var(--i2)}
.v4-ls .op{grid-row:1/3;grid-column:2;align-self:center;display:flex;gap:7px;align-items:center;font-size:13.5px;color:var(--i2)}
.v4-ls .op i{width:6px;height:6px;border-radius:50%;background:#D3D5D8}.v4-ls .op.on i{background:var(--k)}.v4-ls .op em{font-style:normal}
.v4-mr{margin-top:40px;font:400 16px var(--sans,sans-serif);border:0;background:none;color:var(--ink);cursor:pointer;padding:0 0 6px;background:linear-gradient(var(--ink),var(--ink)) 0 100%/100% 1px no-repeat}
.v4-ot{font:200 clamp(34px,3.6vw,60px)/1.25 var(--serif,serif);letter-spacing:-.02em;max-width:22ch}
.v4-ot a{color:#B3B5B9;text-decoration:none;transition:color .4s}.v4-ot a:hover{color:var(--ink)}
.v4-ot a+a::before{content:", ";color:#B3B5B9}
.v4-end{padding:clamp(150px,16vw,260px) 0 clamp(90px,10vw,150px);display:grid;grid-template-columns:7fr 4fr;gap:clamp(30px,6vw,120px);align-items:end}
.v4-end h2{font-size:clamp(52px,6.4vw,112px);line-height:.95}
.v4-end a{justify-self:start;background:var(--ink);color:#fff;text-decoration:none;padding:20px 32px;font-size:16px;transition:transform .4s var(--e),background .3s}.v4-end a:hover{transform:translateY(-3px)}
.v3-rv>*{opacity:0;transform:translateY(28px);transition:opacity 1.2s var(--e),transform 1.2s var(--e)}
.v3-rv.on>*{opacity:1;transform:none}.v3-rv.on>*:nth-child(2){transition-delay:.09s}.v3-rv.on>*:nth-child(3){transition-delay:.18s}
@media(max-width:860px){.v4-hg,.v4-sh,.v4-end{grid-template-columns:1fr}.v4-it{display:block}.v4-it .tx{padding:28px 0 0}.v4-it:nth-of-type(even) .v4-pi{aspect-ratio:4/5}.v4-bd figure{aspect-ratio:4/5}.v4-tb{grid-template-columns:1fr}.v4-ls{columns:1}.v4-fl input{margin-left:0;width:100%}}
@media(prefers-reduced-motion:reduce){.v4 *{animation:none!important;transition:none!important}.v3-rv>*{opacity:1;transform:none}}
</style>'''

JS = (JS3.replace(".v3-op",".v4-op").replace("'.v3-ls a'","'.v4-ls a'").replace(".v3-ls",".v4-ls").replace("v3-it","v4-it").replace(".v3-fl button",".v4-fl button")
      .replace("'.v3-bd img'","'.v4-bd img'").replace("y*.12","y*.08").replace("<i></i>Agora, <b>${ab}</b> de ${tot} estão abertos.","<i></i>${ab} de ${tot} abertos agora"))

def render_cat(cat, L, cs, u, wa, img_base, titulo, intro, ld):
    key, label = cat[0], cat[1]
    it = [l for l in L if l['cat'] == key]
    ind = [l for l in it if l.get('destaque')]
    com = [l for l in ind if FOTOS.get(l['nome'])]; sem = [l for l in ind if not FOTOS.get(l['nome'])]
    resto = sorted([l for l in it if not l.get('destaque')], key=lambda l: l['nome'].lower())
    hf, hc = (FOTO[key], f'{label} em Moema') if key in FOTO else ((LB + FOTOS[com[0]['nome']][0] + '.jpg', com[0]['nome']) if com else (None, ''))
    bd = (f'<div class="in v4-bd"><figure><img src="{img_base}{hf}" alt="{esc(hc)}" loading="eager"></figure><figcaption><span>{esc(hc)}</span><span>Guia Moema · W3W</span></figcaption></div>' if hf else '')
    def acts(l):
        return (f'<a href="{gm(l)}" target="_blank" rel="noopener">Como chegar</a>' + (f'<a href="{esc(l["site"])}" target="_blank" rel="noopener nofollow">Site</a>' if l.get('site') else '')
                + (f'<a href="tel:{esc("".join(c for c in l["tel"] if c.isdigit() or c=="+"))}">Ligar</a>' if l.get('tel') else ''))
    fe = ''.join(f'<article class="v4-it v3-rv" data-h="{esc(l.get("horario"))}"><figure><div class="v4-pi">' + ''.join(f'<img src="{img_base}{LB}{f}.jpg" alt="{esc(l["nome"])}, Moema" loading="lazy">' for f in FOTOS[l['nome']][:2])
                 + f'</div></figure><div class="tx"><h3>{esc(l["nome"])}</h3><p class="ad">{esc(rua(l))}</p>' + (f'<p class="ds">{esc(l["nota"])}</p>' if l.get('nota') else (f'<p class="ds">{esc(hum(l.get("horario")))}</p>' if l.get('horario') else ''))
                 + f'<div class="v4-op"><i></i><em>Horário não informado</em></div><div class="v4-ac">{acts(l)}</div></div></article>' for l in com)
    tb = ''.join(f'<a href="{gm(l)}" target="_blank" rel="noopener" data-h="{esc(l.get("horario"))}"><b>{esc(l["nome"])}</b><span>{esc(rua(l))}</span></a>' for l in sem)
    ls = ''.join(f'<a href="{gm(l)}" target="_blank" rel="noopener" data-h="{esc(l.get("horario"))}"><b>{esc(l["nome"])}</b><span class="ad">{esc(rua(l))}</span><span class="op"><i></i><em></em></span></a>' for l in resto)
    ot = ''.join(f'<a href="{u("moema/"+c[0])}">{esc(c[1].lower() if i else c[1])}</a>' for i, (c, n) in enumerate([x for x in cs if x[0][0] != key]))
    return (CSS + f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script><main class="v4" style="--k:{CK.get(key, chr(35)+"1F4FA0")}">'
        f'<section class="v4-h"><div class="in"><nav class="v4-bc" aria-label="Você está em"><a href="{u("guia-moema")}">Guia Moema</a><span>/</span><a href="{u("moema")}">Moema por categoria</a></nav>'
        f'<div class="v4-hg"><h1><span>{esc(label)}</span><span>em Moema</span></h1><div><p class="v4-ld">{esc(intro)}</p><p class="v4-lv" id="v3Live">{len(it)} lugares</p>'
        f'<div class="v4-lk"><a href="{u("mapa-moema")}?cat={key}">Ver no mapa</a><a href="#lista">Ver a lista</a></div></div></div></div>{bd}</section>'
        + (f'<section class="v4-sec"><div class="in"><div class="v4-sh v3-rv"><h2>A seleção da W3W</h2><p>Casas que conhecemos, frequentamos e indicamos a quem vem morar em Moema.</p></div>{fe}</div></section>' if com else '')
        + (f'<section class="v4-sec"><div class="in"><div class="v4-sh v3-rv"><h2>{"Também indicamos" if com else "A seleção da W3W"}</h2><p>{"Mais endereços da nossa lista." if com else "Casas que conhecemos, frequentamos e indicamos a quem vem morar em Moema."}</p></div><div class="v4-tb v3-rv">{tb}</div></div></section>' if sem else '')
        + f'<section class="v4-sec" id="lista"><div class="in"><div class="v4-sh v3-rv"><h2>Todos de Moema</h2><p>{len(resto)} endereços do bairro, atualizados duas vezes por semana.</p></div>'
        f'<div class="v4-fl"><button data-f="t" aria-pressed="true">Todos</button><button data-f="a" aria-pressed="false">Abertos agora</button><span id="v3N"></span><input id="v3Q" type="search" placeholder="Buscar pelo nome ou rua" aria-label="Buscar na lista"></div>'
        f'<div class="v4-ls">{ls}</div><button id="v3More" class="v4-mr">Ver todos</button></div></section>'
        f'<section class="v4-sec"><div class="in"><div class="v4-sh v3-rv"><h2>Mais de Moema</h2><p>Outros recortes do bairro.</p></div><p class="v4-ot v3-rv">{ot}</p></div></section>'
        f'<div class="in v4-end v3-rv"><h2>Gostou do bairro? Venha morar nele.</h2><a href="{wa}" target="_blank" rel="noopener">Fale com a W3W</a></div></main>' + JS)
