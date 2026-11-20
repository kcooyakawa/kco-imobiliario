#!/usr/bin/env python3
"""Gera o site estático da W3W a partir de empreendimentos.json.
Uso: python3 build.py  ->  escreve em ../site/
"""
import json, os, html, shutil, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, '..', 'w3w')
BASE = os.environ.get('W3W_BASE', '/kco-imobiliario/w3w')   # caminho base no GitHub Pages
SITE = os.environ.get('W3W_SITE', 'https://kcooyakawa.github.io')
FONTS = os.environ.get('W3W_FONTS', '/kco-imobiliario/w3w-fonts')
WA = '5511940297871'
EMAIL = 'w3wimoveis@gmail.com'
TEL = '+55 (11) 94029-7871'
CRECI = 'CRECI 047467-J'
OG = 'https://kcooyakawa.github.io/kco-imobiliario/w3w-share/w3w-og.jpg'
HERO = 'https://w3wimoveis.com.br/wp-content/uploads/2024/12/o-que-fazer-no-parque-ibirapuera.jpeg'

E = json.load(open(os.path.join(ROOT, 'empreendimentos.json'), encoding='utf-8'))
LOGO = open(os.path.join(ROOT, 'logo.svg'), encoding='utf-8').read().strip()
LOGO = LOGO.replace('aria-label="W3W Imóveis"', 'role="img" aria-label="W3W Imóveis"')

esc = html.escape
import time
VER = str(int(time.time()))
def u(p=''): return f'{BASE}/{p}'.rstrip('/') + '/' if p and not p.endswith('.html') else f'{BASE}/{p}'
def wa(msg): return f'https://wa.me/{WA}?text=' + urllib.parse.quote(msg)

BAIRROS = {
 'moema': dict(nome='Moema', titulo='Imóveis novos em Moema',
   lead='Moema reúne ruas arborizadas, o Parque Ibirapuera a poucos minutos, metrô, boa gastronomia e alguns dos lançamentos mais disputados de São Paulo. Selecionamos aqui os empreendimentos que acompanhamos de perto, de studios a apartamentos de alto padrão.',
   desc='Apartamentos e studios novos em Moema: lançamentos, imóveis em obras e prontos para morar, com curadoria da W3W Imóveis.'),
 'vila-nova-conceicao': dict(nome='Vila Nova Conceição', titulo='Imóveis novos na Vila Nova Conceição',
   lead='A Vila Nova Conceição é um dos endereços mais valorizados de São Paulo: vizinha do Ibirapuera, residencial, silenciosa e com projetos assinados por grandes incorporadoras. Aqui estão os empreendimentos que a W3W acompanha no bairro.',
   desc='Apartamentos novos de alto padrão na Vila Nova Conceição: lançamentos, em obras e prontos, com curadoria da W3W Imóveis.'),
}

