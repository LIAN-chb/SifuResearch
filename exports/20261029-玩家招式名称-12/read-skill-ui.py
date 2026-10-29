from pathlib import Path
import gzip,json,struct,hashlib,sys
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'tools'))
from local_bounded_packages import Reader
objects=json.loads(gzip.decompress((R/'inventory/tagged-objects.json.gz').read_bytes()))
packages={p['path']:p for p in json.loads(gzip.decompress((R/'inventory/package-metadata.json.gz').read_bytes()))}
en={(r['namespace'],r['key']):r for r in json.loads((O/'en.json').read_text(encoding='utf-8'))}
zh={(r['namespace'],r['key']):r for r in json.loads((O/'zh-Hans.json').read_text(encoding='utf-8'))}
rows=[];unsupported=[];inline=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for obj in objects:
 if not obj['class'].endswith('SkillUIData.SkillUIData_C'):continue
 p=packages[obj['asset']];asset=R/'extracted'/obj['asset'];uexp=asset.with_suffix('.uexp')
 assert sha(asset)==p['uassetSha256']==obj['sha256']
 e=p['exports'][obj['export_index']-1];start=e['serialOffset']-asset.stat().st_size
 data=uexp.read_bytes();raw=data[start:start+e['serialSize']];assert len(raw)==e['serialSize']
 row={'asset':obj['asset'],'export':obj['export'],'uasset_sha256':sha(asset),'uexp_sha256':sha(uexp),'fields':{}}
 for prop in obj['properties']:
  if prop['type']!='TextProperty' or prop['name'] not in ['Name','Description','Inputs']:continue
  a=prop['valueOffset'];b=a+prop['size'];chunk=raw[a:b];assert len(chunk)==prop['size']
  assert hashlib.sha256(chunk).hexdigest()==prop['value']['sha256']
  rr=Reader(chunk,p['names']);flags=rr.number('I');history=rr.number('b')
  if history==0:
   def text():
    if struct.unpack_from('<i',rr.data,rr.position)[0]==0:rr.position+=4;return ''
    return rr.string()
   ns=text();key=text();source=text();assert rr.position==len(chunk)
   entry=en.get((ns,key));pair=zh.get((ns,key))
   inline.append({'asset':obj['asset'],'field':prop['name'],'namespace':ns,'key':key,'source':source,'en':entry['text'] if entry else None,'zh-Hans':pair['text'] if pair else None,'uexp_value_offset':start+a})
   continue
  if history!=11:
   unsupported.append({'asset':obj['asset'],'field':prop['name'],'history':history});continue
  table=rr.name();key=rr.string();assert rr.position==len(chunk)
  # Namespace is verified by an exact, unique key lookup, not guessed from table filename.
  candidates=[x for (ns,k),x in en.items() if k==key];assert len(candidates)==1,(table,key,len(candidates))
  entry=candidates[0];pair=zh.get((entry['namespace'],key))
  if pair:assert pair['source_hash']==entry['source_hash']
  row['fields'][prop['name']]={'table':table,'namespace':entry['namespace'],'key':key,'en':entry['text'],'zh-Hans':pair['text'] if pair else None,'zh_status':'localized' if pair else 'absent; native text retained separately','uexp_value_offset':start+a,'value_bytes':len(chunk),'en_entry_offset':entry['entry_offset'],'zh_entry_offset':pair['entry_offset'] if pair else None}
 if row['fields']:rows.append(row)
out={'skills':rows,'unsupported':unsupported,'sources':['inventory/tagged-objects.json.gz','inventory/package-metadata.json.gz','https://raw.githubusercontent.com/FabianFG/CUE4Parse/master/CUE4Parse/UE4/Objects/Core/i18N/FText.cs'],'python':sys.version,'script_sha256':sha(Path(__file__)),'scope':'existing 46 SkillUIData exports only; fields reference string tables; not proof all are reachable gameplay skills'}
out['inline_text_fields']=inline
(O/'skill-ui-links.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'skill_exports':len(rows),'fields':sum(len(r['fields']) for r in rows),'unsupported':len(unsupported)}))
for r in rows:
 if r['asset'].endswith('SkillGameplay_Technique_PostPushbackKnockdown.uasset'):print(json.dumps(r,ensure_ascii=True))
