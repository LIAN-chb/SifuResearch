from pathlib import Path
R=Path(__file__).resolve().parents[2]
p=R/'scripts/player_graph_template.html';s=p.read_text(encoding='utf-8')
s=s.replace('<header><div><h1>徒手招式关系图</h1></div>','<header><div class="page-brand"><select id="page-switch" aria-label="武器形态与页面"></select><h1>徒手招式关系图</h1></div>')
s=s.replace('</main>','</main><div id="node-tooltip" role="tooltip" hidden></div>')
s=s.replace('</style>','''.page-brand{display:flex;gap:12px;align-items:center;min-width:0}#page-switch{background:#fffef8;color:#37543e;border:1px solid #c9d4c1;border-radius:6px;padding:4px 6px;font:12px Microsoft YaHei,sans-serif;max-width:155px}.page-brand h1{font-size:15px}#node-tooltip{position:fixed;z-index:40;max-width:min(380px,calc(100vw - 20px));padding:10px 13px;border:1px solid #bdcdb9;border-radius:8px;background:#fffef9;box-shadow:0 5px 18px #284b3028;color:#2c4132;font-size:13px;pointer-events:none}#node-tooltip[hidden]{display:none}#node-tooltip strong{display:block}#node-tooltip small{display:block;font-size:11px;color:#6b7966}.official-names{border-left:3px solid #63875f;padding:7px 10px;background:#f0f4e9;margin:8px 0}.official-names p{margin:2px 0}.node.supplement rect{stroke-dasharray:5 3}.focus-intro{position:absolute;top:14px;left:18px;max-width:min(700px,85vw);font-size:12px;color:#66775f;pointer-events:none}.focus-cost{font-size:16px;margin:8px 0}@media(max-width:760px){.page-brand{gap:10px}.page-brand h1{font-size:13px}#page-switch{max-width:140px;padding:2px 4px}}
</style>''')
needle="const G=DATA.graph"
s=s.replace(needle,"""const pageSwitch=document.getElementById('page-switch');for(const p of DATA.pages){const option=document.createElement('option');option.value=p.file;option.textContent=p.label;option.selected=p.page===DATA.page;pageSwitch.append(option);}pageSwitch.onchange=()=>location.assign(new URL(pageSwitch.value,location.href).href);if(DATA.page==='focus'){document.title='徒手专注';document.querySelector('h1').textContent='徒手专注';const note=document.createElement('p');note.className='focus-intro';note.textContent='在专注模式选择招式；点击查看消耗和覆盖命中配置。普通连段后续尚未接通，暂不绘制推测连线。';document.getElementById('stage').append(note);}
const G=DATA.graph""")
# Helpers are initialized before node event handlers are used.
s=s.replace('const nodeEls=new Map();', '''const nodeEls=new Map(),tooltip=document.getElementById('node-tooltip');
function officialHtml(items){return items?.length?'<div class="official-names">'+items.map(o=>'<p><strong>'+esc(o.name)+'</strong> <span class="muted">'+esc(o.scope)+'</span></p>').join('')+'</div>':'<p class="muted">未见与此动作独立对应的官方菜单名称，保留操作称呼。</p>';}
function hideTooltip(){tooltip.hidden=true;}
function showTooltip(n,event){if(document.body.classList.contains('editing'))return;tooltip.innerHTML=(n.official?.length?n.official.map(o=>'<strong>'+esc(o.name)+'</strong><small>'+esc(o.scope)+'</small>').join(''):'<strong>'+esc(n.label)+'</strong><small>操作称呼 · 未见独立官方名称</small>');tooltip.hidden=false;const box=nodeEls.get(n.id).getBoundingClientRect(),x=event?.clientX??box.right,y=event?.clientY??box.top;const size=tooltip.getBoundingClientRect();tooltip.style.left=Math.max(8,Math.min(innerWidth-size.width-8,x+14))+'px';tooltip.style.top=Math.max(8,Math.min(innerHeight-size.height-8,y+14))+'px';}
''')
s=s.replace("group.append(text,el('title',{},n.label+'：查看前后衔接与详细属性'));", "group.append(text);group.setAttribute('aria-label',n.label+'；'+(n.official?.map(o=>o.name).join('、')||'未见独立官方名称'));group.setAttribute('aria-describedby','node-tooltip');group.addEventListener('pointerenter',e=>{if(e.pointerType!=='touch')showTooltip(n,e);});group.addEventListener('pointermove',e=>{if(!tooltip.hidden)showTooltip(n,e);});group.addEventListener('pointerleave',hideTooltip);group.addEventListener('focus',()=>showTooltip(n));group.addEventListener('blur',hideTooltip);")
s=s.replace("function nodeOrientation(n){return", "function nodeOrientation(n){if(n.action)return n.action.kind==='focus'?'徒手专注':'独立动作入口';return")
s=s.replace("const n=byId.get(id);highlight(id);const pre=", "const n=byId.get(id);hideTooltip();highlight(id);if(n.action){openAction(n);return;}const pre=")
s=s.replace("let content='<h3>招式属性</h3>", "let content='<h3>招式属性</h3>'+officialHtml(n.official)+'")
s=s.replace("esc(c.name)+' · '+c.variants.length", "esc(c.name)+' · '+c.variants.length")
s=s.replace("<p class=\"muted\">技能：'+esc(c.tags.length?'需要解锁；标签见节点证据':'本节点未保存技能标签，其他条件仍可能限制')+'</p>'", "'+officialHtml(c.official)+'<p class=\"muted\">技能：'+esc(c.tags.length?c.tags.map(t=>DATA.skillNames[t.split('.').at(-1).toLowerCase()]||t).join('、'):'本节点未保存技能标签')+'</p>'")
# Add action-specific detail rather than empty normal combo sections.
needle='function select(id)'
action='''function openAction(n){const a=n.action,ws=a.windows||[];let content='<h3>招式属性</h3>'+officialHtml(n.official);if(a.kind==='focus'){content+='<p class="focus-cost">专注消耗：'+esc(num(a.cost))+' 格（配置）</p><p>'+esc(a.entryText)+'</p><p class="muted">以下是专注覆盖命中表配置，敌人具体弱点可覆写；不是整段同步动画最终总伤害。</p><div class="scroll">'+table(['命中段','生命','架势','受击硬直配置帧','格挡架势','弹开架势'],ws.map((w,j)=>[j+1,met(w.damage),met(w.structure),met(w.stun),met(w.guard),met(w.deflect)]))+'</div>'+ws.map((w,j)=>'<div class="hit-properties"><p>段'+(j+1)+'：'+esc(lvl(w))+'；攻击强度 '+power(w.power)+'；韧性比较覆盖 '+met(w.resilience)+'；</p><p>可招架字段 '+bool(w.parriable)+'；推距 '+met(w.push)+'。</p></div>').join('')+'<h3>后续衔接</h3><p>不属于普通连招树；专注结束后的动作许可与具体接招尚未接通。没有据此画连线，也不代表没有后续。</p>';}
else{content+='<h3>操作入口</h3><p>'+esc(a.entry)+'</p><p class="muted">此动作由独立能力输入进入，补充在同一画布中。尚未核到它与普通节点之间的具体衔接边。</p><p class="muted">未接通独立命中表，生命、架势与帧数暂不套用其他招式数值。</p>';}
content+='<details><summary>来源与条件</summary><div class="evidence"><pre>'+esc(JSON.stringify(a,null,2))+'</pre></div></details>';openDrawer(n.label,a.kind==='focus'?'专注名称来自实际弱点配置的本地化引用':'已定位独立能力入口；未伪造普通连段关系',content);}
'''
s=s.replace(needle,action+needle)
s=s.replace("function audit(){lastFocus=", "function audit(){if(DATA.page==='focus'){openDrawer('徒手专注覆盖','5项共享弱点配置','<p>名称来自实际VitalPointData；覆盖命中表逐项保留。敌人可覆盖弱点参数。普通连段后续尚未接通。</p><details><summary>来源与边界</summary><div class=\"evidence\"><pre>'+esc(JSON.stringify(DATA.focusSource,null,2))+'</pre></div></details>');return;}lastFocus=")
s=s.replace("<h3>尚待确认</h3>", "<h3>本次补全</h3><p>原33个连招节点保留；新增3个独立动作入口。25条徒手菜单命名均已对应节点或整套连招。57条条件替换已解码，属于替换招式设置，不作为默认新增节点。</p><h3>尚待确认</h3>")
s=s.replace('标签覆写的具体资源仍有缺口','条件替换的运行期启用、树外其他动作仍有缺口')
s=s.replace("document.getElementById('close').onclick", "window.addEventListener('blur',hideTooltip);svg.addEventListener('pointerdown',hideTooltip);document.getElementById('close').onclick")
p.write_text(s,encoding='utf-8')