CSS = r"""
@font-face{font-family:'PP Editorial New';src:url(__F__/ppeditorial-ultralight.woff2) format('woff2');font-weight:200 300;font-style:normal;font-display:swap}
@font-face{font-family:'PP Editorial New';src:url(__F__/ppeditorial-ultralight-italic.woff2) format('woff2');font-weight:200 300;font-style:italic;font-display:swap}
@font-face{font-family:'PP Editorial New';src:url(__F__/ppeditorial-regular.woff2) format('woff2');font-weight:400 500;font-style:normal;font-display:swap}
@font-face{font-family:'PP Neue Montreal';src:url(__F__/ppneuemontreal-light.woff2) format('woff2');font-weight:300;font-display:swap}
@font-face{font-family:'PP Neue Montreal';src:url(__F__/ppneuemontreal-regular.woff2) format('woff2');font-weight:400;font-display:swap}
@font-face{font-family:'PP Neue Montreal';src:url(__F__/ppneuemontreal-semibold.woff2) format('woff2');font-weight:500 600;font-display:swap}
:root{--ink:#1A1817;--ink-2:#5E6672;--slate:#757E8D;--slate-2:#9AA3AF;--paper:#ECEEF1;--paper-2:#F6F7F9;--line:rgba(26,24,23,.12);
--serif:'PP Editorial New',Georgia,serif;--sans:'PP Neue Montreal',system-ui,sans-serif;--ease:cubic-bezier(.2,.7,.2,1);--w:1200px}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}
img{display:block;max-width:100%}
a{color:inherit;text-decoration:none}
.wrap{max-width:var(--w);margin:0 auto;padding:0 32px}
.eyebrow{font-size:11px;letter-spacing:.22em;text-transform:uppercase;font-weight:500;color:var(--ink-2)}
.serif{font-family:var(--serif);font-weight:300}
.it{font-style:italic}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;border:1px solid var(--ink);padding:14px 26px;font-size:11px;letter-spacing:.2em;text-transform:uppercase;font-weight:500;transition:background .25s var(--ease),color .25s var(--ease);cursor:pointer;background:transparent;color:var(--ink);font-family:var(--sans)}
.btn:hover{background:var(--ink);color:var(--paper-2)}
.btn.solid{background:var(--ink);color:var(--paper-2)}.btn.solid:hover{background:var(--slate);border-color:var(--slate)}
.btn.light{border-color:rgba(246,247,249,.55);color:#F6F7F9}.btn.light:hover{background:#F6F7F9;color:var(--ink)}
/* header */
.hd{position:sticky;top:0;z-index:50;background:rgba(246,247,249,.9);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.hd .wrap{display:flex;align-items:center;justify-content:space-between;height:84px}
.brand{display:flex;flex-direction:column;align-items:center;gap:6px}
.brand svg{height:44px;width:auto;color:var(--ink)}
.creci{font-size:8.5px;letter-spacing:.24em;text-transform:uppercase;color:var(--ink-2)}
.nav{display:flex;align-items:center;gap:6px}
.nav a{font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;font-weight:500;padding:8px 12px;opacity:.72;transition:opacity .2s}
.nav a:hover,.nav a[aria-current]{opacity:1}
.nav .btn{opacity:1;margin-left:8px;padding:11px 18px}
.burger{display:none;background:none;border:0;width:40px;height:40px;cursor:pointer;color:var(--ink)}
@media(max-width:900px){.nav{position:fixed;inset:84px 0 auto 0;flex-direction:column;align-items:stretch;background:var(--paper-2);border-bottom:1px solid var(--line);padding:12px 20px 24px;gap:0;transform:translateY(-120%);transition:transform .35s var(--ease)}
.nav.open{transform:none}.nav a{padding:14px 0;border-bottom:1px solid var(--line)}.nav .btn{margin:16px 0 0}.burger{display:block}.hd .wrap{height:72px}.nav{inset:72px 0 auto 0}.brand svg{height:36px}}
/* hero */
.hero{position:relative;color:#F6F7F9;background:#1A1817 center/cover no-repeat}
.hero::before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,17,16,.86) 0%,rgba(18,17,16,.66) 50%,rgba(18,17,16,.86) 100%)}
.hero .wrap{position:relative;padding-top:96px;padding-bottom:96px}
.hero h1{font-family:var(--serif);font-weight:300;font-size:clamp(34px,5vw,68px);line-height:1.04;letter-spacing:-.02em;max-width:900px}
.hero h1 em{font-style:italic}
.hero p.lead{font-size:clamp(16px,1.4vw,19px);line-height:1.6;color:rgba(246,247,249,.82);max-width:640px;margin:28px 0 48px;font-weight:300}
.bairros{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.bx{position:relative;overflow:hidden;padding:34px;border:1px solid rgba(246,247,249,.18);background:linear-gradient(155deg,rgba(117,126,141,.34),rgba(26,24,23,.72) 70%);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);transition:border-color .35s var(--ease),transform .5s var(--ease)}
.bx::before{content:"";position:absolute;inset:0;pointer-events:none;opacity:.22;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.bx:hover{border-color:rgba(246,247,249,.4);transform:translateY(-2px)}
.bx .eyebrow{color:rgba(246,247,249,.6)}
.bx h2{font-family:var(--serif);font-style:italic;font-weight:300;font-size:36px;line-height:1.05;margin:10px 0 0;padding-bottom:22px;border-bottom:1px solid rgba(246,247,249,.22)}
.bx .meta{font-size:13px;color:rgba(246,247,249,.7);margin:18px 0 22px}
.bx .row{display:flex;gap:8px;flex-wrap:wrap}
.bx .btn{padding:12px 18px}
@media(max-width:767px){.bairros{grid-template-columns:1fr}.bx{padding:24px}.bx h2{font-size:30px}.hero .wrap{padding-top:64px;padding-bottom:64px}}
/* sections */
.sec{padding:112px 0}
.sec-hd{display:flex;align-items:baseline;justify-content:space-between;gap:24px;border-bottom:1px solid var(--line);padding-bottom:22px;margin-bottom:44px;flex-wrap:wrap}
.sec-hd h2,.pg-hd h1{font-family:var(--serif);font-style:italic;font-weight:300;font-size:clamp(38px,4.6vw,64px);line-height:1;letter-spacing:-.02em}
.sec-hd a{font-size:11px;letter-spacing:.2em;text-transform:uppercase;font-weight:500;border-bottom:1px solid currentColor;padding-bottom:2px}
@media(max-width:767px){.sec{padding:64px 0}.wrap{padding:0 20px}}
/* cards */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:24px}
.card{display:flex;flex-direction:column;background:var(--paper-2);border:1px solid var(--line);transition:background .45s var(--ease),border-color .45s var(--ease),color .45s var(--ease)}
.card .ph{position:relative;aspect-ratio:4/5;overflow:hidden;background:#d9dde2}
.card .ph img{width:100%;height:100%;object-fit:cover;transition:transform .9s var(--ease)}
.card:hover .ph img{transform:scale(1.03)}
.tag{position:absolute;background:#F6F7F9;border:1px solid var(--ink);color:var(--ink);font-size:10px;letter-spacing:.2em;text-transform:uppercase;font-weight:500;padding:6px 11px}
.tag.st{top:16px;left:16px}.tags-b{position:absolute;right:12px;bottom:12px;display:flex;gap:6px}.tags-b .tag{position:static}
.card .bd{flex:1;display:flex;flex-direction:column;padding:22px}
.card .bd .eyebrow{font-size:10px}
.card h3{font-family:var(--serif);font-weight:300;font-size:26px;line-height:1.08;letter-spacing:-.01em;margin:6px 0 14px}
.card ul{list-style:none;border-top:1px solid var(--line);padding-top:14px;margin-bottom:20px;font-size:13px;color:var(--ink-2)}
.card li{display:flex;gap:10px;align-items:center;margin-bottom:6px}
.card li svg{flex:0 0 13px;width:13px;height:13px;opacity:.7}
.card .btn{margin-top:auto;width:100%;padding:13px 10px;font-size:10px}
.card:hover{background:var(--slate);border-color:var(--slate);color:#F6F7F9}
.card:hover .eyebrow,.card:hover ul{color:#F6F7F9}.card:hover ul{border-top-color:rgba(246,247,249,.3)}
.card:hover .btn{background:#F6F7F9;color:var(--ink);border-color:#F6F7F9}
/* filters */
.filters{display:flex;gap:28px;flex-wrap:wrap;margin-bottom:36px}
.fg{display:flex;flex-direction:column;gap:10px}
.chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{border:1px solid var(--line);background:transparent;padding:9px 14px;font-family:var(--sans);font-size:11px;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;color:var(--ink);transition:all .2s}
.chip[aria-pressed=true]{background:var(--ink);color:var(--paper-2);border-color:var(--ink)}
.count{font-size:13px;color:var(--ink-2);margin-bottom:18px}
/* page header */
.pg-hd{padding:96px 0 40px}
.pg-hd p{max-width:760px;margin-top:24px;font-family:var(--serif);font-weight:300;font-size:clamp(19px,1.8vw,24px);line-height:1.45}
.crumbs{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-2);margin-bottom:28px}
.crumbs a{border-bottom:1px solid var(--line)}
@media(max-width:767px){.pg-hd{padding:56px 0 24px}}
/* empreendimento */
.emp{display:grid;grid-template-columns:1.25fr 1fr;gap:56px;align-items:start}
.emp .ph img{width:100%;aspect-ratio:4/5;object-fit:cover;background:#d9dde2}
.emp h1{font-family:var(--serif);font-weight:300;font-size:clamp(40px,5vw,72px);line-height:1;letter-spacing:-.02em;margin:10px 0 24px}
.emp .frase{font-family:var(--serif);font-weight:300;font-size:22px;line-height:1.4;margin-bottom:32px}
.ficha{border-top:1px solid var(--line);margin-bottom:32px}
.ficha div{display:flex;justify-content:space-between;gap:24px;padding:14px 0;border-bottom:1px solid var(--line);font-size:15px}
.ficha dt{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-2);font-weight:500}
.ficha dd{text-align:right}
.emp .cta{display:flex;flex-direction:column;gap:10px}
.emp .sticky{position:sticky;top:120px}
@media(max-width:900px){.emp{grid-template-columns:1fr;gap:32px}.emp .sticky{position:static}}
/* quem somos */
.qs p{font-family:var(--serif);font-weight:300;font-size:clamp(20px,2vw,26px);line-height:1.45;max-width:860px;margin-bottom:24px}
.mvv{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.mvv .c{background:var(--paper-2);border:1px solid var(--line);padding:40px;transition:background .45s var(--ease),color .45s var(--ease),border-color .45s var(--ease)}
.mvv .c.full{grid-column:1/-1}
.mvv h3{font-family:var(--serif);font-style:italic;font-weight:300;font-size:36px;margin-bottom:16px}
.mvv p,.mvv li{font-size:15px;line-height:1.6;opacity:.85}
.mvv ul{list-style:none}.mvv li{margin-bottom:10px;padding-left:20px;position:relative}.mvv li::before{content:"—";position:absolute;left:0;color:var(--slate)}
.mvv .c:hover{background:var(--slate);color:#F6F7F9;border-color:var(--slate)}.mvv .c:hover li::before{color:#F6F7F9}
.team{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:20px}
.team .c{border-top:1px solid var(--ink);padding-top:20px}
.team h4{font-family:var(--serif);font-weight:300;font-size:28px}
.team p{font-size:14px;color:var(--ink-2);margin-top:6px}
@media(max-width:767px){.mvv,.team{grid-template-columns:1fr}.mvv .c{padding:28px}}
/* contato */
.ct{display:grid;grid-template-columns:1fr 1fr;gap:64px}
.form label{display:block;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-2);font-weight:500;margin-top:22px}
.form input,.form textarea,.form select{width:100%;border:0;border-bottom:1px solid var(--line);background:transparent;padding:12px 0;font-family:var(--sans);font-size:16px;color:var(--ink);border-radius:0}
.form input:focus,.form textarea:focus,.form select:focus{outline:none;border-bottom-color:var(--ink)}
.form .btn{margin-top:32px}
.form small{display:block;margin-top:14px;color:var(--ink-2);font-size:12px}
.ct .info dt{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-2);margin-top:26px}
.ct .info dd{font-family:var(--serif);font-weight:300;font-size:26px;margin-top:6px}
@media(max-width:900px){.ct{grid-template-columns:1fr;gap:40px}}
/* faixa */
.band{background:var(--ink);color:#F6F7F9}
.band .wrap{display:flex;justify-content:space-between;align-items:center;gap:32px;padding-top:72px;padding-bottom:72px;flex-wrap:wrap}
.band h2{font-family:var(--serif);font-weight:300;font-size:clamp(28px,3.4vw,44px);line-height:1.1;max-width:640px}
.band h2 em{font-style:italic}
/* footer */
.ft{background:var(--ink);color:#C9CED5;border-top:1px solid rgba(246,247,249,.08)}
.ft .top{display:grid;grid-template-columns:1.2fr 1fr 1fr 1fr;gap:40px;padding-top:96px;padding-bottom:72px;border-bottom:1px solid rgba(246,247,249,.1)}
.ft .brand{align-items:center;width:max-content}
.ft .brand svg{height:80px;color:var(--slate-2)}
.ft .creci{color:#8A929C}
.ft h5{font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:var(--slate-2);font-weight:500;margin-bottom:20px}
.ft li{list-style:none;margin-bottom:10px;font-size:15px;font-weight:300;color:#E6E9ED}
.ft li a{background:linear-gradient(currentColor,currentColor) 0 100%/0 1px no-repeat;transition:background-size .35s var(--ease)}.ft li a:hover{background-size:100% 1px}
.ft .bot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding-top:26px;padding-bottom:26px;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8A929C}
@media(max-width:900px){.ft .top{grid-template-columns:1fr 1fr;padding-top:64px}.ft .top>div:first-child{grid-column:1/-1}.ft .bot{flex-direction:column;text-align:center}}
/* whatsapp */
.wa{position:fixed;right:22px;bottom:22px;z-index:60;width:56px;height:56px;border-radius:50%;background:#25D366;display:grid;place-items:center;box-shadow:0 10px 30px -10px rgba(0,0,0,.4);transition:transform .25s var(--ease)}
.wa:hover{transform:scale(1.06)}.wa svg{width:28px;height:28px;color:#fff}

/* v2 home */
.hd.over{position:fixed;left:0;right:0;background:transparent;border-bottom-color:transparent;backdrop-filter:none;-webkit-backdrop-filter:none;color:#F6F7F9;transition:background .35s var(--ease),color .35s var(--ease),border-color .35s}
.hd.over .brand svg,.hd.over .burger{color:#F6F7F9}.hd.over .creci{color:rgba(246,247,249,.7)}.hd.over .nav .btn{border-color:rgba(246,247,249,.6);color:#F6F7F9}
.hd.over.solid{background:rgba(246,247,249,.92);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom-color:var(--line);color:var(--ink)}
.hd.over.solid .brand svg,.hd.over.solid .burger{color:var(--ink)}.hd.over.solid .creci{color:var(--ink-2)}.hd.over.solid .nav .btn{border-color:var(--ink);color:var(--ink)}
@media(max-width:900px){.hd.over .nav{color:var(--ink)}.hd.over .nav .btn{color:var(--ink);border-color:var(--ink)}}
.hx{position:relative;min-height:100svh;color:#F6F7F9;overflow:hidden;background:#1A1817}
.hx video,.terr video,.par-v video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hx::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,17,16,.82) 0%,rgba(18,17,16,.45) 22%,rgba(18,17,16,.2) 50%,rgba(18,17,16,.65) 100%)}
.hx-in{position:relative;z-index:1;padding-top:180px;padding-bottom:80px}
.hx .eyebrow{color:rgba(246,247,249,.75)}
.hx h1{font-family:var(--serif);font-weight:300;font-size:clamp(64px,11vw,176px);line-height:.88;letter-spacing:-.035em;margin:24px 0 32px}
.hx h1 em{font-style:italic}
.hx p{max-width:520px;font-size:clamp(16px,1.3vw,19px);line-height:1.6;color:rgba(246,247,249,.85);font-weight:300}
.hx-cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:36px}
.btn.solid-l{background:#F6F7F9;color:var(--ink);border-color:#F6F7F9}.btn.solid-l:hover{background:transparent;color:#F6F7F9}
.g-hd{display:grid;grid-template-columns:1.3fr 1fr;gap:40px;align-items:end;border-bottom:1px solid var(--line);padding-bottom:28px;margin-bottom:32px}
.g-hd h2,.terr h2,.par h2,.cafe h2{font-family:var(--serif);font-weight:300;font-size:clamp(44px,6vw,96px);line-height:.95;letter-spacing:-.03em;margin-top:12px}
.g-hd h2 em,.terr h2 em,.par h2 em,.cafe h2 em{font-style:italic}
.g-hd p{color:var(--ink-2);font-size:17px;line-height:1.6}
.g-ctl{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;margin-bottom:20px}
.seg{display:flex;border:1px solid var(--ink)}
.sg{background:transparent;border:0;padding:10px 18px;font-family:var(--sans);font-size:11px;letter-spacing:.14em;text-transform:uppercase;font-weight:500;cursor:pointer;color:var(--ink)}
.sg[aria-pressed=true]{background:var(--ink);color:var(--paper-2)}
.gal{display:grid;grid-template-columns:repeat(4,1fr);gap:28px 20px}
.g .ph{position:relative;aspect-ratio:3/4;overflow:hidden;background:#d9dde2}
.g .ph img{width:100%;height:100%;object-fit:cover;transition:transform .9s var(--ease),filter .5s}
.g:hover .ph img{transform:scale(1.04)}
.g .ph::after{content:"";position:absolute;inset:0;background:var(--slate);mix-blend-mode:multiply;opacity:0;transition:opacity .45s var(--ease)}.g:hover .ph::after{opacity:.35}
.gi{padding-top:14px;border-top:0}.gi h3{font-family:var(--serif);font-weight:300;font-size:24px;line-height:1.1;letter-spacing:-.01em}
.gi p{font-size:13px;color:var(--ink-2);margin-top:4px}.gi .sp{color:var(--ink)}
.more{text-align:center;margin-top:48px}
@media(max-width:1100px){.gal{grid-template-columns:repeat(3,1fr)}}
@media(max-width:767px){.gal{grid-template-columns:repeat(2,1fr);gap:22px 12px}.gi h3{font-size:19px}.g-hd{grid-template-columns:1fr;gap:16px}.hx-in{padding-top:130px}}
.terr{position:relative;color:#F6F7F9;background:#1A1817;overflow:hidden}
.terr::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(18,17,16,.85),rgba(18,17,16,.35))}
.terr-in{position:relative;z-index:1;padding-top:140px;padding-bottom:120px}
.terr .eyebrow,.par .eyebrow{color:rgba(246,247,249,.65)}
.terr p{max-width:560px;margin:28px 0 48px;font-size:18px;line-height:1.6;color:rgba(246,247,249,.85);font-weight:300}
.terr-b{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid rgba(246,247,249,.25)}
.terr-b a{padding:22px 20px 22px 0;border-right:1px solid rgba(246,247,249,.15);display:flex;flex-direction:column;gap:6px;transition:padding .35s var(--ease)}
.terr-b a:last-child{border-right:0}.terr-b a+a{padding-left:20px}
.terr-b strong{font-family:var(--serif);font-weight:300;font-size:26px}.terr-b span{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:rgba(246,247,249,.6)}
@media(max-width:767px){.terr-b{grid-template-columns:1fr}.terr-b a,.terr-b a+a{padding:18px 0;border-right:0;border-bottom:1px solid rgba(246,247,249,.15)}}
.soc{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.soc>div{border-top:1px solid var(--ink);padding-top:22px}
.soc h3{font-family:var(--serif);font-weight:300;font-size:34px;line-height:1.05;margin-bottom:10px}
.soc p{margin-top:16px;color:var(--ink-2);font-size:15px;line-height:1.6}
@media(max-width:767px){.soc{grid-template-columns:1fr;gap:32px}}
.par{display:grid;grid-template-columns:1fr 1fr;background:#1A1817;color:#F6F7F9}
.par-v{position:relative;min-height:640px;overflow:hidden}
.par-c{padding:112px 64px}
.mods{margin:44px 0}.mods>div{border-top:1px solid rgba(246,247,249,.18);padding:22px 0}
.mods h3{font-family:var(--serif);font-weight:300;font-size:26px;margin-bottom:8px}.mods p{font-size:15px;line-height:1.6;color:rgba(246,247,249,.72)}
@media(max-width:900px){.par{grid-template-columns:1fr}.par-v{min-height:380px}.par-c{padding:64px 20px}}
.cafe-g{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start}
.cafe-l{margin:28px 0 40px;font-size:18px;line-height:1.6;color:var(--ink-2);max-width:440px}
.cafe-i{border-top:1px solid var(--line)}.cafe-i>div{display:grid;grid-template-columns:140px 1fr;gap:16px;padding:16px 0;border-bottom:1px solid var(--line);align-items:baseline}
.cafe-i dt{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-2);font-weight:500}.cafe-i dd{font-family:var(--serif);font-weight:300;font-size:22px}
.cafe-f{background:var(--paper-2);border:1px solid var(--line);padding:40px}
.cafe-f label:first-of-type{margin-top:0}.two{display:grid;grid-template-columns:1fr 1fr;gap:20px}.two label{margin-top:0}
.cafe-f .btn{width:100%}.cafe-f small a{border-bottom:1px solid}
@media(max-width:900px){.cafe-g{grid-template-columns:1fr;gap:40px}.cafe-f{padding:24px}.two{grid-template-columns:1fr;gap:0}.two>div+div label{margin-top:22px}.cafe-i>div{grid-template-columns:1fr;gap:4px}}

/* v3 */
@media(max-width:900px){.nav{transform:translateY(calc(-100% - 120px))!important;visibility:hidden;transition:transform .35s var(--ease),visibility 0s .35s}.nav.open{transform:none!important;visibility:visible;transition:transform .35s var(--ease)}}
.brand svg{height:50px}.hd .wrap{height:92px}.creci{font-size:9.5px}
@media(max-width:900px){.brand svg{height:42px}.hd .wrap{height:80px}.nav{inset:80px 0 auto 0}}
.hx{min-height:88svh;display:flex;align-items:flex-end}
.hx::after{background:linear-gradient(180deg,rgba(18,17,16,.75) 0%,rgba(18,17,16,.15) 28%,rgba(18,17,16,0) 55%,rgba(18,17,16,.55) 100%)!important}
.hx-in{padding-top:0!important;padding-bottom:56px!important}
.hx h1{margin:0!important}
.hx-b{background:var(--paper)}
.hx-bg{display:grid;grid-template-columns:1fr 1.2fr auto;gap:40px;align-items:center;padding-top:44px;padding-bottom:44px;border-bottom:1px solid var(--line)}
.hx-b p{font-size:18px;line-height:1.55;color:var(--ink-2);max-width:520px}
.hx-b .hx-cta{margin:0}
@media(max-width:900px){.hx-bg{grid-template-columns:1fr;gap:18px}.hx{min-height:72svh}}
.gx{padding-bottom:40px}
.rows{display:flex;flex-direction:column;gap:72px}
.row-s .row-hd{max-width:var(--w);margin:0 auto 24px;padding:0 32px;display:flex;justify-content:space-between;align-items:flex-end;gap:20px}
.row-hd h3{font-family:var(--serif);font-weight:300;font-size:clamp(32px,3.6vw,52px);line-height:1;letter-spacing:-.02em;margin-top:8px}
.rc{font-family:var(--sans);font-size:13px;letter-spacing:.1em;vertical-align:super;color:var(--ink-2)}
.arr{display:flex;gap:8px}.arr button{width:46px;height:46px;border:1px solid var(--ink);background:transparent;cursor:pointer;font-size:16px;color:var(--ink);transition:background .2s,color .2s}.arr button:hover{background:var(--ink);color:var(--paper-2)}
.track{display:flex;gap:20px;overflow-x:auto;scroll-snap-type:x mandatory;padding:0 max(32px,calc((100vw - var(--w))/2 + 32px)) 8px;scrollbar-width:none}
.track::-webkit-scrollbar{display:none}
.track .g{flex:0 0 clamp(250px,24vw,340px);scroll-snap-align:start}
.row-s[data-st="Lançamento"] .track .g:first-child{flex-basis:clamp(300px,40vw,560px)}
.row-s[data-st="Lançamento"] .track .g:first-child .ph{aspect-ratio:4/3.6}
.g .ph{aspect-ratio:3/4}
.gi{display:grid;grid-template-columns:auto 1fr;gap:14px;padding-top:16px;border-top:1px solid var(--line);margin-top:14px}
.gi .n{font-size:11px;letter-spacing:.12em;color:var(--ink-2);padding-top:6px}
@media(max-width:767px){.row-s .row-hd{padding:0 20px}.arr{display:none}.track{padding:0 20px 8px}.track .g{flex-basis:72vw}.row-s[data-st="Lançamento"] .track .g:first-child{flex-basis:84vw}}
.socx{background:#232120;color:#F6F7F9;padding:112px 0}
.g-hd.dk{border-bottom-color:rgba(246,247,249,.15)}.g-hd.dk p,.socx .eyebrow{color:rgba(246,247,249,.65)}
.scs{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.sc-ph{aspect-ratio:4/5;overflow:hidden;background:#2d2b2a;margin-bottom:22px}
.sc-ph img{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.05);transition:transform .9s var(--ease),filter .6s}
.sc:hover .sc-ph img{transform:scale(1.03);filter:grayscale(.2)}
.sc h3{font-family:var(--serif);font-weight:300;font-size:32px;line-height:1.05;margin-bottom:8px}
.sc p{margin-top:14px;font-size:15px;line-height:1.6;color:rgba(246,247,249,.72)}
@media(max-width:767px){.scs{grid-template-columns:1fr;gap:44px}.socx{padding:64px 0}}
.mods>div{display:grid;grid-template-columns:44px 1fr;gap:12px}.mods .n{font-size:12px;letter-spacing:.12em;color:rgba(246,247,249,.55);padding-top:8px}
.cafe{background:var(--slate);color:#F6F7F9;padding:112px 0}
.cafe .eyebrow{color:rgba(246,247,249,.75)}.cafe-l{color:rgba(246,247,249,.85)!important}
.cafe-i{border-top-color:rgba(246,247,249,.3)!important}.cafe-i>div{border-bottom-color:rgba(246,247,249,.3)!important}.cafe-i dt{color:rgba(246,247,249,.7)!important}
.cafe-f{background:transparent!important;border:1px solid rgba(246,247,249,.35)!important}
.cafe-f label{color:rgba(246,247,249,.75)!important}.cafe-f input,.cafe-f textarea,.cafe-f select{color:#F6F7F9!important;border-bottom-color:rgba(246,247,249,.4)!important}
.cafe-f select option{color:var(--ink)}.cafe-f small{color:rgba(246,247,249,.75)!important}
@media(max-width:767px){.cafe{padding:64px 0}}
.ft{background:var(--ink)}
.ft-t{display:grid;grid-template-columns:auto 1fr auto;gap:48px;align-items:center;padding-top:56px;padding-bottom:44px;border-bottom:1px solid rgba(246,247,249,.1)}
.ft-b svg{height:46px!important;color:var(--slate-2)!important}
.ft-n{display:flex;flex-wrap:wrap;gap:10px 26px;justify-content:center}
.ft-n a,.ft-c a{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#C9CED5;transition:color .2s}.ft-n a:hover,.ft-c a:hover{color:#fff}
.ft-c{display:flex;flex-direction:column;gap:8px;text-align:right}.ft-c a{text-transform:none;letter-spacing:.02em;font-size:14px}
.ft-bot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding-top:20px;padding-bottom:24px;font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:#7D858F}
@media(max-width:900px){.ft-t{grid-template-columns:1fr;justify-items:center;text-align:center;gap:28px}.ft-c{text-align:center}.ft-bot{flex-direction:column;align-items:center;text-align:center}}
/* ficha */
html.lock{overflow:hidden}
.sheet{position:fixed;inset:0;z-index:100}
.sh-bg{position:absolute;inset:0;background:rgba(18,17,16,.6);opacity:0;transition:opacity .35s var(--ease)}
.sh-p{position:absolute;left:0;right:0;bottom:0;top:4vh;max-width:1180px;margin:0 auto;background:var(--paper-2);overflow-y:auto;overscroll-behavior:contain;transform:translateY(100%);transition:transform .45s var(--ease);outline:none}
.sheet.on .sh-bg{opacity:1}.sheet.on .sh-p{transform:none}
.sh-grab{width:44px;height:4px;background:rgba(26,24,23,.25);margin:10px auto 0;border-radius:2px}
.sh-x{position:sticky;top:12px;float:right;margin:4px 14px 0 0;z-index:3;width:46px;height:46px;border-radius:50%;border:1px solid var(--line);background:rgba(246,247,249,.92);display:grid;place-items:center;cursor:pointer;color:var(--ink)}
.sh-x:hover{background:var(--ink);color:var(--paper-2)}
.sh-in{padding:16px 48px 56px;clear:both}
.fx-ph{position:relative;aspect-ratio:16/9;overflow:hidden;background:#d9dde2}.fx-ph img{width:100%;height:100%;object-fit:cover}
.fx-b{display:grid;grid-template-columns:1.1fr 1fr;gap:56px;padding:44px 0 36px;border-bottom:1px solid var(--line)}
.fx-t h1,.fx-t h2{font-family:var(--serif);font-weight:300;font-size:clamp(44px,6vw,92px);line-height:.95;letter-spacing:-.03em;margin:14px 0 20px}
.fx-q{font-family:var(--serif);font-style:italic;font-weight:300;font-size:clamp(19px,1.8vw,24px);line-height:1.4;color:var(--ink-2);max-width:520px}
.fx-s{display:grid;grid-template-columns:1fr 1fr;align-content:start;border-top:1px solid var(--ink)}
.fx-s>div{padding:18px 18px 18px 0;border-bottom:1px solid var(--line)}.fx-s>div:nth-child(even){padding-left:18px;border-left:1px solid var(--line)}
.fx-s dt{font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-2);font-weight:500;margin-bottom:8px}
.fx-s dd{font-family:var(--serif);font-weight:300;font-size:24px;line-height:1.2}
.fx-c{display:flex;gap:12px;flex-wrap:wrap;align-items:center;padding-top:28px}.fx-l{font-size:12px;letter-spacing:.14em;text-transform:uppercase;margin-left:auto;border-bottom:1px solid var(--line)}
.fx-n{margin-top:18px;font-size:13px;color:var(--ink-2)}
@media(max-width:900px){.sh-p{top:6vh}.sh-in{padding:8px 18px 40px}.fx-b{grid-template-columns:1fr;gap:28px}.fx-ph{aspect-ratio:4/3}.fx-l{margin-left:0;width:100%}}
.fxp .fx-ph{aspect-ratio:21/9}@media(max-width:900px){.fxp .fx-ph{aspect-ratio:4/3}}

/* v4 hero */
@media(min-width:560px) and (max-width:767px){.scs{grid-template-columns:repeat(3,1fr)!important;gap:14px!important}.sc h3{font-size:22px}.sc p{font-size:13px}}
@media(max-width:559px){.sc-ph{aspect-ratio:1/1}}
.hx>.wrap{width:100%}
.hx{min-height:calc(100svh - 150px)!important;display:flex!important;flex-direction:column;justify-content:space-between}
.hx-top{position:relative;z-index:1;display:flex;justify-content:space-between;padding-top:120px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:rgba(246,247,249,.8)}
.hx h1{font-size:clamp(72px,13vw,210px)!important;line-height:.86!important}
.hx-b .hx-bg{min-height:150px;padding-top:28px;padding-bottom:28px}
.hx-b p{font-family:var(--serif);font-weight:300;font-size:clamp(20px,1.9vw,28px)!important;line-height:1.3!important;color:var(--ink)!important;max-width:560px}
@media(max-width:900px){.hx{min-height:calc(100svh - 230px)!important}.hx-top{padding-top:100px;font-size:10px;gap:12px}.hx-b .hx-bg{min-height:230px}}

/* hero LP */
.hlp{position:relative;height:200vh;background:#0D0D0D}
.hlp-s{position:sticky;top:0;height:100svh;overflow:hidden;color:#F4F2EF}
.hlp video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hlp-sh{position:absolute;inset:0;background:linear-gradient(rgba(13,13,13,.55),rgba(13,13,13,.05) 40%,rgba(13,13,13,.6))}
.hlp-m{position:absolute;left:0;right:0;top:112px;display:grid;grid-template-columns:repeat(4,1fr);gap:20px;font-size:12px;color:#D8D5CF;opacity:calc(1 - var(--h,0)*2)}
.hlp-m span:last-child{text-align:right}
.hlp-t{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;pointer-events:none}
.hlp h1{font-weight:300;letter-spacing:-.03em;line-height:1.02;margin:0}
.ht1,.ht2{display:block;white-space:nowrap;will-change:transform}
.ht1{font-family:var(--sans);font-weight:300;font-size:clamp(64px,15vw,264px);transform:translate3d(calc(var(--h,0)*-42vw),calc(var(--h,0)*-8vh),0) scale(calc(1 + var(--h,0)*.18));opacity:calc(1 - var(--h,0)*.7)}
.ht2{font-family:var(--serif);font-style:italic;font-weight:300;font-size:clamp(66px,15.5vw,284px);margin-top:.06em;padding-left:14vw;transform:translate3d(calc(var(--h,0)*34vw),calc(var(--h,0)*8vh),0) scale(calc(1 + var(--h,0)*.18));opacity:calc(1 - var(--h,0)*.7)}
.hlp-l{position:absolute;left:0;right:0;bottom:36px;display:flex;justify-content:space-between;align-items:flex-end;gap:24px}
.hlp-l p{max-width:36ch;font-size:clamp(16px,1.4vw,20px);color:#F4F2EF;font-weight:300;line-height:1.5}
.cue{display:flex;align-items:center;gap:12px;font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:#D8D5CF;opacity:calc(1 - var(--h,0)*3)}
.cue i{width:1px;height:40px;background:#D8D5CF;transform-origin:center top;animation:cue 2.2s ease-in-out infinite}
@keyframes cue{0%{transform:scaleY(0)}50%{transform:scaleY(1)}100%{transform:scaleY(0);transform-origin:center bottom}}
@media(max-width:760px){.ht2{padding-left:0}.hlp-m{grid-template-columns:1fr 1fr}.hlp-m span:nth-child(n+3){display:none}.hlp-m{top:96px}.hlp-l{flex-direction:column;align-items:flex-start}}
@media(prefers-reduced-motion:reduce){.hlp{height:auto}.hlp-s{position:relative}}

/* portfólio */
.pf{padding:120px 0 96px;background:var(--paper)}
.pf-hd{display:flex;justify-content:space-between;border-bottom:1px solid var(--ink);padding-bottom:14px}
.pf-f{display:flex;flex-wrap:wrap;gap:12px 40px;padding:18px 0 48px}
.pf-g{display:flex;flex-wrap:wrap;gap:4px 18px}
.pf-g button{background:none;border:0;padding:4px 0;font-family:var(--serif);font-weight:300;font-size:20px;color:var(--ink-2);cursor:pointer;position:relative;transition:color .2s}
.pf-g button[aria-pressed=true]{color:var(--ink);font-style:italic}
.pf-g button[aria-pressed=true]::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:var(--ink)}
.pf-g+.pf-g{padding-left:40px;border-left:1px solid var(--line)}
.pf-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:56px 28px}
@media(min-width:1500px){.pf-grid{grid-template-columns:repeat(5,1fr)}}
.pf-grid .g .ph{aspect-ratio:4/5;background:#dfe2e6}
.pf-grid .g .ph img{filter:saturate(.92)}
.pf-st{position:absolute;z-index:1;top:12px;left:12px;font-size:9.5px;letter-spacing:.2em;text-transform:uppercase;font-weight:500;background:rgba(246,247,249,.94);padding:5px 9px;color:var(--ink)}
.pf-grid .gi{grid-template-columns:28px 1fr;gap:10px;margin-top:16px;padding-top:12px;border-top:1px solid var(--line)}
.pf-grid .gi h3{font-size:22px}
.pf-grid .gi p{font-size:12.5px}
@media(max-width:900px){.pf-grid{grid-template-columns:repeat(3,1fr)}}
@media(max-width:767px){.pf{padding:72px 0}.pf-grid{grid-template-columns:repeat(2,1fr);gap:36px 12px}.pf-grid .gi{grid-template-columns:1fr;gap:4px}.pf-grid .gi h3{font-size:18px}.pf-g+.pf-g{padding-left:0;border-left:0}.pf-g button{font-size:17px}.pf-f{gap:10px;padding-bottom:32px}}

.fx-x{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;padding:48px 0;border-bottom:1px solid var(--line)}
.fx-x h4,.fx-cta2 h4{font-family:var(--serif);font-weight:300;font-size:26px;line-height:1.15;margin:10px 0 10px}
.fx-x p{font-size:14.5px;line-height:1.6;color:var(--ink-2)}
.fx-x ul{list-style:none;margin-top:12px}.fx-x li{font-family:var(--serif);font-weight:300;font-size:20px;padding:8px 0;border-bottom:1px solid var(--line)}
.fx-map{padding:40px 0}.fx-map iframe{display:block;width:100%;height:360px;border:0;margin-top:14px;filter:grayscale(1) contrast(1.05)}
.fx-cta2{display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap;background:var(--ink);color:#F6F7F9;padding:36px 40px;margin-bottom:24px}
.fx-cta2 .eyebrow{color:rgba(246,247,249,.6)}.fx-cta2 h4{margin:8px 0 0;max-width:520px}
.fx-cta2 .btn.solid{background:#F6F7F9;color:var(--ink);border-color:#F6F7F9}
.sh-in .fx-l{display:inline-block;margin:0}
@media(max-width:900px){.fx-x{grid-template-columns:1fr;gap:28px}.fx-cta2{padding:28px 22px}.fx-map iframe{height:280px}}

.pf-ov{position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:flex-end;gap:8px;padding:22px;color:#F6F7F9;background:linear-gradient(180deg,rgba(18,17,16,.15),rgba(18,17,16,.72));opacity:0;transition:opacity .45s var(--ease)}
.pf-ov em{font-family:var(--serif);font-style:italic;font-weight:300;font-size:clamp(24px,2.2vw,34px);line-height:1.05;transform:translateY(10px);transition:transform .5s var(--ease)}
.pf-ov small{font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;opacity:.85}
.g:hover .pf-ov,.g:focus-visible .pf-ov{opacity:1}.g:hover .pf-ov em{transform:none}
.pf-grid .g .ph::after{display:none}


/* painel de filtros */
.pf-f{display:grid!important;grid-template-columns:auto 1.4fr 1.2fr;gap:0!important;margin:28px 0 48px;padding:0!important;background:var(--paper-2);border:1px solid var(--line)}
.pf-g{display:flex!important;flex-wrap:wrap;align-items:center;gap:6px!important;padding:18px 22px!important;border-left:1px solid var(--line)!important}
.pf-g:first-child{border-left:0!important}
.pf-lb{width:100%;font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:var(--ink-2);font-weight:500;margin-bottom:6px}
.pf-g button{font-family:var(--sans)!important;font-style:normal!important;font-size:11px!important;letter-spacing:.14em;text-transform:uppercase;font-weight:500;color:var(--ink)!important;padding:10px 14px!important;border:1px solid var(--line)!important;background:transparent;transition:background .2s,color .2s,border-color .2s}
.pf-g button::after{display:none!important}
.pf-g button:hover{border-color:var(--ink)!important}
.pf-g button[aria-pressed=true]{background:var(--ink)!important;color:var(--paper-2)!important;border-color:var(--ink)!important}
@media(max-width:900px){.pf-f{grid-template-columns:1fr}.pf-g{border-left:0!important;border-top:1px solid var(--line)}.pf-g:first-child{border-top:0}.pf-g{padding:14px 16px!important}}
/* selos por fase */
.pf-st{border:0}
.st-lancamento{background:#1A1817!important;color:#F6F7F9!important}
.st-em{background:#757E8D!important;color:#F6F7F9!important}
.st-pronto{background:#EADFCC!important;color:#3B342B!important}
.pf-ov{z-index:2!important}

/* ficha rica (landing) */
body:has(.lx-bar) .wa{bottom:92px}
.lx{position:relative;background:var(--paper-2)}
.lx-h{position:relative;height:min(78vh,760px);overflow:hidden;color:#F6F7F9;background:#1A1817}
.lx-h img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.lx-hs{position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,17,16,.1) 30%,rgba(18,17,16,.82))}
.lx-ht{position:absolute;left:0;right:0;bottom:0;padding:0 48px 44px}
.lx-st{display:inline-block;font-size:10px;letter-spacing:.2em;text-transform:uppercase;font-weight:500;padding:6px 11px;margin-bottom:18px}
.lx-ht h1,.lx-ht h2{font-family:var(--serif);font-weight:300;font-size:clamp(48px,7.5vw,120px);line-height:.92;letter-spacing:-.03em}
.lx-tg{font-family:var(--serif);font-style:italic;font-weight:300;font-size:clamp(22px,2.4vw,34px);margin-top:12px}
.lx-ad{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:rgba(246,247,249,.75);margin-top:18px}
.lx-s{padding:72px 48px;border-bottom:1px solid var(--line);display:grid;grid-template-columns:1fr 1.4fr;gap:56px;align-items:start}
.lx-intro{grid-template-columns:1.4fr 1fr}
.lx-c{font-family:var(--serif);font-weight:300;font-size:clamp(24px,2.4vw,34px);line-height:1.3}
.lx-sig{border-top:1px solid var(--ink)}.lx-sig div{display:flex;justify-content:space-between;gap:20px;padding:14px 0;border-bottom:1px solid var(--line)}
.lx-sig dt,.lx-tec dt{font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-2);font-weight:500}
.lx-sig dd{font-family:var(--serif);font-weight:300;font-size:20px}
.lx-num{display:grid;grid-template-columns:repeat(4,1fr);background:var(--ink);color:#F6F7F9}
.lx-num div{padding:44px 32px;border-left:1px solid rgba(246,247,249,.12)}.lx-num div:first-child{border-left:0}
.lx-num strong{display:block;font-family:var(--serif);font-weight:300;font-size:clamp(44px,5vw,72px);line-height:1;letter-spacing:-.02em}
.lx-num span{display:block;margin-top:12px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:rgba(246,247,249,.7)}
.lx-k h3{font-family:var(--serif);font-weight:300;font-size:clamp(32px,3.4vw,52px);line-height:1;letter-spacing:-.02em;margin:12px 0 14px}.lx-k h3 em{font-style:italic}
.lx-k p,.lx-k li{font-size:15px;line-height:1.6;color:var(--ink-2)}
.lx-k ul{list-style:none;margin-top:8px}.lx-k li{padding:10px 0;border-bottom:1px solid var(--line)}
.lx-t{width:100%;border-collapse:collapse;font-size:15px}
.lx-t th{text-align:left;font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-2);font-weight:500;padding:0 8px 12px 0;border-bottom:1px solid var(--ink)}
.lx-t td{padding:18px 8px 18px 0;border-bottom:1px solid var(--line)}.lx-t td:nth-child(2){font-family:var(--serif);font-size:24px;font-weight:300}
.lx-t a{font-size:11px;letter-spacing:.14em;text-transform:uppercase;white-space:nowrap;border-bottom:1px solid var(--line)}
.lx-dk{background:#232120;color:#F6F7F9;border-bottom:0}.lx-dk .eyebrow{color:rgba(246,247,249,.6)}
.lx-lz{list-style:none;display:grid;grid-template-columns:1fr 1fr;column-gap:32px}
.lx-lz li{font-family:var(--serif);font-weight:300;font-size:21px;padding:14px 0;border-bottom:1px solid rgba(246,247,249,.14)}
.lx-loc iframe{width:100%;height:420px;border:0;filter:grayscale(1) contrast(1.05)}
.lx-tec dl{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--ink)}
.lx-tec dl div{padding:16px 16px 16px 0;border-bottom:1px solid var(--line)}.lx-tec dd{font-family:var(--serif);font-weight:300;font-size:22px;margin-top:6px}
.lx-end{background:var(--slate);color:#F6F7F9;padding:80px 48px;text-align:center}
.lx-end .eyebrow{color:rgba(246,247,249,.75)}.lx-end h3{font-family:var(--serif);font-weight:300;font-size:clamp(32px,4vw,60px);line-height:1.02;margin:16px auto 32px;max-width:820px}.lx-end h3 em{font-style:italic}
.lx-bar{position:sticky;bottom:0;z-index:5;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:14px 48px;background:rgba(246,247,249,.94);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-top:1px solid var(--line)}
.lx-bar span{display:flex;flex-direction:column}.lx-bar strong{font-family:var(--serif);font-weight:300;font-size:22px}.lx-bar small{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-2)}
.sheet.rich .sh-in{padding:0}.sheet.rich .sh-x{position:sticky;top:12px;margin:12px 14px -58px auto;display:grid;float:none}
.sheet.rich .sh-grab{position:relative;z-index:2;margin-bottom:-14px;background:rgba(246,247,249,.6)}
@media(max-width:900px){.lx-ht{padding:0 20px 28px}.lx-s{grid-template-columns:1fr;gap:28px;padding:48px 20px}.lx-intro{grid-template-columns:1fr}.lx-num{grid-template-columns:1fr 1fr}.lx-num div{padding:28px 20px;border-top:1px solid rgba(246,247,249,.12)}.lx-lz{grid-template-columns:1fr}.lx-t th:nth-child(4),.lx-t td:nth-child(4){display:none}.lx-bar{padding:12px 16px}.lx-bar small{display:none}.lx-bar .btn{padding:12px 14px;font-size:10px}.lx-end{padding:56px 20px}.lx-loc iframe{height:300px}.lx-h{height:68vh}}

/* book editorial */
.bk-cover{position:relative;height:min(92vh,900px);overflow:hidden;background:#1A1817;color:#F6F7F9}
.bk-cover img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.bk-sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,17,16,.5) 0%,rgba(18,17,16,0) 25%,rgba(18,17,16,.1) 45%,rgba(18,17,16,.82) 100%)}
.bk-ct{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:space-between;padding:28px 56px 52px}
.bk-top{display:flex;justify-content:space-between;align-items:center;font-size:11px;letter-spacing:.2em;text-transform:uppercase;padding-right:60px}
.bk-ct h1,.bk-ct h2{font-family:var(--serif);font-weight:300;font-size:clamp(56px,10vw,168px);line-height:.88;letter-spacing:-.035em}
.bk-tg{font-family:var(--serif);font-style:italic;font-weight:300;font-size:clamp(22px,2.6vw,38px);margin-top:14px}
.bk-open{display:grid;grid-template-columns:1fr 2fr 1.2fr;gap:56px;padding:96px 56px;align-items:start}
.bk-meta{display:flex;flex-direction:column;gap:10px}
.bk-lead{font-family:var(--serif);font-weight:300;font-size:clamp(26px,2.7vw,40px);line-height:1.22;letter-spacing:-.01em}
.bk-sig div{padding:12px 0;border-bottom:1px solid var(--line)}.bk-sig div:first-child{border-top:1px solid var(--ink)}
.bk-sig dt{font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-2);font-weight:500}.bk-sig dd{font-family:var(--serif);font-weight:300;font-size:22px;margin-top:4px}
.bk-f{margin:0;position:relative}.bk-f img{width:100%;display:block;object-fit:cover;background:#dfe2e6}
.bk-f figcaption{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-2);padding:12px 0 0}
.bk-full img{aspect-ratio:16/8}.bk-full figcaption{padding:12px 56px 0}
.bk-full+.lx-num{margin-top:56px}
.bk-pair{display:grid;grid-template-columns:1.25fr 1fr;gap:20px;padding:96px 56px 40px;align-items:end}
.bk-pair .bk-f:first-child img{aspect-ratio:4/3}.bk-pair .bk-f:last-child img{aspect-ratio:3/4}
.bk-txt{padding:72px 56px;max-width:1180px}
.bk-txt h3,.bk-voo h3,.bk-loc h3{font-family:var(--serif);font-weight:300;font-size:clamp(34px,4.2vw,64px);line-height:1;letter-spacing:-.02em;margin:14px 0 36px}
.bk-txt h3 em,.bk-voo h3 em{font-style:italic}
.bk-voo{position:relative;height:min(86vh,820px);overflow:hidden;color:#F6F7F9}
.bk-voo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.bk-voo::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,17,16,0) 45%,rgba(18,17,16,.7))}
.bk-voo-t{position:absolute;left:56px;bottom:48px;z-index:1}.bk-voo .eyebrow{color:rgba(246,247,249,.75)}.bk-voo h3{margin-bottom:0}
.bk-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:40px 20px;padding:56px 56px 0}
.bk-grid .bk-f img{aspect-ratio:4/5}.bk-grid .bk-f:nth-child(3n+2){margin-top:72px}
.bk-list{list-style:none;columns:3;column-gap:40px}.bk-list li{font-family:var(--serif);font-weight:300;font-size:20px;padding:12px 0;border-bottom:1px solid var(--line);break-inside:avoid}
.bk-loc{display:grid;grid-template-columns:1fr 1.3fr;gap:56px;padding:96px 56px;align-items:start}
.bk-loc ul{list-style:none}.bk-loc li{font-size:15px;color:var(--ink-2);padding:12px 0;border-bottom:1px solid var(--line)}
.bk-loc iframe{width:100%;height:440px;border:0;filter:grayscale(1) contrast(1.05)}
.bk-tec dl{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--ink)}.bk-tec dl div{padding:16px 16px 16px 0;border-bottom:1px solid var(--line)}
.bk-tec dt{font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-2);font-weight:500}.bk-tec dd{font-family:var(--serif);font-weight:300;font-size:22px;margin-top:6px}
.bk-note{margin-top:20px;font-size:12px;color:var(--ink-2)}
.lx-t a{font-weight:500}
@media(max-width:900px){.bk-ct{padding:20px 20px 32px}.bk-top{padding-right:56px;font-size:10px}.bk-open{grid-template-columns:1fr;gap:28px;padding:56px 20px}.bk-full img{aspect-ratio:4/3}.bk-full figcaption{padding:10px 20px 0}
.bk-pair{grid-template-columns:1fr;padding:56px 20px 20px}.bk-pair .bk-f img{aspect-ratio:4/3!important}.bk-txt{padding:48px 20px}.bk-voo{height:64vh}.bk-voo-t{left:20px;bottom:28px}
.bk-grid{grid-template-columns:1fr 1fr;gap:24px 12px;padding:32px 20px 0}.bk-grid .bk-f:nth-child(3n+2){margin-top:0}.bk-grid .bk-f:nth-child(even){margin-top:40px}
.bk-list{columns:1}.bk-loc{grid-template-columns:1fr;padding:56px 20px;gap:28px}.bk-loc iframe{height:300px}.bk-tec dl{grid-template-columns:1fr 1fr}}

/* CTA fixo + motion */
.lx-bar{background:var(--ink)!important;color:#F6F7F9;border-top:0!important;padding:16px 56px!important}
.lx-bar-t{display:flex;flex-direction:column;gap:2px}.lx-bar-t small{color:rgba(246,247,249,.6)!important;display:block!important}
.lx-bar-t strong{font-family:var(--serif);font-weight:300;font-size:clamp(17px,1.8vw,24px)!important;line-height:1.2}.lx-bar-t em{font-style:italic}
.lx-go{white-space:nowrap;animation:pulse 2.8s var(--ease) infinite}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(246,247,249,.35)}50%{box-shadow:0 0 0 10px rgba(246,247,249,0)}}
.rv{opacity:0;transform:translateY(28px);transition:opacity .9s var(--ease),transform .9s var(--ease)}
.rv.in{opacity:1;transform:none}
.bk-cover img,.bk-full img,.bk-voo img{will-change:transform;transform:scale(1.14)}
.bk-full{overflow:hidden}
.back{display:inline-flex;gap:8px;font-size:11px;letter-spacing:.16em;text-transform:uppercase;border-bottom:1px solid var(--line);padding-bottom:2px}
@media(max-width:900px){.lx-bar{padding:12px 16px!important}.lx-bar-t small{display:none!important}.lx-bar-t strong{font-size:15px!important}}
@media(prefers-reduced-motion:reduce){.lx-go{animation:none}.bk-cover img,.bk-full img,.bk-voo img{transform:none}}

/* CTA: topo no desktop, base no celular */
@media(min-width:901px){
.lx{display:flex;flex-direction:column}
.lx-bar{order:-1;position:sticky!important;top:92px;bottom:auto!important;z-index:6}
.sheet .lx-bar{top:0}
.lx>.bk-cover{order:-2}
}
body:has(.lx) .wa,.sheet.rich~.wa{display:none}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}

/* v3 galeria Apple-like */
.pf{padding:112px 0 96px}
.pf-hd2{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;margin-bottom:28px}
.pf-hd2 h2{font-family:var(--serif);font-weight:300;font-size:clamp(40px,5vw,72px);line-height:.95;letter-spacing:-.03em;margin-top:10px}.pf-hd2 h2 em{font-style:italic}
.pf-n{font-size:13px;color:var(--ink-2);font-variant-numeric:tabular-nums;white-space:nowrap}
.pf-bar{position:sticky;top:72px;z-index:20;margin:0 -12px 40px;padding:10px 12px;background:rgba(246,247,249,.78);-webkit-backdrop-filter:saturate(180%) blur(18px);backdrop-filter:saturate(180%) blur(18px);border-radius:16px}
.pf-bar-in{display:flex;flex-wrap:wrap;gap:10px 12px;align-items:center}
.seg{display:inline-flex;gap:2px;padding:3px;border-radius:11px;background:rgba(26,24,23,.07)}
.seg button{border:0;background:transparent;font:500 13px/1 var(--sans);letter-spacing:-.01em;color:var(--ink-2);padding:9px 14px;border-radius:8px;cursor:pointer;white-space:nowrap;transition:background .25s cubic-bezier(.2,.8,.2,1),color .2s,box-shadow .25s}
.seg button:hover{color:var(--ink)}
.seg button[aria-pressed=true]{background:#fff;color:var(--ink);box-shadow:0 1px 2px rgba(0,0,0,.08),0 3px 10px rgba(0,0,0,.06)}
.seg button:active{transform:scale(.97)}
.pf-grid{gap:44px 24px}
.pf-grid .g .ph{border-radius:14px;aspect-ratio:4/5}
.pf-grid .g .ph img{will-change:transform;transition:filter .5s}
.pf-grid .gi{display:block;margin-top:14px;padding:0;border:0}
.pf-grid .gi h3{font-family:var(--serif);font-weight:300;font-size:22px;letter-spacing:-.015em;line-height:1.15}
.pf-grid .gi p{font:400 13px/1.4 var(--sans);color:var(--ink-2);margin-top:4px}
.pf-st{border-radius:999px;top:12px;left:12px;padding:6px 10px;font-size:9.5px;-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px)}
.pf-ov{border-radius:14px}
@media(max-width:767px){.pf-bar{top:60px;margin:0 -20px 28px;border-radius:0;padding:10px 20px;overflow-x:auto}.pf-bar-in{flex-wrap:nowrap}.seg button{padding:8px 11px;font-size:12.5px}.pf-grid{gap:28px 12px}.pf-grid .gi h3{font-size:17px}.pf-grid .gi p{font-size:12px}.pf-hd2{flex-direction:column;align-items:flex-start;gap:8px}}
/* contato compacto */
.cafe{padding:88px 0}
.cafe-g{gap:56px;align-items:center}
.cafe-l{margin:20px 0 24px}
.cafe-r{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:8px}
.cafe-r a{display:inline-block;font:500 13px/1 var(--sans);color:#F6F7F9;padding:10px 14px;border:1px solid rgba(246,247,249,.35);border-radius:999px;transition:background .25s,color .25s}
.cafe-r a:hover{background:#F6F7F9;color:var(--ink)}
.cafe-f{background:#F6F7F9!important;border:0!important;border-radius:18px;padding:28px!important;max-width:480px;justify-self:end;width:100%;box-shadow:0 20px 50px rgba(0,0,0,.18)}
.cafe-f label{color:var(--ink-2)!important;margin-top:16px;font-size:10.5px}
.cafe-f input,.cafe-f textarea,.cafe-f select{color:var(--ink)!important;border-bottom-color:var(--line)!important;padding:9px 0;font-size:15px}
.cafe-f small{color:var(--ink-2)!important}
.cafe-f .btn{margin-top:22px;background:var(--ink);color:#F6F7F9;border-color:var(--ink)}
.cafe-f .two label{margin-top:0}
@media(max-width:900px){.cafe-f{justify-self:stretch;max-width:none;padding:22px!important}.cafe{padding:64px 0}}
.terr video,.par-v video{will-change:transform}
.pf-bar{scrollbar-width:none}.pf-bar::-webkit-scrollbar{display:none}

/* vitrine */
.pf-feat{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);grid-template-rows:1fr 1fr;gap:20px;margin:0 0 56px;height:min(78vh,760px)}
.pf-feat .g{min-width:0;min-height:0}.pf-feat .g:first-child{grid-row:1/3}
.pf-feat .g .ph{aspect-ratio:auto;width:100%;position:relative;height:100%;border-radius:18px;overflow:hidden;background:#dfe2e6}
.pf-feat .g .ph>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.2,.8,.2,1)}
.pf-feat .g:hover .ph img{transform:scale(1.03)}
.vt-t{position:absolute;left:0;right:0;bottom:0;padding:28px;color:#F6F7F9;background:linear-gradient(transparent,rgba(18,17,16,.7));display:flex;flex-direction:column;gap:6px}
.vt-t small{font:500 10.5px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.85}
.vt-t strong{font-family:var(--serif);font-weight:300;font-size:clamp(26px,2.6vw,44px);line-height:1;letter-spacing:-.02em}
.vt-t em{font-family:var(--serif);font-style:italic;font-weight:300;font-size:16px;opacity:.9;max-width:40ch}
.pf-feat .g:not(:first-child) .vt-t em{display:none}
@media(max-width:767px){.pf-feat{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;height:auto;margin:0 -20px 36px;padding:0 20px;gap:12px;scrollbar-width:none}.pf-feat::-webkit-scrollbar{display:none}.pf-feat .g{flex:0 0 84%;scroll-snap-align:center}.pf-feat .g .ph{aspect-ratio:4/5;height:auto}.vt-t{padding:20px}}
/* swipe no card */
.sw{position:absolute;inset:0;display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;z-index:0}
.sw::-webkit-scrollbar{display:none}
.pf-grid .g .ph>img{position:relative;z-index:0}
.sw{pointer-events:none}
@media(hover:none){.sw{pointer-events:auto}}
.sw::before{content:"";flex:0 0 100%;scroll-snap-align:start}
.sw img{flex:0 0 100%;width:100%;height:100%;object-fit:cover;scroll-snap-align:start;background:#dfe2e6}
.sw-d{position:absolute;z-index:2;bottom:10px;left:0;right:0;display:flex;justify-content:center;gap:5px;pointer-events:none}
.sw-d i{width:5px;height:5px;border-radius:50%;background:rgba(255,255,255,.55)}.sw-d i.on{background:#fff}
@media(hover:hover){.g .ph:hover .sw-d{opacity:0}}

/* vitrine v2 — impacto */
.pf-feat{grid-template-columns:minmax(0,1fr) minmax(0,1fr)!important;grid-template-rows:auto auto!important;height:auto!important;gap:16px!important;margin:0 calc(50% - 50vw) 72px!important;padding:0 16px}
.pf-feat .g:first-child{grid-column:1/3;grid-row:1!important}
.pf-feat .g:first-child .ph{height:86vh!important;min-height:560px;border-radius:22px}
.pf-feat .g:not(:first-child) .ph{height:58vh!important;min-height:380px;border-radius:22px}
.pf-feat .g .ph>img{object-position:center 78%}
.pf-feat .g:first-child .vt-t{padding:56px 56px 52px;background:linear-gradient(transparent 40%,rgba(18,17,16,.78))}
.pf-feat .g:first-child .vt-t strong{font-size:clamp(48px,7vw,112px);line-height:.92;letter-spacing:-.035em}
.pf-feat .g:first-child .vt-t em{font-size:clamp(18px,1.6vw,24px);max-width:44ch}
.pf-feat .g:not(:first-child) .vt-t strong{font-size:clamp(30px,3vw,52px)}
.pf-feat .g:first-child .vt-t small::after{content:" · Ver ficha →";opacity:.8}
.pf-feat .vt-t small{display:block;margin-bottom:14px}
@media(max-width:767px){.pf-feat{margin:0 -20px 36px!important;padding:0 20px}.pf-feat .g .ph,.pf-feat .g:first-child .ph,.pf-feat .g:not(:first-child) .ph{height:auto!important;min-height:0;aspect-ratio:4/5!important}.pf-feat .g:first-child .vt-t{padding:22px}.pf-feat .g:first-child .vt-t strong{font-size:38px}}

/* contato prime: sem caixa branca */
.cafe-f{background:transparent!important;box-shadow:none!important;border-radius:0!important;padding:0!important;border-top:1px solid rgba(246,247,249,.35)!important;padding-top:28px!important}
.cafe-f label{color:rgba(246,247,249,.72)!important}
.cafe-f input,.cafe-f textarea,.cafe-f select{color:#fff!important;background:transparent!important;border:0!important;border-bottom:1px solid rgba(246,247,249,.45)!important;font-size:17px;caret-color:#fff}
.cafe-f input:focus,.cafe-f textarea:focus,.cafe-f select:focus{outline:0;border-bottom-color:#fff!important}
.cafe-f select option{color:#1A1817}
.cafe-f input:-webkit-autofill{-webkit-text-fill-color:#fff;transition:background-color 9999s}
.cafe-f .btn{background:#F6F7F9!important;color:#1A1817!important;border-color:#F6F7F9!important}
.cafe-f .btn:hover{background:transparent!important;color:#F6F7F9!important}
.cafe-f small,.cafe-f small a{color:rgba(246,247,249,.65)!important}

.ft-kco{padding-bottom:22px;text-align:center}.ft-kco a{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:rgba(246,247,249,.28);transition:color .3s}.ft-kco a:hover{color:rgba(246,247,249,.6)}
""".replace('__F__', FONTS)

