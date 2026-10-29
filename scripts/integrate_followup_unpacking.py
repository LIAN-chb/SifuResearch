"""Update only the integrated research notes with this batch's confirmed queue evidence."""
from pathlib import Path
import json,hashlib,datetime,shutil
R=Path(r'E:\ProgrameFiles\SifuResearch');V=R/'Sifu';B=R/'notes/vault-backups/followup-unpacking-20261028';B.mkdir(parents=True,exist_ok=True)
changes=[]
def put(rel,s):
 p=V/rel
 if p.exists():
  old=p.read_bytes();dest=B/(hashlib.sha256(old).hexdigest()[:10]+'-'+p.name)
  if not dest.exists():dest.write_bytes(old)
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s.strip()+'\n',encoding='utf-8',newline='\n');changes.append(rel)
def section(s,title,body):
 marker='\n## '+title+'\n'
 if marker in s:
  start=s.index(marker);end=s.find('\n## ',start+len(marker));return s[:start]+marker+'\n'+body.strip()+'\n'+('' if end<0 else s[end:])
 return s.rstrip()+marker+'\n'+body.strip()+'\n'
rel='01机制/连续受击与反击追击的系统链.md';s=(V/rel).read_text(encoding='utf-8')
s=section(s,'补解包更新：连续命中的新旧受击订单','''正常、无前置的Hitted请求现在已接通：**本次命中先计算结果，再安排取消符合条件的旧动画绑定订单，排入新Hitted；取消旧运行订单时会回收旧恢复层和服务。** 这与“只把同一个对象的剩余硬直时间改大”不同。

| 问题 | 本轮确认 | 适用限制 |
|---|---|---|
| 收集哪些旧订单 | Hitted的订单子类型是BoundToAnimState；无前置请求收集Running/Pending中同类别且Starting／Processing的订单ID | 不是所有并行订单都取消；已停止／已取消者不在该谓词集合 |
| 新命中怎样取代旧命中 | 先安排取消旧单，再提交新的播放命令；旧Hitted符合取消集合条件 | 路径有延迟命令处理，不宣称所有回调同帧执行 |
| 已开放的旧恢复许可怎么办 | 旧运行订单取消→OnCancel→具体OnStop→回收其HitRecoveryAvailability；服务随后停止 | 尚未启动订单走自己的取消前回调；新单自己再按计时／条件开放恢复层 |
| 是否保证越打窗口越长 | 不保证。Grunt普通最长策略为false，本次结果不自动和旧剩余时间取max；新订单还按本次时长、冻结及动画覆盖计时 | AlreadyGuardBroken另有max条件；不能直接断言具体某击必缩短窗口 |
| 是否解释完整防无限连 | 只解释普通Hitted怎样被后续命中替换；Dizzy的持续与累计限制仍由另一套状态管线管理 | 具体哪击被AI防住，继续核状态、许可与防御图；不建立全游戏统一拳数规则 |

精确分支见实现E17和`notes/hitted-queue-followup.md`；两份订单全部33条服务配置见[[03配置/订单与服务/Hitted订单与服务]]。''')
s=s.replace('旧订单替换／取消策略及AI消费许可仍缺','正常无前置Hitted的取消／新建已接通；特殊序列、冻结／预测及AI消费许可仍需分别核对')
s=s.replace('刷新读取点、订单提前取消及AI最终调度','特殊刷新分支、订单提前取消及AI最终调度')
put(rel,s)
rel='02实现/连续受击与反击追击的系统链.md';s=(V/rel).read_text(encoding='utf-8')
s=section(s,'后续补解包与执行证据','''| 编号 | 连接 | 精确入口与范围 |
|---|---|---|
| E17 | 普通无前置Hitted：构造新单→取消目标集合→旧单回收→新计时 | ApplyImpact `0x1a47eff–0x1a47f5e`；AFightingCharacter::PlayOrder `0x19c801a`；UOrderComponent::PlayOrder `0x1ae5027–0x1ae5144`、`0x1ae52b6/0x1ae52cb`、`0x1ae556b`；GatherActionTypeOrderIDs `0x1afa580`，谓词`0x1af24a0`；OrderBase::Process `0x1b121f6–0x1b12205`，OnCancel `0x1a006c0`→OnStop虚槽。详见`notes/hitted-queue-followup.md`及`inventory/followup-hitted-type-layouts.json` |
| E18 | 订单服务数组由不透明变为完整配置记录 | `inventory/followup-hitted-assets.json`：OrderHitted与OrderHittedGeneric的默认对象服务数30／3，8份tagged数据导出完整，2份类native后缀保持未解码。解析采用元素计数、内层tag和导出边界校验；服务实际激活需另核。阅读表见[[03配置/订单与服务/Hitted订单与服务]] |
| E19 | 历史解析失败与缺包分开 | `inventory/followup-gap-classification.json`：旧825条中696条为旧读取器未支持delegate属性tag、129条为native后缀；选当前Grunt／主角296条重试，289条字段边界完整、7条仍仅前缀。内部delegate／native数据仍可不透明；不是289条游戏逻辑已恢复 |

注意：PDB的GetSubType虚槽是+0x70，枚举2为BoundToAnimState；GetBaseType是另一槽+0x28。编译器折叠函数时dumpbin可展示别的共享符号别名，以匹配PDB范围和虚槽共同定位。''')
put(rel,s)
rel='00索引/系统线索与关系图.md';s=(V/rel).read_text(encoding='utf-8')
s=s.replace('stun→结束时刻→新订单计时写入已接通E14；剩HittedDB+0x74消费者和旧订单替换／取消，下一查OrderManager::PlayOrder及Hitted OrderDB','正常无前置Hitted取消／新建与回收已闭合E17；剩+0x74消费者、特殊前置序列／冻结／预测及AI层查询')
s=s.replace('最终连续命中刷新／AI消费许可链未全闭合','正常Hitted替换链已闭合；特殊分支与AI消费许可链未全闭合')
s=s.replace('计时写入已补；继续查旧Hitted替换／取消策略与AI层查询','计时写入及正常Hitted替换已补；继续查具体服务／条件与AI层查询')
s=s.replace('HittedRecoveryAvailability','HitRecoveryAvailability')
s=s.replace('Hitted恢复层、持续状态／恢复订单和AI请求分别核对','Hitted恢复层、持续状态／恢复订单和AI请求分别核对')
s=section(s,'补解包进度入口','''[[00索引/解包与解析进度]]汇总本轮定向提取、字段解析与旧缺口重试。[[03配置/订单与服务/索引]]维护订单默认值与服务配置。

新因素：普通受击替换涉及订单子类型、Running/Pending状态、前置依赖、取消命令与许可层句柄；已合并S01／S03。解析器不支持某类属性tag不等于资源不存在，已列为技术缺口E19，不冒充机制发现。''')
put(rel,s)
g=json.loads((R/'inventory/followup-gap-classification.json').read_text(encoding='utf-8'))
put('00索引/解包与解析进度.md','''# 解包与解析进度

[[00索引/首页|首页]] · [[00索引/系统线索与关系图|系统线索]] · [[03配置/订单与服务/索引|订单配置]]

## 本轮可区分的四个阶段

| 对象／问题 | 已提取 | 已解析 | 已接通逻辑 | 已实战验证 |
|---|---|---|---|---|
| Hitted／HittedGeneric订单 | 2份包，各含uasset／uexp，4文件有SHA | 8份数据默认／子对象完整，全部30／3条服务数组；2份类native后缀未解 | 正常无前置Hitted取消旧动画绑定单、排新单、旧层与服务回收已接通 | 否 |
| Hitted相关服务 | 已有挂载引用，按当前问题补提取 | 完整服务字段与实例覆写见配置表 | 按具体服务逐项核；不能把挂载等同激活 | 否 |
| Grunt默认订单／Avoided与Deflected服务 | 复用已提取订单，按引用补父级／服务 | 以独立分支证据清单记录 | 对上具体Grunt引用和服务条件后才升级为确认 | 否 |
| 招架／AI反击动作 | 复用能力、实际AttackDB与动作，按需补蓝图 | 对象引用与字节码分别记录覆盖范围 | 防反模板分流与AI实际成功动作分别核对 | 否 |

## 历史缺口分类与定向重试

| 项目 | 本轮结果 | 解释边界 |
|---|---|---|
| 原825条解析记录 | 696条旧读取器不支持MulticastInlineDelegateProperty；129条native后缀 | 这是导出／解析记录数，不是825个缺失招式或包 |
| 当前主线相关296条重试 | 289条tagged字段边界完整；7条只解析前缀；其余529条暂不重试 | 内部delegate和原生payload仍可不透明；不称289条逻辑已经破解 |
| 原13条未匹配命中引用 | 7条空行名；6条目标表已提取但行未匹配 | 空行名不补造资源；旧版／测试路径标记后降低优先级；不是13个包未解出 |

本轮不重写旧大集合及其覆盖统计；补充记录见`inventory/followup-gap-classification.json`与`inventory/followup-gap-reparsed-objects.json`。旧目录内资源是否仍实际启用由引用证据决定，不能只凭路径删除或断言废弃。

## 后续执行规则

先查已有产物→定向提取资源及父级／默认对象／直接依赖→验证导出边界→恢复字段／引用→接代码消费者→更新机制、实现与配置。遇到新因素，回写系统线索的作用位置、证据、关联、缺口和优先级。

全部工具与产物继续放SifuResearch；本轮未运行游戏、修改游戏／存档或LIAN。自动检查验证文档与证据完整性，不替代实战。
''')
for rel,title,body in [
 ('00索引/首页.md','补解包研究入口','[[00索引/解包与解析进度]]记录提取／解析／逻辑接通／实战四阶段；[[03配置/订单与服务/索引]]收录新增订单与服务配置。正常无前置Hitted的旧单取消与回收已接通，后续继续核具体Grunt服务、许可与AI选择。'),
 ('03配置/配置索引.md','订单与服务补充','新增[[03配置/订单与服务/索引]]，先收录两份Hitted订单及全部33项服务与实例覆写；新配置按研究引用继续扩展，不把服务类名当作运行结论。')]:
 s=(V/rel).read_text(encoding='utf-8');put(rel,section(s,title,body))
lp=R/'inventory/vault-layout.json';layout=json.loads(lp.read_text(encoding='utf-8'))
for rel in changes:
 if rel not in layout['documents']:layout['documents'].append(rel)
lp.write_text(json.dumps(layout,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
(R/'inventory/followup-unpacking-documents.json').write_text(json.dumps({'updated':datetime.datetime.now().astimezone().isoformat(),'documents':changes,'backup_root':str(B)},ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
print(json.dumps({'updated_notes':len(changes),'vault_notes':len(layout['documents'])},ensure_ascii=True))