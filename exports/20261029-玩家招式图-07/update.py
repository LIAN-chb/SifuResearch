from pathlib import Path
R=Path(__file__).resolve().parents[2]
p=R/'scripts/player_graph_template.html'
s=p.read_text(encoding='utf-8')
start=s.index('function variant(')
end=s.index('\nfunction relation(',start)
s=s[:start]+'''function variant(v,i,name='招式配置'){const a=DATA.attacks[v.asset]||DATA.outsideAttacks[v.asset],ws=a.windows;return '<div class="variant"><h4>'+esc(name)+'（正背面待核／上中下段待核）</h4><p class="muted variant-kind">'+esc(v.tier)+' · 姿态变体'+(i+1)+'</p><p class="muted timing">前摇配置：'+num(a.buildup)+' 帧（实际起手待核）</p><p class="muted distance">距离参数：'+num(a.range)+'</p><div class="scroll">'+table(['命中段','生命','架势','受击硬直配置帧','格挡架势','弹开架势'],ws.map((w,j)=>[j+1,met(w.damage),met(w.structure),met(w.stun),met(w.guard),met(w.deflect)]))+'</div>'+ws.map((w,j)=>'<div class="hit-properties"><p>段'+(j+1)+'：'+esc(lvl(w))+'；攻击强度 '+power(w.power)+'；韧性比较覆盖 '+met(w.resilience)+'；</p><p>可招架字段 '+bool(w.parriable)+'；推距 '+met(w.push)+'。</p></div>').join('')+'<details><summary>来源与完整字段</summary><div class="evidence"><p>'+esc(v.asset)+'；姿态槽 '+esc(v.slots.join('、')||'树外候选')+'</p>'+ws.map(w=>'<p>'+esc(w.table)+'／'+esc(w.row)+'</p>'+raw(w.raw)).join('')+raw(a.raw)+'</div></details></div>';}
'''.rstrip()+s[end:]
s=s.replace('width:450px;max-width:94vw','width:650px;max-width:94vw')
s=s.replace('</style>','.variant .timing,.variant .distance{margin:3px 0}.variant-kind{margin:2px 0 8px}.hit-properties{font-size:12px;color:#52634d;margin:10px 0}.hit-properties p{margin:0}.hit-properties p+p{margin-top:3px}.drawer-body>h3:first-child{margin-top:12px}</style>')
s=s.replace("let content='<h3>能接到这里</h3>'", "const relations='<h3>能接到这里</h3>'")
old="+'</details><h3>配置与属性</h3><p class=\"muted\">配置值不等于实战最终效果。硬直指对方受击硬直；前摇配置不等于实测首次命中时刻。特殊反应等级还需比较敌人抗性。</p>';"
assert old in s
s=s.replace(old,"+'</details>';let content='<h3>招式属性</h3>';")
s=s.replace("c.variants.map(variant).join('')","c.variants.map((v,i)=>variant(v,i,c.name)).join('')")
s=s.replace(" const records=G.edges.filter", " content+='<details><summary>属性读法与适用边界</summary><p class=\"muted\">配置值不等于实战最终效果。硬直指对方受击硬直；前摇配置不等于实测首次命中时刻。特殊反应等级还需比较敌人抗性。</p></details>'+relations;\n const records=G.edges.filter")
s=s.replace("textContent=title;document.getElementById('drawer-subtitle')", "textContent=title+(selected!==null&&title===byId.get(selected)?.label?'（正背面待核／上中下段待核）':'');document.getElementById('drawer-subtitle')")
s=s.replace("variant({asset:n.asset,tier:'候选',slots:[]},i)", "variant({asset:n.asset,tier:'候选',slots:[]},i,n.name)")
s=s.replace("svg.addEventListener('pointerup',()=>{drag=null;});", "svg.addEventListener('pointerup',()=>{if(drag&&!moved)closeDrawer();drag=null;});svg.addEventListener('pointercancel',()=>{drag=null;});")
p.write_text(s,encoding='utf-8')
for name in ['build_player_board.py','verify_player_board.py']:
 p=R/'scripts'/name
 p.write_text(p.read_text(encoding='utf-8').replace('20261029-玩家招式图-06','20261029-玩家招式图-07'),encoding='utf-8')
