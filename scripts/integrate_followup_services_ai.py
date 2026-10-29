"""Integrate reviewed service/AI findings; preserve existing reader notes before targeted changes."""
from pathlib import Path
import json,hashlib
R=Path(r'E:\ProgrameFiles\SifuResearch');V=R/'Sifu';B=R/'notes/vault-backups/followup-unpacking-20261028';B.mkdir(parents=True,exist_ok=True)
changed=[]
def put(rel,s):
 p=V/rel
 if p.exists():
  raw=p.read_bytes();b=B/(hashlib.sha256(raw).hexdigest()[:10]+'-'+p.name)
  if not b.exists():b.write_bytes(raw)
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s.strip()+'\n',encoding='utf-8',newline='\n');changed.append(rel)
def section(s,t,b):
 m='\n## '+t+'\n'
 if m in s:
  i=s.index(m);j=s.find('\n## ',i+len(m));return s[:i]+m+'\n'+b.strip()+'\n'+('' if j<0 else s[j:])
 return s.rstrip()+m+'\n'+b.strip()+'\n'
put('03配置/订单与服务/Avoided与Deflected订单服务.md','''# Avoided与Deflected订单服务

[[03配置/订单与服务/索引|订单索引]] · [[01机制/连续受击与反击追击的系统链|机制]] · [[02实现/连续受击与反击追击的系统链|证据]]

## 订单来源与默认引用

| 对象 | 保存引用／配置 | 边界 |
|---|---|---|
| BP_Grunt_Base.OrderComponent.m_OrderDBs | 全局BP_OrderDB、Grunt_OrderDB | 直接配置已核；具体子类覆写仍需按父链查，不能泛化全敌人 |
| 全局BP_OrderDB | 79个订单引用，包含OrderAvoided、OrderDeflected | 数量是该库引用数，不是独立战斗机制数 |
| Grunt_OrderDB | 1项OrderFallOnSlope | 普通闪避／弹开反应沿全局库可见 |
| 两个订单顶层 | ActivationCondition引用OrderServiceIsPlayerCondition；AvailabilityInfo=AllDefensiveOptions，priority10 | 与下面逐服务条件、GenericNone不是同一字段；顶层条件消费与实际布尔体仍待核 |

## 两个订单的全部服务

两者各3条，配置一致；原始下标为0／1／2。下表保留完整配置差异和角色条件边界。

| 下标／服务 | 施加内容 | 服务级条件／反转 | 范围与启动字段 | 操作／优先级 | 停止处理 |
|---|---|---|---|---|---|
| 0 ForceFightingStateOrderService | EFightingState::Avoided；取角色ResistanceDB；Push duration=-1 | 空条件，反转false | FrameRange=true；两端Open；MissingFromAnim=false | 状态服务，不是许可层运算 | 用返回的状态ID PopFightingState |
| 1 AvailabilityLayerOrderService | GenericNone | OrderServiceIsPlayerCondition，反转true | FrameRange=true；两端Open；MissingFromAnim=false | 原生默认SET；BasicGameplay=0；priority10 | 服务句柄Pop；还受IsPawnMaster等生命周期门槛约束 |
| 2 DeflectedParryCancelAvailabilityOrderService | DeflectedParryCancelAL | OrderServiceIsPlayerCondition，反转false | FrameRange=true；下界Inclusive 8.0，上界Open；MissingFromAnim=false | OR；priority20 | 许可层服务停止路径回收；具体激活条件另核 |

`OrderServiceIsPlayerCondition`的资源名、函数名及IsPlayerControlled引用都已读到，但蓝图返回表达式尚未完整解析；因此表中角色方向仍是配置条件，不写成所有NPC都必定执行／所有玩家都必定跳过。8.0的时间基准未闭合，不改写成8帧或8秒。

## 相关动作掩码

| 资源 | 保存动作列表／选取方式 | 四种AI防御动作的位 | 说明 |
|---|---|---|---|
| GenericNone | 正选：Look、MouseLook、DizzyReduction、ReplayMenu | Avoid、Parry、Guard、Dodge均false | 名为None但保留四项；不能说全部输入关闭 |
| AllDefensiveOptions | Guard、Parry、PrepFocus、Avoid、Look、MouseLook、Dodge | 此资源包含四种防御 | 顶层路径资源，不等于逐服务GenericNone，也不据名字认定整单最终结果 |
| DeflectedParryCancelAL | ParryInterrupt、Parry | 仅列保存动作；完整结果还受OR组合和其他层影响 | 玩家侧候选取消许可，条件与8.0基准仍待核 |

## 状态时长与对象区分

Force服务传-1经PushFightingState的负时长分支写入Infinite标志；服务停止时按句柄Pop。它不是Grunt普通Dizzy的3／1.5秒。OrderAvoided本身的0.666／0.5秒配置、OrderDeflected读取所有者GuardDB的时长，以及后来命中产生的Dizzy时长分别管理。

当Avoided成为最高活动状态时，后续攻击可用其抗性矩阵行；当前Base／Adv配置的[击倒,推开,眩晕]为[0,0,1]，InFight为[2,2,11]。有其他更高状态、命中属性覆写或服务未激活时要另算，不从订单名断定必用哪一行。

来源：`inventory/followup-order-services-packages.json`保留10个定向包及文件哈希、完整导出／数组边界；执行见`notes/order-services-followup.md`和`inventory/followup-order-services-disassembly.json`。已提取、已解析及调用已接通分开记录；未实战验证。
''')
a=json.loads((R/'inventory/followup-parry-ai-assets.json').read_text(encoding='utf-8'))
lines=['# Grunt反击条件与动作','', '[[01机制/敌人如何选择防御|防御机制]] · [[03配置/订单与服务/索引|本轮配置入口]] · [[03配置/AI防御/索引|原情境防御表]]','',
'## 对象方向','', '| 场景 | 谁防守／谁后续动作 | 本页覆盖 |','|---|---|---|', '| 玩家招架敌人攻击 | 玩家防守，原攻击者接受反馈 | 下表实际Grunt攻击行与反馈分流 |','| 敌人招架玩家攻击 | Grunt的ParryDeflect节点成功，可能请求AI反击 | 六条完整父链及成功动作／票据引用 |','',
'两侧事件分开核对，不能用AI成功反击配置解释玩家招架后敌人必定眩晕。','',
'## 实际攻击引用与三种结果配置','', '| AttackDB／段 | 动画帧区间 | HitBox行 | 可招架／招架眩晕／闪避眩晕 | 普通生命／架势／硬直帧 | 格挡生命／架势／硬直帧 | 弹开生命／架势／硬直帧 |','|---|---|---|---|---|---|---|']
for at in a['attack_dbs']:
 for h in at['hit_boxes']:
  # Store identity below; flexible exporter variants stay visible in source JSON.
  pass
