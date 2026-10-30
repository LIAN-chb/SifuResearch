// Display only saved attack successors; collapse operations sharing coordinates.
function rangeText(r){
 const lo=r.start.value,hi=r.end.value;
 if(hi===null)return (lo===null?'…':num(lo)+'帧起…')+(r.start.type==='exclusive'?'（不含起点）':'');
 return (lo===null?'…':num(lo))+'–'+num(hi)+'帧'+(r.start.type==='exclusive'?'（不含起点）':'')+(r.end.type==='exclusive'?'（不含终点）':'');
}
function timelineSuccessors(row,config){
 if(config===null||config===undefined||!row.transition)return [];
 return DATA.nodes[config].edges.filter(e=>e.rawInput.split('::').at(-1)===row.transition&&e.target!==null).map(e=>{
  const display=G.canonicalToDisplay[e.target],node=byId.get(display);
  return {id:display,sourceConfig:config,targetConfig:e.target,edge:e.index,
   text:node?.label||DATA.nodes[e.target].name,
   condition:e.conditional?'需满足该衔接分支条件':'',
   probability:e.probability};
 });
}
function timelineWindows(a,config){
 const groups=new Map(),general=new Set(['Dodge','Avoid','Guard','Parry','MoveInterrupt']);
 for(const r of a.timeline.permissions){
  const successors=timelineSuccessors(r,config);
  if(!successors.length&&!general.has(r.action))continue;
  const key=JSON.stringify([r.start,r.end,r.hitConditions]);
  if(!groups.has(key))groups.set(key,{start:r.start,end:r.end,hitConditions:r.hitConditions,operations:[]});
  groups.get(key).operations.push({action:r.action,label:r.label,successors});
 }
 return [...groups.values()].sort((a,b)=>(a.start.value??-Infinity)-(b.start.value??-Infinity));
}
function timelineTip(row,kind,a,v,config){
 const operations=kind==='permission'?(row.operations||[{action:row.action,label:row.label,successors:timelineSuccessors(row,config)}]):[];
 const successors=operations.flatMap(o=>o.successors.map(n=>({...n,input:o.label})));
 const general=operations.filter(o=>!o.successors.length).map(o=>o.label);
 return {kind,title:kind==='buildup'?'动画前摇':kind==='hit'?'攻击判定 · 段'+row.segment:successors.length?(general.length?'衔接／取消窗口':'衔接窗口'):'操作取消窗口',
  range:rangeText(row),context:orientation(v.slots)+' · '+v.tier+(v.conditionTag?' · '+v.conditionTag:''),
  condition:kind==='permission'&&row.hitConditions!==31?'另需满足该窗口的命中结果条件':'',
  successors,operations:general,
  note:kind==='buildup'?'期望前摇：'+num(a.buildup)+'帧（播放控制目标）。':kind==='hit'&&row.specialAction?'此段配置有特殊命中动作。':''};
}
function timeline(a,v,config){
 const t=a.timeline;if(!t)return '';
 const permissions=timelineWindows(a,config),buildup=t.timing.lastBuildupFrame;
 const finite=[0,...t.hits.flatMap(r=>[r.start.value,r.end.value]),...permissions.flatMap(r=>[r.start.value,r.end.value]),buildup].filter(Number.isFinite);
 const left=Math.min(...finite),right=Math.max(1,...finite)*1.08,span=right-left,pct=x=>Math.max(0,Math.min(100,(x-left)/span*100));
 const rows=[];
 for(const r of t.hits)rows.push({r,kind:'hit',label:'攻击判定 · 段'+r.segment});
 for(const r of permissions)rows.push({r,kind:'permission',label:timelineTip(r,'permission',a,v,config).title.replace('窗口','')});
 const track=({r,kind,label})=>{
  const start=r.start.value??left,end=r.end.value,open=end===null;
  const tip=timelineTip(r,kind,a,v,config),key=JSON.stringify(tip);
  const position=open?'left:clamp(0px,calc('+pct(start)+'% - 10px),calc(100% - 20px));width:20px':'left:'+pct(start)+'%;width:'+Math.max(.35,pct(end)-pct(start))+'%';
  return '<div class="time-row"><span class="time-label">'+esc(label)+'</span><div class="time-track"><button type="button" class="time-window '+kind+(kind==='buildup'?' buildup-band':'')+(open?' time-point':'')+'" data-timeline-tip="'+esc(key)+'" data-start="'+esc(start)+'" data-end="'+esc(end??'open')+'" aria-label="'+esc(tip.title+'；'+tip.range)+'" style="'+position+'">'+(open?'…':'')+'</button></div></div>';
 };
 const buildupRange={start:{value:0,type:'inclusive'},end:{value:buildup,type:'inclusive'}};
 const buildupRow=Number.isFinite(buildup)?track({r:buildupRange,kind:'buildup',label:'动画前摇 0–'+num(buildup)}):'';
 const ticks=[left,...[.25,.5,.75].map(f=>left+span*f),right];
 return '<section class="attack-timeline" data-timeline-asset="'+esc(a.asset)+'" aria-label="'+esc(v.tier+'独立动作时间轴')+'"><p class="timeline-caption">'+(Number.isFinite(buildup)?'动画前摇到 '+num(buildup)+' 帧；':'动画前摇末帧未保存；')+'期望前摇 '+num(a.buildup)+' 帧（播放控制目标）。</p><div class="timeline-scroll"><div class="timeline-grid">'+buildupRow+rows.map(track).join('')+'<div class="time-row time-axis"><span>动画帧</span><div class="time-track">'+ticks.map((x,i)=>'<span class="time-tick tick-'+i+'" style="left:'+pct(x)+'%">'+num(Number(x.toFixed(1)))+'</span>').join('')+'</div></div></div></div><p class="timeline-limit">绿色：攻击判定　蓝色：衔接／取消许可　…：该帧起无上界。许可配置未实测，右端不是动作结束。</p></section>';
}
const timelineTooltip=document.createElement('div');timelineTooltip.id='timeline-tooltip';timelineTooltip.role='tooltip';timelineTooltip.hidden=true;document.body.append(timelineTooltip);
let activeTimeWindow=null;
function hideTimelineTooltip(){if(activeTimeWindow){activeTimeWindow.removeAttribute('aria-describedby');activeTimeWindow.classList.remove('time-active');}activeTimeWindow=null;timelineTooltip.hidden=true;}
function showTimelineTooltip(target,event){
 const tip=JSON.parse(target.dataset.timelineTip);hideTooltip();hideTimelineTooltip();activeTimeWindow=target;target.classList.add('time-active');target.setAttribute('aria-describedby','timeline-tooltip');
 const seen=new Set(),successors=tip.successors.filter(n=>{const key=n.input+'|'+n.text+'|'+n.condition;if(seen.has(key))return false;seen.add(key);return true;});
 timelineTooltip.innerHTML='<strong>'+esc(tip.title)+' · '+esc(tip.range)+'</strong>'+(successors.length?'<ul>'+successors.map(n=>'<li>'+esc(n.input)+' → '+esc(n.text)+(n.condition?'（'+esc(n.condition)+'）':'')+'</li>').join(''):'')+(tip.operations?.length?'<p>'+esc(tip.operations.join('、'))+'</p>':'')+(tip.condition?'<p>'+esc(tip.condition)+'</p>':'')+(tip.note?'<p>'+esc(tip.note)+'</p>':'');
 timelineTooltip.hidden=false;
 const box=target.getBoundingClientRect(),size=timelineTooltip.getBoundingClientRect(),x=event?.clientX??box.left+box.width/2,y=event?.clientY??box.bottom;
 timelineTooltip.style.left=Math.max(8,Math.min(innerWidth-size.width-8,x+12))+'px';
 timelineTooltip.style.top=Math.max(8,Math.min(innerHeight-size.height-8,y+12))+'px';
}
document.addEventListener('pointerover',e=>{const target=e.target.closest('[data-timeline-tip]');if(target&&e.pointerType!=='touch')showTimelineTooltip(target,e);});
document.addEventListener('pointerout',e=>{if(e.target.closest('[data-timeline-tip]'))hideTimelineTooltip();});
document.addEventListener('focusin',e=>{const target=e.target.closest('[data-timeline-tip]');if(target)showTimelineTooltip(target);});
document.addEventListener('focusout',e=>{if(e.target.closest('[data-timeline-tip]'))hideTimelineTooltip();});
document.addEventListener('scroll',hideTimelineTooltip,true);window.addEventListener('resize',hideTimelineTooltip);window.addEventListener('blur',hideTimelineTooltip);
document.addEventListener('keydown',e=>{if(e.key==='Escape')hideTimelineTooltip();});