ICON = {
 'tip': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 18V8m0 6h18v4M21 18v-4a3 3 0 0 0-3-3h-7v3"/><circle cx="7" cy="11" r="1.6"/></svg>',
 'met': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 20 20 4M7 17l-1.5-1.5M10 14l-1.5-1.5M13 11l-1.5-1.5M16 8l-1.5-1.5"/></svg>',
 'vag': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 16V11l2-5h10l2 5v5M5 16h14M5 16v2M19 16v2"/><circle cx="8" cy="13.5" r=".8"/><circle cx="16" cy="13.5" r=".8"/></svg>',
}
WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-3.3-.8-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.3 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.5.2.3.7 1.1 1.4 1.8 1 .9 1.8 1.1 2 1.2.3.1.4.1.6-.1l.8-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.4.2.5.3 0 .1 0 .7-.2 1.3Z"/></svg>'

def head(title, desc, path, extra=''):
    url = SITE + u(path)
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="noindex">
<meta name="referrer" content="no-referrer">
<meta property="og:type" content="website"><meta property="og:site_name" content="W3W Imóveis"><meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{OG}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="{FONTS}/ppeditorial-ultralight.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{FONTS}/ppneuemontreal-regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{BASE}/assets/site.css?v={VER}">
<link rel="icon" href="{BASE}/assets/favicon.svg" type="image/svg+xml">
{extra}</head><body>'''

def header(active=''):
    def a(p, t):
        cur = ' aria-current="page"' if active == p else ''
        return f'<a href="{u(p)}"{cur}>{t}</a>'
    return f'''<header class="hd"><div class="wrap">
