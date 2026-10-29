from pathlib import Path
import gzip,json,hashlib,sys,struct,importlib.util
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'tools'))
import local_bounded_packages as q
def read(p):
 p=R/p
 return json.loads(gzip.decompress(p.read_bytes())) if p.suffix=='.gz' else json.loads(p.read_text(encoding='utf-8'))
objects=read('inventory/tagged-objects.json.gz');packages={p['path']:p for p in read('inventory/package-metadata.json.gz')};tables=read('inventory/data-tables.json.gz')
locen={(r['namespace'],r['key']):r for r in read('exports/20261029-玩家招式名称-12/en.json')};loczh={(r['namespace'],r['key']):r for r in read('exports/20261029-玩家招式名称-12/zh-Hans.json')}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def simple(ps):
 return {p['name']+'['+str(p.get('arrayIndex',0))+']':[simple(e) for e in p['arrayElements']] if 'arrayElements' in p else simple(p['value']) if isinstance(p.get('value'),list) else p.get('reference',p.get('tagNames',p.get('value'))) for p in ps}
def ref(p,i):
 if not i:return None
 x=p['imports'][-i-1] if i<0 else p['exports'][i-1];outer=ref(p,x['outer'] if i<0 else x['outerIndex'])
 return (outer+'.' if outer else '')+x['name']
def enrich(ps,p,raw=None):
 for x in ps:
  chunk=raw[x['valueOffset']:x['valueOffset']+x['size']] if raw is not None else None
  if isinstance(x.get('value'),list):enrich(x['value'],p,chunk)
  elif x['type']=='ObjectProperty':x['reference']=ref(p,x['value'])
  elif x.get('struct')=='GameplayTagContainer' and chunk is not None:
   rr=q.Reader(chunk,p['names']);count=rr.number('i');assert 0<=count<1000 and len(chunk)==4+count*8
   x['tagNames']=[rr.name() for _ in range(count)]
  elif x['type']=='ArrayProperty' and x.get('inner')=='StructProperty' and chunk is not None:
   try:
    rr=q.Reader(chunk,p['names']);count=rr.number('i');assert 0<=count<1000
    an,at=rr.name(),rr.name();size,idx=rr.number('i'),rr.number('i');st=rr.name();rr.take(16);guid=rr.number('B')
    if guid==1:rr.take(16)
    assert an==x['name'] and at=='StructProperty' and idx==0 and size==len(chunk)-rr.position
    elements=[]
    for _ in range(count):
     sub=chunk[rr.position:];props,n=q.tags(sub,p['names']);enrich(props,p,sub);rr.position+=n;elements.append(props)
    assert rr.position==len(chunk)
    x['arrayElements']=elements;x['arrayStruct']=st
   except (AssertionError,ValueError,struct.error):pass
def payload(obj):
 p=packages[obj['asset']];f=R/'extracted'/obj['asset'];data=f.with_suffix('.uexp').read_bytes();e=p['exports'][obj['export_index']-1];start=e['serialOffset']-f.stat().st_size
 assert sha(f)==p['uassetSha256']==obj['sha256'];assert 0<=start and start+e['serialSize']<=len(data)
 return p,data[start:start+e['serialSize']],start
