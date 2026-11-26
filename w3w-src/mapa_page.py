"""Mapa de Moema — página do mapa interativo, com estilo cartográfico próprio. Chamado por build.py."""

CATS = [
    ('restaurantes', 'Restaurantes', '#C2553D'), ('pizzarias', 'Pizzarias', '#D9822B'), ('churrascarias', 'Churrascarias', '#8E3B2E'),
    ('japoneses', 'Japoneses', '#B23A48'), ('hamburguerias', 'Hamburguerias', '#C9733A'), ('bares', 'Bares', '#7A4FB5'),
    ('noite', 'Vida noturna', '#4B3BA8'), ('cafes', 'Cafés', '#8A6A4F'), ('docerias', 'Docerias', '#D46A9A'), ('sorveterias', 'Sorveterias', '#4FA3C7'),
    ('padarias', 'Padarias', '#B8893A'), ('mercados', 'Mercados', '#5D7F8C'), ('floriculturas', 'Floriculturas', '#C25C8A'), ('lojas', 'Lojas', '#7D6B5A'),
    ('pet', 'Pet e veterinário', '#C08A2E'), ('lavanderias', 'Lavanderias', '#4D8FB0'), ('chaveiros', 'Chaveiros', '#6B6F78'), ('costureiras', 'Costureiras', '#9C5E7A'), ('bancos', 'Bancos', '#3E5C7A'),
    ('cabeleireiros', 'Cabeleireiros', '#B0607E'), ('estetica', 'Manicure e estética', '#D27FA0'),
    ('farmacias', 'Farmácias', '#2F8F83'), ('saude', 'Saúde', '#2F6FD0'),
    ('concessionarias', 'Concessionárias', '#2E3A4F'), ('oficinas', 'Oficinas', '#5A4A3A'), ('lavarapido', 'Lava-rápido', '#3F8FC0'), ('postos', 'Postos', '#5C677A'),
    ('escolas', 'Escolas', '#5B6CC2'), ('faculdades', 'Faculdades', '#3D4FA8'),
    ('parques', 'Parques', '#3F7F6A'), ('cultura', 'Cultura', '#3D5A99'), ('academias', 'Academias', '#6B7A3A'), ('hoteis', 'Hotéis', '#9A7B4F'),
]

GRUPOS = [
    ('gastronomia', 'Gastronomia', ['restaurantes', 'pizzarias', 'churrascarias', 'japoneses', 'hamburguerias', 'cafes', 'docerias', 'sorveterias', 'padarias', 'bares', 'noite']),
    ('servicos', 'Serviços', ['pet', 'lavanderias', 'chaveiros', 'costureiras', 'bancos', 'lavarapido', 'oficinas']),
    ('beleza', 'Beleza', ['cabeleireiros', 'estetica']),
    ('compras', 'Compras', ['mercados', 'floriculturas', 'lojas']),
    ('saude', 'Saúde', ['farmacias', 'saude']),
    ('carro', 'Carro', ['concessionarias', 'oficinas', 'lavarapido', 'postos']),
    ('educacao', 'Educação', ['escolas', 'faculdades']),
    ('lazer', 'Lazer e cultura', ['parques', 'cultura', 'academias', 'hoteis']),
]

