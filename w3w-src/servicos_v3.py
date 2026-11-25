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
.z3-bg{position:absolute;inset:0;will-change:transform}
.z3-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#05070B 0%,rgba(5,7,11,.75) 40%,rgba(5,7,11,.15) 100%),linear-gradient(180deg,transparent 60%,#05070B 100%)}
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
/* manifesto (css) */
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
.z3-extra{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:16px}
.z3-extra div{padding:22px;border-radius:18px;border:1px solid var(--ln)}
.z3-extra b{display:block;font:300 24px var(--sans);margin-top:12px}
.z3-note{margin-top:22px;color:var(--tx3);font-size:13px}
/* final */
.z3-end{position:relative;padding:24vh clamp(20px,5vw,72px);overflow:hidden;text-align:center}
.z3-end p{color:var(--tx2);font-size:19px;margin:34px auto 38px;max-width:46ch}
.z3-end .z3-cta{justify-content:center}
.rv{opacity:0;transform:translateY(40px);transition:opacity 1s var(--e),transform 1s var(--e)}
.rv.on{opacity:1;transform:none}
@media (max-width:900px){
.z3-hud{display:none}.z3-scroll{display:none!important}
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

/* header e rodapé escuros nesta página */
body:has(.z3) .hd svg,body:has(.z3) .hd svg *{fill:#EEF2F8!important;color:#EEF2F8!important}
body:has(.z3) .hd .brand *{color:#8A94A6!important}
body:has(.z3) .hd{background:rgba(10,12,16,.82);border-bottom:1px solid rgba(238,242,248,.08);color:#EEF2F8}
body:has(.z3) .hd a,body:has(.z3) .hd button,body:has(.z3) .hd .brand{color:#EEF2F8}
body:has(.z3) .hd [class*=cta],body:has(.z3) .hd a[class*=btn]{border-color:rgba(238,242,248,.35)!important;color:#EEF2F8!important;background:transparent!important}
body:has(.z3) .hd span,body:has(.z3) .hd small{color:#8A94A6}
body:has(.z3) .hd button span,body:has(.z3) .hd button i{background:#EEF2F8}
body:has(.z3) .ft{background:#05070B;border-top:1px solid rgba(238,242,248,.06)}
body:has(.z3) .ft-n a{font-size:10.5px!important;font-weight:300!important;letter-spacing:.22em!important;color:#8A94A6!important}
body:has(.z3) .ft-n a:hover{color:#EEF2F8!important}
body:has(.z3) .ft-c a{font-size:13px!important;font-weight:300!important;letter-spacing:.04em!important;color:#8A94A6!important}
body:has(.z3) .ft-bot{font-size:9px!important;font-weight:300;letter-spacing:.2em!important;opacity:.6}
body:has(.z3) .ft-kco{font-size:9px!important;opacity:.45}
body:has(.z3) .ft .brand svg{opacity:.7;transform:scale(.85)}
/* mockups dos serviços */
.z3-card{background:radial-gradient(120% 80% at 70% 0%,rgba(156,203,255,.12),transparent 60%),#0A0E15}
.z3-card::after{display:none}
.z3-cin{justify-content:flex-end}
.z3-k{position:absolute;top:clamp(20px,2.6vw,32px);left:clamp(22px,3vw,40px);z-index:3;font:500 11px var(--mono);letter-spacing:.14em;color:var(--ac)}
.z3-vis{position:absolute;left:0;right:0;top:0;height:58%;display:grid;place-items:center;pointer-events:none}
.z3-vis img{position:static;width:100%;height:100%;object-fit:cover;filter:none;transform:none!important}
.z3-ph{width:min(46%,210px);aspect-ratio:9/17;border-radius:26px;border:1px solid rgba(238,242,248,.18);background:#0d1118;padding:8px;box-shadow:0 30px 60px -20px #000;transform:rotate(-4deg) translateY(12%)}
.z3-ph .sc{border-radius:19px;overflow:hidden;height:100%;background:#fff;display:flex;flex-direction:column;color:#111;font:11px var(--sans)}
.z3-ph .tp{display:flex;align-items:center;gap:6px;padding:8px}
.z3-ph .tp i{width:18px;height:18px;border-radius:50%;background:#111}
.z3-ph .tp small{display:block;color:#888;font-size:9px}
.z3-ph .im{flex:1;overflow:hidden}
.z3-ph .bt{display:flex;justify-content:space-between;padding:8px;background:#1D6FE8;color:#fff;font-weight:500}
.z3-chip2{position:absolute;padding:8px 11px;border-radius:10px;background:rgba(11,15,23,.85);border:1px solid var(--ln);font:500 10px var(--mono);letter-spacing:.06em;color:var(--tx2);backdrop-filter:blur(8px)}
.z3-chip2 b{color:var(--ok);font-weight:500}
.z3-wa{width:min(80%,330px);display:grid;gap:8px;transform:translateY(8%)}
.z3-wa .m{background:#13221c;border:1px solid rgba(123,224,179,.2);border-radius:14px 14px 14px 4px;padding:12px 14px;font:13px/1.45 var(--sans);color:#d8efe5}
.z3-wa .m b{color:#7BE0B3;font:500 10px var(--mono);letter-spacing:.1em;display:block;margin-bottom:6px}
.z3-wa .m.c{display:grid;grid-template-columns:62px 1fr;gap:10px;align-items:center}
.z3-wa .m.c img{width:62px;height:62px;border-radius:8px}
.z3-wa time{font:10px var(--mono);color:var(--tx3);justify-self:end}
.z3-fan{position:relative;width:70%;height:78%}
.z3-fan div{position:absolute;top:10%;width:52%;aspect-ratio:4/5;border-radius:12px;overflow:hidden;box-shadow:0 24px 50px -16px #000;border:1px solid rgba(238,242,248,.12)}
.z3-fan div:nth-child(1){left:0;transform:rotate(-9deg)}
.z3-fan div:nth-child(2){left:24%;transform:translateY(-6%);z-index:2}
.z3-fan div:nth-child(3){left:48%;transform:rotate(9deg)}
.z3-fan span{position:absolute;left:10px;right:10px;bottom:10px;font:300 15px/1.05 var(--serif);font-style:italic;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.6)}
.z3-br{width:min(84%,400px);border-radius:12px;overflow:hidden;border:1px solid rgba(238,242,248,.16);background:#0d1118;box-shadow:0 30px 60px -20px #000;transform:perspective(900px) rotateX(8deg) translateY(10%)}
.z3-br .bar{display:flex;gap:5px;align-items:center;padding:9px 12px;border-bottom:1px solid var(--ln)}
.z3-br .bar i{width:7px;height:7px;border-radius:50%;background:rgba(238,242,248,.2)}
.z3-br .bar span{margin-left:10px;font:10px var(--mono);color:var(--tx3)}
.z3-br .hero{height:120px;position:relative}
.z3-br .hero b{position:absolute;left:14px;bottom:12px;font:300 20px/1 var(--sans);color:#fff;text-shadow:0 2px 10px rgba(0,0,0,.5)}
.z3-br .bd{display:flex;justify-content:space-between;align-items:center;padding:12px 14px;gap:10px}
.z3-br .bd small{font:10px var(--mono);color:var(--tx2)}
.z3-br .bd em{font:500 11px var(--sans);font-style:normal;color:#05070B;background:var(--tx);padding:7px 11px;border-radius:999px}
/* final */
.z3-end{padding:16vh clamp(20px,5vw,72px) 14vh!important;text-align:left!important;border-top:1px solid var(--ln)}
.z3-end::before{content:"";position:absolute;right:-10%;top:-30%;width:70vw;height:70vw;border-radius:50%;background:radial-gradient(circle,rgba(156,203,255,.12),transparent 60%);pointer-events:none}
.z3-endg{position:relative;display:grid;grid-template-columns:1.4fr 1fr;gap:6vw;align-items:end}
.z3-end h2{font:300 clamp(56px,9vw,150px)/.9 var(--sans)!important;letter-spacing:-.05em!important;margin:0!important;color:var(--tx)}
.z3-end h2 em{display:block}
.z3-end ul{list-style:none;padding:0;margin:0 0 30px;display:grid;gap:0;border-top:1px solid var(--ln)}
.z3-end li{display:flex;gap:16px;padding:14px 0;border-bottom:1px solid var(--ln);color:var(--tx2);font-size:15px}
.z3-end li span{font:500 11px var(--mono);color:var(--ac);padding-top:3px}
@media (max-width:900px){.z3-endg{grid-template-columns:1fr}}
.z3-h1b{font-size:clamp(46px,8.4vw,150px)!important;max-width:13ch}
.z3-proof{display:flex;gap:28px;flex-wrap:wrap;margin-top:4vh;padding-top:22px;border-top:1px solid var(--ln);opacity:0;animation:z3f 1s .9s var(--e) forwards}
.z3-proof span{font:13px var(--sans);color:var(--tx2)}
.z3-proof b{color:var(--tx);font-weight:400}
.z3-ey{display:block;color:var(--ac)!important;margin-bottom:14px}
.z3-in{padding:0 clamp(20px,5vw,72px)}
.z3-sh h2,.z3-faq h2{font:300 clamp(40px,5.2vw,88px)/.98 var(--sans);letter-spacing:-.045em;margin:0;max-width:16ch}
.z3-lead{color:var(--tx2);font-size:18px;line-height:1.55;max-width:56ch;margin:24px 0 0}
.z3-como{padding:20vh 0 4vh;border-top:1px solid var(--ln)}
.z3-flow{list-style:none;padding:0;margin:64px 0 0;display:grid;grid-template-columns:repeat(5,1fr);border-top:1px solid var(--ln)}
.z3-flow li{padding:28px 22px 0 0;position:relative}
.z3-flow li::before{content:"";position:absolute;top:-4px;left:0;width:7px;height:7px;border-radius:50%;background:var(--ac);box-shadow:0 0 0 5px rgba(156,203,255,.12)}
.z3-flow span{font:500 11px var(--mono);color:var(--tx3);letter-spacing:.12em}
.z3-flow b{display:block;font:400 clamp(22px,1.9vw,30px)/1.1 var(--sans);letter-spacing:-.02em;margin:14px 0 10px}
.z3-flow p{color:var(--tx2);font-size:15px;line-height:1.5;margin:0}
.z3-flow li:nth-child(2){transition-delay:.08s}.z3-flow li:nth-child(3){transition-delay:.16s}.z3-flow li:nth-child(4){transition-delay:.24s}.z3-flow li:nth-child(5){transition-delay:.32s}
.z3-quem{padding:20vh 0;border-top:1px solid var(--ln)}
.z3-qg{display:grid;grid-template-columns:1fr 1fr;gap:5vw;margin-top:64px}
.z3-team{display:grid;gap:12px}
.z3-team>div{padding:26px 28px;border:1px solid var(--ln);border-radius:20px;background:var(--bg2);transition:border-color .4s}
.z3-team>div:hover{border-color:rgba(156,203,255,.35)}
.z3-team b{display:block;font:400 26px/1.1 var(--sans);letter-spacing:-.02em;margin:10px 0 8px}
.z3-team p{color:var(--tx2);margin:0;font-size:15px;line-height:1.5}
.z3-time{position:relative;padding-left:28px;border-left:1px solid var(--ln)}
.z3-time>div{position:relative;padding:22px 0 26px}
.z3-time>div::before{content:"";position:absolute;left:-32px;top:30px;width:7px;height:7px;border-radius:50%;background:var(--tx);box-shadow:0 0 0 5px var(--bg)}
.z3-time i{font:500 11px var(--mono);font-style:normal;color:var(--ac);letter-spacing:.12em;text-transform:uppercase}
.z3-time b{display:block;font:400 22px/1.15 var(--sans);margin:8px 0 6px}
.z3-time p{color:var(--tx2);margin:0;font-size:15px}
.z3-cfg{display:grid;grid-template-columns:1.25fr 1fr;gap:16px}
.z3-ctl{display:grid;gap:34px;padding:36px;border:1px solid var(--ln);border-radius:24px;background:var(--bg2)}
.z3-hint{color:var(--tx3);font-size:13px;line-height:1.45;margin:8px 0 0}
.z3-seg{display:flex;gap:8px;margin-top:14px}
.z3-seg button{flex:1;height:56px;border-radius:14px;border:1px solid var(--ln);background:none;color:var(--tx);font:300 22px var(--sans);cursor:pointer;transition:background .3s,color .3s,border-color .3s}
.z3-seg button[aria-pressed=true]{background:var(--tx);color:#05070B;border-color:var(--tx)}
.z3-seg button:focus-visible{outline:2px solid var(--ac);outline-offset:3px}
.z3-ctl .z3-tg{margin-top:14px;display:flex;width:max-content;max-width:100%}
.z3-ctl>div>.mono{display:block}
.z3-sw{display:flex;gap:16px;align-items:flex-start;cursor:pointer;position:relative}
.z3-sw input{position:absolute;opacity:0}
.z3-sw>span{flex:none;width:48px;height:28px;border-radius:999px;background:rgba(238,242,248,.14);position:relative;transition:background .3s;margin-top:2px}
.z3-sw>span::after{content:"";position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:var(--tx);transition:transform .4s var(--e)}
.z3-sw input:checked+span{background:var(--ac)}
.z3-sw input:checked+span::after{transform:translateX(20px);background:#05070B}
.z3-sw input:focus-visible+span{outline:2px solid var(--ac);outline-offset:3px}
.z3-sw b{font:400 18px var(--sans)}
.z3-sum{padding:36px;border-radius:24px;background:linear-gradient(170deg,rgba(156,203,255,.16),var(--bg2) 60%);border:1px solid rgba(156,203,255,.35);display:flex;flex-direction:column}
.z3-tot{display:flex;align-items:baseline;gap:8px;margin:18px 0 22px}
.z3-tot b{font:200 clamp(56px,6vw,92px)/1 var(--sans);letter-spacing:-.05em}
.z3-tot small{color:var(--tx2);font-size:16px}
.z3-sum ul{list-style:none;padding:0;margin:0 0 28px;border-top:1px solid var(--ln)}
.z3-sum li{display:flex;justify-content:space-between;gap:12px;padding:12px 0;border-bottom:1px solid var(--ln);font-size:14px;color:var(--tx2)}
.z3-sum li b{color:var(--tx);font-weight:400}
.z3-sum .z3-btn{justify-content:center;margin-top:auto}
.z3-faq{padding:18vh 0;border-top:1px solid var(--ln)}
.z3-fg{display:grid;grid-template-columns:1fr 1.3fr;gap:6vw}
.z3-faq details{border-bottom:1px solid var(--ln);padding:22px 0}
.z3-faq details:first-child{border-top:1px solid var(--ln)}
.z3-faq summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:20px;font:400 19px var(--sans)}
.z3-faq summary::-webkit-details-marker{display:none}
.z3-faq summary::after{content:"+";color:var(--ac);font-weight:300;transition:transform .3s}
.z3-faq details[open] summary::after{transform:rotate(45deg)}
.z3-faq details p{color:var(--tx2);line-height:1.55;margin:14px 0 0;max-width:60ch}
@media (max-width:900px){.z3-flow{grid-template-columns:1fr;border-top:0;border-left:1px solid var(--ln);margin-left:4px}.z3-flow li{padding:0 0 30px 26px}.z3-flow li::before{left:-4px;top:4px}.z3-qg,.z3-cfg,.z3-fg{grid-template-columns:1fr}.z3-ctl,.z3-sum{padding:26px}.z3-proof{gap:14px 22px}}

.z3-man2{position:relative;height:240vh}
.z3-mst{position:sticky;top:0;height:100svh;overflow:hidden}
.z3-mimg{position:absolute;inset:0;margin:0}
.z3-mimg img{width:100%;height:100%;object-fit:cover;object-position:50% 35%;scale:calc(1.14 - var(--m,0)*.14);filter:brightness(.42) saturate(.7)}
.z3-mimg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,#05070B 0%,transparent 22%,transparent 78%,#05070B 100%)}
.z3-ml{position:absolute;margin:0;white-space:nowrap;font:300 clamp(40px,8vw,160px)/1 var(--sans);letter-spacing:-.05em;color:var(--tx);opacity:0;translate:0 40px;transition:opacity 1s var(--e),translate 1.2s var(--e)}
.z3-ml.on{opacity:1;translate:0 0}
.z3-ml em{font-weight:200}
.l1{left:clamp(20px,5vw,72px);top:12%}.l2{right:clamp(20px,5vw,72px);top:29%}.l3{left:clamp(20px,9vw,140px);top:46%}.l4{right:clamp(20px,9vw,160px);top:63%}.l5{left:clamp(20px,5vw,72px);top:78%;font-size:clamp(52px,11vw,210px)}
.z3-msig{position:absolute;right:clamp(20px,5vw,72px);bottom:5%;color:var(--tx3)!important}
.z3-sv{padding:18vh 0 8vh;border-top:1px solid var(--ln)}
.z3-svg{display:grid;grid-template-columns:1.05fr 1fr;gap:6vw;margin-top:8vh}
.z3-stage{position:sticky;top:14vh;height:72vh;border-radius:28px;border:1px solid var(--ln);background:radial-gradient(90% 70% at 50% 0%,rgba(156,203,255,.14),transparent 60%),#0A0E15;overflow:hidden}
.z3-st{position:absolute;inset:0;display:grid;place-items:center;opacity:0;transform:scale(.96);transition:opacity .7s var(--e),transform .9s var(--e)}
.z3-st.on{opacity:1;transform:none}
.z3-items{display:grid}
.z3-it{min-height:72vh;display:flex;flex-direction:column;justify-content:center;padding:6vh 0;border-bottom:1px solid var(--ln);opacity:.35;transition:opacity .5s}
.z3-it.act{opacity:1}
.z3-it:last-child{border:0}
.z3-k2{color:var(--ac)!important}
.z3-it h3{font:300 clamp(36px,3.6vw,60px)/1 var(--sans);letter-spacing:-.04em;margin:16px 0 18px}
.z3-it p{color:var(--tx2);font-size:18px;line-height:1.55;margin:0;max-width:46ch}
.z3-it ul{list-style:none;padding:0;margin:26px 0 30px;display:grid;grid-template-columns:1fr 1fr;gap:10px 20px;font-size:15px;color:var(--tx)}
.z3-it li::before{content:"→ ";color:var(--ac)}
.z3-buy{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;padding-top:22px;border-top:1px solid var(--ln)}
.z3-buy span{font:500 12px var(--mono);letter-spacing:.06em;color:var(--tx2)}
.z3-buy .z3-btn{height:48px}
.z3-lk{font:500 12px var(--mono);letter-spacing:.06em;color:var(--tx2)!important;text-decoration:none}.z3-lk:hover{color:var(--tx)!important}
.z3-mv{display:none;position:relative}
.z3-st img,.z3-mv img{width:100%;height:100%;object-fit:cover;display:block}
.z3-wa .m.c img{width:62px!important;height:62px!important;border-radius:8px}
/* mockups maiores no palco */
.z3-st .z3-ph,.z3-mv .z3-ph{width:min(62%,280px);transform:rotate(-3deg)}
.z3-st .z3-chip2{font-size:11px}
.z3-st .z3-wa,.z3-mv .z3-wa{width:min(84%,420px);transform:none}
.z3-st .z3-wa .m{font-size:15px}
.z3-st .z3-fan,.z3-mv .z3-fan{width:92%;height:82%}
.z3-fan div{width:56%;top:8%}
.z3-fan span{font-size:clamp(18px,1.8vw,26px)}
.z3-br{width:min(92%,560px)!important;transform:perspective(1200px) rotateX(6deg)!important}
.z3-br .lp{background:#F4F2EE;color:#111}
.z3-br .nav{display:flex;justify-content:space-between;align-items:center;padding:10px 14px;font:10px var(--sans);color:#555}
.z3-br .nav b{font:600 12px var(--sans);letter-spacing:.2em;color:#111}
.z3-br .lp .hero{position:relative;height:auto;display:grid;grid-template-columns:1.3fr 1fr;min-height:240px}
.z3-br .lp .hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.z3-br .lp .hero .tx{position:relative;align-self:end;padding:16px;color:#fff;background:linear-gradient(0deg,rgba(0,0,0,.6),transparent)}
.z3-br .lp .hero .tx small{font:9px var(--mono);letter-spacing:.14em;opacity:.8}
.z3-br .lp .hero .tx b{display:block;font:300 24px/1.02 var(--sans);letter-spacing:-.02em;margin-top:6px}
.z3-br .form{position:relative;margin:14px;background:#fff;border-radius:10px;padding:12px;display:grid;gap:7px;align-content:start;box-shadow:0 10px 30px rgba(0,0,0,.25)}
.z3-br .form small{font:600 11px var(--sans);color:#111}
.z3-br .form i{font:10px var(--sans);font-style:normal;color:#999;border:1px solid #e3e3e3;border-radius:6px;padding:7px 8px}
.z3-br .form em{font:600 10px var(--sans);font-style:normal;background:#111;color:#fff;border-radius:999px;padding:8px;text-align:center}
@media (max-width:900px){
.z3-svg{grid-template-columns:1fr}.z3-stage{display:none}
.z3-it{min-height:0;opacity:1;padding:5vh 0}
.z3-mv{display:grid;position:relative;place-items:center;height:380px;margin-bottom:28px;border-radius:22px;border:1px solid var(--ln);background:radial-gradient(90% 70% at 50% 0%,rgba(156,203,255,.14),transparent 60%),#0A0E15;overflow:hidden}
.z3-it ul{grid-template-columns:1fr}
.z3-ml{white-space:normal;max-width:92vw}
.z3-br .lp .hero{grid-template-columns:1fr 1fr;min-height:200px}
}

.z3-dash{position:absolute;right:clamp(20px,4vw,64px);top:190px;width:min(46vw,760px);display:grid;grid-template-columns:repeat(3,1fr);gap:14px;opacity:.9}
.z3-dash>div{border:1px solid rgba(238,242,248,.09);border-radius:18px;background:rgba(11,15,23,.6);padding:18px 20px}
.z3-dash span{font:500 10px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--tx3)}
.dk b{display:block;font:200 clamp(30px,3vw,52px)/1 var(--sans);letter-spacing:-.04em;margin:12px 0 8px;color:var(--tx)}
.dk b em{font-style:normal}
.dk i{font:500 11px var(--mono);font-style:normal;color:var(--ok)}
.dch{grid-column:span 2}
.dch svg{width:100%;height:200px;margin-top:12px;display:block}
.dch .ln{stroke-dasharray:900;stroke-dashoffset:900;animation:z3ln 2.4s .5s var(--e) forwards}
.dch .ar{opacity:0;animation:z3f 1.2s 1.4s forwards}
@keyframes z3ln{to{stroke-dashoffset:0}}
.dbar p{margin:16px 0 0;position:relative;height:30px;border-radius:8px;background:rgba(238,242,248,.04);overflow:hidden}
.dbar p i{position:absolute;inset:0 auto 0 0;width:0;background:linear-gradient(90deg,rgba(156,203,255,.45),rgba(156,203,255,.15));animation:z3w 1.6s 1s var(--e) forwards}
@keyframes z3w{to{width:var(--w)}}
.dbar p b{position:relative;font:400 12px/30px var(--sans);padding-left:10px}
.z3-hud{display:none!important}
@media (max-width:900px){.z3-dash{width:150vw;right:-60vw;top:90px;opacity:.35}}
/* quebras de título */
.z3-sh h2 em,.z3-plh h2 em,.z3-dos h2 em,.z3-faq h2 em{display:block}
/* manifesto tipográfico */
.z3-man3{padding:24vh clamp(20px,5vw,72px);position:relative;overflow:hidden;border-top:1px solid var(--ln)}
.z3-man3::before{content:"";position:absolute;left:50%;top:50%;width:80vw;height:80vw;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle,rgba(156,203,255,.08),transparent 60%);pointer-events:none}
.z3-mg{position:relative;display:grid;grid-template-columns:1fr 3fr;gap:4vw}
.z3-mg aside{border-top:1px solid var(--ln);padding-top:18px}
.z3-mg aside p{color:var(--tx3);font-size:13px;line-height:1.6;margin:18px 0 0;max-width:24ch}
.z3-mt{margin:0;font:300 clamp(34px,5.4vw,100px)/1.04 var(--sans);letter-spacing:-.05em}
@media (min-width:901px){.z3-mt span{white-space:nowrap}}
.z3-mt span{display:block}
.z3-mt span:nth-child(2){padding-left:8%}
.z3-mt span:nth-child(3){padding-left:16%}
.z3-mt span:nth-child(4){padding-left:22%}
.z3-mt .w{opacity:.13;transition:opacity .3s,color .3s}
.z3-mt .w.on{opacity:1}
.z3-mt em .w.on,.z3-mt em.w.on{color:var(--ac)}
@media (max-width:900px){.z3-mg{grid-template-columns:1fr}.z3-mt span{padding-left:0!important}}

.z3-orbs{position:absolute;inset:0;pointer-events:none;z-index:0;overflow:hidden}
.z3-orbs i{position:absolute;width:46vw;height:46vw;border-radius:50%;filter:blur(80px);opacity:.10;background:#9CCBFF}
.z3-orbs i:nth-child(1){left:-12vw;top:120vh}.z3-orbs i:nth-child(2){right:-14vw;top:260vh;background:#7BE0B3;opacity:.06}.z3-orbs i:nth-child(3){left:20vw;top:420vh}
.z3>section,.z3>div:not(.z3-orbs):not(.z3-glow){position:relative;z-index:1}

/* liquid glass */
.z3-btn{position:relative;overflow:hidden;isolation:isolate;backdrop-filter:blur(18px) saturate(1.8);-webkit-backdrop-filter:blur(18px) saturate(1.8);border:1px solid rgba(255,255,255,.22)!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.35),inset 0 -1px 0 rgba(255,255,255,.06),0 10px 30px -12px rgba(0,0,0,.7);transition:transform .5s var(--e),box-shadow .4s,background .3s,color .3s}
.z3-btn.s{background:linear-gradient(180deg,rgba(255,255,255,.14),rgba(255,255,255,.04));color:var(--tx)}
.z3-btn.p{background:linear-gradient(180deg,rgba(255,255,255,.95),rgba(220,232,248,.82));color:#05070B;border-color:rgba(255,255,255,.6)!important}
.z3-btn::before{content:"";position:absolute;inset:0;z-index:-1;background:radial-gradient(120px 60px at var(--mx,50%) var(--my,0%),rgba(255,255,255,.55),transparent 70%);opacity:.0;transition:opacity .3s}
.z3-btn:hover::before{opacity:1}
.z3-btn::after{content:"";position:absolute;top:0;left:-60%;width:40%;height:100%;z-index:-1;background:linear-gradient(100deg,transparent,rgba(255,255,255,.45),transparent);transform:skewX(-20deg);animation:z3sh 4.5s 2s infinite}
@keyframes z3sh{0%,70%{left:-60%}100%{left:130%}}
.z3-btn:hover{box-shadow:inset 0 1px 0 rgba(255,255,255,.5),0 18px 40px -14px rgba(156,203,255,.45)}
.z3-seg button,.z3-tg,.z3-ctl,.z3-sum,.z3-team>div{backdrop-filter:blur(14px) saturate(1.5);-webkit-backdrop-filter:blur(14px) saturate(1.5)}
.z3-tg i{background:linear-gradient(180deg,#fff,rgba(220,232,248,.85));box-shadow:inset 0 1px 0 #fff,0 6px 18px -6px rgba(156,203,255,.6)}
.z3-seg button[aria-pressed=true]{background:linear-gradient(180deg,#fff,rgba(220,232,248,.85));box-shadow:inset 0 1px 0 #fff,0 8px 22px -8px rgba(156,203,255,.6)}
/* barra de progresso */
.z3-pbar{position:fixed;left:0;top:0;height:2px;width:100%;z-index:60;transform-origin:left;transform:scaleX(0);background:linear-gradient(90deg,var(--ac),#fff)}
/* títulos palavra por palavra */
.z3-sp .wd{display:inline-block;overflow:hidden;vertical-align:top;padding:0 .16em .1em;margin:0 -.16em}
.z3-sp .wd>i{display:inline-block;font-style:inherit;transform:translateY(110%) rotate(4deg);transition:transform 1.1s var(--e)}
.z3-sp.on .wd>i{transform:none}
/* holofote nos cartões */
.z3-team>div,.z3-ctl,.z3-sum,.z3-faq details{position:relative}
.z3-team>div::after,.z3-ctl::after,.z3-sum::after,.z3-stage::after{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;background:radial-gradient(380px circle at var(--sx,50%) var(--sy,50%),rgba(156,203,255,.12),transparent 60%);opacity:0;transition:opacity .4s}
.z3-team>div:hover::after,.z3-ctl:hover::after,.z3-sum:hover::after,.z3-stage:hover::after{opacity:1}
/* mockups flutuando */
.z3-st.on>*,.z3-mv>*{animation:z3fl 6s ease-in-out infinite}
@keyframes z3fl{50%{translate:0 -10px}}
.z3-st .z3-chip2{animation:z3fl 5s ease-in-out infinite reverse}
/* linhas que se desenham */
.z3-flow{border-top-color:transparent;position:relative}
.z3-flow::after{content:"";position:absolute;left:0;top:-1px;height:1px;width:100%;background:var(--ln);transform-origin:left;transform:scaleX(var(--fl,0));transition:transform 1.6s var(--e)}
.z3-flow.on::after{--fl:1}
.z3-time{border-left-color:transparent}
.z3-time::before{content:"";position:absolute;left:-1px;top:0;width:1px;height:100%;background:linear-gradient(var(--ac),var(--ln));transform-origin:top;transform:scaleY(0);transition:transform 1.8s var(--e)}
.z3-time.on::before{transform:scaleY(1)}
/* item ativo dos serviços */
.z3-it h3{transition:transform .6s var(--e)}
.z3-it.act h3{transform:translateX(8px)}
.z3-it li{opacity:0;transform:translateY(10px);transition:opacity .5s var(--e),transform .5s var(--e)}
.z3-it.act li,.z3-it.seen li{opacity:1;transform:none}
.z3-it li:nth-child(2){transition-delay:.06s}.z3-it li:nth-child(3){transition-delay:.12s}.z3-it li:nth-child(4){transition-delay:.18s}
@media (max-width:900px){.z3-it li{opacity:1;transform:none}}
/* total animado */
.z3-tot b{display:inline-block;transition:transform .4s var(--e)}
.z3-tot.bump b{transform:scale(1.06)}
@media (prefers-reduced-motion:reduce){.z3-btn::after{display:none}.z3-sp .wd>i{transform:none}.z3-st.on>*,.z3-mv>*{animation:none}}

.z3-blob{position:absolute;border-radius:50%;filter:blur(70px);opacity:.55;mix-blend-mode:screen;animation:z3bl 14s ease-in-out infinite alternate}
.z3-blob.b1{width:42vw;height:42vw;right:-8vw;top:8vh;background:radial-gradient(circle,#3D7DD8,transparent 65%)}
.z3-blob.b2{width:30vw;height:30vw;right:18vw;top:46vh;background:radial-gradient(circle,#7BE0B3,transparent 65%);opacity:.3;animation-duration:18s}
.z3-blob.b3{width:26vw;height:26vw;left:30vw;bottom:-6vh;background:radial-gradient(circle,#9CCBFF,transparent 65%);opacity:.35;animation-duration:22s}
@keyframes z3bl{0%{transform:translate(0,0) scale(1)}50%{transform:translate(-6vw,4vh) scale(1.15)}100%{transform:translate(4vw,-3vh) scale(.95)}}
.z3-live2{padding:18vh 0;border-top:1px solid var(--ln)}
.z3-lg{display:grid;grid-template-columns:.8fr 1.2fr;gap:5vw;align-items:center}
.z3-live2 .z3-dash{position:static;width:auto;opacity:1}
.z3-live2 .z3-dash>div{background:rgba(11,15,23,.7);border-color:rgba(156,203,255,.14)}
.z3-live2 .dch svg{height:240px}
.z3-dash .ln,.z3-dash .ar,.dbar p i{animation:none!important}
.z3-dash .ln{stroke-dasharray:1200;stroke-dashoffset:1200;transition:stroke-dashoffset 2.6s var(--e)}
.z3-dash .ar{opacity:0;transition:opacity 1.2s 1.6s}
.dbar p i{width:0;transition:width 1.8s var(--e)}
.z3-dash.go .ln{stroke-dashoffset:0}.z3-dash.go .ar{opacity:1}.z3-dash.go .dbar p i{width:var(--w)}
.z3-dash .dot{fill:#fff;opacity:0;transition:opacity .4s 2.4s}.z3-dash.go .dot{opacity:1}
.z3-dash .pulse{fill:none;stroke:#9CCBFF;opacity:0}.z3-dash.go .pulse{animation:z3pu 2s 2.6s infinite}
@keyframes z3pu{0%{r:4;opacity:.8}100%{r:18;opacity:0}}
.dk b.tick{color:var(--ok);transition:color .6s}
@media (max-width:900px){.z3-lg{grid-template-columns:1fr}.z3-live2 .z3-dash{grid-template-columns:1fr 1fr}.z3-live2 .dch{grid-column:span 2}.z3-live2 .dk:nth-child(3){grid-column:span 2}}
/* liquid glass de verdade */
.z3-btn{background:linear-gradient(135deg,rgba(255,255,255,.16),rgba(255,255,255,.04) 45%,rgba(255,255,255,.10))!important;color:#fff!important;border:0!important;backdrop-filter:blur(22px) saturate(2) brightness(1.15)!important;-webkit-backdrop-filter:blur(22px) saturate(2) brightness(1.15)!important;box-shadow:inset 0 1.5px 0 rgba(255,255,255,.55),inset 0 -1px 1px rgba(255,255,255,.18),inset 0 0 0 1px rgba(255,255,255,.14),inset 0 -12px 24px -14px rgba(156,203,255,.55),0 16px 40px -16px rgba(0,0,0,.8)!important;text-shadow:0 1px 1px rgba(0,0,0,.25)}
.z3-btn.p{background:linear-gradient(135deg,rgba(156,203,255,.55),rgba(61,125,216,.35) 50%,rgba(156,203,255,.45))!important;box-shadow:inset 0 1.5px 0 rgba(255,255,255,.75),inset 0 -1px 1px rgba(255,255,255,.3),inset 0 0 0 1px rgba(255,255,255,.28),inset 0 -14px 26px -12px rgba(255,255,255,.35),0 18px 44px -14px rgba(61,125,216,.75)!important}
.z3-btn>*{position:relative}
.z3-btn::before{inset:1px!important;border-radius:inherit;background:radial-gradient(140px 70px at var(--mx,30%) var(--my,0%),rgba(255,255,255,.6),transparent 70%)!important;opacity:.35!important;mix-blend-mode:overlay}
.z3-btn:hover::before{opacity:.9!important}
.z3-btn:hover{transform:translateY(-2px) scale(1.02)}
.z3-btn:active{transform:scale(.97)}

.z3-con{margin-top:64px;border:1px solid rgba(156,203,255,.16);border-radius:22px;background:linear-gradient(180deg,rgba(11,15,23,.9),rgba(5,7,11,.9));overflow:hidden;box-shadow:0 40px 90px -40px #000}
.z3-con .bar{display:flex;align-items:center;gap:8px;padding:14px 20px;border-bottom:1px solid var(--ln);font:12px var(--mono);color:var(--tx3)}
.z3-con .bar b{width:9px;height:9px;border-radius:50%;background:rgba(238,242,248,.15)}
.z3-con .bar span{margin-left:8px}.z3-con .bar em{margin-left:auto;font-style:normal;color:var(--ok)}
.z3-pipe{padding:26px 20px 12px;overflow-x:auto}
.z3-pipe svg{width:100%;min-width:620px;height:auto;display:block}
.z3-pipe .nd rect{fill:#0E131D;stroke:rgba(238,242,248,.14)}
.z3-pipe .nd.hi rect{stroke:rgba(156,203,255,.7);fill:rgba(156,203,255,.08)}
.z3-pipe .nd.ok rect{stroke:rgba(123,224,179,.6);fill:rgba(123,224,179,.06)}
.z3-pipe .nd text{fill:var(--tx);font:500 14px var(--sans)}
.z3-pipe .nd .s{fill:var(--tx3);font:11px var(--mono)}
.z3-pipe .ic.m{fill:#5B8DEF}.z3-pipe .ic.g{fill:#F2B84B}
.z3-pipe path.l{stroke:rgba(238,242,248,.18);fill:none;stroke-width:1.4;stroke-dasharray:5 5;animation:z3da 1.2s linear infinite}
@keyframes z3da{to{stroke-dashoffset:-20}}
.z3-pipe circle.d{fill:var(--ac);filter:drop-shadow(0 0 7px rgba(156,203,255,.95))}
.z3-pipe circle.d.g2{fill:var(--ok);filter:drop-shadow(0 0 7px rgba(123,224,179,.95))}
.z3-feed{border-top:1px solid var(--ln);font:13px/1.5 var(--mono);height:200px;overflow:hidden;position:relative}
.z3-feed::after{content:"";position:absolute;left:0;right:0;bottom:0;height:70px;background:linear-gradient(transparent,#05070B)}
.z3-feed div{display:grid;grid-template-columns:76px 1fr auto auto;gap:14px;align-items:center;padding:10px 20px;border-bottom:1px solid var(--ln);color:var(--tx2);animation:z3in .6s var(--e)}
.z3-feed div b{color:var(--tx);font-weight:500}
.z3-feed .sc{color:#06101E;background:var(--ok);border-radius:5px;padding:1px 8px;font-weight:600}
.z3-feed .sc.b{background:var(--ac)}.z3-feed .sc.c{background:var(--tx3);color:var(--tx)}
.z3-feed i{font-style:normal;color:var(--tx3)}
@keyframes z3in{from{opacity:0;transform:translateY(-8px);filter:blur(3px)}}
.z3-con .ft2{display:flex;justify-content:space-between;padding:12px 20px;border-top:1px solid var(--ln);font:11px var(--mono);color:var(--tx3)}
@media (max-width:900px){.z3-feed div{grid-template-columns:60px 1fr auto}.z3-feed i{display:none}}
/* cabeçalho e rodapé próprios */
body:has(.z3) .z3-hd .wrap{display:flex;justify-content:space-between;align-items:center}
.z3-hcta{height:44px!important;padding:0 20px!important;font-size:14px!important}
.z3-ft{background:#05070B;color:#5C677A;text-align:center;padding:64px 20px 90px;border-top:1px solid rgba(238,242,248,.06);font:300 11px/1.8 var(--sans,sans-serif);letter-spacing:.18em;text-transform:uppercase}
.z3-ft svg{width:110px;height:auto;color:#8A94A6;margin-bottom:18px}
.z3-ft p{margin:4px 0}

.z3-pl,.z3-pl *{min-width:0}
.z3-pl{overflow-x:clip}
@media(max-width:360px){.z3-ctl,.z3-sum{padding:20px}.z3-seg{gap:6px}.z3-seg button{font-size:18px;height:50px}.z3-ctl .z3-tg{width:100%}.z3-ctl .z3-tg button{flex:1;padding:0 6px;font-size:12.5px;height:40px}.z3-sum li{font-size:13px}}
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
/* configurador */
const pl=$('.z3-pl'),P=JSON.parse(pl.dataset.p),WA=pl.dataset.wa,tg=$('.z3-tg'),pill=tg.querySelector('i');let N=1,K='mensal';
const fm=n=>n.toLocaleString('pt-BR');const PH={mensal:'Pré-pago, sem permanência.',trimestral:'Período completo, em até 3x.',semestral:'Período completo, em até 6x.'};
const mv=b=>{pill.style.width=b.offsetWidth+'px';pill.style.transform=`translateX(${b.offsetLeft-5}px)`};
const calc=()=>{const d=$('#z3dos').checked,tot=$('#z3tot'),lin=$('#z3lin'),go=$('#z3go');$('#z3ph').textContent=PH[K];
if(N>3){tot.innerHTML='<b style="font-size:.6em">Sob medida</b>';lin.innerHTML='<li><span>4 ou mais campanhas</span><b>proposta personalizada</b></li>';go.textContent='Falar com a W3W →';go.href=WA+encodeURIComponent('Olá! Quero um plano W3W com 4 ou mais campanhas.');return}
const u=P[K][N-1],t=u*N+(d?390*N:0);tot.innerHTML=`<small>R$</small><b>${fm(t)}</b><small>/mês</small>`;
lin.innerHTML=`<li><span>${N} campanha${N>1?'s':''} × R$ ${fm(u)}</span><b>R$ ${fm(u*N)}</b></li>`+(d?`<li><span>Lead Dossiê × ${N}</span><b>R$ ${fm(390*N)}</b></li>`:'')+`<li><span>Período</span><b>${K[0].toUpperCase()+K.slice(1)}</b></li>`;
go.textContent='Quero este plano →';go.href=WA+encodeURIComponent(`Olá! Quero contratar a W3W: ${N} campanha(s), plano ${K}${d?', com Lead Dossiê':''}. Total R$ ${fm(t)}/mês.`)};
$$('.z3-seg button').forEach(b=>b.onclick=()=>{$$('.z3-seg button').forEach(x=>x.setAttribute('aria-pressed',x===b));N=+b.dataset.v;calc()});
tg.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{tg.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b));mv(b);K=b.dataset.k;calc()}));
$('#z3dos').onchange=calc;calc();
requestAnimationFrame(()=>mv(tg.querySelector('[aria-pressed=true]')));addEventListener('resize',()=>mv(tg.querySelector('[aria-pressed=true]')));
/* dash */
const DS=$('#z3dash');const cnt=(el,to,d=1800)=>{const fr=+el.textContent.replace(/\D/g,'')||0,st=performance.now();const k=t=>{const p=Math.min((t-st)/d,1);el.textContent=Math.round(fr+(to-fr)*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(k)};requestAnimationFrame(k)};
if(DS)new IntersectionObserver((es,o)=>{if(!es[0].isIntersecting)return;o.disconnect();DS.classList.add('go');$$('#z3dash [data-to]').forEach(el=>cnt(el,+el.dataset.to,R?1:2200));
if(R)return;const lead=DS.querySelector('.dk b');let n=148;setInterval(()=>{n+=1+Math.round(Math.random()*2);cnt(lead,n,600);lead.classList.add('tick');setTimeout(()=>lead.classList.remove('tick'),700)},3200)},{threshold:.35}).observe(DS);
/* efeitos extras */
const pb=document.createElement('div');pb.className='z3-pbar';document.body.appendChild(pb);
addEventListener('scroll',()=>{const h=document.documentElement;pb.style.transform=`scaleX(${h.scrollTop/(h.scrollHeight-innerHeight)})`},{passive:true});
$$('.z3-sh h2,.z3-plh h2,.z3-dos h2,.z3-faq h2,.z3-end h2').forEach(h=>{const walk=n=>{[...n.childNodes].forEach(c=>{if(c.nodeType===3){const f=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(t=>{if(!t)return;if(/^\s+$/.test(t)){f.append(t);return}const w=document.createElement('span');w.className='wd';const i=document.createElement('i');i.textContent=t;w.append(i);f.append(w)});c.replaceWith(f)}else if(c.nodeType===1&&c.tagName!=='BR')walk(c)})};walk(h);h.classList.add('z3-sp');h.querySelectorAll('.wd>i').forEach((i,k)=>i.style.transitionDelay=k*.05+'s');io.observe(h)});
$$('.z3-flow,.z3-time').forEach(el=>io.observe(el));
const io2=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('seen')}),{threshold:.4});$$('.z3-it').forEach(el=>io2.observe(el));
const fine=matchMedia('(hover:hover)').matches;
if(fine&&!R){$$('.z3-btn').forEach(b=>{b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;b.style.setProperty('--mx',x+'px');b.style.setProperty('--my',y+'px');b.style.transform=`translate(${(x-r.width/2)*.15}px,${(y-r.height/2)*.25}px)`});b.addEventListener('pointerleave',()=>b.style.transform='')});
$$('.z3-team>div,.z3-ctl,.z3-sum,.z3-stage').forEach(c=>c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect();c.style.setProperty('--sx',e.clientX-r.left+'px');c.style.setProperty('--sy',e.clientY-r.top+'px')}));}
const tot=$('#z3tot');new MutationObserver(()=>{tot.classList.add('bump');setTimeout(()=>tot.classList.remove('bump'),250)}).observe(tot,{childList:true});
/* parallax em camadas */
if(!R){const PX=[];const add=(sel,vy,vx=0)=>$$(sel).forEach((el,i)=>PX.push([el,vy,typeof vx==='function'?vx(i):vx]));
add('.z3-mg aside',.05);add('.z3-dcard',-.03);add('.z3-sum',-.02);
add('.z3-time',.06);add('.z3-sum',-.07);add('.z3-ctl',.03);add('.z3-flow li',0,0);$$('.z3-flow li').forEach((el,i)=>PX.push([el,-.03*(i%3+1),0]));add('.z3-faq .rv:first-child',.1);add('.z3-end h2',-.1);add('.z3-dash',.18);add('.z3-dcard',-.06);
const orb=document.createElement('div');orb.className='z3-orbs';orb.innerHTML='<i></i><i></i><i></i>';$('.z3').prepend(orb);const ob=[...orb.children];
const pl2=()=>{const vh=innerHeight;PX.forEach(([el,vy,vx])=>{const r=el.getBoundingClientRect(),c=(r.top+r.height/2-vh/2);if(r.bottom<-200||r.top>vh+200)return;el.style.translate=`${(c*vx*(innerWidth>900?1:.15)).toFixed(1)}px ${(c*vy).toFixed(1)}px`});const y=scrollY;ob.forEach((o,i)=>o.style.translate=`0 ${-(y*(.15+i*.12))}px`);requestAnimationFrame(pl2)};requestAnimationFrame(pl2)}
/* feed do fluxo */
(()=>{const F=$('#z3Feed'),C=$('#z3Clock');if(!F)return;const L=[['Cobertura · Moema','A','Instagram'],['Studio · Moema','B','Google'],['Apto 258 m² · Moema','A','Instagram'],['Casa · Brooklin','A','Facebook'],['Apto 147 m² · Moema','B','Google'],['Studio · investimento','C','Instagram'],['Duplex 625 m² · Moema','A','Instagram'],['Apto 170 m² · Moema','B','Google']],N=['Mariana','Rafael','Helena','Pedro','Camila','Bruno','Lúcia','André'];let k=0;
const t=()=>{const d=new Date();return[d.getHours(),d.getMinutes(),d.getSeconds()].map(x=>('0'+x).slice(-2)).join(':')};
const add=()=>{const x=L[k%L.length],n=N[(k*3)%N.length],r=document.createElement('div');r.innerHTML=`<span>${t()}</span><span><b>${n}</b> · ${x[0]}</span><i>${x[2]}</i><span class="sc ${x[1]==='A'?'':x[1]==='B'?'b':'c'}">${x[1]}</span>`;F.prepend(r);while(F.children.length>6)F.lastChild.remove();k++};
for(let i=0;i<4;i++)add();if(!R)setInterval(add,2600);setInterval(()=>C.textContent=t(),1000);C.textContent=t()})();
/* palco dos serviços */
const sts=$$('.z3-st'),stio=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){const i=e.target.dataset.i;sts.forEach(x=>x.classList.toggle('on',x.dataset.i===i));$$('.z3-it').forEach(x=>x.classList.toggle('act',x===e.target))}}),{rootMargin:'-45% 0px -45% 0px'});$$('.z3-it').forEach(el=>stio.observe(el));
if(R){$$('.z3-mt .w').forEach(l=>l.classList.add('on'));return}
/* cursor */
const g=$('.z3-glow');let gx=-999,gy=-999,cx=-999,cy=-999;
if(matchMedia('(hover:hover)').matches)addEventListener('pointermove',e=>{gx=e.clientX;gy=e.clientY});
/* scroll loop */
const hero=$('.z3-hero'),bg=$('.z3-bg'),hin=$('.z3-hin'),hud=$('.z3-hud'),imgs=[],mf=$('.z3-man3'),mls=$$('.z3-mt .w');
const loop=()=>{const vh=innerHeight;
let r=hero.getBoundingClientRect(),p=Math.min(Math.max(-r.top/(r.height-vh),0),1);
bg.style.transform=`scale(${1.15-p*.12}) translateY(${p*6}%)`;hin.style.transform=`translateY(${-p*120}px)`;hin.style.opacity=1-p*1.1;hud.style.transform=`translateY(${-p*260}px)`;
r=mf.getBoundingClientRect();p=Math.min(Math.max((vh*.8-r.top)/(r.height*.7),0),1);const nn=Math.floor(p*mls.length*1.05);mls.forEach((l,i)=>l.classList.toggle('on',i<nn));
imgs.forEach((im,i)=>{const b=im.parentNode.getBoundingClientRect(),q=(b.left+b.width/2)/innerWidth-.5;im.style.transform=`translateX(${-q*12-8}%)`});

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
    I = IMG
    vis = {
        '01': f"""<div class="z3-ph"><div class="sc"><div class="tp"><i></i><div><b>w3wimoveis</b><small>Patrocinado</small></div></div><div class="im"><img src="{I}/agami-park-residences/fachada.jpg" alt=""></div><div class="bt">Quero mais informações<span>›</span></div></div></div><div class="z3-chip2" style="left:8%;top:22%">Público · <b>Moema + 5 km</b></div><div class="z3-chip2" style="right:8%;top:52%">Verba · <b>por produto</b></div>""",
        '02': f"""<div class="z3-wa"><div class="m"><b>NOVO LEAD · PRIORIDADE A</b>Mariana, 41 · quer morar com a família · decide em até 6 meses.</div><div class="m c"><img src="{I}/agami-park-residences/terraco.jpg" alt=""><div>Cobertura 1.184 m²<br><small style="color:#8fb9a6">Veio do Instagram · Coberturas</small></div></div><time>agora</time></div>""",
        '03': f"""<div class="z3-fan"><div><img src="{I}/la-galerie-moema/lazer-1.jpg" alt=""></div><div><img src="{I}/agami-park-residences/lobby.jpg" alt=""><span>Viver acima<br>do comum.</span></div><div><img src="{I}/agami-park-residences/par-2.jpg" alt=""></div></div>""",
        '04': f"""<div class="z3-br"><div class="bar"><i></i><i></i><i></i><span>w3wimoveis.com.br/agami</span></div><div class="lp"><div class="nav"><b>AGAMI</b><span>Plantas · Lazer · Localização</span></div><div class="hero"><img src="{I}/agami-park-residences/voo.jpg" alt=""><div class="tx"><small>MOEMA · LANÇAMENTO</small><b>Viva ao lado<br>do Ibirapuera.</b></div><div class="form"><small>Quero mais informações</small><i>Nome</i><i>WhatsApp</i><i>Objetivo: morar</i><em>Receber plantas</em></div></div></div></div>""",
    }
    SV = [
        ('01', 'Mídia', 'Tráfego por produto', 'Seu imóvel anunciado no Instagram, Facebook e Google para quem pode comprar: público, verba e criativos próprios para cada empreendimento.', ['Estratégia e públicos', 'Meta Ads e Google Ads', 'Otimização semanal', 'Relatório de leads e visitas'], 'a partir de R$ 1.000 por campanha/mês'),
        ('02', 'Dados', 'Lead Dossiê', 'Cada interessado passa por uma triagem rápida e chega ao corretor com perfil, prioridade A/B/C e roteiro de abordagem, direto no WhatsApp.', ['Triagem no site e no WhatsApp', 'Score de compra', 'Roteiro de abordagem', 'Dentro da LGPD'], '+ R$ 390 por campanha/mês'),
        ('03', 'Criação', 'Direção de arte', 'Imagem e texto à altura do metro quadrado: identidade, book, tratamento de imagem, carrosséis, reels e vídeo, assinados por Head of Art.', ['Identidade e naming', 'Book e ficha técnica', 'Carrosséis e reels', 'Tratamento de imagem'], 'a partir de R$ 1.200'),
        ('04', 'Plataforma', 'Landing page e hub', 'Uma página só do seu imóvel, com formulário de triagem e botão de WhatsApp, e um hub com fichas, textos e imagens para o time vender.', ['Página do produto', 'Formulário de triagem', 'Card para WhatsApp', 'Hub de vendas'], 'a partir de R$ 2.500'),
    ]
    stage = ''.join(f'<div class="z3-st{" on" if i==0 else ""}" data-i="{i}">{vis[n]}</div>' for i,(n,*_) in enumerate(SV))
    items = ''.join(f'''<article class="z3-it" data-i="{i}"><div class="z3-mv" aria-hidden="true">{vis[n]}</div><span class="mono z3-k2">{n} — {k}</span><h3>{t}</h3><p>{d}</p><ul>{''.join(f'<li>{x}</li>' for x in li)}</ul><div class="z3-buy"><a class="z3-lk" href="#planos">Ver planos ↓</a><a class="z3-btn p" href="{wa('Olá! Quero contratar ' + t + ' com a W3W.')}" target="_blank" rel="noopener">Quero este serviço</a></div></article>''' for i,(n,k,t,d,li,pr) in enumerate(SV))
    plan = lambda i, nome, itens, hot=False: f'''<div class="z3-plan{' hot' if hot else ''} rv"><h3>{nome}</h3><div class="z3-pr">R$ <span data-i="{i}">{fm(m[i])}</span><small> /mês por campanha</small></div><ul>{''.join(f'<li>{x}</li>' for x in itens)}</ul><a class="z3-btn {'p' if hot else 's'}" href="{wa('Olá! Quero contratar o plano ' + nome + ' da W3W.')}" target="_blank" rel="noopener">Quero este plano</a></div>'''
    mq = ''.join(f'<span>{x}</span>' for x in ['Tráfego', 'por produto', 'Direção de arte', 'assinada', 'Lead Dossiê', 'antes do olá', 'Moema', 'desde 2004'] * 2)
    css = CSS.replace('%I', IMG)
    return css + f'''
<main class="z3">
<div class="z3-glow" aria-hidden="true"></div>
<section class="z3-hero"><div class="z3-stick"><div class="z3-bg" aria-hidden="true"><i class="z3-blob b1"></i><i class="z3-blob b2"></i><i class="z3-blob b3"></i></div><div class="z3-grid"></div>
<div class="z3-hin">
<div class="z3-top"><span class="mono z3-live"><i></i>Agenda aberta · 2026</span><span class="mono">Marketing e vendas para imóveis de alto padrão</span></div>
<h1 class="z3-h1b"><span class="ln"><span>Não entregamos contatos.</span></span><span class="ln"><span>Entregamos <em>compradores.</em></span></span></h1>
<div class="z3-hsub"><p><b style="color:var(--tx);font-weight:400">A W3W anuncia, atende e vende o seu imóvel.</b> Campanha própria no Meta e no Google, criação de agência e corretores que conhecem Moema há mais de 20 anos.</p>
<div class="z3-cta"><a class="z3-btn p" href="#planos">Montar meu plano →</a><a class="z3-btn s" href="{contato}" target="_blank" rel="noopener">Falar no WhatsApp</a></div></div>
<div class="z3-proof"><span><b>Tráfego pago</b></span><span><b>Lead Dossiê</b></span><span><b>Direção de arte</b></span><span><b>Landing page</b></span><span>a partir de <b>R$ 1.000</b> por campanha</span></div>
</div>
<div class="z3-hud" aria-hidden="true"><div class="z3-chip"><b>A</b>Lead · Cobertura 1.184 m²<span>agora</span></div><div class="z3-chip"><b class="b">B</b>Lead · Studio Moema<span>2 min</span></div><div class="z3-chip"><b>A</b>Visita agendada · sábado<span>5 min</span></div></div>
<div class="z3-scroll mono" aria-hidden="true">Role<i></i></div>
</div></section>

<section class="z3-live2"><div class="z3-in z3-lg">
<div class="z3-sh rv"><span class="mono z3-ey">Resultado que você acompanha</span><h2>Cada lead, cada visita, <em>em tempo real.</em></h2><p class="z3-lead">Relatório semanal com leads, custo, visitas e propostas de cada campanha. Você sabe exatamente o que a verba está gerando.</p><p class="mono z3-fict" style="margin-top:22px">Painel ilustrativo</p></div>
<div class="z3-dash" id="z3dash">
<div class="dk"><span>Leads qualificados</span><b data-to="148">0</b><i>+32% no mês</i></div>
<div class="dk"><span>Custo por lead</span><b>R$ <em data-to="38">0</em></b><i>−18%</i></div>
<div class="dk"><span>Visitas agendadas</span><b data-to="27">0</b><i>+9 na semana</i></div>
<div class="dch"><span>Leads por semana · campanha Coberturas</span><svg viewBox="0 0 600 220" preserveAspectRatio="none"><defs><linearGradient id="zg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9CCBFF" stop-opacity=".35"/><stop offset="1" stop-color="#9CCBFF" stop-opacity="0"/></linearGradient></defs>
<g stroke="rgba(238,242,248,.07)"><line x1="0" y1="55" x2="600" y2="55"/><line x1="0" y1="110" x2="600" y2="110"/><line x1="0" y1="165" x2="600" y2="165"/></g>
<path class="ar" d="M0 190 L60 175 L120 180 L180 150 L240 140 L300 120 L360 125 L420 90 L480 70 L540 60 L600 30 L600 220 L0 220Z" fill="url(#zg)"/>
<path class="ln" d="M0 190 L60 175 L120 180 L180 150 L240 140 L300 120 L360 125 L420 90 L480 70 L540 60 L600 30" fill="none" stroke="#9CCBFF" stroke-width="2"/><circle class="pulse" cx="600" cy="30" r="4"/><circle class="dot" cx="600" cy="30" r="4"/>
<path class="ln2" d="M0 205 L60 200 L120 196 L180 190 L240 182 L300 178 L360 170 L420 160 L480 152 L540 148 L600 140" fill="none" stroke="rgba(238,242,248,.3)" stroke-width="1.5" stroke-dasharray="4 6"/></svg></div>
<div class="dbar"><span>Origem dos leads</span><p><i style="--w:62%"></i><b>Instagram</b></p><p><i style="--w:24%"></i><b>Google</b></p><p><i style="--w:14%"></i><b>Facebook</b></p></div>
</div>
</div></section>

<section class="z3-man3" aria-label="Manifesto"><div class="z3-mg"><aside><span class="mono z3-ey">Manifesto</span><p>W3W Imóveis · Inteligência imobiliária · Moema, desde 2004</p></aside><p class="z3-mt"><span><i class="w" style="font-style:inherit">Imóvel</i> <i class="w" style="font-style:inherit">de</i> <i class="w" style="font-style:inherit">alto</i> <i class="w" style="font-style:inherit">padrão</i></span><span><em><i class="w" style="font-style:inherit">não</i> <i class="w" style="font-style:inherit">se</i> <i class="w" style="font-style:inherit">vende</i></em> <i class="w" style="font-style:inherit">com</i> <i class="w" style="font-style:inherit">anúncio.</i></span><span><i class="w" style="font-style:inherit">Vende-se</i> <i class="w" style="font-style:inherit">com</i> <em><i class="w" style="font-style:inherit">inteligência.</i></em></span></p></div></section>

<section class="z3-sv" id="servicos"><div class="z3-in">
<div class="z3-sh rv"><span class="mono z3-ey">01 · O que entregamos</span><h2>Tudo para o seu imóvel <em>vender mais rápido.</em></h2></div>
<div class="z3-svg"><div class="z3-stage" aria-hidden="true">{stage}</div><div class="z3-items">{items}</div></div>
</div></section>

<section class="z3-como" id="como"><div class="z3-in">
<div class="z3-sh rv"><span class="mono z3-ey">02 · Como funciona</span><h2>Do anúncio à visita, <em>em cinco passos.</em></h2></div>
<ol class="z3-flow">
<li class="rv"><span>01</span><b>Anúncio</b><p>Campanha do seu imóvel no Instagram, Facebook e Google, para o público certo de Moema e região.</p></li>
<li class="rv"><span>02</span><b>Triagem</b><p>O interessado responde 3 perguntas rápidas: objetivo, prazo e faixa de investimento.</p></li>
<li class="rv"><span>03</span><b>Dossiê</b><p>Montamos o perfil do lead com score A/B/C e um roteiro de abordagem.</p></li>
<li class="rv"><span>04</span><b>Corretor</b><p>Tudo chega no WhatsApp do corretor com o card do imóvel, pronto para responder.</p></li>
<li class="rv"><span>05</span><b>Visita e proposta</b><p>Atendimento rápido e preparado. Relatório semanal de leads, visitas e propostas.</p></li>
</ol><div class="z3-con rv" aria-label="Simulação do fluxo de leads da W3W"><div class="bar"><b></b><b></b><b></b><span>w3w · operação de leads</span><em>● simulação ao vivo</em></div>
<div class="z3-pipe"><svg viewBox="0 0 860 220" role="img" aria-label="Fluxo: Meta Ads e Google Ads, triagem, Lead Dossiê e corretor">
<path class="l" id="q1" d="M150 55 C215 55 215 110 280 110"/><path class="l" id="q2" d="M150 165 C215 165 215 110 280 110"/><path class="l" id="q3" d="M420 110 L500 110"/><path class="l" id="q4" d="M640 110 L710 110"/>
<g class="nd"><rect x="10" y="30" width="140" height="50" rx="12"/><circle cx="32" cy="55" r="7" class="ic m"/><text x="48" y="52">Meta Ads</text><text class="s" x="48" y="67">Instagram · Facebook</text></g>
<g class="nd"><rect x="10" y="140" width="140" height="50" rx="12"/><circle cx="32" cy="165" r="7" class="ic g"/><text x="48" y="162">Google Ads</text><text class="s" x="48" y="177">pesquisa · display</text></g>
<g class="nd"><rect x="280" y="82" width="140" height="56" rx="12"/><text x="298" y="106">Triagem</text><text class="s" x="298" y="122">site + WhatsApp</text></g>
<g class="nd hi"><rect x="500" y="82" width="140" height="56" rx="12"/><text x="518" y="106">Lead Dossiê</text><text class="s" x="518" y="122">score · roteiro</text></g>
<g class="nd ok"><rect x="710" y="82" width="140" height="56" rx="12"/><text x="728" y="106">Corretor</text><text class="s" x="728" y="122">WhatsApp · visita</text></g>
<circle class="d" r="4"><animateMotion dur="2.4s" repeatCount="indefinite"><mpath href="#q1"/></animateMotion></circle>
<circle class="d" r="4"><animateMotion dur="2.4s" begin="1.2s" repeatCount="indefinite"><mpath href="#q2"/></animateMotion></circle>
<circle class="d" r="4"><animateMotion dur="1.3s" begin=".4s" repeatCount="indefinite"><mpath href="#q3"/></animateMotion></circle>
<circle class="d g2" r="4"><animateMotion dur="1.3s" begin=".9s" repeatCount="indefinite"><mpath href="#q4"/></animateMotion></circle>
</svg></div>
<div class="z3-feed" id="z3Feed" aria-hidden="true"></div>
<div class="ft2"><span>dados ilustrativos</span><span id="z3Clock">--:--</span></div></div></div></section>

<section class="z3-dos">
<div class="rv"><span class="mono z3-ey">O resultado · Lead Dossiê</span><h2>O corretor sabe quem é <em>antes do primeiro olá.</em></h2>
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


<section class="z3-quem"><div class="z3-in">
<div class="z3-sh rv"><span class="mono z3-ey">03 · Quem implementa</span><h2>Uma imobiliária <em>que faz marketing.</em></h2><p class="z3-lead">Não terceirizamos. Quem cria a campanha conhece o produto, e quem atende o lead vende em Moema há mais de 20 anos.</p></div>
<div class="z3-qg">
<div class="z3-team rv">
<div><span class="mono">Sócio-diretor · CRECI 69.228</span><b>Wilson Rodrigues</b><p>Estratégia comercial, captação e negociação.</p></div>
<div><span class="mono">Sócia · CRECI 81.771</span><b>Marli Setsuko</b><p>Atendimento, carteira de investidores e retaguarda.</p></div>
<div><span class="mono">Sócio · Head of Art</span><b>Kco Oyakawa</b><p>Direção de arte, campanha e dados. Mais de 20 anos em agências, com FIFA™ e Rio 2016.</p></div>
</div>
<div class="z3-time rv"><span class="mono">Implantação</span>
<div><i>Semana 1</i><b>Diagnóstico e briefing</b><p>Produto, público, concorrência, verba e metas.</p></div>
<div><i>Semana 2</i><b>Criação e página</b><p>Peças, textos, landing page e triagem configurados.</p></div>
<div><i>Semana 3</i><b>Campanha no ar</b><p>Anúncios publicados e dossiês chegando ao corretor.</p></div>
<div><i>Toda semana</i><b>Otimização e relatório</b><p>Ajuste de público e verba, com leads, visitas e propostas.</p></div>
</div></div></div></section>

<section class="z3-pl" id="planos" data-p='{json.dumps(planos)}' data-wa="{wa('')}">
<div class="z3-plh"><div><span class="mono z3-ey">04 · Quanto custa</span><h2>Preço claro, <em>por campanha.</em></h2></div></div>
<div class="z3-cfg rv">
<div class="z3-ctl">
<div><span class="mono">Quantas campanhas?</span><p class="z3-hint">Cada imóvel ou empreendimento é uma campanha.</p><div class="z3-seg"><button aria-pressed="true" data-v="1">1</button><button aria-pressed="false" data-v="2">2</button><button aria-pressed="false" data-v="3">3</button><button aria-pressed="false" data-v="4">4+</button></div></div>
<div><span class="mono">Período</span><div class="z3-tg" role="group" aria-label="Período"><i></i><button data-k="mensal" aria-pressed="true">Mensal</button><button data-k="trimestral" aria-pressed="false">Trimestral</button><button data-k="semestral" aria-pressed="false">Semestral</button></div><p class="z3-hint" id="z3ph">Pré-pago, sem permanência.</p></div>
<label class="z3-sw"><input type="checkbox" id="z3dos"><span></span><div><b>Adicionar Lead Dossiê</b><p class="z3-hint">Score, perfil e roteiro de cada lead no WhatsApp. +R$ 390 por campanha/mês.</p></div></label>
</div>
<div class="z3-sum"><span class="mono">Seu plano</span>
<div class="z3-tot" id="z3tot"><small>R$</small><b>1.500</b><small>/mês</small></div>
<ul id="z3lin"></ul>
<a class="z3-btn p" id="z3go" href="#" target="_blank" rel="noopener">Quero este plano →</a>
<p class="z3-hint">Verba de mídia não inclusa, paga direto ao Meta e ao Google.</p></div>
</div>
<div class="z3-extra rv">
<div><span class="mono">Avulso · Criativos</span><b>a partir de R$ 1.200</b></div>
<div><span class="mono">Landing page</span><b>a partir de R$ 2.500</b></div>
<div><span class="mono">Identidade e book</span><b>a partir de R$ 6.000</b></div>
</div>
<p class="z3-note"><b style="color:var(--tx);font-weight:500">É dono do imóvel que quer vender?</b> Você paga a campanha e, quando o imóvel for vendido pela W3W, devolvemos esse valor como desconto na comissão de venda. <a href="{prop}" target="_blank" rel="noopener" style="color:var(--ac)">Saiba mais →</a></p>
</section>

<section class="z3-faq"><div class="z3-in z3-fg">
<div class="rv"><span class="mono z3-ey">Dúvidas</span><h2>Antes de <em>começar.</em></h2></div>
<div class="rv">
<details><summary>A verba de mídia está incluída?</summary><p>Não. Ela é paga direto ao Meta e ao Google, no seu cartão, com total transparência. Indicamos o valor ideal no diagnóstico.</p></details>
<details><summary>Preciso ter corretor próprio?</summary><p>Não. O atendimento pode ser feito pela W3W ou pelo seu time, que recebe o hub com fichas, textos e imagens.</p></details>
<details><summary>O Lead Dossiê é obrigatório?</summary><p>Não, é opcional. Ele usa só dados que o próprio lead informa, dentro da LGPD, sem compra de base.</p></details>
<details><summary>Existe fidelidade?</summary><p>O mensal é pré-pago e sem permanência. Trimestral e semestral têm desconto e valem pelo período completo, em até 3x ou 6x.</p></details>
<details><summary>Sou proprietário. Como funciona?</summary><p>Você investe na campanha do seu imóvel e, se vender com a W3W, o valor é descontado da comissão.</p></details>
</div></div></section>

<section class="z3-end"><div class="z3-endg"><h2 class="rv">Vamos<br>vender <em>do jeito certo.</em></h2>
<div class="rv"><ul><li><span>01</span>Campanha própria para o seu imóvel</li><li><span>02</span>Criação assinada por Head of Art</li><li><span>03</span>Atendimento de quem conhece Moema</li></ul>
<div class="z3-cta"><a class="z3-btn p" href="{contato}" target="_blank" rel="noopener">Falar com a W3W →</a><a class="z3-btn s" href="{BASE}/#imoveis">Ver a vitrine</a></div></div></div></section>
</main>
''' + JS
