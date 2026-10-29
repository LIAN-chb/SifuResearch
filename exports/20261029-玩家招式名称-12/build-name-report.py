from pathlib import Path
import json,re,collections,hashlib
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
pairs=json.loads((O/'paired-texts.json').read_text(encoding='utf-8'));skills=json.loads((O/'skill-ui-links.json').read_text(encoding='utf-8'))
all_en={(r['namespace'],r['key']):r for r in json.loads((O/'en.json').read_text(encoding='utf-8'))}
menu=[r for r in pairs if r['namespace']=='ST_UI_MenuCombo' and r['key'].startswith(('Command_','Special_','BaseCombo_'))]
weapons=[r for r in menu if any('_'+x+'_' in r['key'] for x in ['Bat','Blade','Staff'])];bare=[r for r in menu if r not in weapons]
tech=[s for s in skills['skills'] if '/Techniques/' in s['asset'] and '/OLD/' not in s['asset']]
support=[s for s in skills['skills'] if '/Techniques/' not in s['asset'] and '/OLD/' not in s['asset']]
actionNames={'AttackLight':'轻击','AttackHeavy':'重击','AttackLightHold':'长按轻击','AttackHeavyHold':'长按重击','AttackLightFrontFront':'前前轻','AttackHeavyFrontFront':'前前重','AttackHeavyGuard':'防御重击','Disengage':'快速招式输入（Disengage；具体轻重组合本批不据条目名猜测）','DodgeAttack':'闪避攻击输入','HeavyRushAttack':'奔跑重击','Parry':'格挡输入','ParryFromDown':'倒地时格挡输入','PushbackCancel':'推击恢复输入','ThrowContextualObject':'环境投掷输入','PushFromGrab':'抓取后推掷输入'}
def readable(x):
 if not x:return '本项未保存独立输入文字'
 text=x.get('zh-Hans') or x.get('en') or ''
 text=re.sub(r'<action id="([^"]+)"/>',lambda m:actionNames.get(m[1],m[1]),text)
 text=re.sub(r'<[^>]*>','',text)
 return text.replace('•','〔停顿标记〕').strip()
def table(headers,rows):
 clean=lambda x:str(x).replace('|','／').replace('\n',' ')
 return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(clean(x) for x in row)+' |\n' for row in rows)
