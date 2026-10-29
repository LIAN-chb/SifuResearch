from pathlib import Path
import re
R=Path(r'E:\ProgrameFiles\SifuResearch');V=R/'Sifu'
p=V/'00索引/系统线索与关系图.md';s=p.read_text(encoding='utf-8').replace('\n\n| S18','\n| S18');p.write_text(s,encoding='utf-8',newline='\n')
p=V/'01机制/防反与闪避反击后的追击.md';s=p.read_text(encoding='utf-8');tail='## 不同配置查表'+s.split('## 不同配置查表',1)[1] if '## 不同配置查表' in s else ''
s='''# 防反与闪避反击后的追击

[[00索引/首页|首页]] · [[02实现/防反与闪避反击后的追击|简要实现]] · [[01机制/连续受击与反击追击的系统链|综合场景说明]]

你的实测是“敌人被防反、闪避反击后，能稳定吃下一些连招”。本轮已接通闪避后的特定可惩罚链，并确认招架有多种反馈分支；尚未完整解释每种招架和每套连招的最终恢复时间。

| 场景 | 当前静态确认 | 不能推广的内容 |
|---|---|---|
| 成功闪避 | 来袭攻击的DizzyOnAvoid可选特殊AvoidDB；结果存入原攻击者Avoided订单 | 同一敌人的所有招式并不都带这个标记 |
| 及时反击命中 | 受击目标的GenerateImpact读取该Avoided订单DB；符合条件才标AvoidDizzy并进入Dizzy | 成功闪避本身不直接施加长眩晕；SuperDizzy等gate仍参与 |
| 两种时间 | MainChar_Avoid_AvoidPunishable配置0.666秒，MainChar_Attack_AvoidPunishable配置0.5秒；已找到写入原攻击者Avoided订单并倒计时到零请求停止 | 这是特定反应订单的配置时长，不能当作后续Dizzy或整套连招的时长；外部取消可能提前结束 |
| 招架反馈 | 允许且将破架势时有独立反馈；CanDeflect且来袭DizzyOnParry时有ParryDizzy模板命中 | 普通Grunt原始20行DizzyOnParry为false；尚需核对实际动作引用及缓存覆写，不能把所有招架说成该模板 |
| 后续追击与结束 | 普通硬直、持续状态限制、恢复动作层和AI防御选择各有规则 | 恢复许可不等于AI立即格挡；不能写成统一关闭防御若干秒 |

进入Dizzy后，后续攻击仍走共有的命中、抗性、状态更新和恢复管线。普通／进阶的Dizzy限制不同，而相关抗性矩阵相同。完整对照、固定姿态／命中段及最小实战设计见[[01机制/连续受击与反击追击的系统链]]；剩余缺口按优先级记录在[[00索引/系统线索与关系图]]。

本轮没有运行游戏；以上是本机代码与配置支持的条件路径，不是新增实战结论。

'''+tail
p.write_text(s,encoding='utf-8',newline='\n')
p=V/'02实现/防反与闪避反击后的追击.md'
p.write_text('''# 防反与闪避反击后的追击

[[01机制/防反与闪避反击后的追击|机制说明]] · [[02实现/连续受击与反击追击的系统链|综合实现与证据编号]]

| 路径 | 最短执行链 | 详细入口 |
|---|---|---|
| 闪避选配置 | FilterHit→GetActiveAvoidMatchingAttack→来袭DizzyOnAvoid→特殊AvoidDB→FHitDefenseResult | 综合实现E10；notes/avoid-system-chain.md |
| 原攻击者保存反应窗口 | ScheduleOrderOverAttack→HandleOrderOverAttack→PlayOrder(Avoided=5)；DB duration写入订单；OnUpdate到零RequestStop | 综合实现E11；同一底稿中订单／计时表 |
| 后续反击命中 | 目标GenerateImpact查其Avoided订单→取原DefenseResult的AvoidDB→AvoidDizzy；状态更新在gate通过时施加Dizzy | 综合实现E11；不是本次反击直接复用原HitResult，也不是原防守者成为Dizzy目标 |
| 招架 | OnHitDefense→按破架势／DizzyOnParry选择不同模板→原攻击者GenerateImpact/ApplyImpact | 综合实现E08/E09；notes/parry-system-chain.md；能力CDO与模板引用已核对 |
| 追击结束与AI | 持续状态与Hitted计时／恢复层分开；AI仍经预测、状态、测试序列、记忆和候选验证选择防御 | 综合实现E03–E07；notes/recovery-system-chain.md |

精确RVA、构建哈希、资源版本和当前缺口集中在综合实现篇，避免本主题复制后与主线失步。没有启动运行时操作。
''',encoding='utf-8',newline='\n')
# Obsidian tables require escaped alias separators.
changed=[]
for rel in ['00索引/首页.md','00索引/研究进度与问题.md','00索引/系统线索与关系图.md','01机制/连续受击与反击追击的系统链.md','02实现/连续受击与反击追击的系统链.md','01机制/防反与闪避反击后的追击.md','02实现/防反与闪避反击后的追击.md']:
 p=V/rel;s=p.read_text(encoding='utf-8');out=[]
 for line in s.splitlines():
  if line.startswith('|'):line=re.sub(r'\[\[([^\]\n]*?)(?<!\\)\|([^\]\n]*?)\]\]',lambda m:'[['+m[1]+'\\|'+m[2]+']]',line)
  out.append(line)
 p.write_text('\n'.join(out)+'\n',encoding='utf-8',newline='\n');changed.append(rel)
print('Refined current topic pages and table alias escaping:',len(changed))