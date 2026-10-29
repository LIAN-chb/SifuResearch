from pathlib import Path
R=Path(__file__).resolve().parents[2]
p=R/'Sifu/03配置/玩家攻击/徒手招式板小样.md'
s=p.read_text(encoding='utf-8')
s=s.replace('属性移入抽屉，按原招式配置','属性置于抽屉最上方，前摇配置帧与距离各占一行；正背面与上中下段信息收在招式名字后的括号内，未核实仍标待核。每个命中段分两行：第一行是倒地／推退／眩晕、攻击强度和韧性比较覆盖；第二行是可招架字段和推距。点击画布空白关闭详情，拖动画布保持打开。按原招式配置')
s=s.replace('20261029-玩家招式图-06','20261029-玩家招式图-07').replace('旧01～05版','旧01～06版').replace('当前库内HTML改用06版','当前库内HTML改用07版')
p.write_text(s,encoding='utf-8')
updates={
'研究进度与问题.md':'玩家招式展示（2026-10-29，07版）：[[03配置/玩家攻击/徒手招式板小样]]保留06格位编辑、自动保存及全部图关系；详情改为属性置顶，前摇与距离独立成行，正背面／攻击高度信息在名字后括号内（仍待核），每段反应／强度／韧性和招架／推距分两行。点击画布空白关闭详情，平移不误关。33图节点与03数据保持一致，无新机制或实战结论。',
'解包与解析进度.md':'招式图07批（2026-10-29）：[[03配置/玩家攻击/徒手招式板小样]]只调整详情排版和空白关闭交互，保留06格位与保存；正背面／攻击高度仍待核。结构化配置仍与03完全一致；57原节点、33显示节点、63源边、21默认输入、16情境边、61引用动作及88树外候选不变，无新解包、代码取证或实战验证。'}
for name,new in updates.items():
 p=R/'Sifu/00索引'/name
 lines=p.read_text(encoding='utf-8').splitlines()
 prefix='玩家招式展示（' if name.startswith('研究') else '招式图06批'
 assert sum(line.startswith(prefix) for line in lines)==1
 p.write_text('\n'.join(new if line.startswith(prefix) else line for line in lines)+'\n',encoding='utf-8')
