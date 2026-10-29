from pathlib import Path
import ast
p=Path(r'E:\ProgrameFiles\SifuResearch\scripts\build_configuration_catalog.py')
s=p.read_text(encoding='utf-8')
s=s.replace('import argparse,collections,csv,datetime,gzip,hashlib,json,re','import argparse,collections,csv,datetime,gzip,hashlib,json,re,sys'+chr(10)+'sys.dont_write_bytecode=True'+chr(10)+'from player_labels import field_label,field_note')
old="def prop_table(data):return tab(['保存字段','保存值／引用'],[(k,compact(v)) for k,v in leaves(data)])"
new="def prop_table(data):return tab(['中文标识','原字段路径','保存值／引用','中文说明'],[(field_label(k),k,compact(v),field_note(k)) for k,v in leaves(data)])"
if old not in s:raise ValueError('Original property renderer changed')
s=s.replace(old,new)
s=s.replace("rows.append([k,compact(values[(k,sig)]),'本表全部行'","rows.append([field_label(k),k,compact(values[(k,sig)]),'本表全部行'")
s=s.replace("return tab(['保存字段','配置值','适用行 ID'],rows)","return tab(['中文标识','原字段路径','配置值','适用行 ID'],rows)")
s=s.replace("'inventory/stun-state-data.json']","'inventory/stun-state-data.json','exports/player-field-labels.json']")
s=s.replace('不重复制作用户已有的招式连接图。','玩家输入衔接图另见玩家攻击目录，保留配置连接与运行时边界的区别。')
s=s.replace('不制作招式连接图。','输入衔接图另见玩家攻击目录。')
ast.parse(s);p.write_text(s,encoding='utf-8',newline=chr(10))
