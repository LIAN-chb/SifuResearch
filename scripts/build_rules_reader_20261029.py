"""Publish readable rules from reviewed Markdown sources; no extraction or game access.

Owns the two integrated reader pages and named additions only. Earlier generators
defer these two pages to these sources as well. Backups are keyed by prior hash.
"""
from pathlib import Path
import datetime, hashlib, json, sys

# Compatibility entry: the developer specification supersedes the former reader essay.
_latest_publisher = Path(__file__).with_name('build_state_spec_20261029.py')
if _latest_publisher.is_file():
    import runpy
    runpy.run_path(str(_latest_publisher), run_name='__main__')
    raise SystemExit(0)

R = Path(__file__).resolve().parents[1]
V = R / 'Sifu'
S = R / 'notes/reader-sources/20261029-rules'
B = R / 'notes/backups/20261029-reader-rules'
B.mkdir(parents=True, exist_ok=True)
changed = []

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def save(rel, text):
    p = V / rel
    text = text.rstrip() + '\n'
    if p.exists() and p.read_text(encoding='utf-8-sig') == text:
        return
    if p.exists():
        b = B / (sha(p)[:12] + '-' + rel.replace('/', '__'))
        if not b.exists():
            b.write_bytes(p.read_bytes())
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8', newline='\n')
    changed.append(rel)

def section(rel, title, body):
    old = (V / rel).read_text(encoding='utf-8-sig')
    marker = '\n## ' + title + '\n'
    if marker in old:
        prefix, rest = old.split(marker, 1)
        n = rest.find('\n## ')
        suffix = rest[n:] if n >= 0 else ''
        text = prefix.rstrip() + '\n' + marker + '\n' + body.strip() + '\n' + suffix
    else:
        text = old.rstrip() + '\n' + marker + '\n' + body.strip() + '\n'
    save(rel, text)

for kind, folder in [('mechanism', '01机制'), ('implementation', '02实现')]:
    rel = folder + '/连续受击与反击追击的系统链.md'
    legacy = S / ('legacy-' + kind + '.md')
    if not legacy.exists():
        legacy.write_bytes((V / rel).read_bytes())
    save(rel, (S / (kind + '.md')).read_text(encoding='utf-8'))

section('03配置/受击案例配置对照.md', '通用规则的字段中文说明', '''[[01机制/连续受击与反击追击的系统链|完整规则主文]] · [[02实现/连续受击与反击追击的系统链|简要实现]]

这里补充读规则所需的中文标识，不新增配置值。前面的普通／进阶数值仍是对应资源保存值，不能当作所有敌人或特殊眩晕的最终值。配置开关与运行中的状态记录分开列。

| 所属对象／字段 | 中文标识 | 在规则中的作用与条件 |
|---|---|---|
| 命中结果 `FImpactResult.m_eGuardType` | 本次防守结果类型 | None／Guard／Deflect分流；后两者跳过普通效果等级／抗性选型，不能用基础推开等级保证穿防 |
| 命中行 `FHitboxDataRow.m_AttackPropertyLevelOverrides` | 按目标状态覆写攻击效果 | 目标状态可能使攻击采用另一组等级；不能只读基础值 |
| 攻击等级 `FAttackPropertyLevel.m_bKeepCurrentStateDuration` | 启用已有状态时间相关处理 | 参与剩余时间阈值降级及部分时长计算路径，不等于每次命中刷新完整时长 |
| 同结构 `m_fKeepCurrentStateThresold` | 保时长检查的剩余时间阈值 | 启用检查、对应状态存在且有限、剩余时间低于阈值时，候选推开／击倒／眩晕可改为普通命中；保留原字段拼写 |
| 同结构 `m_bUseCustomDuration`／`m_fCustomDuration` | 使用自定义状态时长／自定义时长值 | 只有执行到该条件分支时使用，不宣称高于所有特殊子状态或动画分支 |
| 同结构 `m_bUseHitAnimDuration` | 使用受击动画时长 | 参与动画时长分支；动画容器与其他前置条件仍需满足 |
| 目标反应 `FPropertyReaction.m_bAlwayKeepCurrentStateDurationOnHit` | 目标侧的保留已有状态时间开关 | 与攻击侧保时长开关来源不同；实际时长按控制流计算，不通用地取旧时间与新配置的最大值 |
| 目标反应 `m_bHoldDuringStructureBroken` | 与架势崩溃状态保持相关 | 对应分支参考架势崩溃剩余时间／无限标记；不能推广到所有状态 |
| 目标反应中的许可配置 | 该状态附带的动作限制 | 已核对眩晕使用GenericNone；Guard／Parry／Avoid／Dodge许可不在其白名单中，状态移除回收自身上下文 |
| 目标 `FSuperDizzyReaction` | 特殊眩晕反应配置 | 单独提供必需时长、累计伤害和次数上限；不能套普通Dizzy表值 |
| 闪避配置 `UAvoidPropertyDB.m_fAvoidedDuration` | 原攻击者被避开后的反应订单时长 | 写入敌人Avoided订单，不是之后眩晕的时长 |
| 同配置 `m_bAvoidedEnterDizzyOnAttacked` | 反应记录期间受击可进入眩晕 | 后续命中读回此配置，再经其他状态条件；不是闪避成功立即眩晕 |

| 运行中状态 `FFightingStateElement` 的字段 | 中文标识 | 谁更新／谁读取 |
|---|---|---|
| `m_fStateDuration`／`m_fElapsedTime` | 本次持续时长／已过时间 | 新元素经过时间清零；剩余时间查询做两者相减；新持续时长不保证等于初始配置 |
| `m_bPause`／`m_bInfinite` | 暂停自动检查／无限时长标记 | 状态Tick先跳过这些元素的时间和累计阈值检查；伤害／命中通知仍有自己的更新条件，其他显式移除仍可能发生 |
| `m_fMaxAccumulatedDamages`／`m_fAccumulatedDamages` | 累计伤害上限／累计伤害 | 上限大于0时启用；有限且未暂停时，累计严格大于上限会退出状态 |
| `m_iMaxAccumulatedHits`／`m_iAccumulatedHits` | 累计次数上限／累计次数 | 运行状态上限大于等于0时参与退出比较，达到即退出；小于0不启用此退出条件。回调累加另要求上限大于0，不能将0与负数混同 |
| `m_LastAttackName`及归组开关 | 上次攻击名／是否按攻击名归组 | OnHit一路按配置比较攻击名，OnDamage一路不因此去重；重建后的名称初始化仍待核 |
| 状态类型及子状态 | 当前受控类别／类别内的特殊版本 | 同为Dizzy也须区分普通与SuperDizzy，不能只看大类套限额 |

字段／分支来源：`notes/20261029-rules-state-update.md`、`notes/20261029-rules-hit-count.md`、`notes/20261029-rules-resolution.md`；闪避配置来源 `notes/avoid-system-chain.md`。''')

