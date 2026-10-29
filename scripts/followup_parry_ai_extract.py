from __future__ import annotations
import gzip, hashlib, json, sys
from pathlib import Path
ROOT=Path(r'E:\ProgrameFiles\SifuResearch')
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'tools'))
import local_bounded_packages as bounded

def load_gz(rel): return json.load(gzip.open(ROOT/rel,'rt',encoding='utf-8'))
def flatprops(items):
    if isinstance(items,dict): return items
    return {p.get('name'):p for p in (items or []) if isinstance(p,dict) and 'name' in p}
def propval(items,name,default=None):
    pp=flatprops(items)
    p=pp.get(name) or pp.get(name+'[0]')
    if not p:return default
    return p.get('value',default) if isinstance(p,dict) else p
def deep_value(x):
    if isinstance(x,dict): return x.get('value',x.get('reference'))
    return x

def handle_ref(props,field):
    p=flatprops(props).get(field,{})
    fields=flatprops(p.get('value',[]))
    return {'table':fields.get('DataTable',{}).get('reference'), 'row':fields.get('RowName',{}).get('value')}

def get_tags_by_asset(tagged,needle):
    return [x for x in tagged if needle in x.get('asset','')]

def file_hashes(asset_rel):
    base=ROOT/'extracted'/Path(*asset_rel.split('/'))
    out={}
    for ext in ('.uasset','.uexp'):
        p=base if base.suffix==ext else base.with_suffix(ext)
        if p.exists(): out[p.suffix]={'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    return out

def asset_hash_record(rel):
    return {'asset':rel,'files':file_hashes(rel)}

def table_row(tables,asset_suffix,rowname):
    t=next((x for x in tables if x['asset'].endswith(asset_suffix)),None)
    if not t:return None
    r=next((r for r in t.get('rows',[]) if r.get('row')==rowname),None)
    if not r:return None
    ps=flatprops(r.get('properties'))
    def val(n): return ps.get(n,{}).get('value')
    impact={}
    for k in ('m_OnHitImpact','m_OnGuardImpact','m_OnDeflectImpact'):
        ip=ps.get(k)
        if not ip:continue
        iv=flatprops(ip.get('value'))
        impact[k]={n:iv.get(n,{}).get('value') for n in ('m_bUseDamage','m_fDamage','m_bUseStructureDamage','m_fStructureDamage','m_bUseSuperDizzyDamage','m_fSuperDizzyDamage','m_bUseNbFrameStuned','m_iNbFrameStuned','m_bUseFreezeFrame','m_fFreezeFrameDuration') if n in iv}
    return {'row':rowname,'m_bParriable':val('m_bParriable'),'m_bDizzyOnParry':val('m_bDizzyOnParry'),'m_bDizzyOnAvoid':val('m_bDizzyOnAvoid'),'m_PlayAvoidedOrder':val('m_bPlayAvoidedOrder'),'impacts':impact}

def attack_cfg(obj):
    props=flatprops(obj.get('properties'))
    attack=props.get('m_Attack',{}).get('value',[])
    ap=flatprops(attack)
    boxes=props.get('m_Attack',{}).get('value',[])
    # ComboAttack is an object-like struct property; nested HitBoxes are below it.
    hb=ap.get('m_HitBoxes',{})
    rows=[]
    for idx,element in enumerate(hb.get('arrayElements',[]) or []):
        ep=flatprops(element)
        frame=flatprops(ep.get('m_FrameRange',{}).get('value',[]))
        anim=flatprops(frame.get('m_Anim',{}).get('value',[]))
        lo=flatprops(anim.get('LowerBound',{}).get('value',[])); hi=flatprops(anim.get('UpperBound',{}).get('value',[]))
        rows.append({'index':idx,'row_handle':handle_ref(element,'m_HitRow'),'frame_range':{'lower':flatprops(lo.get('Value',{}).get('value',[])).get('x') if isinstance(lo.get('Value',{}).get('value'),list) else lo.get('Value',{}).get('value'),'lower_bound_type':lo.get('Type',{}).get('value'),'upper':hi.get('Value',{}).get('value'),'upper_bound_type':hi.get('Type',{}).get('value')},'activation_condition':ep.get('m_activationCondition',{}).get('value'),'metadata':ep.get('m_MetaData',{}).get('value')})
    return {'asset':obj['asset'],'export':obj['export'],'sha256':obj.get('sha256'),'animation_row':handle_ref(attack,'m_AnimationRow'),'animation':ap.get('m_Animation',{}).get('reference'),'hit_boxes':rows}

def contextual(asset_suffix,objects,instance_objects):
    entries=[x for x in objects if x['asset'].endswith(asset_suffix)]
    by_export={x['export']:x for x in entries}
    root=by_export.get(asset_suffix.replace('.uasset',''))
    if not root:
        root=next((x for x in entries if x['class'].endswith('AIContextualDefense')),None)
    if not root:return {'error':'root not found'}
    roots=propval(root['properties'],'m_Nodes',[]) or []
    tests={x['export']:x for x in entries if x['class'].endswith(('AttackMemoryInfluenceTest','AttackPropertiesInfluenceTest','StructureInfluenceTest'))}
    paths=[]
    def walk(name,stack,depth=0):
        if depth>20 or name in stack:return
        node=by_export.get(name)
        if not node:return
        cls=node['class'].split('.')[-1]
        p=node['properties']
        if cls=='DefenseInfluenceNodeParryDeflect':
            actions=propval(p,'m_ActionsOnSuccess',[]) or []
            if actions:
                seqs=[]
                for nm in stack:
                    sn=by_export.get(nm)
                    if sn and sn['class'].endswith('AIInfluence_TestSequence'):
                        sprops=sn['properties']; testrefs=propval(sprops,'m_Tests',[]) or []
                        testdetails=[]
                        for ref in testrefs:
                            testname=ref.rsplit('.',1)[-1]
                            tx=by_export.get(testname)
                            testdetails.append({'name':testname,'properties':tx['properties'] if tx else None})
                        seqs.append({'name':nm,'index':propval(sprops,'m_iNodeIndex'),'probability':propval(sprops,'m_fProbability'),'tests':testdetails})
                raw_actions=[]
                for a in actions:
                    action=a.get('m_Action[0]',{})
                    inst=action.get('m_Instance[0]',{}).get('reference','')
                    ix=action.get('m_Instance[0]',{}).get('index')
                    cdo=next((x for x in instance_objects if x.get('asset')==root['asset'] and x.get('export_index')==ix),None)
                    raw_actions.append({'class':action.get('m_DefaultClassObject[0]',{}).get('reference'),'instance_ref':inst,'instance_export_index':ix,'instance_properties':cdo.get('properties') if cdo else None,'conditions':a.get('m_ConditionsArray[0]',[])})
                paths.append({'sequence_path':seqs,'terminal_node':name,'terminal_index':propval(p,'m_iNodeIndex'),'node_properties':p,'actions':raw_actions})
            return
        links=propval(p,'m_LinkedNodes',[]) or []
        for ref in links:
            walk(ref.rsplit('.',1)[-1],stack+[name],depth+1)
    for ref in roots:
        walk(ref.rsplit('.',1)[-1],[],0)
    # List configured Avoid nodes for comparison; these may not be reachable from roots if no actions.
    avoid=[]
    for n in entries:
        if n['class'].endswith('DefenseInfluenceNodeAvoid'):
            avoid.append({'name':n['export'],'index':propval(n['properties'],'m_iNodeIndex'),'properties':n['properties']})
    return {'asset':root['asset'],'root':root['export'],'roots':roots,'parry_paths_with_actions':paths,'avoid_nodes':avoid}

tagged=load_gz('inventory/tagged-objects.json.gz')
tables=load_gz('inventory/data-tables.json.gz')
context=json.load(open(ROOT/'exports/grunt-contextual-defense.json',encoding='utf-8'))
instance_objects=json.load(open(ROOT/'exports/ai-and-impact-objects.json',encoding='utf-8'))
package_metadata=load_gz('inventory/package-metadata.json.gz')
# specific AttackDBs
wanted=['Grunt_Hook.uasset','Grunt_BaseballHook.uasset','Grunt_Uppercut.uasset']
attack_objects=[x for x in tagged if x.get('class')=='/Script/Sifu.AttackDB' and any(x['asset'].endswith(w) for w in wanted)]
# Combo asset nodes
combo_objects=[]
for suffix in ('/_Base/Grunt_Base_Combo.uasset','/_Advanced/Grunt_Advanced_Combo.uasset'):
    obj=next(x for x in tagged if x['asset'].endswith(suffix) and x.get('class')=='/Script/Sifu.Combo')
    nodes=next((p for p in obj['properties'] if p.get('name')=='m_Nodes'),{})
    matches=[]
    for i,e in enumerate(nodes.get('arrayElements',[]) or []):
        ep=flatprops(e); infos=flatprops(ep.get('m_AttackInfos',{}).get('value',[]))
        refs=list(dict.fromkeys(q.get('reference') or q.get('value') for q in infos.values() if isinstance(q,dict) and isinstance(q.get('reference') or q.get('value'),str)))
        if any(any(n in r for n in ('Grunt_Hook.','Grunt_BaseballHook.','Grunt_Uppercut.')) for r in refs):
            trans=flatprops(ep.get('m_Transitions',{}).get('value',[]))
            matches.append({'node_index':i,'parent_name':trans.get('m_ParentNodeName',{}).get('value'),'attack_refs':refs})
    combo_objects.append({'asset':obj['asset'],'sha256':obj.get('sha256'),'matching_nodes':matches})

# Exact serialized ticket-to-start-entry joins inside the two Grunt Combo assets.
ticket_combo_entries=[]
for suffix in ('/_Base/Grunt_Base_Combo.uasset','/_Advanced/Grunt_Advanced_Combo.uasset'):
    obj=next(x for x in tagged if x['asset'].endswith(suffix) and x.get('class')=='/Script/Sifu.Combo')
    starts=next((p for p in obj['properties'] if p.get('name')=='m_ComboStartNodesContainer'),{})
    for index,entry in enumerate(starts.get('arrayElements',[]) or []):
        ep=flatprops(entry); state=flatprops(ep.get('m_EnumState',{}).get('value',[])); ticket=state.get('m_Value',{}).get('value')
        if ticket not in ('BP_AIAttackTIcketNames::NewEnumerator30','BP_AIAttackTIcketNames::NewEnumerator31'): continue
        trans=flatprops(ep.get('m_ComboTransitions',{}).get('value',[]))
        transitions=[]
        for item in trans.get('m_Transitions',{}).get('arrayElements',[]) or []:
            ip=flatprops(item); tm=ip.get('m_TargetNodes',{}).get('value')
            transitions.append({'input':ip.get('m_eInputTransition',{}).get('value'),'condition_ref':ip.get('m_ConditionInstance',{}).get('reference'),'probability':ip.get('m_fProbability',{}).get('value'),'target_nodes_map':tm})
        ticket_combo_entries.append({'combo_asset':obj['asset'],'start_entry_index':index,'ticket':ticket,'parent_label':trans.get('m_ParentNodeName',{}).get('value'),'phase':ep.get('m_PhaseName',{}).get('value'),'transitions':transitions})

hitbox_rows=[]
for row in ('Hook_HB01','BaseballHook_HB01','Uppercut_HB01'):
    hitbox_rows.append(table_row(tables,'Grunt_HitBoxData.uasset',row))

# contextual defense paths
ctx=[]
for suf in ('Grunt_Base_ContextualDefense.uasset','Grunt_Adv_ContextualDefense.uasset'):
    c=contextual(suf,context,instance_objects)
    c['asset_hashes']=file_hashes(c['asset']) if c.get('asset') else {}
    ctx.append(c)

bp_assets=[]
for suf in ('Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo_Parry.uasset','Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo_Avoid.uasset','Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.uasset'):
    rel='Sifu/Content/'+suf
    bp_assets.append(asset_hash_record(rel))
bp_cdos=[]
for rel in ('Sifu/Content/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo_Parry.uasset','Sifu/Content/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo_Avoid.uasset','Sifu/Content/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.uasset'):
    package=next(x for x in package_metadata if x['path']==rel)
    asset=ROOT/'extracted'/Path(*rel.split('/'))
    payload=asset.with_suffix('.uexp').read_bytes()
    default=next((e for e in package['exports'] if e['name'].startswith('Default__')),None)
    if default:
        start=default['serialOffset']-asset.stat().st_size
        props,used=bounded.tags(payload[start:start+default['serialSize']],package['names'])
        bp_cdos.append({'asset':rel,'sha256':package.get('uassetSha256'),'default_object':default['name'],'parsed_bytes':used,'serial_bytes':default['serialSize'],'properties':props})

# Relevant BP child CDOs inside Grunt contextual packages.
instance_cdos=[]
for x in context:
    if x['export'].startswith('BP_AiLaunchCounterCombo_Parry_C_'):
        instance_cdos.append({'asset':x['asset'],'export':x['export'],'properties':x['properties']})

manifest=json.load(open(ROOT/'inventory/followup-parry-ai-disassembly.json',encoding='utf-8'))
logic_manifest=json.load(open(ROOT/'inventory/followup-parry-ai-logic-disassembly.json',encoding='utf-8'))
helper_manifest=json.load(open(ROOT/'inventory/followup-parry-ai-hitbox-disassembly.json',encoding='utf-8'))
launch_manifest=json.load(open(ROOT/'inventory/followup-parry-ai-launch-disassembly.json',encoding='utf-8'))
row_setter_referrers=[]
for package in package_metadata:
    names=package.get('names',[])
    hits=[n for n in names if n in ('BPF_SetHitboxRow','BPF_SetHitboxDamage','BPF_SetHitboxStructureDamage','BPF_SetHitboxDamageOnRef','BPF_GetHitboxDataRow')]
    if hits:
        rel=package['path']; row_setter_referrers.append({'asset':rel,'referenced_hitbox_helper_names':hits,'package_metadata_uasset_sha256':package.get('uassetSha256'),'files':file_hashes(rel)})
source_asset_paths=[
 'Sifu/Content/DB/AI/Archetypes/Grunt/Attacks/Grunt_HitBoxData.uasset',
 'Sifu/Content/DB/AI/Archetypes/Grunt/Attacks/BareHands/Grunt_Hook.uasset',
 'Sifu/Content/DB/AI/Archetypes/Grunt/Attacks/BareHands/Grunt_BaseballHook.uasset',
 'Sifu/Content/DB/AI/Archetypes/Grunt/Attacks/BareHands/Grunt_Uppercut.uasset',
 'Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Grunt_Base_Combo.uasset',
 'Sifu/Content/DB/AI/Archetypes/Grunt/_Advanced/Grunt_Advanced_Combo.uasset',
 'Sifu/Content/DB/AI/Archetypes/Grunt/Defense/Grunt_Base_ContextualDefense.uasset',
 'Sifu/Content/DB/AI/Archetypes/Grunt/Defense/Grunt_Adv_ContextualDefense.uasset',
 *[f' Sifu/Content/Blueprints/AI/Actions/Defense/CounterCombo/{n}.uasset'.strip() for n in ('BP_AiLaunchCounterCombo_Parry','BP_AiLaunchCounterCombo_Avoid','BP_AiLaunchCounterCombo')]
]
report={
 'research_scope':'Static local Sifu package/PDB evidence; no runtime execution.',
 'sources':{
  'exe_sha256':manifest['exe_sha256'],
  'pdb_guid_age':'fdd64e0f-b9ed-4479-8fd8-efe0038b919d / 1',
  'package_parse':'inventory/tagged-objects.json.gz and inventory/data-tables.json.gz; extracted assets only',
  'pdb_disassembly_manifests':['inventory/followup-parry-ai-disassembly.json','inventory/followup-parry-ai-logic-disassembly.json','inventory/followup-parry-ai-hitbox-disassembly.json','inventory/followup-parry-ai-launch-disassembly.json']
 },
 'hitbox_rows':hitbox_rows,
 'attack_dbs':[attack_cfg(x) for x in attack_objects],
 'combo_membership':combo_objects,
 'ticket_combo_start_entries':ticket_combo_entries,
 'contextual_defenses':ctx,
 'blueprint_assets':bp_assets,
 'blueprint_default_objects':bp_cdos,
 'source_asset_hashes':[asset_hash_record(x) for x in source_asset_paths],
 'parry_action_instances':instance_cdos,
 'hitbox_helper_blueprint_package_name_references':row_setter_referrers,
 'limitations':[
  'The BP_AIAttackTIcketNames enum package is not present in the cooked package list, so NewEnumerator ticket values cannot be translated into readable combo names.',
  'Static serialized values and code do not establish live actor state, cache contents, sequence scheduling order, or which action won in a particular fight.',
  'UHitboxHelper::execBPF_SetHitboxRow is a native Blueprint thunk that copies a full FHitboxDataRow into GetMutableRow; the package-name scan identifies BP_FallHitRequest as the only cooked package containing its function reference. Its graph bytecode and exact call inputs are not decoded here, and other native writers remain outside the targeted callsite scan.',
  'No game runtime, save, or LIAN project was opened or modified.'
 ]
}
out=ROOT/'inventory/followup-parry-ai-assets.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'output':str(out),'hitbox_rows':len(hitbox_rows),'attack_dbs':len(attack_objects),'context_paths':{x['asset']:len(x.get('parry_paths_with_actions',[])) for x in ctx},'blueprint_assets':len(bp_assets)},ensure_ascii=False))
