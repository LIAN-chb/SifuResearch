import ast,json
from pathlib import Path
r=Path(r'E:\ProgrameFiles\SifuResearch');p=r/'scripts/build_configuration_catalog.py';s=p.read_text(encoding='utf-8')
old="text='# '+category+'配置索引\\n\\n'+nav()"
new=old+"\n if category=='玩家攻击':text+='优先阅读：'+wl(OUT+'/玩家攻击/阅读入口','输入衔接图、中文字段与招式伤害对照')+'。\\n\\n'"
if old not in s:raise ValueError('Category index block changed')
s=s.replace(old,new)
ast.parse(s);p.write_text(s,encoding='utf-8',newline=chr(10))