# These three identities are explicitly verified in the asset report and the authored AttackDB windows.
windows={'Hook_HB01':('Grunt_Hook / 段0','22–26'),'BaseballHook_HB01':('Grunt_BaseballHook / 段0','42–45'),'Uppercut_HB01':('Grunt_Uppercut / 段0','22–27')}
for row in a['hitbox_rows']:
 vals=[]
 for k in ['m_OnHitImpact','m_OnGuardImpact','m_OnDeflectImpact']:
  imp=row['impacts'][k];items=[]
  for flag,val in [('m_bUseDamage','m_fDamage'),('m_bUseStructureDamage','m_fStructureDamage'),('m_bUseNbFrameStuned','m_iNbFrameStuned')]:items.append(('开:' if imp.get(flag) else '关:')+str(imp.get(val)))
  vals.append(' / '.join(items))
 w=windows[row['row']];lines.append('| '+' | '.join([w[0],w[1],row['row'],'是／否／是']+vals)+' |')
lines+=['','数值是启用位约束下的保存配置，不是最终实战结果；动画帧区间含端点。三行实际在Base／Advanced Combo中被引用。缓存可完整覆写，但本轮没有找到它实际改写这些Grunt招架标志的证据。','',
'## 成功ParryDeflect的全部已解析动作父链','', '| 杂兵／成功节点索引 | 父链逐层测试（全部需通过） | 成功动作／票据 |','|---|---|---|']
for graph in a['contextual_defenses']:
 kind='普通' if '_Base_' in graph['asset'] else '进阶'
 for p in graph['parry_paths_with_actions']:
  desc=[]
  for seq in p['sequence_path']:
   tests=[]
   for t in seq['tests']:
    v=t.get('properties') or {};get=lambda k:v.get(k+'[0]','未保存')
    if 'm_fMemoryLimit[0]' in v:tests.append(str(get('m_AttackProperties'))+'，记忆'+str(get('m_fMemoryLimit'))+'秒／计数'+str(get('m_uiHitsCount'))+'／原始掩码'+str(get('m_HitTypes')))
    elif 'm_fValueMax[0]' in v:tests.append('AI自身GuardRatio ≤ 配置'+f'{float(get("m_fValueMax")):.6g}')
    else:tests.append('攻击属性'+str(get('m_AttackProperties'))+'；反转='+str(v.get('m_bInverted[0]','原生默认false')))
   desc.append('序列'+str(seq['index'])+'：'+' 且 '.join(tests))
  ticket='31' if p['terminal_index']==43 else '30'
  lines.append('| '+kind+' / '+str(p['terminal_index'])+' | '+' → '.join(desc).replace('|','\\|')+' | BP_AiLaunchCounterCombo_Parry；原始票据'+ticket+' |')
