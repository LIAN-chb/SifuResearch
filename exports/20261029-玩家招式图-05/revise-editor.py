from pathlib import Path
root=Path(__file__).resolve().parents[2]
p=root/'scripts/player_graph_editor.js'
s=p.read_text(encoding='utf-8')
s=s.replace("const KEY='sifu.barehands.layout.v1'","const GRID={x:240,y:120,ox:150,oy:110},KEY='sifu.barehands.layout.v1'")
s=s.replace("width:20,height:20,patternUnits:'userSpaceOnUse'","x:GRID.ox,y:GRID.oy,width:GRID.x,height:GRID.y,patternUnits:'userSpaceOnUse'")
s=s.replace("r:1,fill:'#b6c3ac'","r:2,fill:'#aabca0'")
s=s.replace('>网格吸附</label>','>大网格吸附</label>')
s=s.replace("nodes:snapshot(),snap};","nodes:snapshot(),snap,grid:{x:GRID.x,y:GRID.y}};")
start=s.index('  // All endpoint stubs')
end=s.index('  function pathD',start)
s=s[:start]+'''  // Node-sized editing cells and routing channels are independent.
  const router=globalThis.createPlayerGraphRouter();
  const snapValue=(v,axis)=>{const origin=axis==='x'?GRID.ox:GRID.oy;return origin+Math.round((v-origin)/GRID[axis])*GRID[axis];};
'''+s[end:]
start=s.index('  function unionSegments(')
end=s.index('  function drawBaseline()',start)
s=s[:start]+'''  function unionSegments(source){return router.mergeSegments(source).map(s=>({...s,ids:new Set(s.ids),core:s.ids.some(id=>basePairs.has(id))}));}
'''+s[end:]
start=s.index('  function reserve(')
end=s.index('  highlight=function',start)
s=s[:start]+s[end:]
old="const used=new Set();for(const e of G.edges.filter(e=>e.target!==null&&(e.source===id||e.target===id)).sort((a,b)=>a.id.localeCompare(b.id))){const points=routed(e,true,used)||routes.get(e.id)?.points;if(points){reserve(points,used);active.push({e,points});}}"
new="for(const e of G.edges.filter(e=>e.target!==null&&(e.source===id||e.target===id))){const points=routes.get(e.id)?.points;if(points)active.push({e,points});}"
assert old in s;s=s.replace(old,new)
start=s.index('  function redraw(){')
end=s.index('  function schedule()',start)
s=s[:start]+'''  function redraw(){if(raf){cancelAnimationFrame(raf);raf=0;}const result=router.routeAll(G.nodes,G.edges,basePairs);extent=result.extent;routingFailures=result.failures;routes=new Map(result.routes.map(r=>[r.e.id,r]));for(const n of G.nodes)nodeEls.get(n.id).setAttribute('transform','translate('+n.x+','+n.y+')');updateDecorations();highlight(editing?null:selected);if(routingFailures.length)status('部分连接空间不足，请拉开附近节点',true);window.playerGraphLayout.routes=[...routes.values()].map(r=>({id:r.e.id,points:r.points,source:r.e.source,target:r.e.target}));window.playerGraphLayout.segments=segments.map(s=>({...s,ids:[...s.ids]}));}
'''+s[end:]
s=s.replace("if(snap)target=Math.round(target/20)*20;","if(snap)target=snapValue(target,axis);")
s=s.replace("dx=Math.round((origin.x+dx)/20)*20-origin.x;dy=Math.round((origin.y+dy)/20)*20-origin.y;","dx=snapValue(origin.x+dx,'x')-origin.x;dy=snapValue(origin.y+dy,'y')-origin.y;")
s=s.replace("ns.forEach((n,i)=>n[axis]=Math.round(start+spacing*i));","const first=snap?snapValue(start,axis):start,gap=snap?Math.max(GRID[axis],Math.round(spacing/GRID[axis])*GRID[axis]):spacing;ns.forEach((n,i)=>n[axis]=Math.round(first+gap*i));")
# Save state is visible in reading mode too; no new storage key or automatic resnapping.
old="const $=id=>document.getElementById(id),status=(s,error=false)=>{$('save-state').textContent=s;$('save-state').classList.toggle('error',error);};"
new="const savedBadge=document.createElement('span');savedBadge.id='layout-save-status';savedBadge.style.marginLeft='auto';savedBadge.textContent='默认布局 · 编辑后自动保存';document.querySelector('.legend').append(savedBadge);const $=id=>document.getElementById(id),status=(s,error=false)=>{$('save-state').textContent=s;$('save-state').classList.toggle('error',error);savedBadge.textContent=s;savedBadge.title=s;};"
assert old in s;s=s.replace(old,new)
s=s.replace(".editbar{display:flex;", ".legend{flex-wrap:wrap;height:auto;min-height:37px;gap:7px 18px}#layout-save-status{font-size:11px;max-width:270px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.editbar{display:flex;")
p.write_text(s,encoding='utf-8')