<a class="brand" href="{BASE}/" aria-label="W3W Imóveis, página inicial">{LOGO}<span class="creci">{CRECI}</span></a>
<button class="burger" aria-label="Abrir menu" aria-expanded="false" onclick="var n=document.querySelector('.nav');var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o)"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 8h16M4 16h16"/></svg></button>
<nav class="nav" aria-label="Principal">
<a href="{BASE}/#imoveis">Imóveis</a><a href="{BASE}/#territorio">Território</a><a href="{BASE}/#socios">Sócios</a><a href="{BASE}/#parcerias">Parcerias</a>
<a class="btn" href="{BASE}/#contato">Fale com um consultor</a></nav></div></header>'''

def footer():
    return f"""<footer class="ft"><div class="wrap ft-t">
<a class="brand ft-b" href="{BASE}/">{LOGO}<span class="creci">{CRECI}</span></a>
<nav class="ft-n"><a href="{BASE}/#imoveis">Imóveis</a><a href="{u('moema')}">Moema</a><a href="{u('vila-nova-conceicao')}">Vila Nova Conceição</a><a href="{BASE}/#socios">Sócios</a><a href="{BASE}/#parcerias">Parcerias</a><a href="{u('politica-de-privacidade')}">Privacidade</a></nav>
<div class="ft-c"><a href="{wa('Olá, visitei o site da W3W e quero mais informações.')}" target="_blank" rel="noopener">{TEL}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
</div><div class="wrap ft-bot"><span>W3W Imóveis · Curadoria imobiliária · Desde 2004</span><span>{CRECI} · Moema, São Paulo</span></div><div class="wrap ft-kco"><a href="https://kcooyakawa.github.io/kco-studio/" target="_blank" rel="noopener">Produzido por KCO Studio</a></div></footer>
<a class="wa" href="{wa('Olá, visitei o site da W3W e quero mais informações.')}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">{WA_ICON}</a>
<script src="{BASE}/assets/motion.js?v={VER}" defer></script>
</body></html>"""

def card(e):
    tags = ''.join(f'<span class="tag">{t}</span>' for t in e['tipos'])
    r = e['resumo']
    lis = ''
    if r['tipologias']: lis += f'<li>{ICON["tip"]}{esc(r["tipologias"])}</li>'
    if r['metragem']: lis += f'<li>{ICON["met"]}{esc(r["metragem"])}</li>'
    if r['vagas']: lis += f'<li>{ICON["vag"]}{esc(r["vagas"])}</li>'
    return f'''<a class="card" href="{u('empreendimentos/'+e['slug'])}" data-tipos="{' '.join(e['tipos'])}" data-status="{e['status']}">
