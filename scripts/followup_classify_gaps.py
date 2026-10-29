"""Classify historical parsing gaps and retry only current Grunt/player primary-source records."""
import sys,json,gzip,collections,hashlib,struct
from pathlib import Path
sys.dont_write_bytecode=True
R=Path(r'E:\ProgrameFiles\SifuResearch');sys.path.insert(0,str(R/'tools'));import local_bounded_packages as q
old=json.loads((R/'inventory/deep-parse-overview.json').read_text(encoding='utf-8'));coverage=json.loads((R/'inventory/configuration-catalog-coverage.json').read_text(encoding='utf-8'))
packages={p['path']:p for p in json.load(gzip.open(R/'inventory/package-metadata.json.gz','rt',encoding='utf-8'))}
records=[];parsed=[]
for f in old['failures']:
 asset=f['asset'];lower=asset.lower();historical=any(s in lower for s in ['/_old/','/oldattacks/','/test/','/tests/','/debug/'])
 related=('Grunt/' in asset or '/_MainChar/' in asset) and not historical
 rec={**f,'historical_path':historical,'priority':'直接关联' if related else '后续扩展','gap_kind':'旧读取器未支持的属性tag' if f['error'].startswith('Unsupported tag layout:') else '原生后缀未解码','retry_status':'未重试'}
 if related:
  try:
   p=packages[asset];e=next(e for e in p['exports'] if e['name']==f['export']);path=R/'extracted'/asset;body=path.with_suffix('.uexp').read_bytes();start=e['serialOffset']-path.stat().st_size;end=start+e['serialSize']
   if not 0<=start<=end<=len(body):raise ValueError('Export bounds')
   ps,n=q.tags(body[start:end],p['names']);complete=n==end-start or n+4==end-start and body[start+n:end]==bytes(4)
   rec.update({'tagged_bytes':n,'export_bytes':end-start,'uasset_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'uexp_sha256':hashlib.sha256(body).hexdigest(),'retry_status':'字段边界完整，内部opaque另列' if complete else '仅tagged前缀，原生后缀仍在'})
   parsed.append({'asset':asset,'export':e['name'],'class':f['class'],'complete_tagged_body':complete,'properties':ps,'opaque_values_are_not_semantically_decoded':True})
  except (ValueError,StopIteration,IndexError,KeyError,struct.error) as ex:rec['retry_status']='仍失败';rec['retry_error']=str(ex)
 if '/Barks/' in asset:rec['priority']='后续扩展：语音，不阻塞主线'
 records.append(rec)
unmatched=[]
for x in coverage['attack_hitbox_references']:
 if x['parsed_target']:continue
 historical=any(t in x['attack'].lower() for t in ['/_old/','/oldattacks/','/test/'])
 p=R/'extracted'/x['hitbox_asset']
 unmatched.append({**x,'historical_path':historical,'target_package_present':p.is_file(),'gap_kind':'空行名，不等于缺少资源' if x['row'] in ['None','',None] else '已提取表中的引用行未匹配，不能补造行','priority':'后续扩展：旧资源' if historical else '直接关联到该敌人时再查'})
report={'scope':'Historical825 records are parser/export records, not missing attacks. New targeted extractions have separate manifests.','historical_failure_records':len(records),'counts_by_original_reason':dict(collections.Counter(x['error'] for x in records)),'counts_by_priority':dict(collections.Counter(x['priority'] for x in records)),'retry_counts':dict(collections.Counter(x['retry_status'] for x in records)),'unmatched_hitbox_references':unmatched,'unmatched_counts':dict(collections.Counter(x['gap_kind'] for x in unmatched)),'records':records}
(R/'inventory/followup-gap-classification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
(R/'inventory/followup-gap-reparsed-objects.json').write_text(json.dumps(parsed,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in report.items() if k.endswith('counts') or k in ['historical_failure_records','counts_by_original_reason','counts_by_priority']},ensure_ascii=True))