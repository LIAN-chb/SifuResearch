from pathlib import Path
import json,csv,gzip,hashlib,sys
R=Path(r'E:/ProgrameFiles/SifuResearch')
def sha(p):return hashlib.file_digest(p.open('rb'),'sha256').hexdigest()
src=R/'inventory/object-and-table-properties.csv'
rows=list(csv.DictReader(src.open(encoding='utf-8-sig')))
names={'Grunt_Base_ResistanceDB','Grunt_Adv_ResistanceDB','Grunt_Miniboss_ResistanceDb','BaseResistanceDB'}
selected=[]
for i,r in enumerate(rows,2):
 if (r['export_or_row'] in names and ((r['property'].startswith('m_DownReaction') and any(t in r['property'] for t in ['Accum','m_fDuration'])) or ('m_WallSplash' in r['property'] and 'RowName' in r['property']))) or (r['export_or_row'] in {'WallSplashFar_HB01','WallSplashClose_HB01','WallSplashOnEnvironment_HB01'}):selected.append({'csv_line':i,**r})
tagged=json.load(gzip.open(R/'inventory/tagged-objects.json.gz','rt',encoding='utf-8'))
raw=[]
for ob in tagged:
 if ob['export'] not in names:continue
 ps=[]
 for p in ob['properties']:
  if p['name']=='m_DownReaction':
   q={k:v for k,v in p.items() if k!='value'}
   q['value']=[v for v in p['value'] if v['name'] in {'m_fMaxAccumulatedDamage','m_iMaxAccumatedHits','m_bGroupMaxAccumulatedHitsByAttack','m_Movement'}]
   ps.append(q)
 raw.append({k:ob[k] for k in ['asset','export','class','sha256']}|{'properties':ps})
assert len(raw)==4
for ob in raw:
 down=ob['properties'][0]['value'];d={p['name']:p['value'] for p in down}
 assert d['m_fMaxAccumulatedDamage']==-1.0 and d['m_iMaxAccumatedHits']==2 and d['m_bGroupMaxAccumulatedHitsByAttack']==False
out=R/'inventory/interaction-20261030-wall-config.json'
out.write_text(json.dumps({'source':str(src),'source_sha256':sha(src),'rows':selected,'tagged_source':'inventory/tagged-objects.json.gz','tagged_sha256':sha(R/'inventory/tagged-objects.json.gz'),'tagged_exports':raw,'verification':'Four selected DownReaction exports agree: maxDamage=-1, maxHits=2, groupByAttack=false. No runtime verification.'},ensure_ascii=False,indent=2),encoding='utf-8')
inputs=['scripts/disassemble_research.py','scripts/inspect_types.py','scripts/interaction-20261030-wall-types.py','scripts/interaction-20261030-wall-evidence.py','inventory/pdb_overview.json','inventory/game-procedures.json','inventory/object-and-table-properties.csv','inventory/tagged-objects.json.gz']
outputs=[p for p in (R/'inventory').glob('interaction-20261030-wall-*') if p.suffix=='.json']+[p for p in (R/'logs').glob('interaction-20261030-wall-*/*.txt')]
m={'cwd':str(R),'python':sys.version,'dumpbin_file_version':'14.51.36243.0','method':'Reuse existing tagged/CSV configuration, adapted CodeView member-layout reader with known LF_ONEMETHOD fix, bounded PDB procedure disassembly; EXE SHA checked by disassembler each run.','exe_sha256':'a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254','pdb_sha256_parent_verified':'5925d79b63df58ff98575454f3d31b07a4e0da44f96dc19461fc5b7e56d1b90c','commands':[],'inputs':[{'path':p,'sha256':sha(R/p)} for p in inputs],'outputs':[{'path':str(p.relative_to(R)).replace('\\','/'),'sha256':sha(p),'status':'success'} for p in outputs],'limitations':['Configuration is extracted/parsed, not runtime instance proof.','OrderPushed to collision-service configuration attachment and close-wall selection are not closed by this branch.','Static HandleImpact re-entry does not guarantee final Dizzy, KnockedDown or Hitted outcome.']}
for group in ['interaction-20261030-wall-code','interaction-20261030-wall-more']:
 d=json.loads((R/'inventory'/f'{group}-disassembly.json').read_text())
 names=list(dict.fromkeys(p['name'] for p in d['procedures']))
 m['commands'].append('python scripts/disassemble_research.py --group '+group+' '+' '.join('--name '+n for n in names))
m['commands']+=['python scripts/interaction-20261030-wall-types.py','python scripts/interaction-20261030-wall-evidence.py']
(R/'inventory/interaction-20261030-wall-manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'selected_csv_rows':len(selected),'verified_tagged_exports':len(raw),'output_files':len(outputs)},ensure_ascii=False))