home = '00索引/首页.md'
text = (V / home).read_text(encoding='utf-8-sig')
start = '<!-- readable-rules-20261029:start -->'
end = '<!-- readable-rules-20261029:end -->'
block = start + '\n\n**先读完整规则主文：[[01机制/连续受击与反击追击的系统链]]。** 从一次攻击讲到下一次交互，正文包含状态、时间、累计、动作许可和退出条件，配有双方时序图；无需先逐篇读索引或取证底稿。\n\n' + end
if start in text:
    a, tail = text.split(start, 1)
    _, tail = tail.split(end, 1)
    text = a + block + tail
else:
    title, tail = text.split('\n', 1)
    text = title + '\n\n' + block + '\n' + tail
save(home, text)

body = '''已将规则整理为可独立阅读的[[01机制/连续受击与反击追击的系统链]]，不再以对话说明或底稿代替阅读成果。主文解释一次交互→状态变化→下一次交互，配有双方时序、效果分支和防御恢复判断图；[[02实现/连续受击与反击追击的系统链|简要实现]]及[[03配置/受击案例配置对照#通用规则的字段中文说明|字段中文标识]]同步。

本批是已知证据的阅读整理：未补解包，未产生新的实战结论。普通Hitted到防御实际执行的条件仍是下一项必要取证；状态名称默认初始化和持续性字段消费者保留缺口。旧批次“先对话、不重写阅读篇”是当时错误理解下的执行记录，现已由本批交付纠正。后续整理应直接更新可读产物。

生成源为 `notes/reader-sources/20261029-rules`，脚本为 `scripts/build_rules_reader_20261029.py`；详细执行记录见 `notes/handoffs/20261029-规则阅读整理-01.md`。前段历史优先级以本段为准。'''
for rel in ['00索引/研究进度与问题.md', '00索引/解包与解析进度.md']:
    section(rel, '20261029规则阅读整理交付', body)
    text = (V / rel).read_text(encoding='utf-8-sig')
    current = '最新阅读成果：[[01机制/连续受击与反击追击的系统链|完整规则主文]]；最新整理状态见[[' + rel[:-3] + '#20261029规则阅读整理交付]]。'
    if current not in text:
        title, tail = text.split('\n', 1)
        save(rel, title + '\n\n' + current + '\n' + tail)

section('00索引/系统线索与关系图.md', '规则主文与线索的分工', '''当前完整解释位于[[01机制/连续受击与反击追击的系统链]]；本页继续用于查找证据缺口和展开顺序，不作为读懂主文的前置条件。既有S27–S29已整理进主文，没有新增系统因素。下一项研究仍是S25普通受击的防御实际执行门；阅读整理完成不代表该因果缺口已解决。''')

report = {
    'batch': '20261029-规则阅读整理-01',
    'recorded_at': datetime.datetime.now().astimezone().isoformat(),
    'cwd': str(R), 'python': sys.version,
    'command': r'D:\Programes\PY\python.exe scripts/build_rules_reader_20261029.py',
    'script_sha256': sha(Path(__file__)),
    'changed': changed, 'backup_root': str(B),
    'sources': [{'path': p.relative_to(R).as_posix(), 'sha256': sha(p)} for p in S.glob('*.md')],
    'outputs': [{'path': (V / rel).relative_to(R).as_posix(), 'sha256': sha(V / rel)} for rel in sorted(set(changed))],
    'new_extraction': False, 'runtime_verified': False,
}
(R / 'inventory/reader-rules-20261029-documents.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'changed': len(set(changed)), 'reader_main': 'Sifu/01机制/连续受击与反击追击的系统链.md'}, ensure_ascii=True))
