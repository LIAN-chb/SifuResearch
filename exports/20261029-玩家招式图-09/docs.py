from pathlib import Path
R=Path(__file__).resolve().parents[2]
p=R/'Sifu/03配置/玩家攻击/徒手招式板小样.md';s=p.read_text(encoding='utf-8')
s+='\n09版页面空间调整：桌面标题与操作合并为52px紧凑工具栏；窄屏78px，按钮可横向滚动。图例与操作说明在“说明”按钮内按需展开，不占画布高度。详情从窗口顶部展开至底部，内容独立滚动，关闭按钮固定在抽屉顶部。编辑工具仍只在编辑时占位；保留08版全部研究标注、节点位置与保存格式。当前展示产物见exports/20261029-玩家招式图-09/及notes/handoffs/20261029-玩家招式图-09.md，08为研究证据来源。\n'
p.write_text(s,encoding='utf-8')
for name,prefix,suffix in [('研究进度与问题.md','玩家招式展示（',' 09版仅压缩顶部并改为全窗口高详情，图例收在“说明”，保留08研究结果与布局保存。'),('解包与解析进度.md','招式图08批',' 09展示批仅调整工具栏／说明与全高详情，无新增提取或机制结论。')]:
 p=R/'Sifu/00索引'/name;lines=p.read_text(encoding='utf-8').splitlines();assert sum(x.startswith(prefix) for x in lines)==1
 p.write_text('\n'.join(x+suffix if x.startswith(prefix) else x for x in lines)+'\n',encoding='utf-8')
