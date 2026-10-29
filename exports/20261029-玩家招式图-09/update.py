from pathlib import Path
R=Path(__file__).resolve().parents[2]
p=R/'scripts/player_graph_template.html';s=p.read_text(encoding='utf-8')
css='''
header{height:52px;padding:6px 16px;gap:18px}h1{font-size:17px;white-space:nowrap}.tools{flex-wrap:nowrap;min-width:0;overflow-x:auto;justify-content:flex-start;scrollbar-width:thin}.tools>*{flex-shrink:0}.tool{padding:4px 9px;font-size:12px}.tools label{font-size:11px}#stage{height:calc(100dvh - 52px)}
.drawer{position:fixed;top:0;bottom:0;height:100dvh;z-index:20}.drawer-head{flex-shrink:0;padding:13px 20px 10px}.drawer-body{min-height:0}.help-panel{position:fixed;right:16px;top:58px;width:420px;max-width:calc(100vw - 24px);max-height:70dvh;overflow:auto;z-index:10;background:#fffef9;border:1px solid #ccd6c7;border-radius:9px;box-shadow:0 5px 22px #354e3020;padding:14px;font-size:12px}.help-panel[hidden]{display:none}.help-panel p{margin:7px 0}.help-panel .legend{height:auto;min-height:0;padding:0;display:flex;flex-wrap:wrap;gap:7px 18px}.help-panel .legend span{display:block}#layout-save-status{max-width:145px!important;font-size:10px}
@media(max-width:760px){header{height:78px;padding:5px 10px;gap:3px;flex-direction:column;align-items:stretch;justify-content:center}h1{font-size:15px;line-height:23px}.tools{max-width:none;min-height:34px;width:100%;gap:6px}.tools label{display:inline-flex;align-items:center}.tools .tool{padding:4px 7px}#layout-save-status{display:none}#stage{height:calc(100dvh - 78px)}.help-panel{top:84px;right:12px}.drawer-head{padding:10px 14px}.drawer h2{font-size:17px}.drawer-body{padding-left:14px;padding-right:14px}}
'''
s=s.replace('</style>',css+'</style>',1)
s=s.replace('<h1>徒手招式关系图</h1><p>轻重两行居中 · 点一招看前驱与后继 · 拖动／滚轮缩放</p>','<h1>徒手招式关系图</h1>')
s=s.replace('<button class="tool" id="audit">覆盖与待核</button>','<button class="tool" id="audit">覆盖与待核</button><button class="tool" id="help-toggle" aria-expanded="false" aria-controls="help-panel">说明</button>')
s=s.replace('<div class="legend"><span>','<section class="help-panel" id="help-panel" aria-label="使用说明与图例" hidden><div class="legend"><span>',1)
s=s.replace('方向通用接入 · 用户观察</span></div>','方向通用接入 · 用户观察</span></div><p>点击招式查看属性与前后衔接；点击画布空白关闭详情。拖动画布平移，滚轮缩放。</p><p>编辑布局：每格一个节点，自动保存；导出可作备份。</p><p>关系来自保存配置；虚线通用接入另标来源。无后续保存边不代表实战不能接招。</p></section>',1)
caption='<div class="caption">关系来自保存配置；虚线通用接入另标来源。无后续保存边不代表实战不能接招。</div>'
assert caption in s;s=s.replace(caption,'')
s=s.replace('function openDrawer(title,subtitle,content){','function openDrawer(title,subtitle,content){setHelp(false);')
s=s.replace("document.getElementById('audit').onclick=audit;", """document.getElementById('audit').onclick=audit;
function setHelp(open){document.getElementById('help-panel').hidden=!open;document.getElementById('help-toggle').setAttribute('aria-expanded',String(open));}
document.getElementById('help-toggle').onclick=()=>setHelp(document.getElementById('help-panel').hidden);
document.addEventListener('pointerdown',e=>{if(!e.target.closest('#help-panel,#help-toggle'))setHelp(false);});
document.addEventListener('keydown',e=>{if(e.key==='Escape')setHelp(false);});""")
p.write_text(s,encoding='utf-8')
p=R/'scripts/player_graph_editor.js';s=p.read_text(encoding='utf-8').replace("document.querySelector('.legend').after(bar)","document.querySelector('header').after(bar)").replace("document.querySelector('.legend').append(savedBadge)","document.querySelector('.tools').append(savedBadge)")
p.write_text(s,encoding='utf-8')
for name in ['build_player_board.py','verify_player_board.py']:
 p=R/'scripts'/name;s=p.read_text(encoding='utf-8').replace('20261029-玩家招式待核-08','20261029-玩家招式图-09');p.write_text(s,encoding='utf-8')
