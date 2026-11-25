
(()=>{const $=s=>document.querySelector(s),C=window.MP_CATS,CM=Object.fromEntries(C.map(c=>[c[0],c]));
const R=matchMedia('(prefers-reduced-motion: reduce)').matches;
const hd=document.querySelector('.hd');if(hd)document.querySelector('.mp').style.setProperty('--hdh',hd.offsetHeight+'px');
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
let ALL=[],F={cat:null,open:false,h24:false,q:''},sel=null,map;const norm=s=>String(s||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
fetch('locais.json?v='+Date.now()).then(r=>r.json()).then(d=>{ALL=d.locais.filter(l=>CM[l.cat]);if(d.atualizado){const t=new Date(d.atualizado);$('#mpUpd').textContent='Atualizado em '+t.toLocaleDateString('pt-BR',{day:'2-digit',month:'short'})}
chips();draw()}).catch(()=>{$('#mpList').innerHTML='<p class="mp-empty">Não foi possível carregar os lugares agora.</p>'});
function chips(){const n={};ALL.forEach(l=>n[l.cat]=(n[l.cat]||0)+1);$('#mpChips').innerHTML=`<button aria-pressed="${!F.cat}" data-c="">Todos <small>${ALL.length}</small></button>`+C.filter(c=>n[c[0]]).map(c=>`<button aria-pressed="${F.cat===c[0]}" data-c="${c[0]}"><b style="background:${c[2]}"></b>${c[1]} <small>${n[c[0]]}</small></button>`).join('');
$('#mpChips').querySelectorAll('button').forEach(b=>b.onclick=()=>{F.cat=b.dataset.c||null;chips();draw(true)})}
function list(ign){const q=norm(F.q);return ALL.map(l=>({...l,st:status(l.horario)})).filter(l=>(!F.cat||l.cat===F.cat)&&(ign||!F.open||l.st.k==='o'||l.st.k==='h')&&(ign||!F.h24||l.st.k==='h')&&(!q||norm(l.nome+' '+(l.end||'')+' '+CM[l.cat][1]).includes(q)))}
function draw(fit){const L=list();$('#mpN').textContent=L.length+' lugares';$('#mpNow').textContent=new Date().toLocaleTimeString('pt-BR',{hour:'2-digit',minute:'2-digit'});
$('#mpList').innerHTML=L.length?L.slice(0,300).map((l,i)=>`<div class="mp-it${sel===l.id?' on':''}" data-id="${l.id}" style="animation-delay:${Math.min(i,20)*18}ms"><b style="background:${CM[l.cat][2]}"></b><div><strong>${esc(l.nome)}${l.destaque?'<span class="mp-dest">W3W indica</span>':''}</strong><span>${CM[l.cat][1]}${l.end?' · '+esc(l.end):''}</span></div>${l.st.k!=='?'?`<span class="mp-st ${l.st.k}">${l.st.t}</span>`:''}</div>`).join(''):empty();grid(L);
const ab=$('#mpAll');if(ab)ab.onclick=()=>{F.open=F.h24=false;$('#mpOpen').setAttribute('aria-pressed',false);$('#mp24').setAttribute('aria-pressed',false);draw(true)};
$('#mpList').querySelectorAll('.mp-it').forEach(el=>{el.onclick=()=>pick(el.dataset.id,true);el.onmouseenter=()=>hover(el.dataset.id)});
if(map&&map.getSource('locais')){map.getSource('locais').setData(geo(L));if(fit&&L.length){const b=new maplibregl.LngLatBounds();L.forEach(l=>b.extend([l.lon,l.lat]));map.fitBounds(b,{padding:pad(),maxZoom:16,duration:R?0:1200})}}}
function empty(){const all=list(true).length;return all&&(F.open||F.h24)?`<p class="mp-empty">Nada ${F.h24?'24 horas':'aberto agora'} com essa busca.<br><button class="mp-btn" id="mpAll" style="margin-top:14px">Ver os ${all} resultados</button></p>`:`<p class="mp-empty">Ainda não temos “${esc(F.q)}” no mapa.<br><a class="mp-btn" style="margin-top:14px" href="https://wa.me/5511940297871?text=${encodeURIComponent('Olá! Sugiro incluir no Mapa de Moema: '+F.q)}" target="_blank" rel="noopener">Sugerir este lugar</a></p>`}
function grid(L){const g=$('#mpGrid');if(!g)return;const by={};L.forEach(l=>(by[l.cat]=by[l.cat]||[]).push(l));g.innerHTML=C.filter(c=>by[c[0]]).map(c=>`<h3><b style="background:${c[2]}"></b>${c[1]} <small>${by[c[0]].length}</small></h3><div class="mp-gl">${by[c[0]].map(l=>`<div class="mp-gc" data-id="${l.id}"><strong>${esc(l.nome)}</strong><span>${esc(l.end||CM[l.cat][1])}</span>${l.st.k!=='?'?`<em class="mp-st ${l.st.k}" style="font-style:normal">${l.st.t}</em>`:''}</div>`).join('')}</div>`).join('')||'<p class="mp-empty">Nenhum lugar com esses filtros.</p>';
g.querySelectorAll('.mp-gc').forEach(el=>el.onclick=()=>{setMode(false);pick(el.dataset.id,true)})}
const pad=()=>innerWidth>900?{left:420,right:60,top:80,bottom:80}:{left:30,right:30,top:60,bottom:innerHeight*.5};
const geo=L=>({type:'FeatureCollection',features:L.map(l=>({type:'Feature',id:hash(l.id),properties:{id:l.id,nome:l.nome,cor:CM[l.cat][2],aberto:l.st.k==='o'||l.st.k==='h'?1:0,dest:l.destaque?1:0},geometry:{type:'Point',coordinates:[l.lon,l.lat]}}))});
const hash=s=>{let h=0;for(const c of s)h=(h*31+c.charCodeAt(0))|0;return Math.abs(h)};
const esc=s=>String(s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function pick(id,fly){const l=ALL.find(x=>x.id===id);if(!l)return;sel=id;const st=status(l.horario),c=CM[l.cat];
$('#mpCard').innerHTML=`<button class="x" aria-label="Fechar">✕</button><span class="cat" style="color:${c[2]}">${c[1]}${l.destaque?' · W3W indica':''}</span><h2>${esc(l.nome)}</h2>${st.k!=='?'?`<span class="mp-st ${st.k}">${st.t}</span>`:''}${l.nota?`<p>${esc(l.nota)}</p>`:''}${l.end?`<p>${esc(l.end)}</p>`:''}${l.horario?`<div class="hrs">${esc(human(l.horario))}</div>`:''}
<div class="acts"><a class="mp-btn p" href="https://www.google.com/maps/dir/?api=1&destination=${l.lat},${l.lon}" target="_blank" rel="noopener">Como chegar</a>${l.site?`<a class="mp-btn" href="${esc(l.site)}" target="_blank" rel="noopener">Site</a>`:''}${l.tel?`<a class="mp-btn" href="tel:${esc(l.tel.replace(/[^+\d]/g,''))}">Ligar</a>`:''}</div>`;
$('#mpCard').classList.add('on');$('#mpCard .x').onclick=()=>{$('#mpCard').classList.remove('on');sel=null;draw()};
if(map){map.setFilter('sel',['==',['get','id'],id]);if(fly)map.flyTo({center:[l.lon,l.lat],zoom:Math.max(map.getZoom(),16.2),pitch:55,bearing:-18,padding:pad(),duration:R?0:1600,essential:true})}
document.querySelectorAll('.mp-it').forEach(e=>e.classList.toggle('on',e.dataset.id===id));if(innerWidth<=900)$('#mpPanel').classList.add('min')}
let pop;function hover(id){if(!map)return;const l=ALL.find(x=>x.id===id);if(!l)return;pop&&pop.remove();pop=new maplibregl.Popup({closeButton:false,offset:14}).setLngLat([l.lon,l.lat]).setHTML(`<div class="mp-pop">${esc(l.nome)}</div>`).addTo(map)}
$('#mpQ').oninput=e=>{F.q=e.target.value;draw()};
$('#mpOpen').onclick=e=>{F.open=!F.open;e.currentTarget.setAttribute('aria-pressed',F.open);if(F.open){F.h24=false;$('#mp24').setAttribute('aria-pressed',false)}draw(true)};
$('#mp24').onclick=e=>{F.h24=!F.h24;e.currentTarget.setAttribute('aria-pressed',F.h24);if(F.h24){F.open=false;$('#mpOpen').setAttribute('aria-pressed',false)}draw(true)};
const setMode=l=>{$('.mp').classList.toggle('lista',l);$('#mpMl').setAttribute('aria-pressed',l);$('#mpMm').setAttribute('aria-pressed',!l)};$('#mpMl').onclick=()=>setMode(true);$('#mpMm').onclick=()=>setMode(false);
const setView=d3=>{$('#mpV3').setAttribute('aria-pressed',d3);$('#mpV2').setAttribute('aria-pressed',!d3);if(!map)return;map.easeTo({pitch:d3?52:0,bearing:d3?-16:0,duration:R?0:1200});if(map.getLayer('bld'))map.setPaintProperty('bld','fill-extrusion-height',d3?['coalesce',['get','render_height'],8]:0)};
$('#mpV3').onclick=()=>setView(true);$('#mpV2').onclick=()=>setView(false);
$('#mpHandle').onclick=()=>$('#mpPanel').classList.toggle('min');
setInterval(()=>draw(),60000);
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
map.addControl(new maplibregl.AttributionControl({compact:true,customAttribution:'© <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a> · <a href="https://openfreemap.org" target="_blank">OpenFreeMap</a>'}),'bottom-left');
map.on('load',()=>{
map.addSource('locais',{type:'geojson',data:geo(list())});
map.addLayer({id:'halo',type:'circle',source:'locais',filter:['==',['get','aberto'],1],paint:{'circle-radius':['interpolate',['linear'],['zoom'],13,6,18,16],'circle-color':['get','cor'],'circle-opacity':.18,'circle-blur':.4}});
map.addLayer({id:'pts',type:'circle',source:'locais',paint:{'circle-radius':['interpolate',['linear'],['zoom'],13,['case',['==',['get','dest'],1],5,3],18,['case',['==',['get','dest'],1],11,7]],'circle-color':['get','cor'],'circle-stroke-color':'#fff','circle-stroke-width':['interpolate',['linear'],['zoom'],13,1,18,2.5],'circle-opacity':['case',['==',['get','aberto'],1],1,.55]}});
map.addLayer({id:'sel',type:'circle',source:'locais',filter:['==',['get','id'],''],paint:{'circle-radius':['interpolate',['linear'],['zoom'],13,10,18,22],'circle-color':'rgba(0,0,0,0)','circle-stroke-color':'#14171C','circle-stroke-width':2}});
map.addLayer({id:'dest-lbl',type:'symbol',source:'locais',filter:['==',['get','dest'],1],minzoom:14,layout:{'text-field':['get','nome'],'text-font':['Noto Sans Regular'],'text-size':12,'text-offset':[0,1.3],'text-anchor':'top'},paint:{'text-color':'#14171C','text-halo-color':'#fff','text-halo-width':1.6}});
map.on('click','pts',e=>pick(e.features[0].properties.id,true));
map.on('mouseenter','pts',e=>{map.getCanvas().style.cursor='pointer';hover(e.features[0].properties.id)});
map.on('mouseleave','pts',()=>{map.getCanvas().style.cursor='';pop&&pop.remove()});
/* entrada cinematográfica */
if(!R)setTimeout(()=>map.flyTo({center:[-46.664,-23.601],zoom:14.6,pitch:52,bearing:-16,padding:pad(),duration:3200,essential:true}),400);
let pulse=0;if(!R)(function an(){pulse=(pulse+.02)%1;if(map.getLayer('halo'))map.setPaintProperty('halo','circle-opacity',.12+Math.sin(pulse*Math.PI*2)*.08);requestAnimationFrame(an)})();
});
})();
