"""Publish the developer-oriented state specification; static editorial operation only."""
from pathlib import Path
import datetime, hashlib, json, sys

R = Path(__file__).resolve().parents[1]
V = R / 'Sifu'
S = R / 'notes/reader-sources/20261029-state-spec'
B = R / 'notes/backups/20261029-state-spec-02'
B.mkdir(parents=True, exist_ok=True)
changed = []
managed = set()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(rel, text):
    managed.add(rel)
    p = V / rel
    text = text.rstrip() + '\n'
    if p.read_text(encoding='utf-8-sig') == text: return
    b = B / (sha(p)[:12] + '-' + rel.replace('/', '__'))
    if not b.exists(): b.write_bytes(p.read_bytes())
    p.write_text(text, encoding='utf-8', newline='\n')
    changed.append(rel)
def section(rel, title, body):
    text = (V / rel).read_text(encoding='utf-8-sig')
    marker = '\n## ' + title + '\n'
    if marker in text:
        prefix, rest = text.split(marker, 1)
        n = rest.find('\n## ')
        suffix = rest[n:] if n >= 0 else ''
        text = prefix.rstrip() + '\n' + marker + '\n' + body.strip() + '\n' + suffix
    else: text = text.rstrip() + '\n' + marker + '\n' + body.strip() + '\n'
    save(rel, text)

for source, folder in [('mechanism.md', '01机制'), ('implementation.md', '02实现')]:
    save(folder + '/连续受击与反击追击的系统链.md', (S / source).read_text(encoding='utf-8'))

home = '00索引/首页.md'
text = (V / home).read_text(encoding='utf-8-sig')
start, end = '<!-- readable-rules-20261029:start -->', '<!-- readable-rules-20261029:end -->'
block = start + '\n\n**机制正文：[[01机制/连续受击与反击追击的系统链|战斗状态与事件：系统规格]]。** 以开发者角度定义状态集合、事件接口、转移守卫、字段更新和生命周期。T／D／U／A／C编号贯穿表与图；专题材料用于查配置和证据，不是顺序阅读主线。\n\n' + end
if start in text:
    prefix, rest = text.split(start, 1)
    _, suffix = rest.split(end, 1)
    save(home, prefix + block + suffix)
else:
    title, rest = text.split('\n', 1)
    save(home, title + '\n\n' + block + '\n' + rest)

config = '03配置/受击案例配置对照.md'
text = (V / config).read_text(encoding='utf-8-sig')
text = text.replace('已核对眩晕使用GenericNone；Guard／Parry／Avoid／Dodge许可不在其白名单中，状态移除回收自身上下文', '已核对眩晕配置引用GenericNone；NPC实际选用该上下文时四项许可不允许。其他优先上下文须按有效查询解析；移除只回收自身上下文')
save(config, text)
section(config, '机制规格补充：输入与条件边界', '''[[01机制/连续受击与反击追击的系统链|系统规格正文]]的编号使用下列配置／输入，不另组织玩法问答。

| 输入或常量 | 中文标识 | 对应规则 |
|---|---|---|
| GuardBreak与AlreadyGuardBroken | 本击发生破架势／此前已破架势 | B取前者真且后者假；T2继承倒地次数却要求两者都假，不能用B假代替 |
| ImpactType与FightingState | 本次命中分类／记录的状态类型 | 两套枚举，T0负责映射；Dizzy分别为7／4，不可混用 |
| FImpactResult.m_fInstigatorFreezeDuration | 本次攻击方冻结时长F | 动画时长分支使用A＋F；与Apply入参额外时长τ分开 |
| m_bKeepCurrentStateDuration | 攻击侧保时长分支开关 | D5开启但无旧状态时不回退D7；目标反应侧D6无旧状态才走默认回退 |
| 最高状态搜索常量7,4,3,2,6,8,5,1,0 | 类型查询的固定选择顺序 | 它是本构建代码常量，不是可修改的配置优先级；不删除未被选中的记录 |
| 上下文优先级和允许位 | NPC实际许可查询输入 | 先得到有效上下文输出，再判断动作许可；不是所有状态限制无条件做交集 |

当前原型／命中表具体值仍沿用本页原有保存值，本批未增加或改动配置数值。时长树修订和字段定位见 `notes/20261029-state-spec-refinements.md`。''')

