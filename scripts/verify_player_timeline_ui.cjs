// Pure rendering and event tests with a DOM stub, not a browser substitute.
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),out=path.join(root,'exports','20261029-招式时间轴-14');
const data=JSON.parse(fs.readFileSync(path.join(out,'board-data.json'),'utf8'));
const template=fs.readFileSync(path.join(root,'scripts/player_graph_template.html'),'utf8');
const source=fs.readFileSync(path.join(root,'scripts/player_graph_timeline.js'),'utf8');
const checks=[];function check(name,condition){assert.ok(condition,name);checks.push(name);}
const handlers={},winHandlers={};
function element(){return {hidden:true,style:{},attrs:{},dataset:{},innerHTML:'',classList:{add(){},remove(){}},setAttribute(k,v){this.attrs[k]=v;},removeAttribute(k){delete this.attrs[k];},getBoundingClientRect(){return {left:200,top:300,bottom:320,width:360,height:260};}};}
const document={createElement:element,body:{append(){}},addEventListener(k,fn){(handlers[k]??=[]).push(fn);}};
const context=vm.createContext({DATA:data,G:data.graph,byId:new Map(data.graph.nodes.map(n=>[n.id,n])),document,window:{addEventListener(k,fn){winHandlers[k]=fn;}},innerWidth:390,innerHeight:740,hideTooltip(){}});
vm.runInContext("const esc=s=>String(s??'未保存').replace(/[&<>\"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',\"'\":'&#39;'}[c])); const num=v=>typeof v==='number'?String(Number(v.toPrecision(6))):String(v??'未保存');",context);
for(const prefix of ['function orientation(','function avoidDirections(','function avoidSummary(','function variant(']){
 const line=template.split('\n').find(s=>s.startsWith(prefix));assert.ok(line,prefix);
 if(prefix!=='function variant(')vm.runInContext(line,context);
}
vm.runInContext(source,context);
const variantLine=template.split('\n').find(s=>s.startsWith('function variant('));
const defs=["const met=m=>m?.enabled===true?num(m.value):m?.enabled===false?'未启用':'未保存';", "const table=(h,rs)=>'<table><tr>'+h.map(x=>'<th>'+esc(x)+'</th>').join('')+'</tr>'+rs.map(r=>'<tr>'+r.map(v=>'<td>'+v+'</td>').join('')+'</tr>').join('')+'</table>';", "const raw=obj=>table(['字段','保存内容'],Object.entries(obj||{}).map(([k,v])=>[esc(k),esc(typeof v==='object'?JSON.stringify(v):v)]));", "const lvl=w=>'反应配置',power=v=>v,bool=v=>String(v);"];
vm.runInContext(defs.join('\n')+'\n'+variantLine,context);
const allAttacks={...data.outsideAttacks,...data.attacks};
const decode=s=>s.replace(/&quot;/g,'"').replace(/&#39;/g,"'").replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&amp;/g,'&');
let variants=0,buttons=0;
for(const n of Object.values(data.nodes)){
 const configs=[...n.variants,...n.conditionalVariants.flatMap(e=>e.variants.map(v=>({...v,conditionTag:e.tag})))];
 for(const [i,v] of configs.entries()){
  const html=context.variant(v,i,n.name,n.id),a=allAttacks[v.asset];variants++;
  check('one independent axis '+n.id+':'+i,(html.match(/data-timeline-asset=/g)||[]).length===1&&html.includes('data-timeline-asset="'+v.asset+'"'));
  const tips=[...html.matchAll(/data-timeline-tip="([^"]+)"/g)].map(m=>JSON.parse(decode(m[1])));buttons+=tips.length;
  check('every hit and permission renders '+n.id+':'+i,tips.length===a.timeline.hits.length+a.timeline.permissions.length);
  for(const tip of tips){
   check('tip keeps current tier and tag '+n.id+':'+i,tip.context.includes(v.tier)&&(!v.conditionTag||tip.context.includes(v.conditionTag)));
   check('successors belong to current config '+n.id+':'+i,tip.successors.every(e=>e.sourceConfig===n.id&&n.edges.some(r=>r.index===e.edge&&r.target===e.targetConfig)));
  }
  check('no undefined or invalid coordinates '+n.id+':'+i,!/undefined|NaN|Infinity/.test(html));
 }
}
const jab=Object.values(data.attacks).find(a=>a.asset.endsWith('/MainChar_Jab_FR.uasset'));
const v=data.nodes['44'].variants.find(v=>v.asset===jab.asset),row=jab.timeline.permissions.find(r=>r.action==='AttackLight');
const tip=context.timelineTip(row,'permission',jab,v,44);
check('jab light tooltip points to saved node45',tip.successors.some(e=>e.targetConfig===45));
check('unmapped guard attack has no invented successor',context.timelineSuccessors({transition:null},44).length===0);
check('one action reused in node54 gets node54 successors',context.timelineTip(row,'permission',jab,v,54).successors.every(e=>e.sourceConfig===54));
const target=element();target.dataset.timelineTip=JSON.stringify(tip);target.closest=()=>target;
for(const fn of handlers.focusin)fn({target});
const tooltip=vm.runInContext('timelineTooltip',context);
check('keyboard focus opens tooltip',!tooltip.hidden&&target.attrs['aria-describedby']==='timeline-tooltip');
check('390px placement arithmetic stays within stub viewport',parseFloat(tooltip.style.left)>=8&&parseFloat(tooltip.style.left)+360<=390-8&&parseFloat(tooltip.style.top)>=8);
for(const fn of handlers.scroll)fn({});check('scroll dismisses stale tooltip',tooltip.hidden&&!target.attrs['aria-describedby']);
for(const fn of handlers.pointerover)fn({target,pointerType:'mouse',clientX:385,clientY:730});check('mouse pointer opens tooltip',!tooltip.hidden);
for(const fn of handlers.keydown)fn({key:'Escape'});check('Escape dismisses tooltip',tooltip.hidden);
const malicious={...tip,title:'<img src=x onerror=alert(1)>',successors:[],sources:[]};target.dataset.timelineTip=JSON.stringify(malicious);
context.showTimelineTooltip(target);check('tooltip labels are escaped',tooltip.innerHTML.includes('&lt;img')&&!tooltip.innerHTML.includes('<img'));
const bare=fs.readFileSync(path.join(out,'player-board.html'),'utf8');
const focus=fs.readFileSync(path.join(out,'focus-board.html'),'utf8');
for(const [name,html] of [['barehands',bare],['focus',focus]]){
 check(name+' template markers expanded',!/__DATA__|__EDITOR_JS__|__TIMELINE_JS__|__TIMELINE_CSS__/.test(html));
 const js=html.slice(html.indexOf('<script>')+8,html.lastIndexOf('</script>'));
 new vm.Script(js,{filename:name+'.generated.js'});check(name+' full generated script parses',true);
}
const report={status:'passed',checks:checks.length,variants,windowButtons:buttons,source_sha256:crypto.createHash('sha256').update(source).digest('hex'),html_sha256:crypto.createHash('sha256').update(bare).digest('hex'),not_verified:['Real browser rendering, hover geometry, scrolling, focus and layout persistence','Actual game behavior'],details:checks};
fs.writeFileSync(path.join(out,'timeline-ui-static-verification.json'),JSON.stringify(report,null,2));
console.log(JSON.stringify({status:report.status,checks:report.checks,variants,windowButtons:buttons,not_verified:report.not_verified}));