lines+=['','Push分支两者都经过外层10秒／掩码3，再过内层3秒／掩码2；旧摘录将进阶外层当成内层，已更正。这里的多个记忆测试是串联条件，不能只读其中一个。掩码2／3的精确业务标签未恢复，保留数值。','',
'架势测试读取AI自身的BPF_GetGuardRatio；Inferior分支用小于等于比较，不是严格小于。不将其提前翻译成“剩余架势40%”。','',
'## 反击执行与边界','', '| 环节 | 本轮接通 | 尚缺 |','|---|---|---|',
'| 成功动作 | 六条节点均挂BP_AiLaunchCounterCombo_Parry；空动作条件数组不取消父链测试 | 节点最终竞争获选与成功回调现场 |',
'| 票据到Combo | 原始30／31→Custom Combo 1／2；保存转移概率100% | target-node映射仍opaque，不能据此指认实际首招 |',
'| 额外条件 | Adv两条start entry带MCDomination条件；Base的31带、30未保存该条件 | 条件的精确语义及实战票据请求结果 |',
'| 策略收尾 | 对手攻击结束时检查AI owner自己的IsStun；自身不stun且无指定防御记录时取消tactic | 原始记录byte2语义和严格逐帧顺序 |',
'| Avoid对照 | 当前Grunt Avoid节点未保存同类成功反击动作；Adv额外节点记录FirstAvoid并flush FirstParry | 不能等同全游戏没有闪避反击 |',
'| 全行覆写 | BPF_SetHitboxRow存在；已扫描包名中BP_FallHitRequest引用该函数 | 图字节码、具体传参、其他native写入尚未穷尽 |','',
'证据：`inventory/followup-parry-ai-assets.json`；`notes/parry-ai-followup.md`；架势比较补证在`inventory/followup-structure-test-disassembly.json`，枚举Inferior=1见`inventory/system-recovery-type-layouts.json`。未运行游戏。']
put('03配置/AI防御/Grunt反击条件与动作.md','\n'.join(lines))
rel='03配置/订单与服务/索引.md';s=(V/rel).read_text(encoding='utf-8');s=s.replace('订单描述执行生命周期','新增[[03配置/订单与服务/Avoided与Deflected订单服务]]：两订单全部6条服务及掩码／角色条件。AI条件与动作见[[03配置/AI防御/Grunt反击条件与动作]]。\n\n订单描述执行生命周期');put(rel,s)
# Fix a previously mis-copied inner test, without changing the still-distinct remainder of the AI graph.
rel='01机制/敌人如何选择防御.md';s=(V/rel).read_text(encoding='utf-8')
s=s.replace('| 普通 | BackFrontPush | 3 秒 | 1 | 原始掩码 2；原生反转默认false；具体覆写另查 | 招架／弹开 |','| 普通 | BackFrontPush | 外层10秒，再内层3秒 | 每层1 | 外层掩码3、内层掩码2，并有攻击属性测试；按完整父链串联 | 招架／弹开 |')
s=s.replace('| 进阶 | BackFrontPush | 10 秒 | 1 | 原始掩码 3；原生反转默认false；具体覆写另查 | 招架／弹开 |','| 进阶 | BackFrontPush | 外层10秒，再内层3秒 | 每层1 | 此父链阈值与普通相同；其他图分支仍需分别比较 | 招架／弹开 |')
s=section(s,'本轮补证','完整成功反击父链及实际动作引用见[[03配置/AI防御/Grunt反击条件与动作]]。本轮按原包更正了进阶Push分支的内外层摘录：内层是3秒／掩码2，外层才是10秒／掩码3。两者此分支相同，不表示全图相同。AI owner自身stun与玩家stun仍须分开。')
put(rel,s)
# Append the accurate source correction to the early working note.
p=R/'notes/stun-ai-defense.md';raw=p.read_bytes();bk=B/(hashlib.sha256(raw).hexdigest()[:10]+'-'+p.name)
if not bk.exists():bk.write_bytes(raw)
s=raw.decode('utf-8-sig');lines=[]
for line in s.splitlines():
 if '| `Grunt_Adv_ContextualDefense`, sequence 9' in line:
  line=line.replace('10s, 1 hit, mask 3','3s, 1 hit, mask 2').replace('Same authored parry/deflect edge with a longer memory limit and different raw mask','Inner gate matches Base at 3s/mask2; both also have an outer 10s/mask3 gate, see parry-ai-followup.md')
 lines.append(line)
p.write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
lp=R/'inventory/vault-layout.json';layout=json.loads(lp.read_text(encoding='utf-8'))
for rel in changed:
 if rel not in layout['documents']:layout['documents'].append(rel)
lp.write_text(json.dumps(layout,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
print(json.dumps({'updated_notes':len(changed),'vault_notes':len(layout['documents'])},ensure_ascii=True))