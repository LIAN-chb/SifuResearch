"""Evidence-backed display names; source tree and per-hit values remain authoritative."""
def apply_names(data, texts):
    lookup={(r['namespace'],r['key']):r for r in texts}
    def name(key,scope='招式',via='菜单文字与输入入口'):
        r=lookup[('ST_UI_MenuCombo',key)]
        return {'name':r['zh-Hans'],'en':r['en'],'scope':scope,'key':key,'namespace':r['namespace'],'source_hash':r['source_hash'],'via':via}
    single={2:'Special_PostParryX',17:'Special_PostParryX',18:'Special_PostParryX',19:'Special_PostParryY',21:'Special_PostParryHoldY',22:'Special_RushX',23:'Special_RushY',25:'Special_PostPushedX',26:'Special_PostPushedY',31:'Command_BackForwardY',32:'Command_BackForwardX',33:'Command_HoldX',36:'Command_ForwardForwardY',39:'Command_ForwardForwardX',51:'Command_LBY',52:'Command_YX',55:'Special_ForwardRT',56:'Command_HoldY'}
    combos={12:('BaseCombo_YYXY',['Heavy','Heavy','Light','Heavy']),30:('BaseCombo_XXY',['Light','Light','Heavy']),15:('BaseCombo_XXXY',['Light','Light','Light','Heavy']),9:('BaseCombo_XXXXY',['Light','Light','Light','Light','Heavy']),16:('BaseCombo_YYDelayY',None),50:('BaseCombo_YDelayY',None)}
    for c in data['nodes'].values():c['official']=[]
    scopes={22:'奔跑轻击',23:'奔跑重击',25:'推击后轻击',26:'推击后重击'}
    for i,key in single.items():data['nodes'][str(i)]['official']=[name(key,scopes.get(i,'招式'))]
    # Two combo skills have explicit required tags and direct SkillUI name references.
    for i,(key,sequence) in combos.items():
        if sequence:
            current={next(e['target'] for e in data['defaults'] if e['rawInput']==sequence[0])}
            for inp in sequence[1:]:current={e['target'] for k in current for e in data['nodes'][str(k)]['edges'] if e['rawInput']=='EComboTransition::'+inp and e['target'] is not None}
            assert i in current,(key,current)
        data['nodes'][str(i)]['official']=[name(key,'连招收尾／技能', '保存衔接路径与菜单条目' if sequence else '所需技能标签与技能UI名称')]
    for i,stage in [(44,1),(45,2),(14,3),(7,4),(8,5)]:data['nodes'][str(i)]['official']=[name('BaseCombo_XXXXX','整套连招名 · 第'+str(stage)+'段','轻击主链；名称属于整套连招')]
    for i,stage in [(48,1),(4,2),(5,3),(10,4)]:data['nodes'][str(i)]['official']=[name('BaseCombo_YYYY','整套连招名 · 第'+str(stage)+'段','重击主链；名称属于整套连招')]
    # Exact shared attack assets can carry a known move association, but keep its route context.
    data['nodes']['54']['official']=[name('BaseCombo_YYDelayY','同动作资源 · 鹰击长空后重击','与神龙摆尾节点共享同一攻击资产')]
    for n in data['graph']['nodes']:
        n['official']=[{**o,'config':i} for i in n['configs'] for o in data['nodes'][str(i)]['official']]
        seen=set();n['official']=[o for o in n['official'] if not ((o['name'],o['scope']) in seen or seen.add((o['name'],o['scope'])))]
    return lookup

def hit_window(props,table,row):
    def metric(group,flag,value):
        obj=props.get(group+'[0]',{})
        return {'enabled':obj.get(flag+'[0]'),'value':obj.get(value+'[0]')}
    return {'table':table,'row':row,'resolved':True,'damage':metric('m_OnHitImpact','m_bUseDamage','m_fDamage'),'structure':metric('m_OnHitImpact','m_bUseStructureDamage','m_fStructureDamage'),'stun':metric('m_OnHitImpact','m_bUseNbFrameStuned','m_iNbFrameStuned'),'guard':metric('m_OnGuardImpact','m_bUseStructureDamage','m_fStructureDamage'),'deflect':metric('m_OnDeflectImpact','m_bUseStructureDamage','m_fStructureDamage'),'push':metric('m_OnHitImpact','m_bUseKnockBackDistance','m_fKnockBackDistance'),'power':props.get('m_eAttackPower[0]'),'reaction':props.get('m_eHittedReaction[0]'),'parriable':props.get('m_bParriable[0]'),'resilience':{'enabled':props.get('m_bOverrideResilience[0]'),'value':props.get('m_iOverrideResilienceValue[0]')},'raw':props}

def supplemental_node(identifier,label,action,official,x,y):
    return {'id':identifier,'label':label,'configs':[],'rawNodes':[],'x':x,'y':y,'direction':False,'action':action,'official':official}
