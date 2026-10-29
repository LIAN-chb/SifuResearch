from pathlib import Path
R=Path(__file__).resolve().parents[2]
p=R/'scripts/player_graph_template.html';s=p.read_text(encoding='utf-8')
start=s.index('const regions=document.getElementById');end=s.index('// Orthogonal paths',start)
s=s[:start]+"const regions=document.getElementById('regions'),common=document.getElementById('common-layer');\n"+s[end:]
s=s.replace('<span><i class="key reported-key"></i>方向通用接入 · 用户观察</span>','')
s=s.replace('点击招式查看属性与前后衔接；点击画布空白关闭详情。','详情关闭时，悬停招式预览前后衔接；点击打开属性并锁定连接，点击画布空白关闭详情。')
s=s.replace('关系来自保存配置；虚线通用接入另标来源。','关系来自保存配置。')
start=s.index("+(n.direction?'<p class=\"notice\">");end=s.index("+'<h3>这里能接到",start)
s=s[:start]+s[end:]
s=s.replace('let selected=null,lastFocus=null;',"let selected=null,lastFocus=null,hovered=null;\nfunction readHighlightId(){return drawer.classList.contains('open')?selected:hovered;}")
s=s.replace("lastFocus?.focus({preventScroll:true});}","lastFocus?.focus({preventScroll:true});selected=null;highlight(readHighlightId());}")
s=s.replace("document.getElementById('all-lines').onchange=()=>highlight(selected)","document.getElementById('all-lines').onchange=()=>highlight(readHighlightId())")
p.write_text(s,encoding='utf-8')
p=R/'scripts/player_graph_editor.js';s=p.read_text(encoding='utf-8')
start=s.index('  function updateDecorations()');end=s.index('\n  function redraw()',start)
s=s[:start]+"  function updateDecorations(){regions.replaceChildren();common.replaceChildren();drawCells();}"+s[end:]
s=s.replace('highlight(editing?null:selected)','highlight(editing?null:readHighlightId())')
s=s.replace("if(editing){if(selected!==null)","hovered=null;if(editing){if(selected!==null)")
needle='  window.addEventListener(\'resize\',stageSize);'
assert needle in s
s=s.replace(needle,"""  // Hover previews never open or replace the pinned detail selection.
  for(const [id,node] of nodeEls){
    node.addEventListener('pointerenter',e=>{if(editing||e.pointerType==='touch')return;hovered=id;if(!drawer.classList.contains('open'))highlight(id);});
    node.addEventListener('pointerleave',()=>{if(hovered===id)hovered=null;if(!editing&&!drawer.classList.contains('open'))highlight(null);});
  }
  window.addEventListener('blur',()=>{hovered=null;if(!editing&&!drawer.classList.contains('open'))highlight(null);});
"""+needle)
p.write_text(s,encoding='utf-8')
for name in ['build_player_board.py','verify_player_board.py']:
 p=R/'scripts'/name;p.write_text(p.read_text(encoding='utf-8').replace('20261029-玩家招式图-09','20261029-玩家招式图-10'),encoding='utf-8')
