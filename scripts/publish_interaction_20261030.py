"""Publish navigation and dated evidence updates; preserve generated authoring sources."""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];B=R/'notes/backups/20261030-攻防补证-02';changed=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(rel,text):
 p=R/rel;old=p.read_text(encoding='utf-8-sig')
 if old==text:return
 b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():b.write_bytes(p.read_bytes())
 before=sha(p);p.write_text(text,encoding='utf-8',newline='\n');changed.append(dict(path=rel,before_sha256=before,after_sha256=sha(p)))
def append(rel,heading,body):
 p=R/rel;s=p.read_text(encoding='utf-8-sig');block='\n## '+heading+'\n\n'+body.strip()+'\n'
 marker='\n## '+heading+'\n'
 if marker in s:
  pre,rest=s.split(marker,1);n=rest.find('\n## ');post=rest[n:] if n>=0 else '';s=pre.rstrip()+'\n'+block+post
 else:s=s.rstrip()+'\n'+block
 save(rel,s)
topic='玩家进攻与敌人状态转换调查'
layoutpath='inventory/vault-layout.json';a=json.loads((R/layoutpath).read_text(encoding='utf-8'))
for rel in ['01机制/'+topic+'.md','02实现/'+topic+'.md','03配置/攻防交互补证配置.md']:
 if rel not in a['documents']:a['documents'].append(rel)
if topic not in a['topics']:a['topics'].append(topic)
save(layoutpath,json.dumps(a,ensure_ascii=False,indent=2)+'\n')
append('Sifu/00索引/首页.md','攻防理解调查（2026-10-30）','[[01机制/'+topic+'|玩家进攻与敌人状态转换调查]]对应六组攻防疑问，补入特殊眩晕gauge、攻击期Counter_Hit、预测／当前防御许可、墙撞命中与倒地累计样本；[[03配置/攻防交互补证配置|配置对照]]和[[02实现/'+topic+'|实现证据]]随文可查。未实战，普通Hitted的最终防御执行时序仍保留缺口。')
progress='''阅读报告：[[01机制/玩家进攻与敌人状态转换调查]]；对应[[02实现/玩家进攻与敌人状态转换调查|实现]]及[[03配置/攻防交互补证配置|配置]]。

- 新静态链：SuperDizzy gauge的加量、阈值预测、冷却恢复、进入后重设与AI难度参数来源；Counter_Hit从攻击订单启动至收招／停止清理；防御请求预测许可与节点当前许可；墙撞服务向受推角色／碰撞物体分别提交命中。
- 配置核对：Grunt Base/Adv倒地伤害阈值-1（禁用）、次数2、归组false、Movement时长4；次数与时长均非最终实战拳数／时间。
- 新取证9组42份反汇编输出并核哈希；没有新增全量提取、游戏运行或实战验收。
- 下一步先追普通Hitted现场有效上下文到最终订单接受，再查各敌人实际特殊眩晕难度覆写、近墙Close消费者与派生碰撞服务挂载／BP实现；同时命中的额外规则仍未知。旧“gauge完全未接通／Counter_Hit入口未定位”边界以本段及报告的已恢复子链为准，未声称全部消费者穷尽。

执行与失败记录：`notes/handoffs/20261030-攻防补证-02.md`；输入／输出证据索引 `inventory/interaction-20261030-batch.json`。'''
append('Sifu/00索引/研究进度与问题.md','20261030攻防补证与调查报告',progress)
append('Sifu/00索引/解包与解析进度.md','20261030攻防补证阶段', '''| 阶段 | 本批结果 |
|---|---|
| 已提取 | 复用已有包，不新增全量或定向提取 |
| 已解析 | 补读有界PDB布局、嵌套许可结果字段；核对已有四份倒地配置与墙撞行，具体敌人gauge难度覆写仍缺 |
| 已接通逻辑 | gauge／Counter_Hit／防御两次许可查询／墙撞服务命中递交子链，见[[01机制/玩家进攻与敌人状态转换调查|报告]]；不等于完整动作准入及全部碰撞派生实现 |
| 已实战验证 | 无；配置参数不是保证拳数或最终时长 |

42份新增有界反汇编输出已核哈希；原始清单在 `inventory/interaction-20261030-batch.json`。旧解析失败集合未重跑；本批无需全量补解包，下一步以[[00索引/研究进度与问题#20261030攻防补证与调查报告|本批断点]]为准。''')
append('Sifu/00索引/系统线索与关系图.md','20261030攻防补证因素','''| 因素／作用阶段 | 已接通关系 | 剩余边界 |
|---|---|---|
| SuperDizzy gauge | 本击量→gauge；分类前预测满量；冷却后按速率恢复；推入特殊眩晕后重设 | 各敌人难度覆写、全分类真值表与反馈双路情况 |
| Counter_Hit攻击窗口 | 正式攻击订单Push；release阶段或停止Pop；当前状态抗性参与后续命中 | 不等于同时命中特判；具体订单子类和实际最高状态另核 |
| 预测／当前防御许可 | CanApplyDefenseRequest读预测，节点Apply读当前；最高状态门与移动检查仍存在 | 普通Hitted有效层时序到订单实际接受未闭合 |
| 墙撞新命中 | collision service默认选受推角色DB墙撞行；分别对受推角色和碰撞对象递交HandleImpact | 具体服务挂载／BP覆盖、近墙Close与最终状态 |
| 倒地累计配置 | Grunt Base/Adv伤害阈值禁用、次数2；由状态事件与Tick消费 | 不可换算必打两拳或固定倒地4秒 |

[[01机制/玩家进攻与敌人状态转换调查|调查正文]]与[[02实现/玩家进攻与敌人状态转换调查|证据定位]]。''')
notice='> **2026-10-30 后续补证：** [[01机制/玩家进攻与敌人状态转换调查|攻防调查报告]]补入SuperDizzy积累与恢复、Counter_Hit攻击订单入口、预测／当前防御许可及墙撞子链。本篇原接口缺口按该报告缩小范围；未解决项仍保留，不视为完整系统已恢复。\n\n'
for source,folder in [('mechanism.md','01机制'),('implementation.md','02实现')]:
 for rel in ['notes/reader-sources/20261029-state-spec/'+source,'Sifu/'+folder+'/连续受击与反击追击的系统链.md']:
  s=(R/rel).read_text(encoding='utf-8-sig')
  if notice not in s:
   title,rest=s.split('\n',1);save(rel,title+'\n\n'+notice+rest.lstrip('\n'))