<div class="ph"><img src="{e['img']}" alt="Fachada do {esc(e['nome'])}, {esc(e['bairro'])}" loading="lazy" decoding="async"><span class="tag st">{e['status']}</span><div class="tags-b">{tags}</div></div>
<div class="bd"><span class="eyebrow">{esc(e['bairro'])} · SP</span><h3>{esc(e['nome'])}</h3><ul>{lis}</ul><span class="btn">Ver empreendimento</span></div></a>'''

def band():
    return f'''<section class="band"><div class="wrap"><h2>Atendimento pessoal, <em>do primeiro contato às chaves.</em></h2>
<a class="btn light" href="{wa('Olá, quero ajuda para encontrar um imóvel em Moema ou na Vila Nova Conceição.')}" target="_blank" rel="noopener">Falar com a W3W</a></div></section>'''

def write(path, content):
    p = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(content)

ORG = {"@context": "https://schema.org", "@type": "RealEstateAgent", "name": "W3W Imóveis",
       "url": SITE + BASE + '/', "telephone": TEL, "email": EMAIL, "image": OG,
       "areaServed": ["Moema, São Paulo", "Vila Nova Conceição, São Paulo"],
       "address": {"@type": "PostalAddress", "addressLocality": "São Paulo", "addressRegion": "SP", "addressCountry": "BR"},
       "identifier": CRECI}

VID = 'https://w3wlp.netlify.app/v'
CATS = [('', 'Todos'), ('studios', 'Studios'), ('apartamentos', 'Apartamentos'), ('alto-padrao', 'Alto padrão')]

def strip(e):
    f = e.get('ficha') or {}
    im = (f.get('img') or {})
    xs = [x[0] for x in (im.get('par') or [])] + [x[0] for x in (im.get('lazer') or [])]
    xs = [x for x in xs if x and x != e['img']][:3]
    if not xs: return ''
    return '<span class="sw">' + ''.join(f'<img src="{x}" alt="" loading="lazy" decoding="async">' for x in xs) + '</span><span class="sw-d">' + '<i></i>'*(len(xs)+1) + '</span>'

def gcard(e, i):
    r = e['resumo']
    return f"""<a class="g" href="{u('empreendimentos/'+e['slug'])}" data-slug="{e['slug']}" data-cat="{' '.join(e['categorias'])}" data-b="{e['bairro_slug']}" data-st="{e['status']}">
<div class="ph"><span class="pf-st st-{e['status'].split()[0].lower().replace('ç','c')}">{e['status']}</span><span class="pf-ov"><em>{esc(e['nome'])}</em><small>Ver ficha →</small></span><img src="{e['img']}" alt="{esc(e['nome'])}, {esc(e['bairro'])}" loading="lazy" decoding="async">{strip(e)}</div>
<div class="gi"><span class="n" hidden>{i:02d}</span><h3>{esc(e['nome'])}</h3><p>{esc(e['bairro'])} · {esc(r['metragem'])}</p></div></a>"""

STATUS = [('Lançamento', 'Lançamentos', 'Antes de todo mundo.'), ('Em obras', 'Em obras', 'Garanta na planta.'), ('Pronto', 'Prontos para morar', 'Chaves na mão.')]

def ficha_data():
    return [dict({k: e[k] for k in ('slug', 'nome', 'bairro', 'status', 'frase', 'img', 'resumo', 'categorias')}, bt=BAIRROS[e['bairro_slug']]['lead']) for e in E]

SHEET = r"""<div class="sheet" id="sheet" role="dialog" aria-modal="true" aria-labelledby="sh-t" hidden>
<div class="sh-bg" data-close></div><div class="sh-p" tabindex="-1"><div class="sh-grab" aria-hidden="true"></div>
<button class="sh-x" data-close aria-label="Fechar (Esc)"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M5 5l14 14M19 5L5 19"/></svg></button>
<div class="sh-in"></div></div></div>"""

def rich(e, h='h2'):
    f = e['ficha']; r = e['resumo']; I = f.get('img', {})
    msg = f"Olá, vi o {e['nome']} ({e['bairro']}) no site da W3W e quero receber a tabela e as plantas."
    q = urllib.parse.quote(f"{f.get('endereco', e['nome'])} São Paulo")
    st = e['status'].split()[0].lower().replace('ç', 'c')
    fig = lambda src, cap, cls='': f'<figure class="bk-f {cls}"><img src="{src}" alt="{esc(cap)}" loading="lazy" decoding="async"><figcaption>{esc(cap)}</figcaption></figure>'
    nome = e['nome']
    plantas = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td><a href="{wa(f"Olá, quero receber a planta de {b} ({a}) do {nome}.")}" target="_blank" rel="noopener">Receber planta</a></td></tr>' for a, b, c, d in f['plantas'])
    out = f"""<article class="lx bk">
<header class="bk-cover"><img src="{I.get('capa', e['img'])}" alt="{esc(nome)}"><div class="bk-sh"></div>
<div class="bk-ct"><div class="bk-top"><span>{esc(e['bairro'])} · São Paulo</span><span class="lx-st st-{st}">{e['status']}</span></div>
<{h} id="sh-t">{esc(nome)}</{h}><p class="bk-tg">{esc(f['tagline'])}</p></div></header>
<section class="bk-open"><div class="bk-meta"><span class="eyebrow">{esc(f['endereco'])}</span><span class="eyebrow">{esc(f['entrega']) if 'ronto' in f['entrega'] else 'Entrega ' + esc(f['entrega'])}</span></div>
<p class="bk-lead">{esc(f['conceito'])}</p>
<dl class="bk-sig">{''.join(f'<div><dt>{a}</dt><dd>{esc(b)}</dd></div>' for a, b in f['assinaturas'])}</dl></section>"""
    if I.get('fachada'): out += fig(I['fachada'], I.get('fachada_cap', 'Fachada · Perspectiva ilustrada'), 'bk-full')
    out += f"""<section class="lx-num">{''.join(f'<div><strong>{a}</strong><span>{esc(b)}</span></div>' for a, b in f['destaques'])}</section>"""
    if I.get('par'): out += '<section class="bk-pair">' + ''.join(fig(s2, c2) for s2, c2 in I['par']) + '</section>'
    out += f"""<section class="bk-txt"><span class="eyebrow">As plantas</span><h3>{esc(f.get('faixa', r['metragem']))}, <em>{esc(f.get('plantas_tit', 'tipo, garden e duplex.'))}</em></h3>
<table class="lx-t"><thead><tr><th>Tipologia</th><th>Área</th><th>Suítes</th><th>Vagas</th><th></th></tr></thead><tbody>{plantas}</tbody></table></section>"""
    if I.get('voo'): out += f'<section class="bk-voo"><img src="{I["voo"]}" alt="Lazer do {esc(nome)}" loading="lazy"><div class="bk-voo-t"><span class="eyebrow">O lazer</span><h3>Um clube <em>dentro de casa.</em></h3></div></section>'
    if I.get('lazer'): out += '<section class="bk-grid">' + ''.join(fig(s2, c2) for s2, c2 in I['lazer']) + '</section>'
    out += f'<section class="bk-txt bk-lz"><span class="eyebrow">Tudo o que o lazer oferece</span><ul class="bk-list">{"".join(f"<li>{esc(x)}</li>" for x in f["lazer"])}</ul></section>'
    if I.get('terraco'): out += fig(I['terraco'], I.get('terraco_cap', 'Terraço, duplex de 572 m²'), 'bk-full')
    out += f"""<section class="bk-loc"><div><span class="eyebrow">O endereço</span><h3>{esc(f['endereco'])}</h3><ul>{''.join(f'<li>{esc(x)}</li>' for x in f['local'])}</ul></div>
<iframe loading="lazy" title="Mapa {esc(nome)}" src="https://www.google.com/maps?q={q}&output=embed"></iframe></section>
<section class="bk-txt bk-tec"><span class="eyebrow">Ficha técnica</span><dl>{''.join(f'<div><dt>{a}</dt><dd>{esc(b)}</dd></div>' for a, b in f['tecnica'])}</dl>
<p class="bk-note">Imagens: perspectivas ilustradas fornecidas pela incorporadora. Informações sujeitas a alteração.</p></section>
<section class="lx-end"><span class="eyebrow">Tabela, plantas e condições</span><h3>Receba o material completo <em>do {esc(nome)}.</em></h3>
<a class="btn light solid-l" href="{wa(msg)}" target="_blank" rel="noopener">Receber no WhatsApp</a></section>
<div class="lx-bar"><span class="lx-bar-t"><small>{esc(nome)} · {e['status']}</small><strong>Book completo, tabela e plantas <em>no seu WhatsApp.</em></strong></span>
<a class="btn light solid-l lx-go" href="{wa("Olá, quero receber o book completo, a tabela e as plantas do " + nome + ".")}" target="_blank" rel="noopener">Quero receber <span aria-hidden="true">→</span></a></div></article>"""
    return out

def feat():
    fs = [e for e in E if e['bairro_slug']=='moema' and e['status']=='Lançamento' and e.get('ficha') and 'alto-padrao' in e['categorias']][:3]
    if len(fs) < 3: fs += [e for e in E if e.get('ficha') and e not in fs and 'alto-padrao' in e['categorias']][:3-len(fs)]
    cards = ''.join(f'<a class="g ft" href="{u("empreendimentos/"+e["slug"])}" data-slug="{e["slug"]}"><div class="ph"><img src="{e.get("vitrine") or e["img"]}" alt="{esc(e["nome"])}" loading="lazy" decoding="async"><span class="vt-t"><small>{e["status"]} · {esc(e["bairro"])}</small><strong>{esc(e["nome"])}</strong><em>{esc((e["ficha"].get("tagline") or ""))}</em></span></div></a>' for e in fs)
    return f'<div class="pf-feat">{cards}</div>'

def build_home():
    moema = [e for e in E if e['bairro_slug'] == 'moema']
    outros = [e for e in E if e['bairro_slug'] != 'moema']
    chips = ''.join(f'<button class="chip" data-v="{v}" aria-pressed="{"true" if v=="" else "false"}">{l}</button>' for v, l in CATS)
    rows = ''
    for st, tit, sub in STATUS:
        lst = [e for e in E if e['status'] == st]
        lst = sorted(lst, key=lambda e: (e['bairro_slug'] != 'moema', 'alto-padrao' not in e['categorias']))
        rows += f"""<div class="row-s" data-st="{st}"><div class="row-hd"><div><span class="eyebrow">{sub}</span><h3>{tit} <sup class="rc"></sup></h3></div>
<div class="arr"><button aria-label="Anterior" data-d="-1">←</button><button aria-label="Próximo" data-d="1">→</button></div></div>
<div class="track">{''.join(gcard(e, i+1) for i, e in enumerate(lst))}</div></div>"""
    pg = head('W3W Imóveis — Curadoria imobiliária em Moema',
              'Studios, apartamentos e imóveis de alto padrão em Moema, com curadoria da W3W Imóveis: mais de 20 anos de mercado e atendimento direto com os sócios.', '',
              f'<script type="application/ld+json">{json.dumps(ORG, ensure_ascii=False)}</script>')
    pg += header('').replace('class="hd"', 'class="hd over"')
    socio = lambda img, n, c, t: f'<div class="sc"><div class="sc-ph"><img src="https://w3wlp.netlify.app/img/{img}" alt="{n}" loading="lazy"></div><h3>{n}</h3><span class="eyebrow">{c}</span><p>{t}</p></div>'
    pg += f"""<main>
<section class="hlp" id="inicio"><div class="hlp-s" id="heroStick">
<video autoplay muted loop playsinline preload="auto" poster="{VID}/cidade.jpg"><source src="{VID}/cidade.mp4" type="video/mp4"></video><div class="hlp-sh"></div>
<div class="wrap hlp-m"><span>W3W Imóveis</span><span>Boutique de curadoria imobiliária</span><span>Moema · São Paulo</span><span>Desde 2004</span></div>
<div class="wrap hlp-t"><h1><span class="ht1">Curadoria</span><span class="ht2">imobiliária.</span></h1></div>
<div class="wrap hlp-l"><span class="cue"><i></i>Role</span><p>Selecionamos os melhores imóveis nos endereços mais desejados de São Paulo.</p></div>
</div></section>

<section class="pf" id="imoveis"><div class="wrap">
<div class="pf-hd2"><div><span class="eyebrow">Galeria W3W</span><h2>Imóveis <em>selecionados.</em></h2></div><span class="pf-n"></span></div>
<div class="pf-bar"><div class="pf-bar-in"><div class="seg" data-k="b" role="group"><button data-v="moema" aria-pressed="true">Moema</button><button data-v="outros" aria-pressed="false">Outras regiões</button></div>{''.join(['<div class="seg" data-k="c" role="group">']+[f'<button data-v="{v}" aria-pressed="{"true" if v=="" else "false"}">{l}</button>' for v,l in CATS]+['</div>'])}<div class="seg" data-k="s" role="group"><button data-v="" aria-pressed="true">Todas</button><button data-v="Lançamento" aria-pressed="false">Lançamento</button><button data-v="Em obras" aria-pressed="false">Em obras</button><button data-v="Pronto" aria-pressed="false">Pronto</button></div></div></div>
{feat()}<div class="pf-grid">{''.join(gcard(e, i+1) for i, e in enumerate(sorted(E, key=lambda e: (e['bairro_slug']!='moema', ['Lançamento','Em obras','Pronto'].index(e['status']), 'alto-padrao' not in e['categorias']))))}</div>
<div class="more"><button class="btn" id="more">Ver mais imóveis</button></div>
</div></section>

<section class="terr" id="territorio"><video data-px=".18" autoplay muted loop playsinline preload="none" poster="{VID}/territorio.jpg"><source src="{VID}/territorio.mp4" type="video/mp4"></video>
<div class="wrap terr-in"><span class="eyebrow">Território</span><h2>Nossa casa é <em>Moema.</em></h2>
<p>A W3W nasceu e trabalha em Moema. Conhecemos cada rua, cada lançamento e cada mudança do bairro. Quando a oportunidade certa está ao lado, também acompanhamos de perto Vila Nova Conceição, Itaim Bibi, Brooklin e Paraíso.</p>
<div class="terr-b"><a href="{u('moema')}"><strong>Moema</strong><span>{len(moema)} empreendimentos</span></a>
<a href="{u('vila-nova-conceicao')}"><strong>Vila Nova Conceição</strong><span>{len(outros)} empreendimentos</span></a>
<a href="#contato"><strong>Itaim · Brooklin · Paraíso</strong><span>Sob consulta</span></a></div></div></section>

<section class="socx" id="socios"><div class="wrap">
<div class="g-hd dk"><div><span class="eyebrow">Os sócios</span><h2>Quem decide, <em>atende.</em></h2></div><p>Três sócios à frente de cada negócio, da primeira conversa ao pós-venda.</p></div>
<div class="scs">{socio('socio-wilson.jpg','Wilson Rodrigues','Fundador · Diretor · CRECI 69.228','No mercado imobiliário desde 2004, conduz a W3W e a relação com incorporadoras.')}
{socio('socio-yoko.jpg','Yoko Rodrigues','Sócia · CRECI 42.877','Cuida do relacionamento com clientes investidores e dá suporte a cada negociação.')}
{socio('socio-kco.jpg','Kco Oyakawa','Sócio · Comunicação','Head of Art, com trabalhos para FIFA™, Jogos Olímpicos 2016, Coca-Cola e Itaú.')}</div></div></section>

<section class="par" id="parcerias"><div class="par-v"><video data-px=".14" autoplay muted loop playsinline preload="none" poster="{VID}/torre.jpg"><source src="{VID}/torre.mp4" type="video/mp4"></video></div>
<div class="par-c"><span class="eyebrow">Modelos de parceria</span><h2>Para quem constrói <em>o mercado.</em></h2>
<div class="mods"><div><span class="n">01</span><div><h3>Incorporadoras e construtoras</h3><p>Parceria de lançamento e venda, com inteligência de mercado, marketing e força comercial dedicada.</p></div></div>
<div><span class="n">02</span><div><h3>Imobiliárias</h3><p>Co-corretagem com regras claras, acesso ao portfólio curado e materiais de apresentação de alto padrão.</p></div></div>
<div><span class="n">03</span><div><h3>Corretores</h3><p>Estrutura, empreendimentos qualificados, suporte de marketing e uma marca que abre portas no alto padrão.</p></div></div></div>
<a class="btn light" href="{wa('Olá, quero conversar sobre uma parceria com a W3W.')}" target="_blank" rel="noopener">Propor uma parceria</a></div></section>

<section class="cafe" id="contato"><div class="wrap cafe-g">
<div><span class="eyebrow">Contato</span><h2>Vamos tomar <em>um café?</em></h2>
<p class="cafe-l">Conte o que você procura. Um consultor da W3W responde pessoalmente.</p>
<ul class="cafe-r"><li><a href="{wa('Olá, quero falar com um consultor da W3W.')}" target="_blank" rel="noopener">WhatsApp</a></li><li><a href="mailto:{EMAIL}">E-mail</a></li><li><a href="https://instagram.com/w3wimoveis" target="_blank" rel="noopener">Instagram</a></li><li><a href="https://maps.google.com/?q=Moema+São+Paulo" target="_blank" rel="noopener">Moema · SP</a></li></ul></div>
<form class="form cafe-f" name="contato" method="POST" data-netlify="true" netlify-honeypot="empresa" onsubmit="event.preventDefault();var d=new FormData(this);var m='Olá, sou '+d.get('nome')+' ('+(d.get('perfil')||'')+'). '+(d.get('mensagem')||'');window.open('https://wa.me/{WA}?text='+encodeURIComponent(m),'_blank')">
<input type="hidden" name="form-name" value="contato"><p hidden><input name="empresa"></p>
<div class="two"><div><label for="f-nome">Nome</label><input id="f-nome" name="nome" required autocomplete="name"></div><div><label for="f-tel">WhatsApp ou e-mail</label><input id="f-tel" name="contato" required></div></div>
<label for="f-p">Você é</label><select id="f-p" name="perfil"><option>Comprador ou investidor</option><option>Incorporadora ou construtora</option><option>Imobiliária</option><option>Corretor</option></select>
<label for="f-msg">Mensagem</label><textarea id="f-msg" name="mensagem" rows="2"></textarea>
<button class="btn" type="submit">Enviar mensagem →</button>
<small>Ao enviar, você concorda com a nossa <a href="{u('politica-de-privacidade')}">Política de Privacidade</a>.</small></form>
</div></section></main>
{SHEET}
{''.join(f'<template id="fx-{e[chr(115)+chr(108)+chr(117)+chr(103)]}">'+rich(e)+'</template>' for e in E if e.get('ficha'))}
<script>window.W3W={json.dumps(ficha_data(), ensure_ascii=False)};window.W3W_WA='{WA}';window.W3W_BASE='{BASE}';</script>
<script src="{BASE}/assets/sheet.js?v={VER}" defer></script>
<script>(function(){{var st={{b:'moema',c:'',s:''}},lim=9999,all=[].slice.call(document.querySelectorAll('.pf-grid .g')),more=document.getElementById('more'),num=document.querySelector('.pf-n');
function ap(){{var v=all.filter(function(g){{return (st.b==='moema'?g.dataset.b==='moema':g.dataset.b!=='moema')&&(!st.c||g.dataset.cat.split(' ').indexOf(st.c)>-1)&&(!st.s||g.dataset.st===st.s)}});all.forEach(function(g){{g.hidden=true}});v.forEach(function(g,i){{g.hidden=i>=lim;g.querySelector('.n').textContent=String(i+1).padStart(2,'0')}});num.textContent=v.length+(v.length===1?' imóvel':' imóveis');more.parentNode.hidden=v.length<=lim}}
document.querySelectorAll('.pf-bar .seg').forEach(function(gr){{gr.querySelectorAll('button').forEach(function(b){{b.onclick=function(){{gr.querySelectorAll('button').forEach(function(x){{x.setAttribute('aria-pressed','false')}});b.setAttribute('aria-pressed','true');st[gr.dataset.k]=b.dataset.v;ap()}}}})}});
more.onclick=function(){{lim+=16;ap()}};ap();
var h=document.querySelector('.hd.over');function sc(){{h.classList.toggle('solid',scrollY>window.innerHeight*.6)}}addEventListener('scroll',sc,{{passive:true}});sc();
document.querySelectorAll('.sw').forEach(function(w){{var d=w.nextElementSibling.children;d[0].classList.add('on');w.addEventListener('scroll',function(){{var k=Math.round(w.scrollLeft/w.clientWidth);[].forEach.call(d,function(x,j){{x.classList.toggle('on',j===k)}})}},{{passive:true}})}});
if(!matchMedia('(prefers-reduced-motion: reduce)').matches){{var px=[].slice.call(document.querySelectorAll('[data-px],.pf-grid .g .ph>img,.sc-ph img'));var tk=0;function run(){{tk=0;var H=innerHeight;px.forEach(function(el){{var r=el.parentNode.getBoundingClientRect();if(r.bottom<0||r.top>H)return;var k=parseFloat(el.dataset.px||.06);var d=((r.top+r.height/2)-H/2)*k;el.style.transform='translate3d(0,'+d.toFixed(1)+'px,0) scale('+(1+k*1.4).toFixed(3)+')'}})}}addEventListener('scroll',function(){{if(!tk)tk=requestAnimationFrame(run)}},{{passive:true}});run()}}
}})();</script>"""
    pg += footer()
    write('index.html', pg)

def build():
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    write('assets/site.css', CSS)
    write('assets/motion.js', open(os.path.join(ROOT,'motion.js'),encoding='utf-8').read())
    write('assets/sheet.js', open(os.path.join(ROOT,'sheet.js'),encoding='utf-8').read())
    write('assets/favicon.svg', LOGO.replace('currentColor', '#1A1817'))
    filt_js = '''<script>
