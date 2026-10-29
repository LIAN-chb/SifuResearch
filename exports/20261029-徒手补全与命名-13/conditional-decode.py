"""Read only the MainChar conditional attack map; preserve every tagged boundary."""
from pathlib import Path
import gzip,json,hashlib,importlib.util,struct,sys,collections
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('bounded13',R/'tools/local_bounded_packages.py');q=importlib.util.module_from_spec(spec);spec.loader.exec_module(q)
sha=lambda b:hashlib.sha256(b).hexdigest()
pkgs=json.loads(gzip.decompress((R/'inventory/package-metadata.json.gz').read_bytes()))
pkg=next(p for p in pkgs if p['path'].endswith('/MainChar_ComboTree.uasset'))
old=next(t for t in json.loads((R/'inventory/player-combo-graphs.json').read_text(encoding='utf-8'))['trees'] if t['asset']==pkg['path'])
asset=R/'extracted'/pkg['path'];b=asset.with_suffix('.uexp').read_bytes()
assert sha(asset.read_bytes())==pkg['uassetSha256']==old['uasset_sha256']
assert sha(b)==old['uexp_sha256']
e=next(e for e in pkg['exports'] if e['name']=='MainChar_ComboTree');export_start=e['serialOffset']-asset.stat().st_size
raw=b[export_start:export_start+e['serialSize']];assert len(raw)==e['serialSize']
ps,n=q.tags(raw,pkg['names']);assert raw[n:]==b'\0'*4
arr=next(p for p in ps if p['name']=='m_Nodes');chunk=raw[arr['valueOffset']:arr['valueOffset']+arr['size']]
def array(data,prop):
 rr=q.Reader(data,pkg['names']);count=rr.number('i');assert 0<=count<10000
 assert rr.name()==prop['name'];assert rr.name()=='StructProperty'
 size=rr.number('i');assert rr.number('i')==0
 struct_name=rr.name();rr.take(16);has=rr.number('B');assert has in [0,1]
 if has:rr.take(16)
 assert size==len(data)-rr.position,(prop['name'],size,len(data)-rr.position)
 result=[]
 for _ in range(count):
  at=rr.position;fields,used=q.tags(data[at:],pkg['names']);rr.position+=used
  result.append(norm(fields,data[at:at+used]))
 assert rr.position==len(data)
 return {'struct':struct_name,'count':count,'elements':result,'consumed':rr.position}
def norm(fields,data):
 out={}
 for p in fields:
  k=p['name']+'['+str(p.get('arrayIndex',0))+']';v=p['value'];part=data[p['valueOffset']:p['valueOffset']+p['size']]
  if isinstance(v,list):v=norm(v,part)
  elif p['type']=='ArrayProperty' and p.get('inner')=='StructProperty':v=array(part,p)
  out[k]=v
 return out