# Preserve historical conclusions but make later corrections visible at their original entry.
audit='notes/20261030-攻防理解核对.md';s=(R/audit).read_text(encoding='utf-8-sig')
marker='> 后续调查修订（2026-10-30）'
if marker not in s:
 title,rest=s.split('\n',1);save(audit,title+'\n\n'+marker+'：本稿是补证前的核对记录。SuperDizzy积累／恢复、Counter_Hit入口、预测／当前许可和墙撞消费者已由[后续调查](../Sifu/01机制/玩家进攻与敌人状态转换调查.md)推进；原B／C／F相应“未恢复”范围以新报告为准，原始判断保留历史身份。\n'+rest)
append('notes/retrospectives/0005-先核接口this再追播放倍率.md','20261030攻防补证复用','''本次复用同构建public虚表→PE槽→短getter／匹配枚举→调用实参→字段布局的方法，闭合节点GetInputAction与AFightingCharacter::IsAvailable，并把两份缓存映射到嵌套m_Prediction／m_Current。函数折叠导致dumpbin标签可属于另一函数，不能按显示标签命名。OrderAttackInterface+0x60也由16批public定位后重读当前PE，确认为GetAttackState。

代表性失败：第一轮只搜无基类后缀的AFightingCharacter虚表未命中，改搜实际public发现AActor主表，不能把未命中当成无该接口。类型读取继续复用内存LF_ONEMETHOD固定宽度修正。背景分支额度中断后，保留输出并核哈希，仅补跑缺少可复现适配脚本的七类型读取；没有为恢复会话重跑所有解包。证据 `inventory/interaction-20261030-batch.json` 及 `notes/20261030-攻防补证-defense.md`。仍限本构建，未记录完整耗时成本，未实战。''')
append('notes/tool-capabilities.md','20261030攻防补证复用边界','''本批复用PDB public虚表槽与PE定点读取，交叉核输入动作及接口this，见 `inventory/interaction-20261030-counter-slot.json`、`inventory/interaction-20261030-defense-character-slot.json`。同址函数折叠时，dumpbin标题不能单独决定语义，须结合所属vtable、PDB符号及枚举。嵌套字段布局可区分预测与当前结果；不能仅靠布尔实参猜缓存用途。七类型复现脚本 `scripts/interaction_20261030_dizzy_types.py` 仅应用已知格式适配，非新通用解析器；复盘0005追加实际案例。''')
out=R/'inventory/interaction-20261030-publication.json'
out.write_text(json.dumps(dict(command='D:/Programes/PY/python.exe scripts/publish_interaction_20261030.py',script_sha256=sha(Path(__file__)),backup=str(B),changed=changed,source_policy='Manual new report; existing state-spec notice synchronized to authoring sources; no bulk catalog generation.'),ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(changed=len(changed)),ensure_ascii=False))
