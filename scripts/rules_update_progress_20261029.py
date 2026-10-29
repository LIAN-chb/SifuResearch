"""Merge the bounded rules batch into progress pages; leave reader chapters intact.

Run after older page generators when rebuilding. Only these named sections are owned here.
"""
from pathlib import Path
import hashlib, json

R = Path(__file__).resolve().parents[1]
V = R / 'Sifu'
B = R / 'notes/backups/20261029-rules-01'
B.mkdir(parents=True, exist_ok=True)
sections = {
    '00索引/研究进度与问题.md': '''本段为本批人工维护状态的生成源，脚本：`scripts/rules_update_progress_20261029.py`。本轮先在对话讲通用规则，不批量改写机制阅读篇；下面的新增底稿不是要求读者逐篇跳读。

| 事项 | 最新状态 |
|---|---|
| 研究单位 | 一次交互的结果判定→状态更新→动作许可→下一次交互；具体案例只用于核证，不再把C01两动作窗口作为先决目标 |
| 已接通 | 防守结果绕过普通效果抗性分支；普通伤害路径的伤害通知→状态更新→命中通知；重复受击的分字段继承；有限未暂停状态的时间／累计退出判断 |
| 重要边界 | 计数不直接等于拳数；新状态elapsed清零不等于完整时长刷新；普通Dizzy与SuperDizzy不能共用限额解释；解除一份状态限制不等于AI立刻执行防御 |
| 仍缺 | 普通Hitted期间，AI防御评估如何通过实际执行门；状态重建后攻击名默认初始化；持续性字段的真正消费者 |
| 下一项必要取证 | 追NPC防御请求到动作启动／订单接受的检查，区分状态禁用、现行动作限制与AI未选择；成功标准是列出通过／拒绝的条件，不求固定拳数 |

证据底稿：`notes/20261029-rules-resolution.md`、`notes/20261029-rules-hit-count.md`、`notes/20261029-rules-state-update.md`；交接：`notes/handoffs/20261029-通用状态规则-01.md`。未实战验证，无需用户操作。''',
    '00索引/解包与解析进度.md': '''本段生成源：`scripts/rules_update_progress_20261029.py`。本批没有重新解包全量资源；复用已提取资产，补充定向PDB类型解析与函数取证。

| 阶段 | 本批实际完成与边界 |
|---|---|
| 已提取 | 复用现有来源包；未增加全量提取，也未覆盖旧资产集合 |
| 已解析 | 核对组件委托与状态字段类型；复用前轮已解析的条件蓝图作为交叉查询证据，未声称本批重新执行 |
| 已接通逻辑 | 普通伤害委托经派生健康组件到状态累计；同一路径先伤害通知、再状态更新、后命中通知；状态更新字段传递和退出检查分工 |
| 失败／限制 | 不带BPF前缀的GetFightingStateTimeLeft不在索引，已保留失败项并转查实际BPF包装；未知字段消费者、全部实例覆写与运行时激活仍缺 |
| 已实战验证 | 无；静态结果不推出固定拳数、最终窗口或自动实战验收 |

清单：`inventory/rules-20261029-count-batch.json`、`inventory/rules-20261029-state-update.json`、`inventory/rules-20261029-batch.json`。当前优先项以[[00索引/研究进度与问题#20261029通用状态规则批次]]为准。''',
    '00索引/系统线索与关系图.md': '''本段生成源：`scripts/rules_update_progress_20261029.py`。合并旧时间／累计／状态覆写因素，新增交互事件的作用位置；不新增假定的防无限连总开关。

| 因素与位置 | 证据及已知作用 | 关联与缺口 | 优先级／回查 |
|---|---|---|---|
| S27 防守结果到效果分类 | ComputeImpactType中GuardType非None时跳过普通效果等级／抗性选型；不能用推开等级证明穿防 | 关联S18攻击覆写与既有抗性；破架势和反馈另有分支 | 直接关联；底稿rules-resolution R01–R03 |
| S28 事件顺序与状态累计（合并既有计数因素） | 普通伤害路径OnDamage→UpdateFightingStateFromImpact→OnHit；前后可能面对不同元素，计数来源和归组策略不同 | 关联同态重建；新元素攻击名默认值仍未核，不换算拳数 | 直接关联；底稿rules-hit-count及rules-state-update |
| S29 状态时长与分字段继承（合并既有时间因素） | 时间来源、累计继承和自动退出分开判断；普通Dizzy与SuperDizzy不同；暂停／无限跳过本段Tick时间和累计检查 | 关联状态退出与许可回收；持续性字段消费者仍缺 | 直接关联；底稿rules-state-update |
| S25普通受击执行门续接 | 既有E23只证明条件性重评估，不能推出此前所有入口禁防 | 继续追AI防御请求→动作／订单接受，定位实际阻止执行的条件 | 阻塞主线；底稿rules-resolution R04／R07 |

以上前三条已接通的关系：防守结果→分类路径；普通伤害通知→状态更新→命中通知；状态退出→回收自身许可。尚待接通：普通Hitted中防御评估→实际动作执行。这里的顺序为已核对分支中的调用顺序，不代表全部命中类型的统一实战帧序。'''
}
changed = []
marker = '\n## 20261029通用状态规则批次\n'
for rel, body in sections.items():
    p = V / rel
    old = p.read_text(encoding='utf-8-sig')
    if marker in old:
        prefix, section = old.split(marker, 1)
        next_heading = section.find('\n## ')
        suffix = section[next_heading:] if next_heading >= 0 else ''
        new = prefix.rstrip() + marker + '\n' + body.strip() + '\n' + suffix
    else:
        new = old.rstrip() + '\n' + marker + '\n' + body.strip() + '\n'
    if new != old:
        digest = hashlib.sha256(p.read_bytes()).hexdigest()[:12]
        backup = B / (digest + '-' + p.name)
        if not backup.exists():
            backup.write_bytes(p.read_bytes())
        p.write_text(new, encoding='utf-8', newline='\n')
        changed.append(rel)
print(json.dumps({'updated': changed, 'reader_chapters_rewritten': False}, ensure_ascii=True))