out='# 《师父》游戏正式招式名查询（简体中文）\n\n2026-10-29。仅供查阅，本批没有将名称填入招式图，也没有改动图的生成脚本。\n\n'
out+='名称主要直接读取本机游戏包 `Localization/Game/zh-Hans/Game.locres`，按相同namespace、key和source hash与英文对照；技能另外追到SkillUIData的Name／Description／Inputs三个文本引用。名称确为游戏随包文本，但旧版／占位／替换招式的可用性另行区分，不把所有文本条目当成当前基础徒手动作。\n\n'
out+='## 先确认你举的例子\n\n**推击对手后接重击：追亡逐北（Chasing Trip Kick）。** 证据是同一技能UI对象的名字和输入字段直接对应，输入原文含`AttackHeavy`与“对被推击的对手”；不是根据变量名翻译。推击后轻击则是**乘胜追击（Chasing Strikes）**。\n\n'
out+='## 已有技能UI直接连接名称与输入的徒手招式\n\n'
out+=table(['官方简中名','官方英文名','技能UI保存的输入说明','名称文本键'],[(s['fields']['Name']['zh-Hans'],s['fields']['Name']['en'],readable(s['fields'].get('Inputs')),s['fields']['Name']['key']) for s in tech])
out+='\n这里的“停顿标记”来自技能输入文字的圆点；具体操作窗口本批不推断。对图中某个前后向变体是否该共用同一官方名，还需按实际动作引用核对；不能仅凭动作很像就套名。\n\n'
out+='## 徒手菜单中的完整命名条目\n\n下表保留游戏菜单文字键，便于区分整套连招与单招；**编码不是已核实的出招顺序**，不凭`YX`等键名推断轻重同时按、快速交替或具体按键。没有武器限定词的条目暂列默认／徒手菜单；菜单蓝图如何排版和显示的全部条件本批未恢复。\n\n'
out+=table(['官方简中名','官方英文名','菜单文字键'],[(r['zh-Hans'],r['en'],r['key']) for r in bare])
out+='\n**“疾风连环”是Light Attacks对应的连招菜单名称，不能由此把每一击都改叫“疾风连环”。“重击”确实也是游戏中的名称，英文为Heavy Attacks。** `碎背肘／正蹬／升龙爪／回旋踢／骤雨连环／神龙摆尾`等按菜单条目区分整套连招标题，不预设都是单节点名字。\n\n'
out+='## 武器菜单中的名称\n\n单独收录，避免混到徒手基础图中。同中文名可能对应不同英文或武器动作，应保留来源键。\n\n'
out+=table(['官方简中名','官方英文名','武器菜单文字键'],[(r['zh-Hans'],r['en'],r['key']) for r in weapons])
out+='\n## 其他技能与专注名称\n\n以下有技能UI直接引用；“专注”与动作技能不当普通连招节点。旧路径另留结构化清单，不混入此表。\n\n'
out+=table(['游戏简中名','英文名','来源文字键'],[(s['fields']['Name']['zh-Hans'],s['fields']['Name']['en'],s['fields']['Name']['key']) for s in support])
cheat=[r for r in pairs if r['namespace']=='UI_Cheats' and r['key'].startswith('Cheat_') and r['key'].endswith('_Title')]
out+='\n## 替换招式名称：单独候选\n\n这些来自游戏的Cheat替换招式标题，不能据此将默认徒手动作改名；同名可能重复，保留键。\n\n'
out+=table(['游戏简中名','英文名','替换招式文字键'],[(r['zh-Hans'],r['en'],r['key']) for r in cheat])
out+='\n## 覆盖与证据\n\n'
out+=f'读取三份本地化文件共388017字节；英文2690条、简中2648条，同键且源hash相同配对{len(pairs)}条。命名菜单条目{len(menu)}条（{len(bare)}条无武器限定、{len(weapons)}条武器限定），去重简中名{len(set(r["zh-Hans"] for r in menu))}个；这不是游戏所有可执行动作的数量。\n\n'
out+='解析现有46个SkillUIData导出的保存字段，28个对象形成81条StringTable文本引用；另28条内联Base文本为14组Name／Description，包含Dummy或旧占位名，单列不拿来补官方招式。输入文字简中缺失的8个条目保留英文原始action标记，不伪造中文本地化。\n\n'
out+='逐项键、二进制偏移、source hash及中英文值见同目录`paired-texts.json`；技能字段到文字键的链见`skill-ui-links.json`；完整查询数据为`name-catalog.json`。菜单映射到33图节点的最终命名尚未验收，本批没有实施。\n\n'
out+='官网仅用于交叉核英文拼写，见[官方1.19/1.20补丁说明](https://www.sifugame.com/news/patch-1-19-1-20-arenas-day-1-patch)和`web-sources.json`。官网没有足够的简中名证据，简中名称以本机官方资源为依据。\n'
(O/'官方招式名称对照.md').write_text(out,encoding='utf-8')
catalog={'menu':menu,'barehands_menu_candidates':bare,'weapon_menu':weapons,'skill_ui':tech,'other_skill_ui':support,'replacement_move_titles':cheat,'limits':['menu key is not by itself confirmed player input','names of full combos are not names of every hit','old paths and dummy UI excluded from active skill table','no changes to graph','per-node mapping not yet accepted']}
(O/'name-catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'menu_entries':len(menu),'barehands_candidates':len(bare),'weapon_entries':len(weapons),'menu_unique_names':len({r['zh-Hans'] for r in menu}),'technique_ui':len(tech),'other_skill_ui':len(support),'replacement_titles':len(cheat)},ensure_ascii=True))