(function(){var st={tipo:'',status:''};var cards=[].slice.call(document.querySelectorAll('.card'));var cnt=document.querySelector('.count');
function apply(){var n=0;cards.forEach(function(c){var ok=(!st.tipo||c.dataset.tipos.indexOf(st.tipo)>-1)&&(!st.status||c.dataset.status===st.status);c.hidden=!ok;if(ok)n++});cnt.textContent=n+(n===1?' empreendimento':' empreendimentos')}
document.querySelectorAll('.chip').forEach(function(b){b.addEventListener('click',function(){var g=b.dataset.g;document.querySelectorAll('.chip[data-g='+g+']').forEach(function(x){x.setAttribute('aria-pressed','false')});b.setAttribute('aria-pressed','true');st[g]=b.dataset.v;apply()})});apply()})();
</script>'''

    build_home()


    # BAIRROS
    for slug, b in BAIRROS.items():
        lst = [e for e in E if e['bairro_slug'] == slug]
        chips = lambda g, vals: ''.join(f'<button class="chip" data-g="{g}" data-v="{v}" aria-pressed="{"true" if v=="" else "false"}">{lab}</button>' for v, lab in vals)
        bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + BASE + '/'},
            {"@type": "ListItem", "position": 2, "name": b['nome'], "item": SITE + u(slug)}]}
        pg = head(f"{b['titulo']} | W3W Imóveis", b['desc'], slug, f'<script type="application/ld+json">{json.dumps(bc, ensure_ascii=False)}</script>')
        pg += header(slug)
        pg += f'''<main><section class="pg-hd"><div class="wrap"><div class="crumbs"><a href="{BASE}/">Home</a> / {b['nome']}</div>
