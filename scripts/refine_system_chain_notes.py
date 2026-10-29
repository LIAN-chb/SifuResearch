from pathlib import Path
R=Path(r'E:\ProgrameFiles\SifuResearch');V=R/'Sifu'
repls={
'前置可惩罚配置窗口与之后Dizzy持续时间分开':'前置Avoided订单窗口与之后Dizzy持续时间分开',
'对手实际订单／profile进入退出、延迟命中边界及完整追击许可':'已闭合原攻击者订单保存与倒计时；具体招式引用、外部提前取消及完整追击许可仍待核对',
'两份profile分别列出；计时的实际生效／退出不可直接用字段名补齐':'两份profile分别列出；已找到时长写入原攻击者Avoided订单、按delta倒计时并到零RequestStop；仍可能提前取消',
'GenerateImpact读取此配置，标记AvoidDizzy；状态更新检查该位及SuperDizzy相关条件后施加Dizzy':'成功闪避后在原攻击者安排Avoided订单并保存所选DB；玩家后续命中时，GenerateImpact从受击目标的该订单读回DB，标记AvoidDizzy；满足状态条件后施加Dizzy',
'计时的实际生效／退出不可直接用字段名补齐':'原攻击者Avoided订单消费此计时，到期请求停止；不是Dizzy时长',
'原避免成功到订单保存的桥见底稿最新结论':'FilterHit→原攻击者ScheduleOrderOverAttack→HandleOrderOverAttack(0x19c0590)→PlayOrder(5)，订单保存原结果；Start(0x1ade250)设时长，Update(0x1ae3a30)到零RequestStop',
'否，尚未找到该字段的计时消费者；Dizzy由状态管线及目标ResistanceDB决定':'否；已找到它写入原攻击者Avoided订单，按delta倒计时；之后Dizzy由状态管线及目标ResistanceDB决定',
'需要订单保存／退出与实际反击时间对应':'订单保存与倒计时已闭合；仍需实际招式引用、提前取消及状态时间对应',
'V -. 原攻击者订单保存桥按底稿继续核对 .-> O':'V --> O',
'原攻击者订单保存、期限字段消费和退出；固定Hook与Jab引用':'订单保存与期限消费已闭合；继续固定Hook与Jab实际引用、外部停止和命中当刻SuperDizzy条件',
'S04／S05，固定订单保存与实际命中行；补退出消费者':'S04／S05，闪避订单保存与计时已闭合；继续固定实际命中行、提前取消及状态刷新',
'未解问题已缩到实际命中行／覆写、刷新读取点、profile退出条件及AI最终调度':'未解问题已缩到实际命中行／覆写、刷新读取点、订单提前取消及AI最终调度',
'| E05 | 持续状态时间／伤害／计数退出，影响后续状态与恢复订单 | DefenseComponent状态更新与FFightingStateElement；ApplyFightingStateFromImpact `0x1a46990` |':'| E05 | 持续状态时间／伤害／计数退出，影响后续状态与恢复订单 | UDefenseComponent::TickComponent `0x196a130`、OnDamage `0x1965280`、OnHit `0x19653b0`；ApplyFightingStateFromImpact `0x1a46990` |'
}
paths=[R/'scripts/build_system_chain_notes.py']+[V/x for x in ['01机制/连续受击与反击追击的系统链.md','02实现/连续受击与反击追击的系统链.md','00索引/系统线索与关系图.md']]
for p in paths:
 s=p.read_text(encoding='utf-8-sig')
 for a,b in repls.items():s=s.replace(a,b)
 p.write_text(s,encoding='utf-8',newline='\n')
print('Updated chain and graph with confirmed Avoided-order bridge and timer consumer.')