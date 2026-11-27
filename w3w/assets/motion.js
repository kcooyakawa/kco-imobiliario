(function(){
var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
function init(root){
  var sc=root.closest('.sh-p')||null;
  var rev=[].slice.call(root.querySelectorAll('.bk-open>*,.bk-f,.lx-num>div,.bk-txt>*,.bk-list li,.bk-loc>*,.bk-tec dl>div,.lx-end>*'));
  if(rm){return}
  rev.forEach(function(el,i){el.classList.add('rv');el.style.transitionDelay=((i%4)*70)+'ms'});
  var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);var n=en.target.querySelector&&en.target.querySelector('strong');if(n&&en.target.parentNode.classList.contains('lx-num'))count(n)}})},{root:sc,threshold:.15});
  rev.forEach(function(el){io.observe(el)});
  var par=[].slice.call(root.querySelectorAll('.bk-cover img,.bk-full img,.bk-voo img'));
  var src=sc||window;
  function tick(){var vh=innerHeight;par.forEach(function(img){var r=img.parentNode.getBoundingClientRect();if(r.bottom<0||r.top>vh)return;var p=(r.top+r.height/2-vh/2)/vh;img.style.transform='translate3d(0,'+(p*-8).toFixed(2)+'%,0) scale(1.14)'})}
  src.addEventListener('scroll',function(){requestAnimationFrame(tick)},{passive:true});tick();
}
function count(el){var t=el.textContent,m=t.match(/^([\d.,]+)(.*)$/);if(!m)return;var to=parseFloat(m[1].replace('.','').replace(',','.')),suf=m[2],t0=performance.now();(function f(n){var k=Math.min(1,(n-t0)/1200),e=1-Math.pow(1-k,3);el.textContent=Math.round(to*e)+suf;if(k<1)requestAnimationFrame(f)})(t0)}
window.W3WMotion=init;
document.querySelectorAll('main .lx').forEach(init);
})();
/* Menu: fecha ao clicar e leva até a seção certa, corrigindo a rota enquanto imagens carregam */
(function(){
var OFF=80,rm=matchMedia('(prefers-reduced-motion: reduce)').matches,job=0;
function hdr(){var h=document.querySelector('.hd');return h?h.getBoundingClientRect().height+8:OFF}
function close(){var n=document.querySelector('.nav');if(n)n.classList.remove('open');var b=document.querySelector('.burger');if(b)b.setAttribute('aria-expanded','false')}
function go(t){
  var id=++job,start=performance.now(),stable=0;
  document.documentElement.style.scrollBehavior='auto';
  function y(){return t.getBoundingClientRect().top+scrollY-hdr()}
  /* carrega já as imagens entre a posição atual e o destino */
  [].forEach.call(document.images,function(im){if(im.loading==='lazy'){var r=im.getBoundingClientRect().top+scrollY;if(r<y()+innerHeight)im.loading='eager'}});
  function tick(){
    if(id!==job)return;
    var cur=scrollY,dst=Math.max(0,Math.min(y(),document.documentElement.scrollHeight-innerHeight)),d=dst-cur;
    if(Math.abs(d)<2){window.scrollTo(0,dst);if(++stable>12||performance.now()-start>4000){document.documentElement.style.scrollBehavior='';return}}
    else{stable=0;window.scrollTo(0,rm?dst:cur+d*0.18+(d>0?1:-1))}
    requestAnimationFrame(tick)
  }
  requestAnimationFrame(tick);
  ['wheel','touchstart','keydown'].forEach(function(ev){addEventListener(ev,function c(){job++;document.documentElement.style.scrollBehavior='';removeEventListener(ev,c)},{once:true,passive:true})});
}
function norm(p){return p.replace(/index\.html$/,'').replace(/\/?$/,'/')}
document.addEventListener('click',function(e){
  var a=e.target.closest&&e.target.closest('a[href*="#"]');if(!a)return;
  if(a.closest('.nav'))close();
  var u=new URL(a.href,location.href);if(!u.hash||norm(u.pathname)!==norm(location.pathname))return;
  var t=document.getElementById(decodeURIComponent(u.hash.slice(1)));if(!t)return;
  e.preventDefault();history.pushState(null,'',u.hash);setTimeout(function(){go(t)},40);
},true);
/* vindo de outra página com #secao */
if(location.hash.length>1){var t0;try{t0=document.getElementById(decodeURIComponent(location.hash.slice(1)))}catch(_){}
  if(t0){if('scrollRestoration' in history)history.scrollRestoration='manual';addEventListener('load',function(){go(t0)});setTimeout(function(){go(t0)},50)}}
document.addEventListener('keydown',function(e){if(e.key==='Escape')close()});
})();