<h1>{b['titulo']}</h1><p>{b['lead']}</p></div></section>
<section class="sec" style="padding-top:24px"><div class="wrap">
<div class="filters"><div class="fg"><span class="eyebrow">Tipo</span><div class="chips">{chips('tipo', [('', 'Todos'), ('Apartamento', 'Apartamentos'), ('Studio', 'Studios')])}</div></div>
<div class="fg"><span class="eyebrow">Status</span><div class="chips">{chips('status', [('', 'Todos'), ('Lançamento', 'Lançamento'), ('Em obras', 'Em obras'), ('Pronto', 'Pronto')])}</div></div></div>
<p class="count"></p><div class="grid">{''.join(card(e) for e in lst)}</div></div></section>{band()}</main>'''
        pg += f'''<script>(function(){{var t=new URLSearchParams(location.search).get('tipo');if(t){{var b=document.querySelector('.chip[data-g=tipo][data-v="'+t+'"]');if(b)setTimeout(function(){{b.click()}},0)}}}})();</script>''' + filt_js
        pg += footer()
        write(f'{slug}/index.html', pg)

    # EMPREENDIMENTOS
    for e in E:
        r = e['resumo']
        b = BAIRROS[e['bairro_slug']]
        desc = f"{e['nome']} em {e['bairro']}, São Paulo: {r['tipologias']}, {r['metragem']}. {e['status']}. Atendimento personalizado W3W Imóveis."
        rows = [('Tipologias', r['tipologias']), ('Metragem', r['metragem'])] + ([('Vagas', r['vagas'])] if r['vagas'] else []) + [('Bairro', f"{e['bairro']}, São Paulo")]
        ficha = ''.join(f'<div><dt>{k}</dt><dd>{esc(v)}</dd></div>' for k, v in rows)
        msg = f"Olá, vi o {e['nome']} ({e['bairro']}) no site da W3W e quero mais informações."
        ld = {"@context": "https://schema.org", "@type": "Residence", "name": e['nome'], "image": e['img'], "description": desc,
              "address": {"@type": "PostalAddress", "addressLocality": "São Paulo", "addressRegion": "SP", "addressCountry": "BR", "streetAddress": e['bairro']}}
        bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + BASE + '/'},
            {"@type": "ListItem", "position": 2, "name": b['nome'], "item": SITE + u(e['bairro_slug'])},
            {"@type": "ListItem", "position": 3, "name": e['nome'], "item": SITE + u('empreendimentos/' + e['slug'])}]}
        rel = [x for x in E if x['bairro_slug'] == e['bairro_slug'] and x['slug'] != e['slug']][:3]
        pg = head(f"{e['nome']} — {r['tipologias']} em {e['bairro']} | W3W Imóveis", desc, 'empreendimentos/' + e['slug'],
                  f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(bc, ensure_ascii=False)}</script>')
        pg += header(e['bairro_slug'])
        pg += f'''<main><section class="pg-hd" style="padding-bottom:0"><div class="wrap"><div class="crumbs"><a class="back" href="{BASE}/#imoveis">← Voltar à galeria</a></div></div></section>
