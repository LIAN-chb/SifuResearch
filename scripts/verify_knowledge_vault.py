"""Validate the topic-based vault's links and saved static evidence, not game behavior."""
import ast, datetime, hashlib, json, re
from pathlib import Path
ROOT = Path(r'E:\ProgrameFiles\SifuResearch')
VAULT = ROOT/'Sifu'
EXE = Path(r'E:\Games_Little\Epic\Sifu\Sifu\Binaries\Win64\Sifu-Win64-Shipping.exe')
EXPECTED = 'a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254'
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8*1024*1024),b''): h.update(b)
    return h.hexdigest()
errors=[]
layout=json.loads((ROOT/'inventory/vault-layout.json').read_text(encoding='utf-8'))
docs={p.relative_to(VAULT).with_suffix('').as_posix():p.read_text(encoding='utf-8-sig')
      for p in VAULT.rglob('*.md') if '.obsidian' not in p.relative_to(VAULT).parts}
expected_docs={str(Path(p).with_suffix('')).replace('\\','/') for p in layout['documents']}
if set(docs)!=expected_docs:errors.append('Document inventory differs: '+repr(sorted(set(docs)^expected_docs)))
for name in docs:
    root_note = '/' not in name and name+'.md' in layout.get('root_documents', [])
    if not root_note and name.split('/')[0] not in layout['directories']:errors.append('Note outside configured directories: '+name)
headings={name:set(re.findall(r'^#{1,6}\s+(.+?)\s*$',s,re.M)) for name,s in docs.items()}
links=[]
for name,s in docs.items():
    if '\ufffd' in s:errors.append(name+': invalid replacement character')
    for target in re.findall(r'\[\[([^\]]+)\]\]',s):
        ref=target.split('|',1)[0].rstrip(chr(92))
        file,_,heading=ref.partition('#')
        file=(file or name).removesuffix('.md')
        valid=file in docs and (not heading or heading in headings[file])
        links.append({'from':name,'target':target,'valid':valid})
        if not valid:errors.append(name+': broken link '+target)
topics=layout['topics']
for topic in topics:
    for source,target in [('01机制','02实现'),('02实现','01机制')]:
        if '[['+target+'/'+topic not in docs.get(source+'/'+topic,''):
            errors.append('Missing reciprocal topic link '+source+' -> '+target+'/'+topic)
referenced_sources=set()
for name,s in docs.items():
    for ref in re.findall(r'(?<![\w/])(?:notes|exports|inventory|logs|scripts)/[A-Za-z0-9_./-]+\.(?:json|gz|csv|md|py|txt)',s):
        referenced_sources.add(ref)
        if not (ROOT/ref).is_file():errors.append(name+': missing evidence path '+ref)

manifests=[]
for p in sorted((ROOT/'inventory').glob('*disassembly.json')):
    a=json.loads(p.read_text(encoding='utf-8-sig'))
    if not a.get('exe_sha256'):continue
    if a['exe_sha256']!=EXPECTED:errors.append('Manifest EXE mismatch '+p.name)
    count=0;missing=[]
    for item in a.get('procedures',[]):
        if item.get('status')!='disassembled':
            missing.append(item.get('name'));continue
        dest=Path(item['file'])
        if not dest.is_file():errors.append('Missing assembly '+str(dest))
        elif sha(dest)!=item['assembly_sha256']:errors.append('Assembly hash mismatch '+str(dest))
        count+=1
    manifests.append({'file':p.name,'verified_output_entries':count,'unresolved_names':missing})
syntax=[]
for p in sorted((ROOT/'scripts').glob('*.py')):
    try:ast.parse(p.read_text(encoding='utf-8-sig'),filename=str(p));syntax.append(p.name)
    except SyntaxError as e:errors.append('Syntax '+p.name+': '+str(e))
sources=['notes/stun-ai-defense.md','notes/resilience-damage.md','notes/counter-punish.md','notes/group-ai-state.md',
'inventory/stun-state-data.json','inventory/stun-state-type-layouts.json','inventory/action-resilience-type-layouts.json',
'exports/grunt-contextual-defense.json','exports/state-reaction-settings.csv','exports/state-resistance-matrices.csv','exports/hit-impact-values.csv']
for s in sources:
    if not (ROOT/s).is_file():errors.append('Missing source '+s)
exe_sha=sha(EXE)
if exe_sha!=EXPECTED:errors.append('EXE changed')
report={'checked_at':datetime.datetime.now().astimezone().isoformat(),'status':'passed' if not errors else 'failed',
'vault':str(VAULT),'notes':{n:{'sha256':sha(VAULT/(n+'.md')),'bytes':(VAULT/(n+'.md')).stat().st_size} for n in docs},
'wikilinks_checked':len(links),'links':links,'topic_pairs_checked':len(topics),'exe_sha256':exe_sha,
'evidence_manifests':manifests,'python_scripts_syntax_checked':syntax,'source_files_checked':sorted(set(sources)|referenced_sources),
'errors':errors,'manual_review':['Terminology: health damage, Structure, Resilience, Resistance and stun are kept distinct.',
'Configuration samples and user observations are marked separately from code facts.',
'Dizzy state permission and AI consumer connected statically; service condition bytecode and runtime activation remain unresolved.'],
'not_verified':['Runtime behavior, final damage values, exact follow-up windows and enemy action service instances.'],
'mutations':'This checker writes only its verification report under SifuResearch/inventory; it does not launch or modify the game.'}
out=ROOT/'inventory/knowledge-vault-verification.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':report['status'],'notes':len(docs),'wikilinks':len(links),'scripts':len(syntax),
'assembly_output_entries':sum(x['verified_output_entries'] for x in manifests),'errors':errors},ensure_ascii=True))
raise SystemExit(bool(errors))
