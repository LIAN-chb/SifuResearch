"""Cross-check existing view values against original parsed AttackDB/table fields."""
from pathlib import Path
import gzip,json,hashlib,collections,sys
R=Path(__file__).resolve().parents[2]; O=Path(__file__).resolve().parent
def read(p):
    f=R/p
    return json.load(gzip.open(f,'rt',encoding='utf8')) if f.suffix=='.gz' else json.loads(f.read_text(encoding='utf8'))
def value(ps,name):return next((p.get('value') for p in ps if p['name']==name),None)
def prop(ps,name):return next((p for p in ps if p['name']==name),{})
objects={o['asset']:o for o in read('inventory/tagged-objects.json.gz') if o['class'].endswith('.AttackDB')}
tables={t['asset']:t for t in read('inventory/data-tables.json.gz')}
view=read('exports/20261029-徒手补全与命名-13/board-data.json');rows=[]
for asset,a in view['attacks'].items():
    ps=value(objects[asset]['properties'],'m_Attack');handle=value(ps,'m_AnimationRow')
    ref=prop(handle,'DataTable')['reference'];table='Sifu/Content/'+ref[6:].split('.')[0]+'.uasset';name=value(handle,'RowName')
    tr=next(r for r in tables[table]['rows'] if r['row']==name)
    wanted=value(ps,'m_iWantedBuildupFrames');last=value(tr['properties'],'m_iLastBuildupFrame');hit=value(tr['properties'],'m_fHitFrame')
    assert wanted==a['buildup']
    hits=[]
    for i,w in enumerate(a['windows']):
        bounds=w['window']['m_FrameRange[0]']['m_Anim[0]'];hits.append({'segment':i+1,'bounds':bounds,'condition':w['window'].get('m_activationCondition[0]')})
    rows.append({'asset':asset,'animationTable':table,'animationRow':name,'wantedBuildupFrames':wanted,'lastBuildupFrame':last,'hitFrameReference':hit,'fps':value(ps,'m_fAnimFrameRate'),'frameDelta':value(ps,'m_fAnimFrameDeltaTime'),'hitBoxes':hits,
                 'sourceNodes':[int(k) for k,n in view['nodes'].items() if any(v['asset']==asset for v in n['variants'])]})
inputs=['inventory/tagged-objects.json.gz','inventory/data-tables.json.gz','exports/20261029-徒手补全与命名-13/board-data.json']
report={'status':'passed','rows':rows,'count':len(rows),'sources':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in inputs},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'python':sys.version,'limits':['Parsed original fields and references, not gameplay measurement','Activation conditions require code and runtime inputs; do not assume every HitBox activates']}
(O/'asset-snapshot.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'status':'passed','attacks':len(rows)}))
