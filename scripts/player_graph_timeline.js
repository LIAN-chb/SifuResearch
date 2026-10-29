// Each variant supplies its own action and source node. Only tracks inside that
// variant share coordinates. DOM strings are escaped at the point of rendering.
function rangeText(r){
 const b=(x,lower)=>x.type==='open'?(lower?'无有限下界':'无有限上界'):num(x.value)+'帧（'+(x.type==='inclusive'?'含':'不含')+'端点）';
 return b(r.start,true)+' → '+b(r.end,false);
}
function timelineSuccessors(row,config){
 if(config===null||config===undefined||!row.transition)return [];
 return DATA.nodes[config].edges.filter(e=>e.rawInput.split('::').at(-1)===row.transition&&e.target!==null).map(e=>{
  const display=G.canonicalToDisplay[e.target],node=byId.get(display);
  return {id:display,sourceConfig:config,targetConfig:e.target,edge:e.index,
   text:(node?.label||DATA.nodes[e.target].name)+'（图节点 '+display+'，配置 '+e.target+'）',
   condition:e.conditional?'另需分支条件 '+e.key:'无额外保存分支条件',
   probability:e.probability};
 });
}
function timelineTip(row,kind,a,v,config){
 const r=a.timeline, next=kind==='permission'?timelineSuccessors(row,config):[];
 const condition=kind==='permission'?(row.hitConditions===31?'命中结果条件：覆盖代码全部5个分支。':'命中结果条件掩码 '+row.hitConditions+'：具体分支符号尚未恢复。'):'命中段按下方同号属性读取；激活条件保留在来源详情。';
 return {title:kind==='hit'?'攻击判定 · 段'+row.segment:row.label+' · 攻击订单许可',
  range:rangeText(row),context:orientation(v.slots)+' · '+v.tier+(v.conditionTag?' · 条件 '+v.conditionTag:''),
  condition,successors:next,
  note:kind==='permission'?(next.length?'后继是当前配置保存的衔接目标；实际选择仍受输入栈、技能与启动条件约束。':row.transition?'此输入在当前配置没有已保存后继；默认入口及其他系统路径未由此轴证明。':'此操作未通过通用连招映射接通后继，不能据此推定目标招式。'):row.specialAction?'含特殊命中启动器配置；不等于必然触发。':'',
  sources:kind==='hit'?['命中表行：'+row.row]:(row.sources||[]).map(s=>'原窗口'+(s.index+1)+' · '+rangeText(s.range)),
  boundary:row.end.type==='open'?'右侧箭头表示没有保存有限上界；绘图区右端不是动作结束。':''};
}
function timeline(a,v,config){
 const t=a.timeline;if(!t)return '<p class="notice">此动作尚无可定位的动画时间轴证据。</p>';
 const span=t.viewEnd-t.viewStart,pct=x=>Math.max(0,Math.min(100,(x-t.viewStart)/span*100));
 const rows=[];
 for(const r of t.hits)rows.push({r,kind:'hit',label:'攻击判定 · 段'+r.segment});
 for(const r of t.permissions)rows.push({r,kind:'permission',label:r.label});
 const track=({r,kind,label})=>{
  const start=r.start.value===null?t.viewStart:r.start.value,end=r.end.value===null?t.viewEnd:r.end.value;
  const tip=timelineTip(r,kind,a,v,config),key=JSON.stringify(tip);
  return '<div class="time-row"><span class="time-label">'+esc(label)+'</span><div class="time-track"><button type="button" class="time-window '+kind+(r.end.type==='open'?' open-end':'')+(r.start.type==='exclusive'?' exclusive-start':'')+(r.end.type==='exclusive'?' exclusive-end':'')+'" data-timeline-tip="'+esc(key)+'" data-start="'+esc(start)+'" data-end="'+esc(r.end.value??'open')+'" aria-label="'+esc(tip.title+'；'+tip.range)+'" style="left:'+pct(start)+'%;width:'+Math.max(.35,pct(end)-pct(start))+'%"></button></div></div>';
 };
 const markerRows=t.markers.map(m=>'<div class="time-row"><span class="time-label">'+esc(m.label)+'</span><div class="time-track marker-track"><span class="time-marker" style="left:'+pct(m.frame)+'%"><b>'+num(m.frame)+'</b></span></div></div>').join('');
 const ticks=[t.viewStart,...[.25,.5,.75].map(f=>t.viewStart+span*f),t.viewEnd];
 return '<section class="attack-timeline" data-timeline-asset="'+esc(a.asset)+'" aria-label="'+esc(v.tier+'独立动作时间轴')+'"><p class="timeline-caption">动画帧 · 绿色为攻击判定，蓝色为当前攻击订单许可。悬停或按Tab聚焦查看详情。</p><p class="timeline-limit">'+esc(t.rule)+' '+esc(t.missing)+'</p><div class="timeline-scroll"><div class="timeline-grid">'+markerRows+rows.map(track).join('')+'<div class="time-row time-axis"><span>动画帧坐标</span><div class="time-track">'+ticks.map((x,i)=>'<span class="time-tick tick-'+i+'" style="left:'+pct(x)+'%">'+num(Number(x.toFixed(1)))+'</span>').join('')+'</div></div></div></div><p class="timeline-limit">'+(t.animationEnd===null?'动作实际结束帧尚未恢复；右端仅为显示范围。':'动作结束帧：'+num(t.animationEnd)+'；窗口有效期仍受订单生命周期管理。')+(t.timing.sourceAnimation?' 已核源动画 '+num(t.timing.sourceAnimation.numFrames)+' 帧（约 '+num(t.timing.sourceAnimation.sequenceLengthSeconds)+' 秒），未当作当前动作结束。':'')+' 前摇配置 '+num(a.buildup)+' 帧是播放控制参数；不等于按键到命中的实测帧数。无有限上界的窗口用箭头延续。</p>'+(t.unresolved.length?'<p class="notice">'+t.unresolved.length+'条窗口的坐标或许可尚未接通，见来源详情。</p>':'')+'</section>';
}
const timelineTooltip=document.createElement('div');timelineTooltip.id='timeline-tooltip';timelineTooltip.role='tooltip';timelineTooltip.hidden=true;document.body.append(timelineTooltip);
let activeTimeWindow=null;
function hideTimelineTooltip(){if(activeTimeWindow){activeTimeWindow.removeAttribute('aria-describedby');activeTimeWindow.classList.remove('time-active');}activeTimeWindow=null;timelineTooltip.hidden=true;}
function showTimelineTooltip(target,event){
 const tip=JSON.parse(target.dataset.timelineTip);hideTooltip();hideTimelineTooltip();activeTimeWindow=target;target.classList.add('time-active');target.setAttribute('aria-describedby','timeline-tooltip');
 timelineTooltip.innerHTML='<strong>'+esc(tip.title)+'</strong><p>'+esc(tip.range)+'</p><p>'+esc(tip.context)+'</p><p>'+esc(tip.condition)+'</p>'+(tip.successors.length?'<p>保存后继：</p><ul>'+tip.successors.map(n=>'<li>'+esc(n.text)+'；'+esc(n.condition)+(n.probability!==100?'；选择权重 '+num(n.probability):'')+'</li>').join(''):'')+(tip.note?'<p>'+esc(tip.note)+'</p>':'')+(tip.boundary?'<p>'+esc(tip.boundary)+'</p>':'')+'<small>'+tip.sources.map(esc).join('<br>')+'</small>';
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