appendices = ['受击硬直与脱离', '敌人如何选择防御', '防反与闪避反击后的追击', '攻击冲击力韧性与伤害', '群体AI与状态反馈', '受击与追击案例']
notice = '> **专题附录。** 当前状态模型和转换条件统一维护在[[01机制/连续受击与反击追击的系统链|系统规格正文]]。本页保留专题数据、案例或历史证据；重复的系统解释以规格编号为准，不作为另一条必读主线。'
for name in appendices:
    rel = '01机制/' + name + '.md'
    p = V / rel
    if not p.exists(): continue
    managed.add(rel)
    text = p.read_text(encoding='utf-8-sig')
    if notice not in text:
        title, rest = text.split('\n', 1)
        save(rel, title + '\n\n' + notice + '\n' + rest)

body = '''本批按用户的开发者学习目标重构为[[01机制/连续受击与反击追击的系统链|战斗状态与事件：系统规格]]，替代上一版“按专题串结论／回答不能一直连”的组织方式。正文定义状态集合、输入事件、T0–T6顺序转移、D1–D9时长条件树、U1–U7更新／退出、A1–A6许可接口及C1–C5上游接口；时序选定前置状态并展开真实守卫。

本次对已有Update／Apply等原始段重新核条件：D5攻击侧keep无旧状态不回退默认；动画分支额外时间是攻击方冻结时间；两个破架势标记分别检查与合取判断不能混同。固定最高状态查询顺序已读当前EXE常量并核对枚举。没有新增全量解包或实战验证。

后续目的改为逐接口恢复系统，而不是答某个连招现象。具体缺口按正文第9节维护：分类器完整树、默认时长内部、动作准入、构造初值、其他调用者、Opened、Tick时间输入和返回标签消费。详细执行见 `notes/handoffs/20261029-机制规格-02.md`；产物清单 `inventory/state-spec-20261029-batch.json`。'''
for rel in ['00索引/研究进度与问题.md', '00索引/解包与解析进度.md']:
    section(rel, '20261029机制规格重构', body)
    text = (V / rel).read_text(encoding='utf-8-sig')
    mark = '当前机制主文：[[01机制/连续受击与反击追击的系统链|战斗状态与事件：系统规格]]；当前恢复范围与缺口见[[' + rel[:-3] + '#20261029机制规格重构]]。'
    if mark not in text:
        title, rest = text.split('\n', 1)
        save(rel, title + '\n\n' + mark + '\n' + rest)
section('00索引/系统线索与关系图.md', '机制规格的接口缺口', '''系统关系的权威定义和守卫统一在[[01机制/连续受击与反击追击的系统链|系统规格正文]]；此页只跟踪展开入口，不替代正文。

| 因素／位置 | 已确定的接口与证据 | 关联与未解部分 | 优先级 |
|---|---|---|---|
| S25／A6 动作准入 | 许可查询和防御评估有静态入口 | 评估结果到实际订单／动作接受的具体谓词；不再以解释固定连打为验收 | 阻塞完整系统接口 |
| S29／D5 时间分支修订 | 攻击侧keep缺状态走0基线并绕过默认计算，目标侧D6另有回退 | GetDuration内部、各调用的τ与冻结时间F分开；底稿state-spec-refinements P3/P4 | 直接关联 |
| S30 Opened附加接口 | T1的部分Apply参数使PushOpenedState被调用 | 完整生命周期和消费者未恢复，不将Opened名称译成已确认动作能力 | 直接关联，非本轮扩查 |
| S31 Tick时间输入 | Tick只消费传入Δt | 全局／角色时间缩放和冻结怎样形成Δt未恢复 | 后续扩展 |
| S28／U1至U7 累计记录 | 两类事件分别遍历当时存在的状态，按精确守卫更新 | 构造初值、其他状态调用者和具体配置变体 | 直接关联 |

证据：`notes/20261029-state-spec-refinements.md`，正文同名接口编号给出下一项必要取证。''')

report = {'batch': '20261029-机制规格-02', 'recorded_at': datetime.datetime.now().astimezone().isoformat(),
          'command': r'D:\Programes\PY\python.exe scripts/build_state_spec_20261029.py',
          'python': sys.version, 'script_sha256': sha(Path(__file__)), 'changed': sorted(set(changed)),
          'sources': [{'path': p.relative_to(R).as_posix(), 'sha256': sha(p)} for p in S.glob('*.md')],
          'outputs': [{'path': (V / rel).relative_to(R).as_posix(), 'sha256': sha(V / rel)} for rel in sorted(managed)],
          'backup_root': str(B), 'runtime_verified': False}
(R / 'inventory/state-spec-20261029-documents.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'changed': len(set(changed)), 'specification': 'Sifu/01机制/连续受击与反击追击的系统链.md'}, ensure_ascii=True))
