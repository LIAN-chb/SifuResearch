import ast,datetime,difflib,hashlib,json,re,shutil,sys
from pathlib import Path
sys.dont_write_bytecode=True
r=Path(r'E:\ProgrameFiles\SifuResearch');sys.path.insert(0,str(r/'scripts'))
s=(r/'scripts/build_configuration_catalog.py').read_text(encoding='utf-8')
s=s.replace("tab(['中文标识','原字段路径','保存值／引用','中文说明'],[(field_label(k),k,compact(v),field_note(k)) for k,v in leaves(data)])","tab(['保存字段','保存值／引用'],[(k,compact(v)) for k,v in leaves(data)])")
s=s.replace("rows.append([field_label(k),k,compact(values[(k,sig)])","rows.append([k,compact(values[(k,sig)])")
s=s.replace("return tab(['中文标识','原字段路径','配置值','适用行 ID'],rows)","return tab(['保存字段','配置值','适用行 ID'],rows)")
s=s.split('if args.check:',1)[0];g={};exec(compile(s,'prior_renderer_review','exec'),g)
manifest=r/'inventory/configuration-catalog-coverage.json';report=json.loads(manifest.read_text(encoding='utf-8'))
def canonical(text):
 out=[]
 for line in text.splitlines():
  if line.startswith('|'):
   cells=[x.strip() for x in re.split(r'(?<!\\)\|',line)[1:-1]]
   if cells and all(re.fullmatch(':?-+:?',x) for x in cells):cells=['---']*len(cells)
   out.append('|'.join(cells))
  else:out.append(line)
 return '\n'.join(out)
changed=[]
for rel,meta in report['documents'].items():
 p=r/'Sifu'/rel;current=p.read_text(encoding='utf-8');h=hashlib.sha256(current.encode()).hexdigest()
 if h!=meta['sha256']:
  prior=g['docs'][rel]
  assert hashlib.sha256(prior.encode()).hexdigest()==meta['sha256'],'Prior reconstruction differs'
  assert canonical(current)==canonical(prior),'Substantive edit must be preserved: '+rel
  changed.append((rel,p,current,h))
backup=r/'notes/vault-backups'/('table-format-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S'));backup.mkdir(parents=True,exist_ok=False)
for rel,p,current,h in changed:
 dest=backup/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
 report['documents'][rel]['sha256']=h;report['documents'][rel]['bytes']=len(current.encode())
manifest.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8',newline=chr(10))
print(json.dumps({'format_only_files_verified':len(changed),'backup':str(backup)},ensure_ascii=True))
