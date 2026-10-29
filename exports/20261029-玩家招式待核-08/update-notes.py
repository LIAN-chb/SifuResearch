from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[2]
p=R/'inventory/player-unknown-08-display-evidence.json';d=json.loads(p.read_text(encoding='utf-8'))
for f in d['sources']:d['sources'][f]=hashlib.sha256((R/f).read_bytes()).hexdigest()
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
p=R/'Sifu/03配置/玩家攻击/徒手招式板小样.md';s=p.read_text(encoding='utf-8')
s=s.replace('正背面与上中下段信息收在招式名字后的括号内，未核实仍标待核','正背面及可避方向配置收在招式名字后的括号内；逐段列出下潜／跳避／侧闪，尚不硬归为唯一上中下段')
s=s.replace('轻重快速连按／同时按与Alt映射待核','Alt已核为与普通输入共用的短按松键手势（≤0.2秒），互列同键输入栈兄弟；不能据此翻成轻重快速连按或同时按')
s=s.replace('姿态槽对应正背面、方向手势与任意动作后接入范围均待核对','姿态槽正背面及方向输入组合已静态接通；方向参照与任意动作后接入范围仍待核对')
s=s.replace('exports/20261029-玩家招式图-07/、notes/handoffs/20261029-玩家招式图-07.md','exports/20261029-玩家招式待核-08/、notes/handoffs/20261029-玩家招式待核-08.md').replace('旧01～06版','旧01～07版').replace('当前库内HTML改用07版','当前库内HTML改用08版')
s+='\n本次待核项查询及边界见[[03配置/玩家攻击/招式待核项与已确认信息]]，正背面、输入与可避方向的证据分别保留，不将配置许可写成实测保证。\n'
p.write_text(s,encoding='utf-8')
for name,prefix,text in [
('研究进度与问题.md','玩家招式展示（','玩家招式展示（2026-10-29，08版）：[[03配置/玩家攻击/招式待核项与已确认信息]]已静态核实四象限对应前左／前右／后右／后左并接GetAttackName取槽，图详情标正面／背面／正背通用。短按松键≤0.2秒为普通与Alt共有手势，互列同键输入栈兄弟；长按为同键达到0.2秒。逐段可避配置按Jump1/Duck2/SideLeft4/SideRight8解码，不能直接等同唯一上中下段。具体标签覆写、最终前摇与运行期接招仍留缺口；图布局与数值不变，无实战验证。'),
('解包与解析进度.md','招式图07批','招式图08批（2026-10-29）：[[03配置/玩家攻击/招式待核项与已确认信息]]复用保存树与命中表，补匹配PDB定向类型、EXE反射枚举及调用证据，闭合朝向槽和普通／Alt短按松键、方向组合与长按条件；无新解包。57原节点、33显示节点、63源边、61引用动作及88候选不变，命中数值不改；新增90树内窗口的可避方向解码。具体Tag覆写字节、唯一攻击高度与实测时序未闭合。')]:
 p=R/'Sifu/00索引'/name;s=p.read_text(encoding='utf-8');lines=s.splitlines();assert sum(l.startswith(prefix) for l in lines)==1;p.write_text('\n'.join(text if l.startswith(prefix) else l for l in lines)+'\n',encoding='utf-8')
p=R/'Sifu/00索引/系统线索与关系图.md';s=p.read_text(encoding='utf-8')
s=s.replace('槽0/1／2/3动作不同，条件覆写尚未解','槽0/1正面、2/3背面已由GetAttackName与象限枚举接通；标签条件覆写的具体条目尚未解')
s+='\n玩家招式待核08补充：[[03配置/玩家攻击/招式待核项与已确认信息]]记录朝向四槽、普通与Alt共用短按松键手势／同键输入栈，以及可避方向位。高度分类仍须接具体AvoidMatchCondition，不能把目标部位或强度当攻击上下段；不改变受击主链的实战完成状态。\n'
p.write_text(s,encoding='utf-8')
p=R/'scripts/build_player_readable.py';s=p.read_text(encoding='utf-8')
s=s.replace('具体方向参照、Alt 手势和时间阈值未核实时保留说明','Alt与普通同键共用≤0.2秒短按松键，互为输入栈兄弟，不能当额外轻重组合；具体方向参照和运行期选择仍保留边界')
s=s.replace("index+='## 徒手招式图", "index+=wl(BASE+'/招式待核项与已确认信息','朝向、输入和可避方向的查询结果')+'\\n\\n'\nindex+='## 徒手招式图")
p.write_text(s,encoding='utf-8')
for f in ['notes/handoffs/20261029-玩家招式图-07.md','notes/handoffs/20261028-玩家招式板-02.md']:
 p=R/f;s=p.read_text(encoding='utf-8');s+='\n后续修订：08批已按匹配PDB/代码闭合正背面四槽及普通/Alt共用短按松键，并解码可避方向配置；此前相应待核表述保留历史身份。具体边界见notes/player-unknown-08-quadrant.md、-input.md、-height.md及08交接。\n';p.write_text(s,encoding='utf-8')
