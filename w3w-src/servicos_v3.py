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
.z3-bg{position:absolute;inset:-6%;background:url("%I/agami-park-residences/voo.jpg") center/cover;transform:scale(1.15);will-change:transform;filter:saturate(.75) brightness(.55)}
.z3-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,7,11,.85) 0%,rgba(5,7,11,.2) 45%,#05070B 98%)}
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
/* palco dos serviços */
const sts=$$('.z3-st'),stio=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){const i=e.target.dataset.i;sts.forEach(x=>x.classList.toggle('on',x.dataset.i===i));$$('.z3-it').forEach(x=>x.classList.toggle('act',x===e.target))}}),{rootMargin:'-45% 0px -45% 0px'});$$('.z3-it').forEach(el=>stio.observe(el));
if(R){$$('.z3-ml').forEach(l=>l.classList.add('on'));return}
/* cursor */
const g=$('.z3-glow');let gx=-999,gy=-999,cx=-999,cy=-999;
if(matchMedia('(hover:hover)').matches)addEventListener('pointermove',e=>{gx=e.clientX;gy=e.clientY});
/* scroll loop */
const hero=$('.z3-hero'),bg=$('.z3-bg'),hin=$('.z3-hin'),hud=$('.z3-hud'),imgs=[],mf=$('.z3-man2'),mls=$$('.z3-ml');
const loop=()=>{const vh=innerHeight;
let r=hero.getBoundingClientRect(),p=Math.min(Math.max(-r.top/(r.height-vh),0),1);
bg.style.transform=`scale(${1.15-p*.12}) translateY(${p*6}%)`;hin.style.transform=`translateY(${-p*120}px)`;hin.style.opacity=1-p*1.1;hud.style.transform=`translateY(${-p*260}px)`;
r=mf.getBoundingClientRect();p=Math.min(Math.max(-r.top/(r.height-vh),0),1);mf.style.setProperty('--m',p);mls.forEach((l,i)=>l.classList.toggle('on',p>i*.15-.02));
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
    items = ''.join(f'''<article class="z3-it" data-i="{i}"><div class="z3-mv" aria-hidden="true">{vis[n]}</div><span class="mono z3-k2">{n} — {k}</span><h3>{t}</h3><p>{d}</p><ul>{''.join(f'<li>{x}</li>' for x in li)}</ul><div class="z3-buy"><span>{pr}</span><a class="z3-btn p" href="{wa('Olá! Quero contratar ' + t + ' com a W3W.')}" target="_blank" rel="noopener">Contratar</a></div></article>''' for i,(n,k,t,d,li,pr) in enumerate(SV))
    plan = lambda i, nome, itens, hot=False: f'''<div class="z3-plan{' hot' if hot else ''} rv"><h3>{nome}</h3><div class="z3-pr">R$ <span data-i="{i}">{fm(m[i])}</span><small> /mês por campanha</small></div><ul>{''.join(f'<li>{x}</li>' for x in itens)}</ul><a class="z3-btn {'p' if hot else 's'}" href="{wa('Olá! Quero contratar o plano ' + nome + ' da W3W.')}" target="_blank" rel="noopener">Quero este plano</a></div>'''
    mq = ''.join(f'<span>{x}</span>' for x in ['Tráfego', 'por produto', 'Direção de arte', 'assinada', 'Lead Dossiê', 'antes do olá', 'Moema', 'desde 2004'] * 2)
    css = CSS.replace('%I', IMG)
    return css + f'''
<main class="z3">
<div class="z3-glow" aria-hidden="true"></div>
<section class="z3-hero"><div class="z3-stick"><div class="z3-bg"></div><div class="z3-grid"></div>
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

<section class="z3-man2" aria-label="Manifesto"><div class="z3-mst"><figure class="z3-mimg"><img src="{IMG}/agami-park-residences/fachada.jpg" alt=""></figure>
<p class="z3-ml l1">Imóvel de alto padrão</p><p class="z3-ml l2"><em>não se vende</em></p><p class="z3-ml l3">com anúncio.</p><p class="z3-ml l4">Vende-se com</p><p class="z3-ml l5"><em>inteligência.</em></p>
<span class="mono z3-msig">Manifesto W3W</span></div></section>

<section class="z3-sv" id="servicos"><div class="z3-in">
<div class="z3-sh rv"><span class="mono z3-ey">01 · O que entregamos</span><h2>Tudo o que seu imóvel precisa <em>para vender.</em></h2></div>
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
</ol></div></section>

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
<p class="z3-note">Proprietário? Invista na campanha e, se vender com a W3W, o valor é descontado da comissão. <a href="{prop}" target="_blank" rel="noopener" style="color:var(--ac)">Saiba mais →</a></p>
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
