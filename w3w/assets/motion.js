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