focus=[]
for obj in objects:
 if not(obj['asset'].startswith('Sifu/Content/DB/AI/_Shared/Focus/') and obj['class']=='/Script/Sifu.VitalPointData' and '/Weapon/' not in obj['asset'] and not obj['asset'].endswith('VitalPointDataBase.uasset')):continue
 props=simple(obj['properties']);p,raw,start=payload(obj);np=next(x for x in obj['properties'] if x['name']=='m_Name');chunk=raw[np['valueOffset']:np['valueOffset']+np['size']]
 assert hashlib.sha256(chunk).hexdigest()==np['value']['sha256'];rr=q.Reader(chunk,p['names']);flags=rr.number('I');history=rr.number('b');assert history==11
 table=rr.name();key=rr.string();assert rr.position==len(chunk)
 matches=[r for (ns,k),r in locen.items() if k==key];assert len(matches)==1,(table,key)
 en=matches[0];zh=loczh[(en['namespace'],key)];assert en['source_hash']==zh['source_hash']
 hit=props['m_FocusAttackEffect[0]']['m_HitBox[0]'];handle=hit['m_HitRow[0]'];rel='Sifu/Content/'+handle['DataTable[0]'][6:].split('.')[0]+'.uasset'
 tr=next(t for t in tables if t['asset']==rel);row=next(r for r in tr['rows'] if r['row']==handle['RowName[0]'])
 f=R/'extracted'/obj['asset']
 focus.append({'asset':obj['asset'],'object':obj['export'],'source_sha256':sha(f),'uexp_sha256':sha(f.with_suffix('.uexp')),'name':zh['text'],'en':en['text'],'nameText':{'table':table,'namespace':en['namespace'],'key':key,'source_hash':en['source_hash'],'uexp_offset':start+np['valueOffset']},'cost':props['m_iFocusPointsCost[0]'],'slot':props['m_Slot[0]']['m_Value[0]'],'animation':props['m_SyncAnimToPlay[0]']['m_InstigatorAnim[0]']['m_animation[0]'],'victimAnimation':props['m_SyncAnimToPlay[0]']['m_VictimAnim[0]']['m_animation[0]'],'checkCondition':props['m_CheckConditionBlueprint[0]'],'hitTable':rel,'hitRow':row['row'],'hitProperties':simple(row['properties']),'window':hit,'raw':props,'attackAssets':[],'entry':'进入专注模式→选择目标弱点→执行专注攻击','entryEvidence':'VitalPointData m_Name/m_SyncAnimToPlay/m_FocusAttackEffect; no ComboTree source edge asserted','followups':[],'followupStatus':'not-in-the-saved-ComboTree; post-focus action/availability links not restored','limits':['共享弱点配置，敌人变体可覆写；不是所有敌人都可执行','专注消耗为保存配置，不推技能/难度/运行时倍率','不是AttackDB基础连段；同步动作和OverridingHitBox保持独立']})
(O/'focus-data.json').write_text(json.dumps({'nodes':focus,'edges':[],'source':'shared VitalPointData and exact m_Name FText references','limits':['no invented ComboTree edges','shared config, not enemy-specific final values','not runtime tested']},ensure_ascii=False,indent=2),encoding='utf-8')
cdos=[]
for suffix in ['BP_PushAbility.uasset','BP_KnockdownAttackAbility.uasset','BP_ParryFromDownAbility.uasset','BP_FocusAbility.uasset','BP_AttackAbility.uasset']:
 p=next(p for p in packages.values() if p['path'].endswith('/'+suffix));asset=R/'extracted'/p['path'];data=asset.with_suffix('.uexp').read_bytes();assert sha(asset)==p['uassetSha256']
 for i,e in enumerate(p['exports']):
  if not e['name'].startswith('Default__'):continue
  start=e['serialOffset']-asset.stat().st_size;raw=data[start:start+e['serialSize']];ps,n=q.tags(raw,p['names']);enrich(ps,p,raw)
  cdos.append({'asset':p['path'],'object':e['name'],'source_sha256':sha(asset),'uexp_sha256':sha(asset.with_suffix('.uexp')),'consumed':n,'bytes':len(raw),'trailing_hex':raw[n:].hex(),'properties':simple(ps),'raw_properties':ps})
(O/'actions-ability-cdos.json').write_text(json.dumps(cdos,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'focuses':[(n['en'],n['cost'],n['hitRow']) for n in focus],'ability_cdos':len(cdos)},ensure_ascii=True))
for c in cdos:print(c['asset'],json.dumps(c['properties'],ensure_ascii=True)[:8000])