rr=q.Reader(chunk,pkg['names']);count=rr.number('i');assert count==57
assert rr.name()=='m_Nodes' and rr.name()=='StructProperty';size=rr.number('i');assert rr.number('i')==0;assert rr.name()=='ComboNode';rr.take(16);assert rr.number('B')==0;assert size==len(chunk)-rr.position
node_proofs=[];all_refs=set();entries=[]
for i in range(count):
 start=rr.position;node,used=q.tags(chunk[start:],pkg['names']);rr.position+=used
 p=next(p for p in node if p['name']=='m_ConditionalAttacks');rel=start+p['valueOffset'];data=chunk[rel:rel+p['size']]
 assert sha(data)==old['nodes'][i]['m_ConditionalAttacks[0]']['sha256']
 header=q.Reader(chunk[start:],pkg['names'],p['offset']);assert header.name()=='m_ConditionalAttacks' and header.name()=='MapProperty';header.take(8);key_type=header.name();value_type=header.name();assert (key_type,value_type)==('StructProperty','StructProperty')
 r=q.Reader(data,pkg['names']);removed=r.number('i');assert 0<=removed<10000;removed_keys=[]
 for _ in range(removed):
  fields,kused=q.tags(data[r.position:],pkg['names']);removed_keys.append(norm(fields,data[r.position:r.position+kused]));r.position+=kused
 n=r.number('i');assert 0<=n<10000;parsed=[]
 for j in range(n):
  begin=r.position;key,kused=q.tags(data[begin:],pkg['names']);r.position+=kused
  assert len(key)==1 and key[0]['name']=='TagName' and key[0]['type']=='NameProperty'
  tag=key[0]['value'];vbegin=r.position;fields,vused=q.tags(data[vbegin:],pkg['names']);r.position+=vused;value=norm(fields,data[vbegin:r.position])
  base={int(p['arrayIndex']):p['value'] for p in fields if p['name']=='m_Attacks'}
  assert set(base)=={0,1,2,3},(i,tag,base)
  def asset_path(x):return 'Sifu/Content/'+x[6:].split('.')[0]+'.uasset' if isinstance(x,str) and x.startswith('/Game/') else None
  variants=[]
  for path in sorted(set(base.values())):
   ap=asset_path(path)
   if ap:variants.append({'slots':[slot for slot,x in base.items() if x==path],'asset':ap,'reference':path,'tier':'基础'});all_refs.add(ap)
  charged=value.get('m_ChargedAttacks[0]',{})
  for cidx,c in enumerate(charged.get('elements',[])):
   for slot in range(4):
    path=c.get('m_Attacks['+str(slot)+']');ap=asset_path(path)
    if ap:variants.append({'slots':[slot],'asset':ap,'reference':path,'tier':'蓄力档位'+str(cidx)});all_refs.add(ap)
  entry={'node':i,'index':j,'tag':tag,'byte_offset_in_map':begin,'uexp_offset':export_start+arr['valueOffset']+rel+begin,'key_bytes':kused,'value_bytes':vused,'entry_sha256':sha(data[begin:r.position]),'infos':value,'variants':variants}
  parsed.append(entry);entries.append(entry)
 assert r.position==len(data),(i,r.position,len(data))
 node_proofs.append({'node':i,'map_uexp_offset':export_start+arr['valueOffset']+rel,'bytes':len(data),'sha256':sha(data),'removed_keys':removed_keys,'entries':parsed,'consumed':r.position})
assert rr.position==len(chunk)
board=json.loads((R/'exports/20261029-玩家招式图-10/board-data.json').read_text(encoding='utf-8'))
outside={r['asset'] for r in board['coverage']['outsideTree']};inside=set(board['attacks'])
summary={'nodes':len(node_proofs),'nonempty_maps':sum(bool(n['entries']) for n in node_proofs),'entries':len(entries),'tags':dict(collections.Counter(e['tag'] for e in entries)),'unique_referenced_assets':len(all_refs),'previous_tree_assets_referenced':len(all_refs&inside),'previous_outside_candidates_referenced':len(all_refs&outside),'new_assets_not_in_either':sorted(all_refs-inside-outside),'charged_tiers':sum(e['infos'].get('m_ChargedAttacks[0]',{}).get('count',0) for e in entries)}
report={'status':'passed','source':{'asset':pkg['path'],'uasset_sha256':sha(asset.read_bytes()),'uexp_sha256':sha(b),'node_array_bytes':len(chunk),'node_array_consumed':rr.position},'summary':summary,'nodes':node_proofs,'all_referenced_assets':sorted(all_refs),'referenced_previous_outside_candidates':sorted(all_refs&outside),'unreferenced_previous_outside_candidates':sorted(outside-all_refs),'limits':['saved conditional replacement configs, not a runtime trace','GetAttackInfos tag-selection semantics previously evidenced in player-unknown-08-quadrant; this batch adds exact map entries','all observed conditional keys are Attack.Modifiers.*, not new default-tree transitions','same original node adjacency must be preserved; conditions are original-node variants, not standalone transition edges'],'python':sys.version,'script_sha256':sha(Path(__file__).read_bytes()),'parser_sha256':sha((R/'tools/local_bounded_packages.py').read_bytes())}
(O/'conditional-attacks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=True))
