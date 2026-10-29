"""Export raw state-reaction settings, state matrices and verified recovery masks."""
import csv,gzip,json,sys
from pathlib import Path
R=Path(r'E:\ProgrameFiles\SifuResearch');B=R/'extracted';sys.path.insert(0,str(R/'tools'));import external_read_packages as q
objs=json.load(gzip.open(R/'inventory/tagged-objects.json.gz','rt',encoding='utf-8'));cdo=json.load(gzip.open(R/'inventory/stun-ai-default-objects.json.gz','rt',encoding='utf-8'));pkgs=json.load(gzip.open(R/'inventory/package-metadata.json.gz','rt',encoding='utf-8'))
def get(ps,n,idx=0):return next((x for x in ps if x['name']==n and x['arrayIndex']==idx),None)
def scalar(ps,n):
 p=get(ps,n);return p['value'] if p and not isinstance(p['value'],(dict,list)) else None
def nested(ps,n):
 p=get(ps,n);return p['value'] if p and isinstance(p['value'],list) else []
def flat(ps,prefix=''):
 out={}
 for p in ps:
  key=prefix+p['name']+'['+str(p['arrayIndex'])+']';v=p['value']
  if isinstance(v,list):out.update(flat(v,key+'.'))
  elif 'reference' in p:out[key]=p['reference']
  elif not isinstance(v,dict):out[key]=v
 return out
reactions=[];matrices=[];hitted=[]
states=['OutOfFight','InFight','Counter_Hit','KnockedDown','Dizzy','Pushed','Avoided','StructureBroken','Parried']
for o in objs:
 if o['class'].endswith('.AttackPropertiesResistanceDB'):
  for group in ('m_DownReaction','m_DizzyReaction','m_PushedReaction','m_SuperDizzyReaction','m_StructureBrokenReaction'):
   ps=nested(o['properties'],group)
   if group=='m_PushedReaction':ps=nested(ps,'m_BasePushReaction')
   if ps:
    selected={p['name']:p['value'] for p in ps if not isinstance(p['value'],(dict,list))}
    reactions.append({'asset':o['asset'],'reaction':group,**selected})
  m=nested(o['properties'],'m_ResistanceMatrix')
  for row in m:
   if row['name']!='m_Matrix' or not isinstance(row['value'],list):continue
   p=row['value'];i=row['arrayIndex'];levels={x['arrayIndex']:x['value'] for x in p if x['name']=='m_Level'}
   matrices.append({'asset':o['asset'],'state_index':i,'state':states[i] if i<len(states) else 'unknown','knockdown_resistance_col0':levels.get(0),'push_resistance_col1':levels.get(1),'dizzy_resistance_col2':levels.get(2),**{x['name']:x['value'] for x in p if x['name']!='m_Level' and not isinstance(x['value'],(dict,list))}})
 if o['class'].endswith('.HittedDB'):
  hitted.append({'asset':o['asset'],**flat(o['properties'])})
for name,rows in [('state-reaction-settings.csv',reactions),('state-resistance-matrices.csv',matrices)]:
 keys=list(dict.fromkeys(k for x in rows for k in x))
 with (R/'exports'/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)
layers=[]
for p in pkgs:
 if not p['path'].endswith(('AIHittedRecovery.uasset','HittedRecovery.uasset')):continue
 f=B/p['path'];e=p['exports'][0];st=e['serialOffset']-f.stat().st_size;raw=f.with_suffix('.uexp').read_bytes()[st:st+e['serialSize']];props,n=q.tags(raw,p['names']);x=get(props,'m_inputActionArray')
 if n+4!=len(raw) or raw[n:]!=b'\0'*4 or x is None or x.get('inner')!='EnumProperty':raise ValueError('Unexpected recovery layer layout')
 data=raw[x['valueOffset']:x['valueOffset']+x['size']];rr=q.Reader(data,p['names']);count=rr.number('i')
 if count<0 or len(data)!=4+count*8:raise ValueError('Enum array byte count mismatch')
 layers.append({'asset':p['path'],'uasset_sha256':p['uassetSha256'],'actions':[rr.name() for _ in range(count)],'native_inverse_default':False,'native_inverse_evidence':'logs/stun-ai-layer-semantics/InternalConstructor_UAvailabilityLayerData_-0x1c1fd20.asm.txt','mask_generation':'all false then listed actions true; current-context op0 is replacement, not an unconditional bypass of other contexts'})
refs=[]
for o in cdo:
 hits=[x for x in o['object_references'] if x.get('ref') and ('Grunt_Base_ResistanceDB' in x['ref'] or 'Grunt_Adv_ResistanceDB' in x['ref'])]
 if hits:refs.append({'asset':o['asset'],'export':o['export'],'references':hits})
report={'reaction_rows':len(reactions),'matrix_rows':len(matrices),'hitted_assets':hitted,'recovery_layers':layers,'grunt_archetype_resistance_refs':refs,'scope':'Serialized fields and local code mappings. No live object/default-parent merge or runtime effective-value claim.','counter_warning':'These are state counters, not guaranteed punch counts; event routing, grouping and refresh rules matter.'}
(R/'inventory/stun-state-data.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'reaction_rows':len(reactions),'matrix_rows':len(matrices),'hitted_db_count':len(hitted),'layers':len(layers),'archetype_refs':len(refs)},ensure_ascii=False))
