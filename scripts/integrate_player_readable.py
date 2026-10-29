import datetime,json,shutil
from pathlib import Path
R=Path(r'E:\ProgrameFiles\SifuResearch');V=R/'Sifu'
changes={}
p=V/'00索引/首页.md';s=p.read_text(encoding='utf-8').replace('不重复制作已有招式连接图。','新增带输入、节点和命中段伤害关联的玩家招式衔接图。')
s+='\n## 玩家攻击优先阅读\n\n| 内容 | 入口 |\n|---|---|\n| 从输入到招式再到伤害 | [[03配置/玩家攻击/阅读入口]] |\n| 徒手轻重击与完整输入图 | [[03配置/玩家攻击/输入衔接图-徒手]] |\n| 每个玩家字段的中文名、原名和说明 | [[03配置/玩家攻击/字段中文说明]] |\n\nL/H 表示轻击／重击动作输入；条件、技能标签、默认回退与配置伤害分开标注。中文招式名目前是辅助直译，不冒充官方对应。\n'
changes[p]=s
p=V/'00索引/术语与证据说明.md';s=p.read_text(encoding='utf-8').replace('不重复制作招式连接图；玩家受击仅在共享逻辑直接相关时顺带研究','按输入维护玩家招式衔接图并关联伤害；玩家受击仅在共享逻辑直接相关时顺带研究')
s+='\n## 玩家攻击中文标识与输入图\n\n字段译名与原名同列，说明哪些是仅凭字段名称翻译、哪些有实际代码支持。入口：[[03配置/玩家攻击/字段中文说明]]、[[03配置/玩家攻击/输入与衔接图读法]]。图中的中文动作名为辅助直译；默认回退、条件分支和技能要求保留，不将配置边当成稳定命中保证。\n'
changes[p]=s
for folder in ['01机制','02实现']:
 p=V/folder/'攻击冲击力韧性与伤害.md';s=p.read_text(encoding='utf-8')
 s+='\n## 玩家输入与伤害查找\n\n可从 [[03配置/玩家攻击/阅读入口]] 按“输入 → 节点 → 动作资源 → 命中段”查看。[[03配置/玩家攻击/输入衔接图-徒手]] 给出轻重击阅读图与完整配置图；[[03配置/玩家攻击/字段中文说明]] 附全部当前玩家字段的中文标识与边界。其他武器图由阅读入口进入。图上的数值为命中段配置，不求和为整招伤害，也不保证敌人无法恢复或格挡。\n'
 changes[p]=s
backup=R/'notes/vault-backups'/('player-readable-nav-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S'));backup.mkdir(parents=True,exist_ok=False)
for p,s in changes.items():
 dst=backup/p.relative_to(V);dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst);p.write_text(s,encoding='utf-8',newline=chr(10))
p=R/'inventory/vault-layout.json';d=json.loads(p.read_text(encoding='utf-8'));d['documents']=sorted(x.relative_to(V).as_posix() for x in V.rglob('*.md') if '.obsidian' not in x.parts);d['player_reading_home']='03配置/玩家攻击/阅读入口.md';p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8',newline=chr(10))
print(json.dumps({'notes':len(d['documents']),'navigation_notes_changed':len(changes),'backup':str(backup)},ensure_ascii=True))