CSS = r"""
<style>
body:has(.mp){background:#EEEBE5;overflow:hidden}
body:has(.mp) .hd,body:has(.mp) .ft{display:none!important}
.mp-logo{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;color:var(--tx);text-decoration:none}
.mp-logo svg{height:30px;width:auto}
.mp-logo a{color:var(--tx);display:flex}.mp-logo nav{display:flex;gap:6px}.mp-logo nav a{font:500 10.5px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--tx2);padding:7px 10px;border-radius:999px;background:rgba(14,17,22,.05);text-decoration:none}.mp-logo nav a:hover{color:var(--ac)}
.mp{height:100svh!important;--bg:#EEEBE5;--tx:#14171C;--tx2:#4F5662;--tx3:#8C93A0;--ln:rgba(20,23,28,.1);--ac:#2F6FD0;--ok:#1E9E6A;--mono:ui-monospace,'SF Mono',Menlo,monospace;--e:cubic-bezier(.16,1,.3,1);position:relative;height:calc(100svh - var(--hdh,96px));min-height:560px;overflow:hidden;color:var(--tx)}
#mpMap{position:absolute;inset:0;background:#EEEBE5}
.mp-glass{background:linear-gradient(135deg,rgba(255,255,255,.78),rgba(255,255,255,.52));backdrop-filter:blur(22px) saturate(1.7);-webkit-backdrop-filter:blur(22px) saturate(1.7);box-shadow:inset 0 1.5px 0 #fff,inset 0 0 0 1px rgba(20,23,28,.07),0 30px 60px -30px rgba(20,23,28,.45)}
.mp-panel{position:absolute;left:20px;top:20px;bottom:20px;width:380px;border-radius:26px;display:flex;flex-direction:column;overflow:hidden;z-index:3;animation:mpin .9s var(--e) both}
@keyframes mpin{from{opacity:0;transform:translateX(-24px)}}
.mp-hd{padding:24px 24px 14px}
.mp-hd .ey{font:500 10.5px var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--ac)}
.mp-hd h1{font:300 40px/.95 var(--sans);letter-spacing:-.045em;margin:10px 0 0}
.mp-hd h1 em{font-family:var(--serif);font-style:italic;font-weight:200;color:var(--ac)}
.mp-hd p{margin:10px 0 0;font:13px/1.45 var(--sans);color:var(--tx2)}
.mp-search{margin:6px 24px 0;position:relative}
.mp-search input{width:100%;height:46px;border-radius:999px;border:0;padding:0 18px 0 42px;font:15px var(--sans);color:var(--tx);background:rgba(255,255,255,.75);box-shadow:inset 0 0 0 1px var(--ln);outline:none;transition:box-shadow .3s}
.mp-search input:focus{box-shadow:inset 0 0 0 1.5px var(--ac)}
.mp-search svg{position:absolute;left:16px;top:15px;width:16px;height:16px;color:var(--tx3)}
.mp-tg{display:flex;gap:8px;padding:14px 24px 0}
.mp-tg button{flex:1;height:40px;border-radius:999px;border:0;font:500 13px var(--sans);color:var(--tx2);background:rgba(255,255,255,.55);box-shadow:inset 0 0 0 1px var(--ln);cursor:pointer;display:inline-flex;align-items:center;justify-content:center;gap:8px;transition:all .3s var(--e)}
.mp-tg button i{width:7px;height:7px;border-radius:50%;background:var(--ok)}
.mp-tg button[aria-pressed=true]{color:#fff;background:linear-gradient(135deg,#2F6FD0,#1E4E9E);box-shadow:inset 0 1px 0 rgba(255,255,255,.5),0 10px 22px -10px rgba(47,111,208,.7)}
.mp-tg button[aria-pressed=true] i{background:#7BE0B3;box-shadow:0 0 0 4px rgba(123,224,179,.25)}
.mp-grp{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;padding:14px 24px 0}
.mp-grp button{height:58px;border:0;border-radius:16px;background:rgba(255,255,255,.55);box-shadow:inset 0 0 0 1px var(--ln);font:500 11.5px/1.2 var(--sans);color:var(--tx2);cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;transition:all .3s var(--e);padding:4px}
.mp-grp button svg{width:18px;height:18px}
.mp-grp button[aria-pressed=true]{background:linear-gradient(135deg,#2F6FD0,#1E4E9E);color:#fff;box-shadow:inset 0 1px 0 rgba(255,255,255,.45),0 10px 22px -10px rgba(47,111,208,.7)}
.mp-chips{display:none!important;gap:6px;overflow-x:auto;padding:14px 24px;scrollbar-width:none;flex:none}
.mp-chips::-webkit-scrollbar{display:none}
.mp-chips button{flex:none;display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 13px;border-radius:999px;border:0;font:500 12.5px var(--sans);color:var(--tx2);background:rgba(255,255,255,.6);box-shadow:inset 0 0 0 1px var(--ln);cursor:pointer;transition:all .25s}
.mp-chips button b{width:8px;height:8px;border-radius:50%}
.mp-chips button small{font:11px var(--mono);color:var(--tx3)}
.mp-chips button[aria-pressed=true]{background:var(--tx);color:#fff}
.mp-chips button[aria-pressed=true] small{color:rgba(255,255,255,.6)}
.mp-count{padding:0 24px 8px;font:500 10.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--tx3);display:flex;justify-content:space-between}
.mp-list{flex:1;overflow-y:auto;padding:0 12px 12px;scrollbar-width:thin}
.mp-it{display:grid;grid-template-columns:10px 1fr auto;gap:12px;align-items:center;padding:13px 12px;border-radius:16px;cursor:pointer;transition:background .25s,transform .35s var(--e);animation:mpli .5s var(--e) both}
@keyframes mpli{from{opacity:0;transform:translateY(8px)}}
.mp-it:hover,.mp-it.on{background:rgba(255,255,255,.75)}
.mp-it b{width:10px;height:10px;border-radius:50%}
.mp-it strong{display:block;font:400 15px/1.25 var(--sans)}
.mp-it span{font:12px var(--sans);color:var(--tx3)}
.mp-st{font:500 10.5px var(--mono);letter-spacing:.06em;padding:4px 8px;border-radius:999px;white-space:nowrap}
.mp-st.o{color:#0F7A50;background:rgba(30,158,106,.12)}.mp-st.c{color:var(--tx3);background:rgba(20,23,28,.05)}.mp-st.h{color:#1E4E9E;background:rgba(47,111,208,.12)}
.mp-dest{display:inline-block;font:500 9.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:#9A6B12;margin-left:6px}
.mp-empty{padding:30px 12px;text-align:center;color:var(--tx3);font-size:14px}
.mp-card{position:absolute;right:20px;bottom:20px;width:360px;border-radius:26px;padding:24px;z-index:3;transform:translateY(20px);opacity:0;pointer-events:none;transition:all .5s var(--e)}
.mp-card.on{transform:none;opacity:1;pointer-events:auto}
.mp-card .fv{position:absolute;right:56px;top:14px;width:34px;height:34px;border-radius:50%;border:0;background:rgba(20,23,28,.06);cursor:pointer;font-size:17px;color:var(--tx2);transition:transform .3s var(--e)}
.mp-card .fv.on{color:#C2553D;background:rgba(194,85,61,.1)}
.mp-card .fv:active{transform:scale(1.25)}
.mp-it .hf{color:#C2553D;margin-left:6px;font-size:12px}
.mp-card .x{position:absolute;right:14px;top:14px;width:34px;height:34px;border-radius:50%;border:0;background:rgba(20,23,28,.06);cursor:pointer;font-size:16px;color:var(--tx2)}
.mp-card .cat{font:500 10.5px var(--mono);letter-spacing:.14em;text-transform:uppercase}
.mp-card h2{font:300 30px/1.02 var(--sans);letter-spacing:-.035em;margin:10px 40px 10px 0}
.mp-card p{margin:6px 0 0;font:14px/1.5 var(--sans);color:var(--tx2)}
.mp-card .hrs{margin-top:14px;padding-top:14px;border-top:1px solid var(--ln);font:12px/1.6 var(--mono);color:var(--tx2);white-space:pre-line}
.mp-fix{display:block;margin-top:14px;font:500 12px var(--sans);color:var(--ac);text-decoration:none}
.mp-card .acts{display:flex;gap:8px;margin-top:18px;flex-wrap:wrap}
.mp-btn{display:inline-flex;align-items:center;gap:8px;height:44px;padding:0 18px;border-radius:999px;font:500 14px var(--sans);text-decoration:none;color:var(--tx);background:linear-gradient(135deg,rgba(255,255,255,.85),rgba(255,255,255,.5));box-shadow:inset 0 1.5px 0 #fff,inset 0 0 0 1px rgba(20,23,28,.08),0 10px 24px -14px rgba(20,23,28,.4);transition:transform .4s var(--e)}
.mp-btn.p{color:#fff;background:linear-gradient(135deg,#2F6FD0,#1E4E9E);box-shadow:inset 0 1.5px 0 rgba(255,255,255,.5),0 14px 30px -12px rgba(47,111,208,.7)}
.mp-btn:hover{transform:translateY(-2px)}
.mp-tools{position:absolute;right:20px;top:20px;z-index:4;display:flex;gap:8px;align-items:center}
.mp-seg{display:flex;padding:4px;border-radius:999px}
.mp-seg button{border:0;background:none;height:34px;padding:0 14px;border-radius:999px;font:500 12.5px var(--sans);color:var(--tx2);cursor:pointer;transition:all .3s var(--e)}
.mp-seg button[aria-pressed=true]{background:var(--tx);color:#fff;box-shadow:inset 0 1px 0 rgba(255,255,255,.2)}
.mp-grid{position:absolute;left:420px;right:20px;top:76px;bottom:20px;z-index:3;border-radius:26px;overflow-y:auto;padding:28px;opacity:0;pointer-events:none;transform:translateY(16px);transition:all .5s var(--e)}
.mp.lista .mp-grid{opacity:1;pointer-events:auto;transform:none}
.mp.lista .mp-card,.mp.lista .mp-cta{display:none}
.mp-grid{padding-top:0!important}
.mp-top{position:absolute;left:420px;right:20px;top:76px;z-index:3;display:flex;gap:6px;overflow-x:auto;padding:8px;border-radius:999px;scrollbar-width:none;animation:mpin .9s .2s var(--e) both}
.mp-top::-webkit-scrollbar{display:none}
.mp-top button{flex:none;height:36px;padding:0 14px;border-radius:999px;border:0;font:500 12.5px var(--sans);color:var(--tx2);background:rgba(255,255,255,.6);cursor:pointer;display:inline-flex;align-items:center;gap:8px;transition:all .25s var(--e)}
.mp-top button b{width:8px;height:8px;border-radius:50%}
.mp-top button small{font:11px var(--mono);color:var(--tx3)}
.mp-top button[aria-pressed=true]{background:var(--tx);color:#fff}.mp-top button[aria-pressed=true] small{color:rgba(255,255,255,.6)}
.mp.lista .mp-top{display:none}
.mp.lista .mp-panel{opacity:0;pointer-events:none;transform:translateX(-24px);transition:all .4s var(--e)}
.mp.lista .mp-grid{left:20px}
.mp-panel{transition:opacity .4s var(--e),transform .4s var(--e),height .5s var(--e)}
.mp-gnav{position:sticky;top:0;z-index:2;display:flex;gap:6px;overflow-x:auto;padding:18px 0 14px;margin-bottom:6px;background:linear-gradient(#F4F1EC 75%,rgba(244,241,236,0));scrollbar-width:none}
.mp-gnav::-webkit-scrollbar{display:none}
.mp-gnav button{flex:none;height:38px;padding:0 15px;border-radius:999px;border:0;font:500 13px var(--sans);color:var(--tx2);background:rgba(255,255,255,.75);box-shadow:inset 0 0 0 1px var(--ln);cursor:pointer;display:inline-flex;align-items:center;gap:8px}
.mp-gnav button b{width:8px;height:8px;border-radius:50%}
.mp-gnav button small{font:11px var(--mono);color:var(--tx3)}
.mp-gnav button[aria-pressed=true]{background:var(--tx);color:#fff}.mp-gnav button[aria-pressed=true] small{color:rgba(255,255,255,.6)}
.mp-grid h3{font:300 28px/1 var(--sans);letter-spacing:-.03em;margin:28px 0 14px;display:flex;align-items:center;gap:10px}
.mp-grid h3:first-child{margin-top:0}
.mp-grid h3 b{width:10px;height:10px;border-radius:50%}
.mp-grid h3 small{font:11px var(--mono);color:var(--tx3)}
.mp-gl{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px}
.mp-gc{padding:16px 18px;border-radius:18px;background:rgba(255,255,255,.7);box-shadow:inset 0 0 0 1px var(--ln);cursor:pointer;transition:transform .35s var(--e),box-shadow .3s}
.mp-gc:hover{transform:translateY(-3px);box-shadow:inset 0 0 0 1px rgba(47,111,208,.3),0 16px 30px -20px rgba(20,23,28,.4)}
.mp-gc strong{display:block;font:400 16px/1.25 var(--sans);margin-bottom:4px}
.mp-gc span{display:block;font:12.5px var(--sans);color:var(--tx3);margin-bottom:10px}
.mp-upd{padding:10px 14px;border-radius:999px;font:500 10.5px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--tx2);display:flex;align-items:center;gap:8px}
.mp-upd{position:static!important}
.mp-upd i{width:7px;height:7px;border-radius:50%;background:var(--ok);animation:mpp 2s infinite}
@keyframes mpp{0%{box-shadow:0 0 0 0 rgba(30,158,106,.5)}70%{box-shadow:0 0 0 8px rgba(30,158,106,0)}}
.mp-cta{position:absolute;left:420px;bottom:20px;z-index:2;padding:12px 16px;border-radius:18px;font:13px/1.4 var(--sans);color:var(--tx2);max-width:300px}
.mp-cta a{color:var(--ac);font-weight:500;text-decoration:none}
.maplibregl-ctrl-bottom-right{right:390px!important}
.maplibregl-ctrl-group{border-radius:14px!important;overflow:hidden;box-shadow:0 10px 24px -12px rgba(20,23,28,.4)!important}
.maplibregl-ctrl-attrib{font:10px var(--sans)!important;background:rgba(255,255,255,.6)!important;border-radius:8px 0 0 0}
.mp-pop{font:500 12px var(--sans);padding:6px 10px;border-radius:10px;background:#14171C;color:#fff;white-space:nowrap;pointer-events:none}
.maplibregl-popup-content{padding:0!important;background:none!important;box-shadow:none!important}
.maplibregl-popup-tip{display:none}
.mp-handle{display:none}
@media (max-width:900px){
.mp-grp{display:flex;overflow-x:auto;padding:12px 20px 0;scrollbar-width:none}.mp-grp button{flex:0 0 82px}
.mp{height:calc(100svh - var(--hdh,80px))}
.mp-panel{left:10px;right:10px;top:auto;bottom:10px;width:auto;height:46%;border-radius:24px;transition:height .5s var(--e)}
.mp-panel.min{height:132px}.mp-panel.min .mp-logo{display:none}.mp-panel.min .mp-hd{cursor:pointer}
.mp-handle{display:block;width:64px;height:6px;padding:10px 0;background-clip:content-box!important;border-radius:5px;background:rgba(20,23,28,.18);margin:10px auto 0;border:0;cursor:pointer}
.mp-hd{padding:10px 20px 6px}.mp-hd h1{font-size:28px}.mp-hd p{display:none}
.mp-search{margin:6px 20px 0}.mp-tg,.mp-chips{padding-left:20px;padding-right:20px}
.mp-card{left:10px;right:10px;width:auto;bottom:10px;z-index:4}
.mp-cta{display:none}.mp-top{left:10px;right:10px;top:58px}.mp-tools{top:10px;right:10px;left:10px;justify-content:flex-end}.mp-upd{display:none}.mp-grid{left:10px;right:10px;top:62px;bottom:10px;padding:20px;z-index:5}
.maplibregl-ctrl-bottom-right{right:0!important;bottom:48%!important}
}
@media (prefers-reduced-motion:reduce){.mp *{animation:none!important;transition:none!important}}

/* tema grafite W3W no painel e na lista */
.mp-panel,.mp-grid{--tx:#F3F2EF;--tx2:#C5CBD4;--tx3:#8F98A6;--ln:rgba(255,255,255,.11);--ac:#8DB8FF;color:var(--tx)}
.mp-panel.mp-glass,.mp-grid.mp-glass,.mp-panel,.mp-grid{background:linear-gradient(160deg,rgba(58,66,79,.94),rgba(34,40,49,.96))!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.12),inset 0 0 0 1px rgba(255,255,255,.06),0 30px 60px -30px rgba(10,14,20,.55)!important}
.mp-panel button:not([aria-pressed=true]),.mp-grid button:not([aria-pressed=true]),.mp-panel input,.mp-grid input{background:rgba(255,255,255,.07)!important;color:var(--tx2)!important;box-shadow:inset 0 0 0 1px var(--ln)!important}
.mp-panel input::placeholder{color:var(--tx3)}
.mp-panel svg,.mp-grid svg{color:inherit}
.mp-logo svg path,.mp-logo svg g{fill:#F3F2EF}
.mp-panel a,.mp-grid a{color:var(--tx)}
.mp-logo nav a{background:rgba(255,255,255,.08)!important;color:var(--tx2)!important}
.mp-panel ::-webkit-scrollbar-thumb,.mp-grid ::-webkit-scrollbar-thumb{background:rgba(255,255,255,.2)}
.mp-gnav{background:linear-gradient(rgba(40,46,56,.98) 70%,rgba(40,46,56,0))!important}
.mp-gnav button[aria-pressed=true]{background:#F3F2EF!important;color:#1C2129!important}
.mp-gnav button[aria-pressed=true] small{color:rgba(28,33,41,.55)!important}
.mp-gc{background:rgba(255,255,255,.06)!important;box-shadow:inset 0 0 0 1px var(--ln)!important}
.mp-gc:hover{background:rgba(255,255,255,.11)!important}
.mp-gc *{border-color:var(--ln)}
.mp-top{--tx:#F3F2EF;--tx2:#C5CBD4;--tx3:#8F98A6;background:linear-gradient(160deg,rgba(58,66,79,.94),rgba(34,40,49,.96))!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 20px 40px -24px rgba(10,14,20,.55)!important;backdrop-filter:blur(18px)}
.mp-top button{background:rgba(255,255,255,.07)!important;color:var(--tx2)!important}
.mp-top button[aria-pressed=true]{background:#F3F2EF!important;color:#1C2129!important}
.mp-top button[aria-pressed=true] small{color:rgba(28,33,41,.55)!important}
.mp-tools .mp-glass{--tx2:#C5CBD4;background:linear-gradient(160deg,rgba(58,66,79,.94),rgba(34,40,49,.96))!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 16px 32px -20px rgba(10,14,20,.55)!important}
.mp-tools .mp-seg button{color:#C5CBD4}
.mp-tools .mp-seg button[aria-pressed=true]{background:#F3F2EF;color:#1C2129}
.mp-tools .mp-upd{color:#C5CBD4}

@media(max-width:900px){
.mp-panel{height:78%}
.mp-panel>*{flex-shrink:0}
.mp-panel:not(.min){overflow-y:auto;-webkit-overflow-scrolling:touch;overscroll-behavior:contain}
.mp-panel.min{overflow:hidden}
.mp-handle{position:sticky;top:0;z-index:5}
.mp-panel .mp-list{flex:none;overflow:visible;padding-bottom:24px}
.mp-hd p{display:none}
.mp-hd h1{font-size:34px}
.mp-grp{display:flex!important;overflow-x:auto;scrollbar-width:none;gap:8px}
.mp-grp::-webkit-scrollbar{display:none}
.mp-grp button{flex:none;width:86px}
body:has(.mp) .wa{bottom:auto!important;top:150px!important;right:12px!important;transform:scale(.82);transform-origin:top right}
}

/* celular: sem painel, só barra de cima */

.mp-panel{display:none!important}
.mp-mob{display:flex;position:absolute;left:10px;right:10px;top:10px;z-index:6;gap:8px;align-items:center;padding:6px 6px 6px 14px;border-radius:999px;background:linear-gradient(160deg,rgba(58,66,79,.96),rgba(34,40,49,.97));box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 16px 32px -20px rgba(10,14,20,.55)}
.mp-mob .lg{display:flex;color:#F3F2EF;flex:none}.mp-mob .lg svg{height:24px;width:auto}.mp-mob .lg svg path,.mp-mob .lg svg g{fill:#F3F2EF}
.mp-mob .mp-search{margin:0;flex:1;min-width:0}
.mp-mob .mp-search input{height:40px;background:rgba(255,255,255,.08)!important;color:#F3F2EF!important;box-shadow:inset 0 0 0 1px rgba(255,255,255,.1)!important;font-size:16px;padding-left:38px}
.mp-mob .mp-search input::placeholder{color:#8F98A6}
.mp-mob .mp-search svg{top:12px;left:14px;color:#8F98A6}
.mp-tools{top:64px!important;left:10px!important;right:10px!important;justify-content:flex-start!important;flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none}
.mp-tools::-webkit-scrollbar{display:none}
.mp-tools .mp-tg{display:flex;gap:6px;flex:none;margin:0}
.mp-tools .mp-tg button{height:42px;padding:0 14px;border-radius:999px;border:0;font:500 12.5px var(--sans);white-space:nowrap;background:linear-gradient(160deg,rgba(58,66,79,.94),rgba(34,40,49,.96))!important;color:#C5CBD4!important;display:inline-flex;align-items:center;gap:7px}
.mp-tools .mp-tg button i{width:7px;height:7px;border-radius:50%;background:#3DDC97}
.mp-tools .mp-tg button[aria-pressed=true]{background:#F3F2EF!important;color:#1C2129!important}
.mp-top{top:118px!important}
.mp-grid{top:172px!important}
.mp-card{left:10px!important;right:10px!important;bottom:10px!important;width:auto!important}
body:has(.mp) .wa{top:auto!important;bottom:16px!important;transform:scale(.85);transform-origin:bottom right}

.mp-panel .mp-st.o,.mp-grid .mp-st.o{color:#5FE3A8;background:rgba(61,220,151,.12)}
.mp-panel .mp-st.c,.mp-grid .mp-st.c{color:#9AA3B0;background:rgba(255,255,255,.07)}
.mp-panel .mp-st.h,.mp-grid .mp-st.h{color:#9CC2FF;background:rgba(141,184,255,.14)}
.mp-tools{align-items:center!important}.mp-tools .mp-seg button{padding:0 11px}.mp-grid{top:118px!important}

.mp-mob{justify-content:space-between;padding:8px 8px 8px 16px}
.mp-mob .gm{flex:none;font:500 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:#F3F2EF;text-decoration:none;padding:10px 14px;border-radius:999px;background:rgba(255,255,255,.09)}
.mp-msb{position:absolute;left:10px;right:78px;bottom:14px;z-index:6;padding:6px;border-radius:999px;background:linear-gradient(160deg,rgba(58,66,79,.96),rgba(34,40,49,.97));box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 16px 32px -16px rgba(10,14,20,.6)}
.mp-msb .mp-search{margin:0}
.mp-msb .mp-search input{height:44px;background:rgba(255,255,255,.08)!important;color:#F3F2EF!important;box-shadow:inset 0 0 0 1px rgba(255,255,255,.1)!important;font-size:16px;padding-left:40px}
.mp-msb .mp-search input::placeholder{color:#8F98A6}
.mp-msb .mp-search svg{top:14px;left:15px;color:#8F98A6}
.mp:has(.mp-card.on) .mp-msb{opacity:0;pointer-events:none}
.mp-grid{bottom:76px!important}
.maplibregl-ctrl-bottom-left,.maplibregl-ctrl-bottom-right{bottom:70px!important}
body:has(.mp) .wa{bottom:16px!important}


.mp-search input::-webkit-search-cancel-button{filter:invert(1) grayscale(1);opacity:.6}
.mp-sg{position:absolute;left:0;right:0;top:calc(100% + 8px);z-index:20;max-height:min(360px,50vh);overflow-y:auto;padding:6px;border-radius:20px;background:linear-gradient(160deg,rgba(58,66,79,.98),rgba(34,40,49,.99));box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 24px 48px -16px rgba(10,14,20,.6);display:none}
.mp-sg.on{display:block;animation:mpsg .25s var(--e)}
@keyframes mpsg{from{opacity:0;transform:translateY(-6px)}}
.mp-sg button,.mp-panel .mp-sg button:not([aria-pressed=true]){display:flex;align-items:center;gap:12px;width:100%;text-align:left;border:0;background:none!important;box-shadow:none!important;height:auto!important;padding:10px 12px;border-radius:14px;cursor:pointer;color:#F3F2EF!important}
.mp-sg button:hover,.mp-sg button.k,.mp-panel .mp-sg button.k:not([aria-pressed=true]),.mp-panel .mp-sg button:hover:not([aria-pressed=true]){background:rgba(255,255,255,.08)!important}
.mp-sg b{flex:none;width:9px;height:9px;border-radius:50%}
.mp-sg span{flex:1;min-width:0}
.mp-sg strong{display:block;font:500 14.5px var(--sans);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mp-sg small{display:block;font:12px var(--sans);color:#8F98A6;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:2px}
.mp-sg em{flex:none;font:500 10px var(--mono);letter-spacing:.06em;text-transform:uppercase;font-style:normal;color:#5FE3A8;background:rgba(61,220,151,.12);padding:4px 8px;border-radius:999px}
.mp-sg p{margin:0;padding:14px;color:#8F98A6;font-size:14px}
.mp-msb .mp-sg{top:auto;bottom:calc(100% + 14px);left:-6px;right:-6px}
@keyframes mpsgu{from{opacity:0;transform:translateY(6px)}}
.mp-msb .mp-sg.on{animation-name:mpsgu}

@media(min-width:901px){
.mp-mob{left:20px;right:auto;top:20px;width:400px}
.mp-tools{top:20px!important;left:436px!important;right:20px!important}
.mp-top{top:76px!important;left:20px!important;right:20px!important}
.mp-grid{top:136px!important;left:20px!important;right:20px!important;bottom:92px!important}
.mp-msb{left:50%;right:auto;width:min(560px,calc(100% - 200px));transform:translateX(-50%);bottom:22px}
.mp-card{left:auto!important;right:20px!important;bottom:96px!important;width:380px!important}
body:has(.mp) .wa{bottom:22px!important;right:20px!important}
}

.mp-tools .mp-tg{padding:0!important;height:42px;align-items:center}
.mp-tools .mp-upd{height:42px;display:inline-flex;align-items:center;box-sizing:border-box}
@media(min-width:901px){
.mp-top{right:auto!important;max-width:calc(100% - 40px)}
.mp-cta{left:20px!important;right:auto!important;bottom:52px!important;top:auto!important;max-width:340px}
}
@media(max-width:900px){.mp-tools .mp-upd{display:none}}
/* atalhos */
.mp-ints{position:absolute;left:10px;right:10px;bottom:76px;z-index:6;display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding:4px 2px;mask-image:linear-gradient(90deg,#000 88%,transparent)}
.mp-ints::-webkit-scrollbar{display:none}
.mp-ints button{flex:none;display:inline-flex;align-items:center;gap:7px;height:38px;padding:0 15px;border-radius:999px;border:0;cursor:pointer;font:500 13px var(--sans);color:#E9EBEE;background:linear-gradient(160deg,rgba(58,66,79,.94),rgba(34,40,49,.96));box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 10px 24px -14px rgba(10,14,20,.6);transition:transform .25s var(--e),background .25s}
.mp-ints button:active{transform:scale(.96)}
.mp-ints button svg{width:15px;height:15px}
.mp-ints button[aria-pressed=true]{background:#F3F2EF;color:#1C2129}
.mp-ints button.ld svg{animation:mpspin 1s linear infinite}
@keyframes mpspin{to{transform:rotate(360deg)}}
.mp:has(.mp-card.on) .mp-ints,.mp.rota .mp-ints,.mp.rota .mp-msb{opacity:0;pointer-events:none}
.mp-ints,.mp-msb{transition:opacity .3s}
@media(min-width:901px){.mp-ints{left:50%;right:auto;transform:translateX(-50%);width:min(760px,calc(100% - 200px));bottom:86px;justify-content:center}.mp-grid{bottom:140px!important}}
@media(max-width:900px){.mp-grid{bottom:126px!important}}
.mp.lista .mp-ints{opacity:1}
/* eu */
.mp-me{width:18px;height:18px;border-radius:50%;background:#2F6FD0;border:3px solid #fff;box-shadow:0 0 0 0 rgba(47,111,208,.5);animation:mpme 2s infinite}
@keyframes mpme{70%{box-shadow:0 0 0 16px rgba(47,111,208,0)}100%{box-shadow:0 0 0 0 rgba(47,111,208,0)}}
/* aviso */
.mp-toast{position:absolute;left:50%;bottom:136px;z-index:9;transform:translate(-50%,12px);width:min(440px,calc(100% - 24px));padding:14px 18px;border-radius:18px;font:14px/1.45 var(--sans);color:#E9EBEE;background:linear-gradient(160deg,rgba(58,66,79,.97),rgba(34,40,49,.98));box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 24px 48px -18px rgba(10,14,20,.6);opacity:0;pointer-events:none;transition:all .45s var(--e);cursor:pointer}
.mp-toast.on{opacity:1;transform:translate(-50%,0);pointer-events:auto}
.mp-toast strong{color:#fff;font-weight:500}.mp-toast u{color:#8DB8FF;text-underline-offset:3px}
@media(min-width:901px){.mp-toast{bottom:146px}}
/* botão ? */
.mp-mob .hq{flex:none;width:36px;height:36px;border-radius:50%;border:0;cursor:pointer;margin-left:auto;margin-right:6px;font:500 15px var(--sans);color:#F3F2EF;background:rgba(255,255,255,.09)}
.mp-mob .gm{margin-left:0}
/* folha (sobre / roteiros) */
.mp-sheet{position:absolute;inset:0;z-index:20;background:rgba(14,17,22,.35);backdrop-filter:blur(4px);display:flex;align-items:flex-end;justify-content:center;opacity:0;pointer-events:none;transition:opacity .35s}
.mp-sheet.on{opacity:1;pointer-events:auto}
.mp-sheet .in{position:relative;width:min(620px,100%);max-height:88%;overflow-y:auto;margin:12px;padding:30px 26px 26px;border-radius:28px;color:#F3F2EF;background:linear-gradient(160deg,#3A424F,#222831);box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 40px 80px -30px rgba(0,0,0,.6);transform:translateY(30px);transition:transform .5s var(--e)}
.mp-sheet.on .in{transform:none}
.mp-sheet .x{position:absolute;right:16px;top:16px;width:34px;height:34px;border-radius:50%;border:0;cursor:pointer;color:#F3F2EF;background:rgba(255,255,255,.09)}
.mp-sheet .ey,.mp-rt .ey{font:500 10.5px var(--mono);letter-spacing:.14em;text-transform:uppercase;color:#8DB8FF}
.mp-sheet h3{font:300 clamp(30px,6vw,40px)/1 var(--sans);letter-spacing:-.04em;margin:12px 0 14px}
.mp-sheet h3 em{font-family:var(--serif);font-style:italic;color:#8DB8FF}
.mp-sheet h4{font:500 11px var(--mono);letter-spacing:.14em;text-transform:uppercase;color:#8F98A6;margin:26px 0 8px}
.mp-sheet p{margin:0;font:14.5px/1.55 var(--sans);color:#C5CBD4}.mp-sheet p.ld{font-size:16px;color:#E3E6EA}
.mp-sheet .sb{display:grid;gap:10px;margin-top:20px}
.mp-sheet .sb div{display:grid;grid-template-columns:34px 1fr;gap:2px 10px;padding:14px;border-radius:16px;background:rgba(255,255,255,.06)}
.mp-sheet .sb b{grid-row:span 2;font:500 11px var(--mono);color:#8DB8FF;padding-top:3px}
.mp-sheet .sb strong{font:500 15px var(--sans)}.mp-sheet .sb span{font:13.5px/1.45 var(--sans);color:#AEB6C2}
.mp-sheet .fp{display:grid;gap:10px}@media(min-width:600px){.mp-sheet .fp{grid-template-columns:1fr 1fr}}
.mp-sheet .fp a{display:flex;flex-direction:column;gap:6px;padding:18px;border-radius:18px;text-decoration:none;color:#F3F2EF;background:rgba(255,255,255,.07);box-shadow:inset 0 0 0 1px rgba(255,255,255,.08);transition:background .25s}
.mp-sheet .fp a:hover{background:rgba(255,255,255,.12)}
.mp-sheet .fp strong{font:500 15px var(--sans)}.mp-sheet .fp span{font:13px/1.45 var(--sans);color:#AEB6C2}.mp-sheet .fp i{font-style:normal;font:500 13px var(--sans);color:#8DB8FF;margin-top:auto;padding-top:6px}
.mp-sheet .rl{display:grid;gap:10px}
.mp-sheet .rl button{display:flex;flex-direction:column;gap:5px;text-align:left;padding:18px;border-radius:18px;border:0;cursor:pointer;color:#F3F2EF;background:rgba(255,255,255,.07);box-shadow:inset 0 0 0 1px rgba(255,255,255,.08);transition:background .25s,transform .25s var(--e)}
.mp-sheet .rl button:hover{background:rgba(255,255,255,.12)}.mp-sheet .rl button:active{transform:scale(.98)}
.mp-sheet .rl strong{font:400 20px var(--sans);letter-spacing:-.02em}.mp-sheet .rl span{font:13.5px/1.45 var(--sans);color:#C5CBD4}.mp-sheet .rl small{font:500 10.5px/1.6 var(--mono);color:#8F98A6;letter-spacing:.04em}
/* faixa do roteiro */
.mp-rt{position:absolute;left:10px;right:10px;bottom:12px;z-index:7;padding:16px 16px 14px;border-radius:24px;color:#F3F2EF;background:linear-gradient(160deg,rgba(58,66,79,.97),rgba(34,40,49,.98));box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 24px 48px -16px rgba(10,14,20,.6);transform:translateY(130%);transition:transform .5s var(--e)}
.mp.rota .mp-rt{transform:none}
.mp-rt .rh{display:flex;align-items:center;gap:10px;margin-bottom:12px}.mp-rt .rh strong{font:400 18px var(--sans);letter-spacing:-.02em;flex:1}
.mp-rt .x{width:32px;height:32px;border-radius:50%;border:0;cursor:pointer;color:#F3F2EF;background:rgba(255,255,255,.09)}
.mp-rt .st{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none}.mp-rt .st::-webkit-scrollbar{display:none}
.mp-rt .st button{flex:none;display:flex;align-items:center;gap:10px;padding:8px 14px 8px 8px;border-radius:999px;border:0;cursor:pointer;color:#F3F2EF;background:rgba(255,255,255,.07);text-align:left}
.mp-rt .st i{width:26px;height:26px;border-radius:50%;display:grid;place-items:center;font:500 12px var(--mono);font-style:normal;background:#F3F2EF;color:#1C2129}
.mp-rt .st span{font:500 13.5px var(--sans);white-space:nowrap}.mp-rt .st small{display:block;font:11px var(--sans);color:#8F98A6}
@media(min-width:901px){.mp-rt{left:50%;right:auto;width:min(760px,calc(100% - 200px));transform:translate(-50%,130%)}.mp.rota .mp-rt{transform:translate(-50%,0)}}
.mp.rota .mp-card.on~.mp-rt,.mp.rota:has(.mp-card.on) .mp-rt{opacity:0;pointer-events:none}
/* cartão do lugar mais bonito */
.mp-card{padding:0!important;overflow:hidden}
.mp-card .bn{height:92px;padding:18px 22px;display:flex;align-items:flex-end;gap:8px;background:radial-gradient(120% 140% at 0% 0%,color-mix(in srgb,var(--c) 85%,#fff 15%),color-mix(in srgb,var(--c) 70%,#1C2129 30%));position:relative}
.mp-card .bn::after{content:"";position:absolute;inset:0;background:repeating-linear-gradient(115deg,rgba(255,255,255,.07) 0 2px,transparent 2px 14px);pointer-events:none}
.mp-card .bn .cat{color:#fff!important;font:500 10.5px var(--mono);letter-spacing:.14em;text-transform:uppercase;position:relative;z-index:1}
.mp-card .bn .w3{position:relative;z-index:1;font:500 10px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:#1C2129;background:#F3F2EF;padding:4px 8px;border-radius:999px}
.mp-card h2,.mp-card>p,.mp-card>.mp-st,.mp-card .hrs,.mp-card .acts,.mp-card .mp-fix,.mp-card .dist{margin-left:22px!important;margin-right:22px!important}
.mp-card h2{margin-top:18px!important}
.mp-card .mp-fix{display:block;margin-bottom:20px!important;margin-top:14px}
.mp-card .dist{display:block;font:500 11px var(--mono);letter-spacing:.06em;color:#2F6FD0;margin:-2px 0 8px}
.mp-card .x,.mp-card .fv{background:rgba(255,255,255,.85)!important;backdrop-filter:blur(8px);z-index:2}
.mp-card>.mp-st{display:inline-block}
body:has(.mp.rota) .wa,body:has(.mp-sheet.on) .wa{opacity:0;pointer-events:none}
</style>
"""


