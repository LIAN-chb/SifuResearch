from pathlib import Path
R=Path(__file__).resolve().parents[2]
p=R/'Sifu/03配置/玩家攻击/徒手招式板小样.md';s=p.read_text(encoding='utf-8');s+='\n10版交互：移除画布分类浮字、核心底色框及方向通用虚线；数据中的用户观察与原连接仍保留，不把观察补成实际边。详情关闭时鼠标悬停预览节点前后连接，移出恢复概览；点击打开详情后锁定当前连接，再点击其他节点可切换，关闭详情后恢复悬停。编辑态禁用悬停，触屏维持点击查看。当前产物见exports/20261029-玩家招式图-10/及notes/handoffs/20261029-玩家招式图-10.md。\n';p.write_text(s,encoding='utf-8')
for name,prefix,suffix in [('研究进度与问题.md','玩家招式展示（',' 10版清除画布分类／公共方向装饰，详情关闭时悬停预览连接、打开时锁定；数据不变。'),('解包与解析进度.md','招式图08批',' 10展示批仅清理装饰与新增悬停预览，未改变配置或证据。')]:
 p=R/'Sifu/00索引'/name;lines=p.read_text(encoding='utf-8').splitlines();assert sum(x.startswith(prefix) for x in lines)==1;p.write_text('\n'.join(x+suffix if x.startswith(prefix) else x for x in lines)+'\n',encoding='utf-8')