''' + (rich(e,'h1') if e.get('ficha') else f'''<section class="sec fxp" style="padding-top:8px"><div class="wrap">
<div class="fx-ph"><img src="{e['img']}" alt="Fachada do {esc(e['nome'])}, {esc(e['bairro'])}" decoding="async"><span class="tag st">{e['status']}</span></div>
<div class="fx-b"><div class="fx-t"><span class="eyebrow">{esc(e['bairro'])} · {e['status']}</span><h1>{esc(e['nome'])}</h1>{f'<p class="fx-q">{esc(e["frase"])}</p>' if e['frase'] else ''}</div>
<dl class="fx-s">{ficha}</dl></div>
<div class="fx-c"><a class="btn solid" href="{wa(msg)}" target="_blank" rel="noopener">Quero a ficha completa</a><a class="btn" href="{wa('Olá, quero agendar uma visita ao ' + e['nome'] + '.')}" target="_blank" rel="noopener">Agendar visita</a></div>
<p class="fx-n">Plantas, lazer, incorporadora e previsão de entrega: fale com um consultor.</p></div></section>
''') + f'''<section class="sec" style="padding-top:0"><div class="wrap"><div class="sec-hd"><h2>Também em {e['bairro']}</h2><a href="{u(e['bairro_slug'])}">Ver todos</a></div>
<div class="grid">{''.join(card(x) for x in rel)}</div></div></section>{band()}</main>'''
        pg += footer()
        write(f"empreendimentos/{e['slug']}/index.html", pg)

    # QUEM SOMOS
    pg = head('Quem somos | W3W Imóveis', 'A W3W Imóveis é uma imobiliária boutique com mais de 20 anos de experiência no mercado imobiliário de alto padrão em Moema e Vila Nova Conceição.', 'quem-somos')
    pg += header('quem-somos')
    pg += f'''<main><section class="pg-hd"><div class="wrap"><div class="crumbs"><a href="{BASE}/">Home</a> / Quem somos</div><h1>Quem somos</h1></div></section>
<section class="sec qs" style="padding-top:16px"><div class="wrap">
<p>Nossa trajetória de mais de 20 anos de experiência no mercado imobiliário nos permitiu construir uma rede sólida de relacionamentos e adquirir um profundo conhecimento das dinâmicas deste setor.</p>
<p>Nosso foco é proporcionar agilidade e eficiência nas negociações, aproveitando nossa expertise para identificar as melhores oportunidades de negócios para nossos clientes. Oferecemos serviços que priorizam a confiança e a satisfação.</p>
<div class="team"><div class="c"><h4>Wilson Rodrigues</h4><p>Sócio-diretor · CRECI 69.228</p></div><div class="c"><h4>Marli Oyakawa (Yoko)</h4><p>Sócia · CRECI 42.877</p></div></div>
</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="sec-hd"><h2>Missão, Visão e Valores</h2></div><div class="mvv">
<div class="c"><h3>Missão</h3><p>Entender as necessidades dos nossos clientes para apresentar oportunidades de negócios personalizadas que superem suas expectativas, proporcionando decisões informadas e seguras.</p></div>
<div class="c"><h3>Visão</h3><p>Ser reconhecida como uma empresa que torna o processo de compra e venda de imóveis uma experiência gratificante e memorável.</p></div>
<div class="c full"><h3>Valores</h3><ul><li>Clareza e Honestidade: mantemos uma comunicação transparente em todas as etapas do nosso processo de atendimento, construindo relacionamentos de confiança.</li><li>Foco na Satisfação do Cliente: buscamos maneiras de exceder suas expectativas.</li><li>Ética em Nossos Relacionamentos: agimos com integridade, respeitando todos os envolvidos nas negociações.</li><li>Respeito às Diferenças Sociais: tratamos clientes e parceiros com dignidade.</li></ul></div>
</div></div></section>{band()}</main>'''
    pg += footer()
    write('quem-somos/index.html', pg)

    # CONTATO
    pg = head('Contato | W3W Imóveis', 'Fale com a W3W Imóveis pelo WhatsApp, e-mail ou formulário. Atendimento personalizado para imóveis em Moema e Vila Nova Conceição.', 'contato')
    pg += header('contato')
    opts = ''.join(f'<option>{esc(e["nome"])}</option>' for e in sorted(E, key=lambda x: x['nome']))
    pg += f'''<main><section class="pg-hd"><div class="wrap"><div class="crumbs"><a href="{BASE}/">Home</a> / Contato</div><h1>Fale conosco</h1>
<p>Conte o que você procura e respondemos pessoalmente, pelo canal que preferir.</p></div></section>
<section class="sec" style="padding-top:16px"><div class="wrap ct">
<form class="form" name="contato" method="POST" data-netlify="true" netlify-honeypot="empresa" onsubmit="if(!this.hasAttribute('data-live')){{event.preventDefault();var d=new FormData(this);var m='Olá, sou '+d.get('nome')+'. '+(d.get('interesse')?'Interesse: '+d.get('interesse')+'. ':'')+(d.get('mensagem')||'');window.open('https://wa.me/{WA}?text='+encodeURIComponent(m),'_blank')}}">
<input type="hidden" name="form-name" value="contato"><p hidden><input name="empresa"></p>
<label for="f-nome">Nome</label><input id="f-nome" name="nome" required autocomplete="name">
<label for="f-tel">WhatsApp</label><input id="f-tel" name="telefone" type="tel" required autocomplete="tel">
<label for="f-mail">E-mail</label><input id="f-mail" name="email" type="email" autocomplete="email">
<label for="f-int">Interesse</label><select id="f-int" name="interesse"><option value="">Selecione (opcional)</option><option>Apartamento em Moema</option><option>Studio em Moema</option><option>Apartamento na Vila Nova Conceição</option><option>Investimento</option>{opts}</select>
<label for="f-msg">Mensagem</label><textarea id="f-msg" name="mensagem" rows="4"></textarea>
<button class="btn solid" type="submit">Enviar</button>
<small>Ao enviar, você concorda com a nossa <a href="{u('politica-de-privacidade')}" style="border-bottom:1px solid">Política de Privacidade</a>.</small></form>
<dl class="info"><dt>WhatsApp</dt><dd><a href="{wa('Olá, visitei o site da W3W e quero mais informações.')}" target="_blank" rel="noopener">{TEL}</a></dd>
<dt>E-mail</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd><dt>Atendimento</dt><dd>Moema · São Paulo</dd><dt>Registro</dt><dd>{CRECI}</dd></dl>
</div></section></main>'''
    pg += footer()
    write('contato/index.html', pg)

    # PRIVACIDADE (resumo provisório)
    pg = head('Política de Privacidade | W3W Imóveis', 'Política de Privacidade e LGPD da W3W Imóveis.', 'politica-de-privacidade')
    pg += header('')
    pg += f'''<main><section class="pg-hd"><div class="wrap"><div class="crumbs"><a href="{BASE}/">Home</a> / Política de Privacidade</div><h1>Política de Privacidade</h1>
<p>Esta página receberá o texto completo da Política de Privacidade / LGPD do site atual na migração. Para dúvidas sobre seus dados, fale conosco pelo e-mail {EMAIL} ou pelo telefone {TEL}.</p></div></section></main>'''
    pg += footer()
    write('politica-de-privacidade/index.html', pg)

    write('robots.txt', 'User-agent: *\nDisallow: /\n')
    print('ok', len(E), 'empreendimentos')

if __name__ == '__main__':
    build()