def render(wa, cats_json, grupos_json='[]', logo='', base=''):
    return CSS + f'''
<main class="mp">
<div id="mpMap" aria-label="Mapa de Moema"></div>
<aside class="mp-panel mp-glass" id="mpPanel">
<button class="mp-handle" aria-label="Expandir lista" id="mpHandle"></button>
<div class="mp-hd"><div class="mp-logo"><a href="{base}/" aria-label="W3W Imóveis, voltar ao site">{logo}</a><nav><a href="{base}/guia-moema/">Guia Moema</a><a href="{base}/">← Site W3W</a></nav></div><span class="ey">Guia Moema · Mapa vivo</span><h1>Moema <em>agora.</em></h1><p>Restaurantes, bares, cafés, docerias, farmácias e serviços 24 horas do bairro, com o que está aberto neste momento.</p></div>
<div class="mp-search"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input id="mpQ" type="search" placeholder="Buscar um lugar" aria-label="Buscar um lugar"></div>
<div class="mp-tg"><button id="mpOpen" aria-pressed="false"><i></i>Aberto agora</button><button id="mp24" aria-pressed="false">24 horas</button></div>
<div class="mp-grp" id="mpGrp" role="group" aria-label="O que você procura"></div><div class="mp-chips" id="mpChips" role="group" aria-label="Categorias"></div>
<div class="mp-count"><span id="mpN">—</span><span id="mpNow"></span></div>
<div class="mp-list" id="mpList"></div>
</aside>
<div class="mp-tools"><div class="mp-seg mp-glass" role="group" aria-label="Visualização"><button id="mpV3" aria-pressed="true">3D</button><button id="mpV2" aria-pressed="false">2D</button></div><div class="mp-seg mp-glass" role="group" aria-label="Modo"><button id="mpMm" aria-pressed="true">Mapa</button><button id="mpMl" aria-pressed="false">Lista</button></div><div class="mp-upd mp-glass"><i></i><span id="mpUpd">Atualizado toda semana</span></div></div>
<nav class="mp-top mp-glass" id="mpTop" aria-label="Filtrar o mapa por setor"></nav>
<section class="mp-grid mp-glass" aria-label="Lista de lugares"><nav class="mp-gnav" id="mpGnav" aria-label="Setores"></nav><div id="mpGrid"></div></section>
<div class="mp-cta mp-glass">Tem um negócio em Moema? <a href="{wa('Olá! Tenho um negócio em Moema e quero aparecer no Mapa de Moema da W3W.')}" target="_blank" rel="noopener">Apareça no mapa →</a></div>
<article class="mp-card mp-glass" id="mpCard" aria-live="polite"></article>
</main>
<link rel="stylesheet" href="../assets/maplibre/maplibre-gl.css">
<script src="../assets/maplibre/maplibre-gl.js"></script>
<script>window.MP_CATS={cats_json};window.MP_GRP={grupos_json};</script>
<script src="mapa.js"></script>
'''


