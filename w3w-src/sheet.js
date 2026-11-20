(function(){
var S=document.getElementById('sheet');if(!S)return;var P=S.querySelector('.sh-p'),IN=S.querySelector('.sh-in'),last=null,data={};
(window.W3W||[]).forEach(function(e){data[e.slug]=e});
function wa(m){return 'https://wa.me/'+window.W3W_WA+'?text='+encodeURIComponent(m)}
function esc(s){return String(s||'').replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
var IDEAL={'studios':['Investimento para renda','Primeiro imóvel','Pied-à-terre em São Paulo'],'apartamentos':['Casais e famílias pequenas','Quem quer morar perto do Ibirapuera'],'alto-padrao':['Famílias que buscam espaço','Patrimônio de longo prazo']};
var FASE={'Lançamento':'Condições de lançamento e melhor escolha de unidades. Ideal para quem quer comprar na planta com tabela inicial.','Em obras':'Compra com pagamento facilitado durante a obra e valorização até a entrega das chaves.','Pronto':'Pronto para morar ou alugar: visita ao imóvel real e mudança imediata.'};
function html(e){var r=e.resumo,specs=[['Tipologias',r.tipologias],['Metragem',r.metragem],['Vagas',r.vagas],['Bairro',e.bairro+', São Paulo']].filter(function(x){return x[1]});
var ideal=[];(e.categorias||[]).forEach(function(c){(IDEAL[c]||[]).forEach(function(x){if(ideal.indexOf(x)<0)ideal.push(x)})});
var q=encodeURIComponent(e.nome+' '+e.bairro+' São Paulo');
return '<div class="fx-ph"><img src="'+e.img+'" alt="'+esc(e.nome)+'"><span class="tag st">'+esc(e.status)+'</span></div>'+
'<div class="fx-b"><div class="fx-t"><span class="eyebrow">'+esc(e.bairro)+' · '+esc(e.status)+'</span><h2 id="sh-t">'+esc(e.nome)+'</h2>'+(e.frase?'<p class="fx-q">'+esc(e.frase)+'</p>':'')+'</div>'+
'<dl class="fx-s">'+specs.map(function(x){return '<div><dt>'+x[0]+'</dt><dd>'+esc(x[1])+'</dd></div>'}).join('')+'</dl></div>'+
'<div class="fx-c"><a class="btn solid" target="_blank" rel="noopener" href="'+wa('Olá, vi o '+e.nome+' ('+e.bairro+') no site da W3W e quero a ficha completa.')+'">Quero a ficha completa</a>'+
'<a class="btn" target="_blank" rel="noopener" href="'+wa('Olá, quero agendar uma visita ao '+e.nome+'.')+'">Agendar visita</a></div>'+
'<div class="fx-x"><div><span class="eyebrow">Momento da obra</span><h4>'+esc(e.status)+'</h4><p>'+(FASE[e.status]||'')+'</p></div>'+
(ideal.length?'<div><span class="eyebrow">Ideal para</span><ul>'+ideal.map(function(x){return '<li>'+x+'</li>'}).join('')+'</ul></div>':'')+
'<div><span class="eyebrow">O bairro</span><h4>'+esc(e.bairro)+'</h4><p>'+esc(e.bt||'')+'</p></div></div>'+
'<div class="fx-map"><span class="eyebrow">Localização aproximada</span><iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa '+esc(e.nome)+'" src="https://www.google.com/maps?q='+q+'&output=embed"></iframe></div>'+
'<div class="fx-cta2"><div><span class="eyebrow">Ficha completa</span><h4>Plantas, tabela, incorporadora e previsão de entrega.</h4></div><a class="btn solid" target="_blank" rel="noopener" href="'+wa('Olá, quero receber a ficha completa do '+e.nome+' (plantas, tabela e entrega).')+'">Receber no WhatsApp</a></div>'+
'<a class="fx-l" href="'+window.W3W_BASE+'/empreendimentos/'+e.slug+'/">Abrir página do empreendimento ↗</a>'}
function open(slug,push){var e=data[slug];if(!e)return;last=document.activeElement;var tp=document.getElementById('fx-'+slug);IN.innerHTML=tp?tp.innerHTML:html(e);S.classList.toggle('rich',!!tp);S.hidden=false;P.style.transform='';P.scrollTop=0;
document.documentElement.classList.add('lock');requestAnimationFrame(function(){S.classList.add('on')});if(tp&&window.W3WMotion)window.W3WMotion(IN.querySelector('.lx'));P.focus();if(push)history.pushState({sheet:slug},'','#'+slug)}
function close(fromPop){if(S.hidden)return;S.classList.remove('on');document.documentElement.classList.remove('lock');setTimeout(function(){S.hidden=true;IN.innerHTML=''},350);if(last)last.focus();if(!fromPop&&history.state&&history.state.sheet)history.back()}
document.addEventListener('click',function(ev){var a=ev.target.closest('a.g[data-slug]');if(a&&!ev.metaKey&&!ev.ctrlKey){ev.preventDefault();open(a.dataset.slug,true)}if(ev.target.closest('[data-close]'))close()});
document.addEventListener('keydown',function(ev){if(ev.key==='Escape')close()});
addEventListener('popstate',function(){if(history.state&&history.state.sheet)open(history.state.sheet,false);else close(true)});
// arrastar para baixo
var y0=null,dy=0;P.addEventListener('touchstart',function(ev){if(P.scrollTop<=0){y0=ev.touches[0].clientY;dy=0;P.style.transition='none'}},{passive:true});
P.addEventListener('touchmove',function(ev){if(y0===null)return;dy=ev.touches[0].clientY-y0;if(dy>0){P.style.transform='translateY('+dy+'px)'}else{y0=null;P.style.transform=''}},{passive:true});
P.addEventListener('touchend',function(){P.style.transition='';if(y0!==null&&dy>110)close();else P.style.transform='';y0=null});
if(location.hash&&data[location.hash.slice(1)])open(location.hash.slice(1),false);
})();
