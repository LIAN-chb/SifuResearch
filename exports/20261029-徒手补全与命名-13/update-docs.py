from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
p=R/'scripts/build_player_board.py';s=p.read_text(encoding='utf-8')
needle="(vault_html.parent/'徒手专注.html').write_text(focus_html,encoding='utf-8')"
s=s.replace(needle,needle+"\n(OUT/'徒手招式板.html').write_bytes(vault_html.read_bytes())\n(OUT/'徒手专注.html').write_text(focus_html,encoding='utf-8')")
s+='''
# Human-readable coverage is generated from the same identity mapping as the tooltips.
by_display={n['id']:n for n in data['graph']['nodes']}
note='# 徒手节点覆盖核对\\n\\n[[03配置/玩家攻击/徒手招式板小样|图的使用说明]] · [[03配置/玩家攻击/阅读入口|阅读入口]]\\n\\n'
note+='[打开徒手招式图]('+vault_html.as_uri()+') · [打开徒手专注]('+(vault_html.parent/'徒手专注.html').as_uri()+')\\n\\n'
note+='13版保留原33个连招位置及全部63条源边，补入抓取后推掷、攻击倒地对手、倒地格挡反击3个独立能力入口，共36节点。独立入口暂未接通与普通节点的具体边，未伪造连线。原布局恢复时保留旧节点格位，新节点补入空格；新增前JSON另存浏览器备份。\\n\\n'
note+='名称气泡按下表的官方菜单身份对应；整套连招名有范围说明，不代表其中每击有独立官方名。没有找到独立名的节点明确采用操作称呼。\\n\\n| 官方菜单名称 | 图中位置／操作称呼 |\\n|---|---|\\n'
for r in data['completeness']['menuCoverage']:
    note+='| '+r['name']+' | '+'、'.join(by_display[i]['label'] for i in r['nodes'])+' |\\n'
note+='\\n徒手专注另页包含'+ '、'.join(f['name'] for f in focusSource['nodes'])+'，各自列消耗与覆盖命中表。实际弱点对象的m_Name直接指向FocusNames；不能拿旧技能UI的解除武器名套给戳眼。敌人可覆盖参数，表行不是动画整段最终总效果。专注结束的动作许可／具体跟进尚未恢复，未画推测后续边。\\n\\n'
note+='条件Map已对57原节点完全读取，21非空、57条件条目全部为Attack.Modifiers替换设置，引用70动作，其中51来自先前88树外候选。它们留在原节点的替换配置证据，不作默认新增节点。其余37候选含21旧版、10特殊、6常规；六常规在既有tagged属性范围未查到入口，仍留覆盖审计，不因文件存在就加点。\\n\\n'
note+='证据底稿：notes/player-completeness-13-conditional.md与notes/player-completeness-13-actions.md；批次数据／验证在exports/20261029-徒手补全与命名-13/。未运行游戏，不宣称完整穷尽所有运行期动作。\\n'
(ROOT/'Sifu/03配置/玩家攻击/徒手节点覆盖核对.md').write_text(note,encoding='utf-8')
'''
p.write_text(s,encoding='utf-8')
p=R/'scripts/player_graph_template.html';s=p.read_text(encoding='utf-8')
s=s.replace("c.savedNodes+'个保存节点收纳为'+G.nodes.length+'个图节点；'", "c.savedNodes+'个保存节点收纳为'+G.nodes.filter(n=>!n.action).length+'个连招图节点，另补'+G.nodes.filter(n=>n.action).length+'个独立动作节点；'")
s=s.replace("document.addEventListener('keydown',e=>{if(e.key==='Escape')setHelp(false);});", "document.addEventListener('keydown',e=>{if(e.key==='Escape'){setHelp(false);hideTooltip();}});")
p.write_text(s,encoding='utf-8')
p=R/'scripts/build_player_readable.py';s=p.read_text(encoding='utf-8')
s=s.replace("BOARD_LINK='", "FOCUS_LINK='[在浏览器打开徒手专注（HTML）]('+(V/BASE/'招式板/徒手专注.html').as_uri()+')'\nBOARD_LINK='")
s=s.replace("57个保存节点收纳为33个图节点，63条连接与21类默认输入保留。共线只合并视觉显示，不新增招式关系；方向通用接入以用户观察虚线区分。朝向、Alt手势及条件覆写仍待核。", "57个保存节点收纳为33个连招节点，另补3个独立能力入口；63条源连接与21类默认输入保留。官方名见悬浮气泡，详情保留操作称呼及配置差异；条件替换已解码但不作为默认新增节点。")
s=s.replace("index+='## 徒手招式图", "index+=FOCUS_LINK+'：左上角可切换徒手图／专注；'+wl(BASE+'/徒手节点覆盖核对','节点与官方名覆盖核对')+'。\\n\\n'\nindex+='## 徒手招式图")
s=s.replace("text+='\\n'+BOARD_LINK+", "text+='\\n'+FOCUS_LINK+'。\\n'+BOARD_LINK+")
p.write_text(s,encoding='utf-8')
p=R/'Sifu/03配置/玩家攻击/徒手招式板小样.md';s=p.read_text(encoding='utf-8')
s+='\n13版：[[03配置/玩家攻击/徒手节点覆盖核对]]维护25条徒手菜单名称对应。原33连招节点保留，补3独立能力入口；每个节点悬浮显示官方名称或明确操作称呼，详情同时保留两者和具体技能名，整套连招标题标明范围。左上角切换徒手图／徒手专注，后者5项按实际FocusNames名称和覆盖命中配置展示，具体后续未接通。旧33节点布局自动恢复并备份，新增节点安排在空格；两页布局分别保存，不用重新导出才能持续保存。\n'
s=s.replace('条件攻击覆写未完整解码','徒手条件攻击覆写已完整解为替换设置；具体运行期启用仍未全部验证')
p.write_text(s,encoding='utf-8')
p=R/'Sifu/03配置/玩家攻击/招式待核项与已确认信息.md';s=p.read_text(encoding='utf-8')
s=s.replace('已核选择函数，具体Tag→动作条目仍未解码；轻击第1段存在非空覆写，基础显示不是最终版本保证','13批已解57条件条目，全部是Attack.Modifiers替换设置，具体Tag和四槽资产见本批证据；不混入默认图，运行期启用顺序仍待验证')
s+='\n13批修订：[[03配置/玩家攻击/徒手节点覆盖核对]]已补独立动作入口、官方名称与徒手专注。旧“条件Map具体条目未解码”由本批有界读取取代；机制的运行期效果仍未实测。\n'
p.write_text(s,encoding='utf-8')
for name,prefix,new in [('研究进度与问题.md','玩家招式展示（','徒手图13版（2026-10-29）：[[03配置/玩家攻击/徒手节点覆盖核对]]保留33连招节点并补3独立能力入口，25菜单名逐项关联、气泡和详情显示官方名及整套连招范围。徒手专注另页5项，左上角切换。旧节点格位保留、两页保存隔离；没有已核边的补充动作／专注不画猜测线。'),('解包与解析进度.md','招式图08批','徒手补全13批（2026-10-29）：复用原包有界读取，57节点条件Map完全消费，21非空57条全为替换设置；定位3独立能力入口和5徒手专注弱点对象，25菜单名对应已检查。无新增游戏写入或实战，仍保留6常规候选入口及专注后续缺口，详见[[03配置/玩家攻击/徒手节点覆盖核对]]。')]:
 p=R/'Sifu/00索引'/name;lines=p.read_text(encoding='utf-8').splitlines();i=next(i for i,l in enumerate(lines) if l.startswith(prefix));lines[i:i+1]=[lines[i],'',new];p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
p=R/'Sifu/00索引/系统线索与关系图.md';s=p.read_text(encoding='utf-8')
s=s.replace('标签条件覆写的具体条目尚未解','标签条件覆写的57条已解为替换设置，运行期启用仍待核')
s+='\n徒手13批：[[03配置/玩家攻击/徒手节点覆盖核对]]补独立Ability动作入口与专注VitalPointData链。专注的实际m_Name到FocusNames、覆盖命中表已接通；结束后的许可／普通连招跟进仍是具名缺口，不能据未查到ComboTree边断言不能衔接。\n';p.write_text(s,encoding='utf-8')
p=R/'Sifu/项目工作流与规则.md';s=p.read_text(encoding='utf-8');s+='\n徒手命名进入[ADR-0008](../adr/0008-补全徒手节点并应用名称标注.md)执行阶段：官方名用于气泡和详情，保留操作称呼；专注另页，补点与连线分别按证据验收。\n';p.write_text(s,encoding='utf-8')
p=R/'inventory/vault-layout.json';d=json.loads(p.read_text(encoding='utf-8'));d['documents']=sorted(set(d['documents']+['03配置/玩家攻击/徒手节点覆盖核对.md']));p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