JS = r"""
(()=>{const $=s=>document.querySelector(s),C=window.MP_CATS,CM=Object.fromEntries(C.map(c=>[c[0],c]));
const R=matchMedia('(prefers-reduced-motion: reduce)').matches;

/* horários (formato OpenStreetMap) */
const DN=['Su','Mo','Tu','We','Th','Fr','Sa'],PT={Mo:'Seg',Tu:'Ter',We:'Qua',Th:'Qui',Fr:'Sex',Sa:'Sáb',Su:'Dom'};
function days(spec){const out=new Set();spec.split(',').forEach(p=>{const m=p.trim().match(/^(Mo|Tu|We|Th|Fr|Sa|Su)(?:-(Mo|Tu|We|Th|Fr|Sa|Su))?$/);if(!m)return;let a=DN.indexOf(m[1]),b=m[2]?DN.indexOf(m[2]):a;for(let i=0;i<8;i++){out.add(a);if(a===b)break;a=(a+1)%7}});return out}
function parse(h){if(!h)return null;h=h.trim();if(h==='24/7')return'24';const rules=[];for(let r of h.split(';')){r=r.trim();if(!r||/^PH/.test(r))continue;let m=r.match(/^([A-Za-z,\- ]+?)\s+(.+)$/),ds,ts;if(m&&/^(Mo|Tu|We|Th|Fr|Sa|Su)/.test(m[1])){ds=days(m[1].replace(/\s/g,''));ts=m[2]}else{ds=new Set([0,1,2,3,4,5,6]);ts=r}
if(/off|closed/i.test(ts)){rules.push({ds,off:1});continue}const iv=[];ts.split(',').forEach(t=>{const x=t.trim().match(/^(\d{1,2}):(\d{2})-(\d{1,2}):(\d{2})\+?$/);if(x)iv.push([+x[1]*60+ +x[2],+x[3]*60+ +x[4]])});if(iv.length)rules.push({ds,iv})}return rules.length?rules:null}
function status(h,now=new Date()){const p=parse(h);if(!p)return{k:'?'};if(p==='24')return{k:'h',t:'24 horas'};const d=now.getDay(),mn=now.getHours()*60+now.getMinutes(),yd=(d+6)%7;
const act=day=>{let iv=null;p.forEach(r=>{if(r.ds.has(day))iv=r.off?[]:r.iv});return iv||[]};
for(const [a,b] of act(d)){if(b>a?mn>=a&&mn<b:mn>=a)return{k:'o',t:'Aberto · fecha '+fmt(b)}}
for(const [a,b] of act(yd)){if(b<a&&mn<b)return{k:'o',t:'Aberto · fecha '+fmt(b)}}
const nx=act(d).filter(([a])=>a>mn).sort((x,y)=>x[0]-y[0])[0];return{k:'c',t:nx?'Abre '+fmt(nx[0]):'Fechado'}}
const fmt=m=>{m%=1440;const h=Math.floor(m/60),mi=m%60;return h+'h'+(mi?String(mi).padStart(2,'0'):'')};
const human=h=>h==='24/7'?'Aberto 24 horas':h.replace(/Mo|Tu|We|Th|Fr|Sa|Su/g,x=>PT[x]).replace(/;\s*/g,'\n').replace(/off/g,'fechado').replace(/PH/g,'Feriados');
/* estado */
const G=window.MP_GRP||[],IC={gastronomia:'<path d="M7 3v8a2 2 0 0 0 2 2v8M11 3v8M3 3v8a2 2 0 0 0 2 2M17 21V3c2 1 4 4 4 8h-4"/>',servicos:'<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',beleza:'<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.1 15.9M14.5 14.5 20 20M8.1 8.1 12 12"/>',compras:'<path d="M6 2 3 6v14h18V6l-3-4zM3 6h18M16 10a4 4 0 0 1-8 0"/>',saude:'<path d="M12 21s-8-4.5-8-11a5 5 0 0 1 8-4 5 5 0 0 1 8 4c0 6.5-8 11-8 11z"/>',carro:'<path d="M5 17h14M5 17a2 2 0 1 1-4 0v-5l3-6h16l3 6v5a2 2 0 1 1-4 0M7 17a2 2 0 1 1-4 0"/>',educacao:'<path d="M22 10 12 5 2 10l10 5 10-5zM6 12v5c3 2 9 2 12 0v-5"/>',lazer:'<circle cx="12" cy="12" r="9"/><path d="M12 3a14 14 0 0 1 0 18M3 12h18"/>'};
let FAV=new Set();try{FAV=new Set(JSON.parse(localStorage.getItem('mpFav')||'[]'))}catch(e){}
const saveFav=()=>{try{localStorage.setItem('mpFav',JSON.stringify([...FAV]))}catch(e){}};
const toggleFav=id=>{FAV.has(id)?FAV.delete(id):FAV.add(id);saveFav();chips();draw()};
let GS=null,ALL=[],F={fav:false,cat:null,open:false,h24:false,q:''},sel=null,map;const norm=s=>String(s||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
fetch('locais.json?v='+Date.now()).then(r=>r.json()).then(d=>{ALL=d.locais.filter(l=>CM[l.cat]);if(d.atualizado){const t=new Date(d.atualizado);$('#mpUpd').textContent='Atualizado em '+t.toLocaleDateString('pt-BR',{day:'2-digit',month:'short'})}
chips();draw()}).catch(()=>{$('#mpList').innerHTML='<p class="mp-empty">Não foi possível carregar os lugares agora.</p>'});
function chips(){const n={};ALL.forEach(l=>n[l.cat]=(n[l.cat]||0)+1);
$('#mpGrp').innerHTML=G.map(g=>`<button aria-pressed="${GS===g[0]}" data-g="${g[0]}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">${IC[g[0]]||''}</svg>${g[1]}</button>`).join('');
$('#mpGrp').querySelectorAll('button').forEach(b=>b.onclick=()=>{GS=GS===b.dataset.g?null:b.dataset.g;F.cat=null;chips();draw(true)});
const inG=c=>!GS||G.find(g=>g[0]===GS)[2].includes(c);const tot=ALL.filter(l=>inG(l.cat)).length;
$('#mpChips').innerHTML=`<button aria-pressed="${!F.cat}" data-c="">Todos <small>${tot}</small></button>`+C.filter(c=>n[c[0]]&&inG(c[0])).map(c=>`<button aria-pressed="${F.cat===c[0]}" data-c="${c[0]}"><b style="background:${c[2]}"></b>${c[1]} <small>${n[c[0]]}</small></button>`).join('');
$('#mpChips').querySelectorAll('button').forEach(b=>b.onclick=()=>{F.cat=b.dataset.c||null;chips();draw(true)})}
function list(ign,noCat){const q=norm(F.q);const gc=GS?G.find(g=>g[0]===GS)[2]:null;return ALL.map(l=>({...l,st:status(l.horario)})).filter(l=>(!F.fav||FAV.has(l.id))&&(!gc||gc.includes(l.cat))&&(noCat||!F.cat||l.cat===F.cat)&&(ign||!F.open||l.st.k==='o'||l.st.k==='h')&&(ign||!F.h24||l.st.k==='h')&&(!q||norm(l.nome+' '+(l.end||'')+' '+CM[l.cat][1]).includes(q)))}
function draw(fit){const L=list();$('#mpN').textContent=L.length+' lugares';$('#mpNow').textContent=new Date().toLocaleTimeString('pt-BR',{hour:'2-digit',minute:'2-digit'});
$('#mpList').innerHTML=L.length?L.slice(0,300).map((l,i)=>`<div class="mp-it${sel===l.id?' on':''}" data-id="${l.id}" style="animation-delay:${Math.min(i,20)*18}ms"><b style="background:${CM[l.cat][2]}"></b><div><strong>${esc(l.nome)}${FAV.has(l.id)?'<span class="hf">♥</span>':''}${l.destaque?'<span class="mp-dest">W3W indica</span>':''}</strong><span>${CM[l.cat][1]}${l.end?' · '+esc(l.end):''}</span></div>${l.st.k!=='?'?`<span class="mp-st ${l.st.k}">${l.st.t}</span>`:''}</div>`).join(''):empty();grid(L);catbar($('#mpTop'));
const ab=$('#mpAll');if(ab)ab.onclick=()=>{F.open=F.h24=false;$('#mpOpen').setAttribute('aria-pressed',false);$('#mp24').setAttribute('aria-pressed',false);draw(true)};
$('#mpList').querySelectorAll('.mp-it').forEach(el=>{el.onclick=()=>pick(el.dataset.id,true);el.onmouseenter=()=>hover(el.dataset.id)});
if(map&&map.getSource('locais')){map.getSource('locais').setData(geo(L));if(fit&&L.length){const b=new maplibregl.LngLatBounds();L.forEach(l=>b.extend([l.lon,l.lat]));map.fitBounds(b,{padding:pad(),maxZoom:16,duration:R?0:1200})}}}
function empty(){const all=list(true).length;return all&&(F.open||F.h24)?`<p class="mp-empty">Nada ${F.h24?'24 horas':'aberto agora'} com essa busca.<br><button class="mp-btn" id="mpAll" style="margin-top:14px">Ver os ${all} resultados</button></p>`:`<p class="mp-empty">Ainda não temos “${esc(F.q)}” no mapa.<br><a class="mp-btn" style="margin-top:14px" href="https://wa.me/5511940297871?text=${encodeURIComponent('Olá! Sugiro incluir no Mapa de Moema: '+F.q)}" target="_blank" rel="noopener">Sugerir este lugar</a></p>`}
function catbar(nv,L0){if(!nv)return;const base=list(false,true);const cnt={};base.forEach(l=>cnt[l.cat]=(cnt[l.cat]||0)+1);
nv.innerHTML=`<button aria-pressed="${F.fav}" data-fav="1">♥ Favoritos <small>${FAV.size}</small></button><button aria-pressed="${!F.cat&&!F.fav}" data-c="">Todos <small>${base.length}</small></button>`+C.filter(c=>cnt[c[0]]).map(c=>`<button aria-pressed="${F.cat===c[0]}" data-c="${c[0]}"><b style="background:${c[2]}"></b>${c[1]} <small>${cnt[c[0]]}</small></button>`).join('');
nv.querySelectorAll('button').forEach(b=>b.onclick=()=>{if(b.dataset.fav){F.fav=!F.fav;F.cat=null;chips();draw(true);return}F.fav=false;F.cat=b.dataset.c||null;chips();draw(true);const g=document.querySelector('.mp-grid');if(g)g.scrollTop=0});
const on=nv.querySelector('[aria-pressed=true]');if(on&&F.cat)nv.scrollLeft=on.offsetLeft-nv.clientWidth/2+on.offsetWidth/2}
function grid(L0){const g=$('#mpGrid');if(!g)return;const cnt={};L0.forEach(l=>cnt[l.cat]=(cnt[l.cat]||0)+1);
catbar($('#mpGnav'),L0);const gs=F.cat;const L=gs?L0.filter(l=>l.cat===gs):L0;const by={};L.forEach(l=>(by[l.cat]=by[l.cat]||[]).push(l));g.innerHTML=C.filter(c=>by[c[0]]).map(c=>`<h3><b style="background:${c[2]}"></b>${c[1]} <small>${by[c[0]].length}</small></h3><div class="mp-gl">${by[c[0]].map(l=>`<div class="mp-gc" data-id="${l.id}"><strong>${esc(l.nome)}</strong><span>${esc(l.end||CM[l.cat][1])}</span>${l.st.k!=='?'?`<em class="mp-st ${l.st.k}" style="font-style:normal">${l.st.t}</em>`:''}</div>`).join('')}</div>`).join('')||'<p class="mp-empty">Nenhum lugar com esses filtros.</p>';
g.querySelectorAll('.mp-gc').forEach(el=>el.onclick=()=>{setMode(false);pick(el.dataset.id,true)})}
const pad=()=>innerWidth>900?{left:420,right:60,top:80,bottom:80}:{left:30,right:30,top:60,bottom:innerHeight*.5};
const geo=L=>({type:'FeatureCollection',features:L.map(l=>({type:'Feature',id:hash(l.id),properties:{id:l.id,nome:l.nome,cor:CM[l.cat][2],aberto:l.st.k==='o'||l.st.k==='h'?1:0,dest:l.destaque?1:0},geometry:{type:'Point',coordinates:[l.lon,l.lat]}}))});
const hash=s=>{let h=0;for(const c of s)h=(h*31+c.charCodeAt(0))|0;return Math.abs(h)};
const esc=s=>String(s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function pick(id,fly){const l=ALL.find(x=>x.id===id);if(!l)return;sel=id;const st=status(l.horario),c=CM[l.cat];
$('#mpCard').innerHTML=`<button class="x" aria-label="Fechar">✕</button><button class="fv${FAV.has(l.id)?' on':''}" aria-label="Favoritar" aria-pressed="${FAV.has(l.id)}">${FAV.has(l.id)?'♥':'♡'}</button><div class="bn" style="--c:${c[2]}"><span class="cat">${c[1]}</span>${l.destaque?'<span class="w3">W3W indica</span>':''}</div><h2>${esc(l.nome)}</h2>${window.mpKm&&window.mpKm(l)!=null?`<span class="dist">${window.mpKm(l)<1?Math.round(window.mpKm(l)*1000)+' m':window.mpKm(l).toFixed(1).replace('.',',')+' km'} de você · ${Math.max(1,Math.round(window.mpKm(l)*13))} min a pé</span>`:''}${st.k!=='?'?`<span class="mp-st ${st.k}">${st.t}</span>`:''}${l.nota?`<p>${esc(l.nota)}</p>`:''}${l.end?`<p>${esc(l.end)}</p>`:''}${l.horario?`<div class="hrs">${esc(human(l.horario))}${l.conferido?'<br><span style="color:#1E9E6A">✓ Confirmado pela W3W</span>':(l.fonte_horario==='site'?'<br><span style="opacity:.7">Conforme o site do estabelecimento</span>':'')}</div>`:''}
<div class="acts"><a class="mp-btn p" href="https://www.google.com/maps/dir/?api=1&destination=${l.lat},${l.lon}" target="_blank" rel="noopener">Como chegar</a>${l.site?`<a class="mp-btn" href="${esc(l.site)}" target="_blank" rel="noopener">Site</a>`:''}${l.tel?`<a class="mp-btn" href="tel:${esc(l.tel.replace(/[^+\d]/g,''))}">Ligar</a>`:''}</div><a class="mp-fix" href="https://wa.me/5511940297871?text=${encodeURIComponent('Olá! Sou do '+l.nome+' e quero atualizar nosso horário no Mapa de Moema: ')}" target="_blank" rel="noopener">${l.horario?'Horário errado? Avise a W3W':'É o responsável? Informe o horário'} →</a>`;
$('#mpCard').classList.add('on');$('#mpCard .fv').onclick=()=>{toggleFav(id);pick(id,false)};$('#mpCard .x').onclick=()=>{$('#mpCard').classList.remove('on');sel=null;pop&&pop.remove();$('#mpPanel').classList.remove('min');if(map)map.setFilter('sel',['==',['get','id'],'']);draw()};
if(map){map.setFilter('sel',['==',['get','id'],id]);if(fly)map.flyTo({center:[l.lon,l.lat],zoom:Math.max(map.getZoom(),16.2),pitch:55,bearing:-18,padding:pad(),duration:R?0:1600,essential:true})}
document.querySelectorAll('.mp-it').forEach(e=>e.classList.toggle('on',e.dataset.id===id));if(innerWidth<=900)$('#mpPanel').classList.add('min')}
let pop;function hover(id){if(!map||!matchMedia('(hover:hover)').matches)return;const l=ALL.find(x=>x.id===id);if(!l)return;pop&&pop.remove();pop=new maplibregl.Popup({closeButton:false,offset:14}).setLngLat([l.lon,l.lat]).setHTML(`<div class="mp-pop">${esc(l.nome)}</div>`).addTo(map)}
$('#mpQ').oninput=e=>{F.q=e.target.value;draw()};
$('#mpOpen').onclick=e=>{F.open=!F.open;e.currentTarget.setAttribute('aria-pressed',F.open);if(F.open){F.h24=false;$('#mp24').setAttribute('aria-pressed',false)}draw(true)};
$('#mp24').onclick=e=>{F.h24=!F.h24;e.currentTarget.setAttribute('aria-pressed',F.h24);if(F.h24){F.open=false;$('#mpOpen').setAttribute('aria-pressed',false)}draw(true)};
const setMode=l=>{$('.mp').classList.toggle('lista',l);$('#mpMl').setAttribute('aria-pressed',l);$('#mpMm').setAttribute('aria-pressed',!l)};$('#mpMl').onclick=()=>setMode(true);$('#mpMm').onclick=()=>setMode(false);
const setView=d3=>{$('#mpV3').setAttribute('aria-pressed',d3);$('#mpV2').setAttribute('aria-pressed',!d3);if(!map)return;map.easeTo({pitch:d3?52:0,bearing:d3?-16:0,duration:R?0:1200});if(map.getLayer('bld'))map.setPaintProperty('bld','fill-extrusion-height',d3?['coalesce',['get','render_height'],8]:0)};
$('#mpV3').onclick=()=>setView(true);$('#mpV2').onclick=()=>setView(false);
$('#mpHandle').onclick=()=>$('#mpPanel').classList.toggle('min');
$('.mp-hd').addEventListener('click',()=>{if($('#mpPanel').classList.contains('min'))$('#mpPanel').classList.remove('min')});
$('#mpQ').addEventListener('focus',()=>$('#mpPanel').classList.remove('min'));
if(window.maplibregl)setTimeout(()=>{if(map)map.on('dragstart',()=>{if(innerWidth<=900&&!$('#mpCard').classList.contains('on'))$('#mpPanel').classList.add('min')})},0);
(()=>{const m=document.createElement('div');m.className='mp-mob';const lg=document.querySelector('.mp-logo a');if(lg){const a=lg.cloneNode(true);a.className='lg';m.append(a)}const gl=document.querySelector('.mp-logo nav a');if(gl){const g=gl.cloneNode(true);g.className='gm';m.append(g)}document.querySelector('.mp').append(m);const sb=document.createElement('div');sb.className='mp-msb';sb.append(document.querySelector('.mp-search'));document.querySelector('.mp').append(sb);const tg=document.querySelector('.mp-tg');if(tg)document.querySelector('.mp-tools').append(tg)})();
/* sugestões da busca */
(()=>{const q=$('#mpQ');if(!q)return;const sg=document.createElement('div');sg.className='mp-sg';sg.setAttribute('role','listbox');q.parentNode.append(sg);let res=[],ix=-1;
const close=()=>{sg.classList.remove('on');ix=-1};
const go=l=>{close();q.blur();if($('#mpMl')&&$('#mpMl').getAttribute('aria-pressed')==='true')$('#mpMm').click();setTimeout(()=>pick(l.id,true),60)};
const show=()=>{const t=norm(q.value.trim());if(t.length<2){close();return}
res=ALL.map(l=>{const n=norm(l.nome);const s=n.startsWith(t)?0:n.split(/\s+/).some(w=>w.startsWith(t))?1:n.includes(t)?2:norm(CM[l.cat][1]).includes(t)?3:9;return[s,l]}).filter(x=>x[0]<9).sort((a,b)=>a[0]-b[0]||a[1].nome.localeCompare(b[1].nome)).slice(0,8).map(x=>x[1]);
sg.innerHTML=res.length?res.map((l,i)=>{const st=status(l.horario);return`<button type="button" role="option" data-i="${i}"><b style="background:${CM[l.cat][2]}"></b><span><strong>${esc(l.nome)}</strong><small>${esc(CM[l.cat][1])}${(l.end||l.endereco)?' · '+esc(l.end||l.endereco):''}</small></span>${st&&(st.k==='o'||st.k==='h')?'<em>Aberto</em>':''}</button>`}).join(''):'<p>Nenhum lugar com esse nome.</p>';
sg.classList.add('on');sg.querySelectorAll('button').forEach(b=>b.onclick=()=>go(res[+b.dataset.i]))};
q.addEventListener('input',show);q.addEventListener('focus',show);
q.addEventListener('keydown',e=>{const bs=[...sg.querySelectorAll('button')];if(e.key==='Enter'){e.preventDefault();if(res.length)go(res[Math.max(ix,0)])}else if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();ix=(ix+(e.key==='ArrowDown'?1:-1)+bs.length)%bs.length;bs.forEach((b,i)=>b.classList.toggle('k',i===ix))}else if(e.key==='Escape')close()});
document.addEventListener('pointerdown',e=>{if(!q.parentNode.contains(e.target))close()});})();
/* ===== intenções, perto de mim, roteiros, sobre ===== */
(()=>{
const SVG={pin:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s-7-6.1-7-11.5A7 7 0 0 1 19 9.5C19 14.9 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',rt:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8.5 18H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.5"/></svg>'};
const INT=[['almoco','Almoço agora',['restaurantes','japoneses','churrascarias','hamburguerias','pizzarias'],1],['cafe','Café para trabalhar',['cafes','padarias','docerias'],1],['noite','Aberto de madrugada',null,1],['kids','Programa com crianças',['parques','cultura','sorveterias','docerias'],0],['pet','Pet',['pet'],0]];
const ROT=[{id:'sab',t:'Um sábado em Moema',d:'Café da manhã de padaria, parque, almoço sem pressa, doce e jantar.',s:['w521400165','f62842a9da3bf540a7193dd02','w521402703','f519ba195498ede1bb53b5bad','w596585888']},
{id:'cafe',t:'Rota dos cafés',d:'Cinco paradas para quem trabalha de notebook ou gosta de um bom café.',s:['n12750164559','w1107535725','f4ebc503a30f88739f46f8e79','f530d0215498eb63e492780a7','w732230691']},
{id:'noite',t:'Noite no bairro',d:'Dos drinques ao som ao vivo, os bares que a W3W indica.',s:['f4bc6606251b376b008881b6f','f5442d69e498eb4249672d239','f50808fd0e4b0134247d7055b','f4beedc262c082d7f58ff3042','n9969076355']}];
const mp=document.querySelector('.mp');
/* filtro de intenção dentro de list() */
const _list=list;window.__it=null;window.__near=null;
const km=(a,b)=>{const R=6371,t=x=>x*Math.PI/180,dl=t(b[1]-a[1]),dn=t(b[0]-a[0]);const h=Math.sin(dl/2)**2+Math.cos(t(a[1]))*Math.cos(t(b[1]))*Math.sin(dn/2)**2;return 2*R*Math.asin(Math.sqrt(h))};
list=function(ign,noCat){let L=_list(ign,noCat);const it=window.__it&&INT.find(i=>i[0]===window.__it);
if(it){L=L.filter(l=>it[0]==='noite'?(l.st.k==='h'||(l.st.k==='o'&&['bares','noite','hamburguerias','pizzarias','farmacias','postos','mercados'].includes(l.cat))):(it[2].includes(l.cat)&&(!it[3]||l.st.k==='o'||l.st.k==='h')))}
if(window.__near){L.forEach(l=>l.km=km(window.__near,[l.lon,l.lat]));L.sort((a,b)=>a.km-b.km)}return L};
window.mpKm=l=>window.__near?km(window.__near,[l.lon,l.lat]):null;
/* faixa de atalhos acima da busca */
const bar=document.createElement('div');bar.className='mp-ints';
bar.innerHTML=`<button data-a="near">${SVG.pin}Perto de mim</button><button data-a="rot">${SVG.rt}Roteiros W3W</button>`+INT.map(i=>`<button data-i="${i[0]}">${i[1]}</button>`).join('');
mp.append(bar);
bar.querySelectorAll('[data-i]').forEach(b=>b.onclick=()=>{const on=window.__it===b.dataset.i;window.__it=on?null:b.dataset.i;bar.querySelectorAll('[data-i]').forEach(x=>x.setAttribute('aria-pressed',x===b&&!on));draw(true)});
let me=null;
bar.querySelector('[data-a=near]').onclick=e=>{const b=e.currentTarget;if(window.__near){window.__near=null;b.setAttribute('aria-pressed',false);me&&me.remove();draw();return}
if(!navigator.geolocation){toast('Seu navegador não permite localização.');return}b.classList.add('ld');
navigator.geolocation.getCurrentPosition(p=>{b.classList.remove('ld');const c=[p.coords.longitude,p.coords.latitude];
if(km(c,[-46.664,-23.601])>6){toast('Você está fora de Moema. Mostrando o centro do bairro.');window.__near=[-46.664,-23.601]}else window.__near=c;
b.setAttribute('aria-pressed',true);if(map&&window.maplibregl){const el=document.createElement('div');el.className='mp-me';me&&me.remove();me=new maplibregl.Marker({element:el}).setLngLat(window.__near).addTo(map);map.flyTo({center:window.__near,zoom:16,pitch:45,duration:1400})}draw()},
()=>{b.classList.remove('ld');toast('Não foi possível pegar sua localização. Verifique a permissão do navegador.')},{enableHighAccuracy:true,timeout:9000})};
/* roteiros */
const sh=document.createElement('div');sh.className='mp-sheet';mp.append(sh);
const openSheet=h=>{const t=document.querySelector('.mp-toast');t&&t.classList.remove('on');sh.innerHTML=`<div class="in"><button class="x" aria-label="Fechar">✕</button>${h}</div>`;sh.classList.add('on');sh.querySelector('.x').onclick=()=>sh.classList.remove('on');sh.onclick=e=>{if(e.target===sh)sh.classList.remove('on')}};
bar.querySelector('[data-a=rot]').onclick=()=>{openSheet(`<span class="ey">Roteiros W3W</span><h3>Moema em <em>um passeio.</em></h3><div class="rl">${ROT.map(r=>{const st=r.s.map(id=>ALL.find(l=>l.id===id)).filter(Boolean);return`<button data-r="${r.id}"><strong>${r.t}</strong><span>${r.d}</span><small>${st.map(l=>esc(l.nome)).join(' → ')}</small></button>`}).join('')}</div>`);
sh.querySelectorAll('[data-r]').forEach(b=>b.onclick=()=>{sh.classList.remove('on');rota(ROT.find(r=>r.id===b.dataset.r))})};
const strip=document.createElement('div');strip.className='mp-rt';mp.append(strip);
function rota(r){const st=r.s.map(id=>ALL.find(l=>l.id===id)).filter(Boolean);if(!st.length)return;mp.classList.add('rota');
strip.innerHTML=`<div class="rh"><span class="ey">Roteiro W3W</span><strong>${r.t}</strong><button class="x" aria-label="Fechar roteiro">✕</button></div><div class="st">${st.map((l,i)=>`<button data-id="${l.id}"><i>${i+1}</i><span>${esc(l.nome)}<small>${CM[l.cat][1]}</small></span></button>`).join('')}</div>`;
strip.querySelector('.x').onclick=fimRota;strip.querySelectorAll('[data-id]').forEach(b=>b.onclick=()=>pick(b.dataset.id,true));
if(map&&window.maplibregl){const fc={type:'FeatureCollection',features:[{type:'Feature',geometry:{type:'LineString',coordinates:st.map(l=>[l.lon,l.lat])},properties:{}},...st.map((l,i)=>({type:'Feature',geometry:{type:'Point',coordinates:[l.lon,l.lat]},properties:{n:String(i+1),id:l.id}}))]};
if(map.getSource('rota'))map.getSource('rota').setData(fc);else{map.addSource('rota',{type:'geojson',data:fc});
map.addLayer({id:'rota-l',type:'line',source:'rota',filter:['==',['geometry-type'],'LineString'],layout:{'line-cap':'round','line-join':'round'},paint:{'line-color':'#2F3742','line-width':4,'line-dasharray':[0.2,1.8]}});
map.addLayer({id:'rota-p',type:'circle',source:'rota',filter:['==',['geometry-type'],'Point'],paint:{'circle-radius':13,'circle-color':'#2F3742','circle-stroke-color':'#fff','circle-stroke-width':2.5}});
map.addLayer({id:'rota-n',type:'symbol',source:'rota',filter:['==',['geometry-type'],'Point'],layout:{'text-field':['get','n'],'text-font':['Noto Sans Regular'],'text-size':12,'text-allow-overlap':true},paint:{'text-color':'#fff'}});
map.on('click','rota-p',e=>pick(e.features[0].properties.id,true))}
['rota-l','rota-p','rota-n'].forEach(id=>map.setLayoutProperty(id,'visibility','visible'));
const b=new maplibregl.LngLatBounds();st.forEach(l=>b.extend([l.lon,l.lat]));map.fitBounds(b,{padding:{top:200,bottom:230,left:60,right:60},pitch:40,duration:1400})}}
function fimRota(){mp.classList.remove('rota');if(map&&map.getLayer('rota-l'))['rota-l','rota-p','rota-n'].forEach(id=>map.setLayoutProperty(id,'visibility','none'))}
/* sobre o mapa */
const WA='https://wa.me/5511940297871?text=';
const sobre=()=>openSheet(`<span class="ey">Mapa vivo de Moema · W3W</span><h3>O bairro inteiro, <em>num mapa só.</em></h3>
<p class="ld">Um guia vivo de Moema feito pela W3W Imóveis: restaurantes, cafés, bares, serviços e o que está aberto agora, para quem mora, trabalha ou está chegando no bairro.</p>
<div class="sb"><div><b>01</b><strong>Ache o que precisa</strong><span>Busque pelo nome ou use os atalhos: almoço agora, café para trabalhar, aberto de madrugada.</span></div><div><b>02</b><strong>Veja o que está aberto</strong><span>Horários conferidos nos sites dos lugares e, quando possível, confirmados pela W3W.</span></div><div><b>03</b><strong>Salve e saia andando</strong><span>Favorite seus lugares, siga os roteiros W3W e abra a rota no seu app de mapas.</span></div></div>
<h4>Faça parte</h4><div class="fp"><a href="${WA+encodeURIComponent('Olá! Tenho um negócio em Moema e quero aparecer no Mapa de Moema da W3W.')}" target="_blank" rel="noopener"><strong>Tenho um negócio em Moema</strong><span>Corrija seus dados, confirme o horário ou conheça os planos de destaque, cupom e roteiros.</span><i>Falar com a W3W →</i></a>
<a href="${WA+encodeURIComponent('Olá! Quero receber as novidades de Moema da W3W.')}" target="_blank" rel="noopener"><strong>Moro ou vou morar em Moema</strong><span>Receba novidades do bairro, lugares novos e roteiros no WhatsApp.</span><i>Quero receber →</i></a></div>`);
const mob=document.querySelector('.mp-mob');if(mob){const q=document.createElement('button');q.className='hq';q.setAttribute('aria-label','O que é o Mapa de Moema');q.textContent='?';q.onclick=sobre;mob.insertBefore(q,mob.querySelector('.gm'))}
/* aviso da primeira visita */
function toast(t,ms=4200){let el=document.querySelector('.mp-toast');if(!el){el=document.createElement('div');el.className='mp-toast';mp.append(el)}el.innerHTML=t;el.classList.add('on');clearTimeout(el._t);el._t=setTimeout(()=>el.classList.remove('on'),ms);el.onclick=()=>el.classList.remove('on')}
window.mpToast=toast;
let seen=false;try{seen=localStorage.getItem('mpSeen')}catch(e){}
if(!seen){setTimeout(()=>{toast('<strong>Moema inteira num mapa.</strong> Veja o que está aberto agora, busque, siga os roteiros e salve favoritos. <u>Saiba mais</u>',6500);const el=document.querySelector('.mp-toast');el.onclick=()=>{el.classList.remove('on');sobre()}},1800);try{localStorage.setItem('mpSeen','1')}catch(e){}}
})();
setInterval(()=>draw(),60000);new MutationObserver(()=>{const p=$('#mpPanel');if(p.classList.contains('min'))p.scrollTop=0}).observe($('#mpPanel'),{attributes:true,attributeFilter:['class']});
/* mapa com estilo próprio */
if(!window.maplibregl)return;
const T='https://tiles.openfreemap.org';
const P={paper:'#EEEBE5',block:'#E7E3DB',park:'#DCE3E4',water:'#BCD0E4',bld:'#E2DDD3',road:'#FFFFFF',case:'#D6CFC3',major:'#FBF9F5',ink:'#5A5F69',label:'#8A8478'};
const style={version:8,glyphs:T+'/fonts/{fontstack}/{range}.pbf',sources:{om:{type:'vector',url:T+'/planet'}},layers:[
{id:'bg',type:'background',paint:{'background-color':P.paper}},
{id:'res',type:'fill',source:'om','source-layer':'landuse',filter:['in',['get','class'],['literal',['residential','commercial','retail']]],paint:{'fill-color':P.block}},
{id:'park',type:'fill',source:'om','source-layer':'park',paint:{'fill-color':P.park}},
{id:'green',type:'fill',source:'om','source-layer':'landcover',filter:['in',['get','class'],['literal',['grass','wood']]],paint:{'fill-color':P.park,'fill-opacity':.8}},
{id:'water',type:'fill',source:'om','source-layer':'water',paint:{'fill-color':P.water}},
{id:'water-ln',type:'line',source:'om','source-layer':'water',paint:{'line-color':'#A9C1DA','line-width':.8}},
{id:'rd-case',type:'line',source:'om','source-layer':'transportation',filter:['in',['get','class'],['literal',['primary','secondary','tertiary','trunk','motorway']]],layout:{'line-cap':'round','line-join':'round'},paint:{'line-color':P.case,'line-width':['interpolate',['exponential',1.6],['zoom'],12,1.5,18,26]}},
{id:'rd-minor',type:'line',source:'om','source-layer':'transportation',filter:['in',['get','class'],['literal',['minor','service','street','residential']]],layout:{'line-cap':'round','line-join':'round'},paint:{'line-color':P.road,'line-width':['interpolate',['exponential',1.6],['zoom'],13,.6,18,14]}},
{id:'rd-major',type:'line',source:'om','source-layer':'transportation',filter:['in',['get','class'],['literal',['primary','secondary','tertiary','trunk','motorway']]],layout:{'line-cap':'round','line-join':'round'},paint:{'line-color':P.major,'line-width':['interpolate',['exponential',1.6],['zoom'],12,1,18,22]}},
{id:'rail',type:'line',source:'om','source-layer':'transportation',filter:['==',['get','class'],'rail'],paint:{'line-color':'#B9B2A6','line-width':1,'line-dasharray':[3,3]}},
{id:'bld',type:'fill-extrusion',source:'om','source-layer':'building',minzoom:14,paint:{'fill-extrusion-color':['interpolate',['linear'],['coalesce',['get','render_height'],10],0,'#E4DFD6',60,'#D9D3C8',140,'#CEC7BA'],'fill-extrusion-height':['coalesce',['get','render_height'],8],'fill-extrusion-base':['coalesce',['get','render_min_height'],0],'fill-extrusion-opacity':.92}},
{id:'rd-lbl',type:'symbol',source:'om','source-layer':'transportation_name',minzoom:14,layout:{'symbol-placement':'line','text-field':['get','name'],'text-font':['Noto Sans Regular'],'text-size':['interpolate',['linear'],['zoom'],14,9.5,18,13],'text-letter-spacing':.08,'text-transform':'uppercase'},paint:{'text-color':P.label,'text-halo-color':P.paper,'text-halo-width':1.4}},
{id:'park-lbl',type:'symbol',source:'om','source-layer':'park',filter:['has','name'],layout:{'text-field':['get','name'],'text-font':['Noto Sans Italic'],'text-size':13,'text-letter-spacing':.04},paint:{'text-color':'#6E8086','text-halo-color':P.park,'text-halo-width':1.2}},
{id:'place',type:'symbol',source:'om','source-layer':'place',filter:['in',['get','class'],['literal',['suburb','neighbourhood','quarter']]],layout:{'text-field':['upcase',['get','name']],'text-font':['Noto Sans Regular'],'text-size':['interpolate',['linear'],['zoom'],12,10,16,15],'text-letter-spacing':.32},paint:{'text-color':P.ink,'text-halo-color':P.paper,'text-halo-width':2}}
]};
map=new maplibregl.Map({container:'mpMap',style,center:[-46.664,-23.601],zoom:R?14.4:13.2,pitch:R?40:0,bearing:R?-14:0,attributionControl:false,maxBounds:[[-46.74,-23.66],[-46.59,-23.55]]});
map.addControl(new maplibregl.NavigationControl({showCompass:true,visualizePitch:true}),'bottom-right');
map.addControl(new maplibregl.AttributionControl({compact:true,customAttribution:'© <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a> · Dados de lugares: <a href="https://foursquare.com" target="_blank">Foursquare</a> · <a href="https://openfreemap.org" target="_blank">OpenFreeMap</a>'}),'bottom-left');
map.on('load',()=>{
map.addSource('locais',{type:'geojson',data:geo(list())});
map.addLayer({id:'halo',type:'circle',source:'locais',filter:['==',['get','aberto'],1],paint:{'circle-radius':['interpolate',['linear'],['zoom'],13,6,18,16],'circle-color':['get','cor'],'circle-opacity':.18,'circle-blur':.4}});
map.addLayer({id:'pts',type:'circle',source:'locais',paint:{'circle-radius':['interpolate',['linear'],['zoom'],13,['case',['==',['get','dest'],1],5,3],18,['case',['==',['get','dest'],1],11,7]],'circle-color':['get','cor'],'circle-stroke-color':'#fff','circle-stroke-width':['interpolate',['linear'],['zoom'],13,1,18,2.5],'circle-opacity':['case',['==',['get','aberto'],1],1,.55]}});
map.addLayer({id:'sel',type:'circle',source:'locais',filter:['==',['get','id'],''],paint:{'circle-radius':['interpolate',['linear'],['zoom'],13,10,18,22],'circle-color':'rgba(0,0,0,0)','circle-stroke-color':'#14171C','circle-stroke-width':2}});
map.addLayer({id:'dest-lbl',type:'symbol',source:'locais',filter:['==',['get','dest'],1],minzoom:14,layout:{'text-field':['get','nome'],'text-font':['Noto Sans Regular'],'text-size':12,'text-offset':[0,1.3],'text-anchor':'top'},paint:{'text-color':'#14171C','text-halo-color':'#fff','text-halo-width':1.6}});
map.on('click',e=>{const r=innerWidth<=900?16:9,p=e.point,f=map.queryRenderedFeatures([[p.x-r,p.y-r],[p.x+r,p.y+r]],{layers:['pts','dest-lbl'].filter(id=>map.getLayer(id))});if(!f.length)return;let b=f[0],bd=1e9;f.forEach(x=>{const q=map.project(x.geometry.coordinates),d=(q.x-p.x)**2+(q.y-p.y)**2;if(d<bd){bd=d;b=x}});pick(b.properties.id,true)});
map.on('mouseenter','pts',e=>{map.getCanvas().style.cursor='pointer';hover(e.features[0].properties.id)});
map.on('mouseleave','pts',()=>{map.getCanvas().style.cursor='';pop&&pop.remove()});
/* entrada cinematográfica */
if(!R)setTimeout(()=>map.flyTo({center:[-46.664,-23.601],zoom:14.6,pitch:52,bearing:-16,padding:pad(),duration:3200,essential:true}),400);
let pulse=0;if(!R)(function an(){pulse=(pulse+.02)%1;if(map.getLayer('halo'))map.setPaintProperty('halo','circle-opacity',.12+Math.sin(pulse*Math.PI*2)*.08);requestAnimationFrame(an)})();
});
})();
"""
