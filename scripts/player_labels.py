"""Chinese field labels for stored player attack configuration; not runtime claims."""
import json,re
from pathlib import Path
LABELS=json.loads((Path(__file__).resolve().parent.parent/'exports/player-field-labels.json').read_text(encoding='utf-8'))
def field_label(path):
 def sub(m):
  k=m.group(0)
  return LABELS[k]['label'] if k in LABELS else '未核中文义（'+k+'）'
 return re.sub(r'[A-Za-z_][A-Za-z0-9_]*',sub,path).replace('.', ' → ')
def field_note(path):
 names=re.findall(r'[A-Za-z_][A-Za-z0-9_]*',path)
 return LABELS.get(names[-1],{}).get('note','该字段暂保留原名；中文语义待核。') if names else '索引或数据项。'
