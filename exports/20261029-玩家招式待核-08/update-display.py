from pathlib import Path
import json,hashlib,shutil
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
files=['scripts/build_player_readable.py','inventory/player-readable-catalog.json','inventory/knowledge-vault-verification.json','Sifu/03配置/玩家攻击/徒手招式板小样.md','Sifu/00索引/研究进度与问题.md','Sifu/00索引/解包与解析进度.md','Sifu/00索引/系统线索与关系图.md']
catalog=json.loads((R/'inventory/player-readable-catalog.json').read_text(encoding='utf-8'))
files += ['Sifu/'+p for p in catalog['documents']]
for f in files:
 p=O/'backup'/f;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(R/f,p)
types=json.loads((R/'inventory/player-unknown-08-quadrant-types.json').read_text(encoding='utf-8'))
quad=next(x for x in types['layouts'] if x['name']=='EQuadrantTypes')
heights=json.loads((R/'inventory/player-unknown-08-height-enums.json').read_text(encoding='utf-8'))
avoid={str(r['references'][0]['next_int64']):r['name'].split('::')[-1] for r in heights['rows'] if r['name'].startswith('EAvoidableDefenseMatrix::')}
evidence={'quadrants':{str(f['value']):f['name'] for f in quad['fields']},'avoidBits':avoid,'sources':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['inventory/player-unknown-08-quadrant-types.json','inventory/player-unknown-08-height-enums.json','inventory/player-unknown-08-input-evidence.json']},'limits':['quadrants relative to body/pelvis and target, not camera','avoid bits are saved permissions; match conditions remain','input short-release gesture shared by normal and Alt; contextual stack selection','final startup timing not measured']}
(R/'inventory/player-unknown-08-display-evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2),encoding='utf-8')
p=R/'scripts/build_player_board.py';s=p.read_text(encoding='utf-8').replace('20261029-玩家招式图-07','20261029-玩家招式待核-08')
s=s.replace("'轻击变体（手势待核）'","'短按轻击松开·变体'").replace("'重击变体（手势待核）'","'短按重击松开·变体'")
s=s.replace("data['graph']=build_graph(data)","data['research']=read('inventory/player-unknown-08-display-evidence.json')\ndata['graph']=build_graph(data)")
s=s.replace("'exports/player-field-labels.json']","'exports/player-field-labels.json','inventory/player-unknown-08-display-evidence.json']")
s=s.replace('start labels/Alt gestures/orientation need verification','Alt shares short-release gesture with normal input; contextual stack selection applies; quadrant mapping confirmed; attack height classification remains unverified')
p.write_text(s,encoding='utf-8')
p=R/'scripts/player_graph_template.html';s=p.read_text(encoding='utf-8')
at=s.index('function variant(')
helpers='''const quadrantNames={FrontLeft:'前左',FrontRight:'前右',BackRight:'后右',BackLeft:'后左'};
function orientation(slots){const names=(slots||[]).map(i=>DATA.research.quadrants[i]);return names.length===4?'正背通用':names.length&&names.every(n=>n?.startsWith('Front'))?'正面':names.length&&names.every(n=>n?.startsWith('Back'))?'背面':'朝向未接通';}
function avoidDirections(w){const mask=w.raw['m_iAvoidableDefenseMatrix[0]'];if(!Number.isInteger(mask))return '未保存';const labels={Jump:'跳避',Duck:'下潜',SideLeft:'左侧闪',SideRight:'右侧闪'},known=Object.entries(DATA.research.avoidBits).filter(([v])=>Number(v)>0),parts=known.filter(([v])=>mask&Number(v)).map(([,n])=>labels[n]||n),bits=known.reduce((a,[v])=>a|Number(v),0);if(mask&~bits)parts.push('未知位 '+(mask&~bits));return parts.join('／')||'无这些方向';}
function avoidSummary(ws){const dirs=[...new Set(ws.map(avoidDirections))];return dirs.length===1?'可避配置：'+dirs[0]:dirs.length?'各段可避方向不同':'无命中段';}
function nodeOrientation(n){return [...new Set(n.configs.flatMap(k=>DATA.nodes[k].variants.map(v=>orientation(v.slots))))].join('／')||'朝向未接通';}
'''
s=s[:at]+helpers+s[at:]
s=s.replace("esc(name)+'（正背面待核／上中下段待核）'","esc(name)+'（'+esc(orientation(v.slots))+'；'+esc(avoidSummary(ws))+'）'")
# The literal heading is followed immediately by </h4>, so replace independently.
s=s.replace("esc(name)+'（正背面待核／上中下段待核）</h4>'","esc(name)+'（'+esc(orientation(v.slots))+'；'+esc(avoidSummary(ws))+'）</h4>'")
s=s.replace("+'；推距 '+met(w.push)+'。</p>","+'；推距 '+met(w.push)+'。</p>")
s=s.replace("'<div class=\"hit-properties\"><p>段'","'<p class=\"muted avoid-directions\">段'+(j+1)+'可避方向（配置）：'+esc(avoidDirections(w))+'</p><div class=\"hit-properties\"><p>段'")
s=s.replace("?'（正背面待核／上中下段待核）':''", "?'（'+nodeOrientation(byId.get(selected))+'）':''")
s=s.replace("let content='<h3>招式属性</h3>';", "let content='<h3>招式属性</h3><p class=\"muted\">正背相对身体／骨盆与目标。可避方向是配置许可，还需闪避匹配；目前不把它硬归为唯一上／中／下段。</p>';")
s=s.replace("+'</details>'+relations;", "+'</details>'+relations+'<details open><summary>输入手势已核查</summary><p class=\"muted\">短按轻击／重击后在0.2秒内松开。普通输入与变体输入使用同一手势，变体选择还受输入栈及动作许可影响；并非额外一套搓招，也不能据Alt名称判为轻重同时按。长按配置同键达到0.2秒，实际生效仍取决于当前许可。</p></details>';")
s=s.replace('正背面槽位、上中下段、Alt与快速连按／同时按、条件攻击覆写，均未用字段名猜成确定玩法。','正背面四槽与短按松键已由静态证据确认；唯一上中下段分类、轻重连按／同时按的具体招式、标签覆写的具体资源仍有缺口。各命中段显示已核可避方向配置。')
p.write_text(s,encoding='utf-8')
p=R/'scripts/verify_player_board.py';s=p.read_text(encoding='utf-8').replace('20261029-玩家招式图-07','20261029-玩家招式待核-08')
old="check('layout editor does not alter board data',d==json.loads((R/'exports/20261029-玩家招式图-03/board-data.json').read_text(encoding='utf-8')))"
new="""prior=json.loads((R/'exports/20261029-玩家招式图-03/board-data.json').read_text(encoding='utf-8'))
prior=json.loads(json.dumps(prior,ensure_ascii=False).replace('轻击变体（手势待核）','短按轻击松开·变体').replace('重击变体（手势待核）','短按重击松开·变体'))
check('only researched labels and evidence added; all graph/config values preserved',{k:v for k,v in d.items() if k!='research'}==prior)
check('quadrant enum order confirmed',[d['research']['quadrants'][str(i)] for i in range(4)]==['FrontLeft','FrontRight','BackRight','BackLeft'])
check('avoid enum bits confirmed',[d['research']['avoidBits'][str(i)] for i in [1,2,4,8]]==['Jump','Duck','SideLeft','SideRight'])
check('display evidence sources unchanged',all(hashlib.sha256((R/p).read_bytes()).hexdigest()==h for p,h in d['research']['sources'].items()))"""
assert old in s;s=s.replace(old,new);p.write_text(s,encoding='utf-8')
p=R/'scripts/build_player_readable.py';s=p.read_text(encoding='utf-8')
s=s.replace('轻击变体 Alt（具体手势待核）','轻击短按松开变体（≤0.2秒；与普通输入同手势，受输入栈限制）').replace('重击变体 Alt（具体手势待核）','重击短按松开变体（≤0.2秒；与普通输入同手势，受输入栈限制）')
s=s.replace('同一节点可引用四个姿态槽；不等同于四个不同输入方向','0前左、1前右、2后右、3后左；按身体／骨盆相对目标选槽，镜像交换左右；不是四次命中')
p.write_text(s,encoding='utf-8')
