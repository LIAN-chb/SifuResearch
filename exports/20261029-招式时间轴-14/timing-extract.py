"""Project-local animation markers and special hit-action audit; no inferred duration."""
from pathlib import Path
import json,gzip,hashlib,sys
R=Path(__file__).resolve().parents[2]; O=Path(__file__).resolve().parent
def load(p):
    p=R/p
    return json.load(gzip.open(p,'rt',encoding='utf8')) if p.suffix=='.gz' else json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
tables={t['asset']:t for t in load('inventory/data-tables.json.gz')}
d=load('exports/20261029-徒手补全与命名-13/board-data.json')
out={};special=[];checks=[]
for asset,a in {**d['attacks'],**d['outsideAttacks']}.items():
    raw=a.get('raw',{}); ref=raw.get('m_AnimationRow[0]',{}); table=ref.get('DataTable[0]'); row=ref.get('RowName[0]')
    table='Sifu/Content/'+table[6:].split('.')[0]+'.uasset' if table and table.startswith('/Game/') else None
    rows=tables.get(table,{}).get('rows',[]); rr=next((r for r in rows if r['row']==row),None)
    props={p['name']:p.get('value') for p in rr['properties']} if rr else {}
    bounds=[w.get('window',{}).get('m_FrameRange[0]',{}).get('m_Anim[0]',{}) for w in a.get('windows',[])]
    out[asset]={'fps':raw.get('m_fAnimFrameRate[0]'),'wantedBuildupFrames':a.get('buildup'),'animation':raw.get('m_Animation[0]'),'animationTable':table,'animationRow':row,'lastBuildupFrame':props.get('m_iLastBuildupFrame'),'hitMarkerFrame':props.get('m_fHitFrame'),'animationEndFrame':None,'elapsedSeconds':None,'rangeSource':'Animation sequence native frame count and playback range not decoded; do not infer from last window.','hitBounds':bounds,'status':'configuration-markers-only'}
    for j,w in enumerate(a.get('windows',[])):
        action=w.get('action') or w.get('raw',{}).get('m_hitAction[0]')
        if action:
            nodes=[{'id':n['id'],'name':n['name'],'tiers':[v['tier'] for v in n['variants'] if v['asset']==asset]} for n in d['nodes'].values() if any(v['asset']==asset for v in n['variants'])]
            special.append({'asset':asset,'segment':j+1,'action':action,'nodes':nodes,'scope':'saved hit-row launcher reference; runtime execution not confirmed'})
    checks.append({'asset':asset,'animationRowResolved':rr is not None,'boundsPreserved':len(bounds)==len(a.get('windows',[]))})
sources=['inventory/data-tables.json.gz','exports/20261029-徒手补全与命名-13/board-data.json','inventory/pdb_overview.json']
report={'attacks':out,'specialHitActions':special,'candidates':[{'field':f,'purpose':p} for f,p in [('m_fGameplayRange','游戏距离参数，非必然命中距离'),('m_fMaxTrackingAngle','追踪角度覆盖'),('m_bWantSnap / m_fCustomMaxDisSnap','贴近位移及距离覆盖'),('m_bWantSnapDuringStrike / m_bWantSnapBack','出手阶段位移和回位'),('m_AttackProperties','动作标签及条件替换关联'),('m_activationCondition / m_uiHitConditions','判定段／许可窗口条件')]],'sources':{p:sha(p) for p in sources},'checks':checks,'limits':['No elapsed-time conversion: initial play-rate consumer chain remains incomplete.','No native AnimSequence frame-count decoder exists in current tagged objects.']}
probe=O/'timing-animation-probe.json'
if probe.exists():
    sample=json.loads(probe.read_text(encoding='utf8'))
    for a in out.values():
        anim=a.get('animation')
        path='Sifu/Content/'+anim[6:].split('.')[0]+'.uasset' if anim and anim.startswith('/Game/') else None
        if path==sample['asset']:
            a['sourceAnimation']={'numFrames':sample['scalars']['NumFrames'],'sequenceLengthSeconds':sample['scalars']['SequenceLength'],'evidence':'timing-animation-probe.json','scope':'source sequence, not confirmed action playback range'}
    report['sources'][str(probe.relative_to(R)).replace('\\','/')]=sha(probe.relative_to(R))
    report['limits'][1]='Jab_FR source sequence NumFrames/SequenceLength decoded by existing bounded tagged reader; remaining animations not extracted in this probe.'
(O/'timing-data.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'attacks':len(out),'resolvedRows':sum(c['animationRowResolved'] for c in checks),'specialHitActions':len(special)},ensure_ascii=False))
