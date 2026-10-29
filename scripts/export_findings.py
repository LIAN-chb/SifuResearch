"""Create focused, source-addressable research exports; no effective-value claims."""
import collections,csv,gzip,json,re
from pathlib import Path
R=Path(r'E:\ProgrameFiles\SifuResearch');objs=json.load(gzip.open(R/'inventory/tagged-objects.json.gz','rt',encoding='utf-8'));tables=json.load(gzip.open(R/'inventory/data-tables.json.gz','rt',encoding='utf-8'))
def get(ps,n,idx=0):return next((p for p in ps if p['name']==n and p.get('arrayIndex',0)==idx),None)
def val(ps,n):
 p=get(ps,n);return p.get('value') if p else None
def nested(ps,n):
 p=get(ps,n);return p['value'] if p and isinstance(p['value'],list) else []
def simple(ps):
 out={}
 for p in ps:
  name=p['name']+'['+str(p.get('arrayIndex',0))+']';v=p['value']
  if isinstance(v,list):out[name]=simple(v)
  elif 'arrayElements' in p:out[name]=[simple(e) for e in p['arrayElements']]
  elif 'tagNames' in p:out[name]=p['tagNames']
  elif 'reference' in p:out[name]={'index':v,'reference':p['reference']}
  elif 'arrayReferences' in p:out[name]=p['arrayReferences']
  elif 'arrayValues' in p:out[name]=p['arrayValues']
  else:out[name]=v
 return out
def writecsv(name,rows):
 if not rows:return
 fields=list(dict.fromkeys(k for r in rows for k in r))
 with (R/'exports'/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
impact=[]
for t in tables:
 for row in t['rows']:
  for kind in ('m_OnHitImpact','m_OnGuardImpact','m_OnDeflectImpact'):
   ps=nested(row['properties'],kind)
   if ps:impact.append({'asset':t['asset'],'row':row['row'],'outcome':kind,**{p['name']:p['value'] for p in ps if not isinstance(p['value'],(list,dict))}})
writecsv('hit-impact-values.csv',impact)
timing=[];timinglookup={}
for t in tables:
 for row in t['rows']:
  ps=row['properties']
  if get(ps,'m_fHitFrame'):
   d={'table':t['asset'],'row':row['row'],'last_buildup_frame_authored':val(ps,'m_iLastBuildupFrame'),'hit_frame_authored':val(ps,'m_fHitFrame')}
   timinglookup[(t['asset'],row['row'])]=d
   if '/_MainChar/' in t['asset']:timing.append(d)
writecsv('mainchar-authored-timing.csv',timing)
attacks=[];windows=[];boxes=[]
for o in objs:
 if '/_MainChar/' not in o['asset'] or not o['class'].endswith('.AttackDB'):continue
 a=nested(o['properties'],'m_Attack');h=nested(a,'m_AnimationRow');tp=get(h,'DataTable');rp=val(h,'RowName');ref=tp.get('reference') if tp else None
 local='Sifu/Content/'+ref[len('/Game/'):].split('.')[0]+'.uasset' if ref and ref.startswith('/Game/') else ''
 d={'attack_db':o['asset'],'contains_old_path':'/_old/' in o['asset'],'animation_row_table':local,'animation_row':rp,'anim_frame_rate_stored':val(a,'m_fAnimFrameRate'),'wanted_buildup_frames_stored':val(a,'m_iWantedBuildupFrames'),**{k:v for k,v in timinglookup.get((local,rp),{}).items() if k not in ('table','row')}}
 attacks.append(d)
 for key,out in [('m_AvailabilityLayerWindows',windows),('m_HitBoxes',boxes)]:
  p=get(a,key)
  if p and 'arrayElements' in p:
   for i,ep in enumerate(p['arrayElements']):out.append({'attack_db':o['asset'],'contains_old_path':'/_old/' in o['asset'],'index':i,'properties':simple(ep)})
writecsv('mainchar-attackdb-timing.csv',attacks)
for name,data in [('mainchar-availability-windows.json',windows),('mainchar-hitbox-windows.json',boxes)]:
 (R/'exports'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
tickets=[{'asset':o['asset'],'export':o['export'],'config':simple(nested(o['properties'],'m_Config'))} for o in objs if '/DB/AI/Tickets/' in o['asset'] and o['class'].endswith('AIAttackTicketData')]
(R/'exports/ai-attack-tickets.json').write_text(json.dumps(tickets,ensure_ascii=False,indent=2),encoding='utf-8')
defense=[{'asset':o['asset'],'export':o['export'],'class':o['class'],'properties':simple(o['properties'])} for o in objs if o['asset'].endswith(('Grunt_Base_ContextualDefense.uasset','Grunt_Adv_ContextualDefense.uasset'))]
(R/'exports/grunt-contextual-defense.json').write_text(json.dumps(defense,ensure_ascii=False,indent=2),encoding='utf-8')
summary={'hit_impact_rows_by_outcome':len(impact),'distinct_hitbox_rows':len({(x['asset'],x['row']) for x in impact}),'mainchar_authored_timing_rows':len(timing),'mainchar_attack_db_objects':len(attacks),'mainchar_availability_window_records':len(windows),'mainchar_hitbox_window_records':len(boxes),'ai_attack_ticket_assets':len(tickets),'grunt_contextual_defense_objects':len(defense),'warnings':['Stored values only; defaults, curve scaling, active difficulty and runtime application must be linked before declaring effective values.','_old paths are retained and explicitly marked; no claim that an asset is used in gameplay.','Open range bounds retain their Type field; their stored numeric Value is not an effective endpoint.','Availability layers are not universally equivalent to cancel windows.']}

# Keep resilience override / resistance matrices separate from Structure damage.
with (R/'inventory/object-and-table-properties.csv').open(encoding='utf-8-sig') as f:
 resistance=[x for x in csv.DictReader(f) if re.search(r'resilien|resistan',x['property'],re.I)]
writecsv('resilience-and-resistance-values.csv',resistance)
summary['resilience_resistance_property_rows']=len(resistance)

(R/'exports/export-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(summary,ensure_ascii=False,indent=2))
