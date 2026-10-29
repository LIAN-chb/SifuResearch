"""Single-layout, read-only prototype requested by the user; no automatic graph layout."""
from pathlib import Path
import json, hashlib

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'exports/20261028-玩家招式板-01'
OUT.mkdir(parents=True, exist_ok=True)
source = ROOT / 'inventory/player-combo-graphs.json'
tree = next(t for t in json.loads(source.read_text(encoding='utf-8'))['trees'] if t['asset'].endswith('/MainChar_ComboTree.uasset'))
names = {44:'轻击第1段',45:'轻击第2段',14:'轻击第3段',7:'轻击第4段',8:'轻击第5段',48:'重击第1段',4:'重击第2段',5:'重击第3段',10:'重击第4段',32:'推掌／推踢',31:'扫腿',36:'向前踢击',30:'向前踢击后续',11:'抓击后续',12:'肘击后续',9:'连续抓击',15:'击倒收尾',25:'推击后追打',26:'推击后击倒',33:'长按轻击起手',34:'长按轻击后·轻',35:'长按轻击后·重',37:'前踢后·轻',38:'前踢后·重'}
descriptions = {44:['刺拳','勾拳'],45:['双段打击','双段打击'],14:['头部拳击','肘击'],7:['掌击','腹部挥击'],8:['三段打击','三段打击'],48:['腹部掌击','腹部掌击'],4:['踢腿','踢腿'],5:['喉部拳击','喉部拳击'],10:['肘击','双段收尾'],32:['推掌','推踢'],31:['扫腿','扫腿'],36:['向前踢击','向前踢击']}
inputs = {'Light':'轻击','Heavy':'重击','LightHold':'长按轻击','HeavyHold':'长按重击','HeavyAlt':'重击变体（手势待核）'}
def resolve(i):
    seen = set()
    while tree['nodes'][i].get('m_NodeRedirect[0]', -1) >= 0:
        assert i not in seen
        seen.add(i)
        i = tree['nodes'][i]['m_NodeRedirect[0]']
    return i
nodes = {}
for i,n in enumerate(tree['nodes']):
    variants = []
    for k,v in n.get('m_AttackInfos[0]',{}).items():
        if k.startswith('m_Attacks[') and v != 'None':
            variants.append({'slot': k, 'asset': v})
    edges = []
    for e in tree['edges']:
        if e['source'] != f'N{i}' or e['target'] < 0: continue
        target = resolve(e['target'])
        edges.append({'target':target,'input':inputs.get(e['input'].split('::')[-1], '其他输入'), 'conditional':bool(e.get('condition',{}).get('reference')), 'key':e.get('condition_result'), 'rawTarget':e['target']})
    nodes[str(i)] = {'id':i,'name':names.get(i,'分支招式（动作名待核）'),'descriptions':descriptions.get(i,[]),'variants':variants,'edges':edges,'tags':n.get('m_RequiredTags[0]',[]),'rawName':n.get('m_Transitions[0]',{}).get('m_ParentNodeName[0]')}
light=[44,45,14,7,8]; heavy=[48,4,5,10]
for row,kind in [(light,'轻击'),(heavy,'重击')]:
    for a,b in zip(row,row[1:]):
        assert any(e['target']==b and e['input']==kind for e in nodes[str(a)]['edges'])
assert tree['defaults']['m_DefaultAttacks[0]']==light[0]
assert tree['defaults']['m_DefaultAttacks[6]']==heavy[0]
data={'nodes':nodes,'light':light,'heavy':heavy,'special':[32,31,36], 'source':tree['asset']}
template = r'''<!doctype html>
<html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>徒手招式板 · 阅读小样</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f4f2ec;color:#242c29;font:16px/1.6 'Microsoft YaHei',sans-serif}main{max-width:1260px;margin:auto;padding:36px 32px 60px}.eyebrow{color:#68796b;letter-spacing:.14em;font-size:12px}h1{font-size:30px;margin:6px 0}h2{font-size:19px;margin:22px 0 12px}p{margin:6px 0}.muted{color:#687169;font-size:13px}.heading{display:flex;justify-content:space-between;align-items:center}.badge{border:1px solid #bac6ba;border-radius:30px;padding:4px 12px;font-size:12px}.scroll{overflow:auto}.board{position:relative;min-width:900px;padding:12px 0 20px}.row{display:grid;grid-template-columns:78px repeat(5,minmax(0,1fr));gap:24px;align-items:center;position:relative}.row+.row{margin-top:65px}.row-label{font-size:15px;font-weight:bold}.row-label small{display:block;font-size:12px;font-weight:normal;color:#6c756d}.move{position:relative;width:100%;text-align:left;border:1px solid #d5d9d0;background:#fffef9;color:inherit;border-radius:12px;padding:16px 12px;cursor:pointer;min-height:113px;box-shadow:0 3px 10px #22332205;font-family:inherit}.move strong{display:block;font-size:16px}.move .desc{display:block;font-size:12px;color:#647266;margin-top:9px}.move .tag{display:block;font-size:11px;color:#7a8179;margin-top:6px}.move:focus-visible{outline:3px solid #628b70}.move[aria-pressed=true]{background:#e7efe5;border:2px solid #416d4e;padding:15px 11px}.move.target{box-shadow:0 0 0 3px #bdcdb7}.chain:not(:last-child):after{content:'→';position:absolute;right:-21px;top:37px;color:#82917e;font-size:21px}.heavy .move{border-top:3px solid #a48763}.light .move{border-top:3px solid #62816b}svg.connections{position:absolute;inset:0;pointer-events:none;width:100%;height:100%;overflow:visible;color:#477b54;z-index:2}.specials{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.specials .move{min-height:95px}.detail{margin-top:24px;padding:20px 24px;background:#fffef9;border:1px solid #d5d9d0;border-radius:12px}.detail h2{margin:0 0 8px}.links{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px}.link{font:inherit;font-size:14px;background:#eef2e9;border:1px solid #d0dbcd;border-radius:7px;padding:8px 12px;cursor:pointer;color:#294734}.link small{display:block;color:#6d736a;font-size:11px;text-align:left}details{margin-top:18px;font-size:13px}summary{cursor:pointer;color:#627164}.evidence{overflow-wrap:anywhere;max-height:270px;overflow:auto}footer{margin-top:20px;font-size:12px;color:#71796f}.empty{font-size:13px;color:#7a8179}.route-note{font-size:12px;color:#74786d;margin-left:102px;margin-top:12px}@media(max-width:650px){main{padding:22px 16px}.specials{grid-template-columns:1fr}.heading{align-items:start;gap:15px}h1{font-size:25px}}
</style>
<main><div class="heading"><div><div class="eyebrow">SIFU / 徒手</div><h1>轻重两条线，换招看去向</h1></div><span class="badge">布局小样 · 配置路线</span></div>
<p class="muted">点击一招，只突出它下一次轻击、重击的去向。名称按操作位置标记，动作描述为暂名。</p>
<div class="scroll"><div class="board" id="board"><svg class="connections" aria-hidden="true"></svg><div class="row light" id="light"><div class="row-label">连续轻击<small>每次按轻击 →</small></div></div><div class="row heavy" id="heavy"><div class="row-label">连续重击<small>每次按重击 →</small></div></div><div class="route-note">基础路线常显；换招连线随选择显示。带“条件”的衔接仍需满足对应配置条件。</div></div></div>
<div class="heading"><h2>独立方向招式</h2><span class="muted">接入范围待核，不逐招拉入线</span></div>
<div class="specials" id="specials"></div>
<section class="detail" aria-live="polite" id="detail"></section>
<footer>同招变体合并展示；正面／背面的槽位对应尚待核对。配置连通不保证连续命中；小样未覆盖全部徒手招式。</footer>
</main><script>
const DATA=__DATA__;
const nodes=DATA.nodes, board=document.getElementById('board'), detail=document.getElementById('detail');
let selected=44;
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function makeCard(id,chain=false){const n=nodes[id],b=document.createElement('button');b.className='move'+(chain?' chain':'');b.dataset.node=id;b.setAttribute('aria-pressed','false');const label=n.descriptions.length?[...new Set(n.descriptions)].join(' ／ '):'动作待核';const entry={32:'后→前＋轻击 · 输入类型',31:'后→前＋重击 · 输入类型',36:'前→前＋重击 · 输入类型'}[id];b.innerHTML='<strong>'+esc(n.name)+'</strong><span class="desc">'+esc(entry||label)+'</span><span class="tag">'+(entry?'实际手势与可接时机待核':'同招变体合并 · 朝向待核')+'</span>';b.onclick=()=>select(id);return b;}
for(const [row,ids] of [['light',DATA.light],['heavy',DATA.heavy],['specials',DATA.special]])for(const id of ids)document.getElementById(row).append(makeCard(id,row!=='specials'));
function edgesOf(n){const out=[];for(const e of n.edges){const old=out.find(x=>x.input===e.input&&x.target===e.target&&x.conditional===e.conditional);if(!old)out.push(e);}return out;}
function select(id){selected=Number(id);const n=nodes[id],edges=edgesOf(n);document.querySelectorAll('.move').forEach(b=>{b.setAttribute('aria-pressed',String(Number(b.dataset.node)===selected));b.classList.toggle('target',edges.some(e=>e.target===Number(b.dataset.node)));});detail.innerHTML='<h2>'+esc(n.name)+'</h2><p class="muted">'+(n.descriptions.length?'动作暂名：'+esc([...new Set(n.descriptions)].join(' ／ ')):'此分支的玩家常用名称待核对。')+'</p><div class="links">'+(edges.length?edges.map((e,i)=>'<button class="link" data-edge="'+i+'">'+esc(e.input)+' → '+esc(nodes[e.target].name)+(e.conditional?'<small>有条件分支；不是无条件接续</small>':'')+'</button>').join(''):'<span class="empty">未保存后续输入连接；不据此判定实战不可接其他招。</span>')+'</div><p class="muted" style="margin-top:12px">'+(n.tags.length?'需要技能解锁；具体条件见证据详情。':'本节点未保存技能标签；其他运行条件仍可能限制。')+'</p><details><summary>查看来源、变体与未确认项</summary><div class="evidence"><p>内部定位：节点 '+n.id+' · '+esc(n.rawName)+'</p><p>来源：'+esc(DATA.source)+'</p><p>姿态槽不当作命中次数；下列资源未作正背面已确认映射。</p>'+n.variants.map(v=>'<p>'+esc(v.slot)+'：'+esc(v.asset)+'</p>').join('')+'<p>技能标签：'+esc(n.tags.join('、')||'本节点未保存')+'</p><p>条件攻击覆写及运行时选择未完整恢复。伤害不在小样中合并成一个最终数值。</p><p>保存连接：'+esc(JSON.stringify(n.edges))+'</p></div></details>';detail.querySelectorAll('[data-edge]').forEach(b=>b.onclick=()=>select(edges[Number(b.dataset.edge)].target));draw();}
function draw(){const svg=board.querySelector('svg');svg.innerHTML='<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10" fill="currentColor"/></marker></defs>';const start=board.querySelector('[data-node="'+selected+'"]');if(!start)return;const r=board.getBoundingClientRect(),a=start.getBoundingClientRect();for(const e of edgesOf(nodes[selected])){const end=board.querySelector('[data-node="'+e.target+'"]');if(!end)continue;const b=end.getBoundingClientRect(),same=Math.abs(a.top-b.top)<5;const x1=(same?a.right:a.left+a.width/2)-r.left,y1=(same?a.top+a.height/2:(a.top<b.top?a.bottom:a.top))-r.top,x2=(same?b.left:b.left+b.width/2)-r.left,y2=(same?b.top+b.height/2:(a.top<b.top?b.top:b.bottom))-r.top;const path=document.createElementNS('http://www.w3.org/2000/svg','path');path.setAttribute('d',same?'M'+x1+','+y1+' L'+x2+','+y2:'M'+x1+','+y1+' C'+x1+','+(y1+y2)/2+' '+x2+','+(y1+y2)/2+' '+x2+','+y2);path.setAttribute('fill','none');path.setAttribute('stroke','currentColor');path.setAttribute('stroke-width','2');path.setAttribute('marker-end','url(#arrow)');if(e.conditional)path.setAttribute('stroke-dasharray','5 4');svg.append(path);}}
new ResizeObserver(draw).observe(board);select(44);
</script></html>'''
html = template.replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
(OUT/'player-board-prototype.html').write_text(html,encoding='utf-8')
(OUT/'board-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
manifest={'source':str(source.relative_to(ROOT)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'asset':tree['asset'],'uasset_sha256':tree['uasset_sha256'],'uexp_sha256':tree['uexp_sha256'],'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':['two default entries match','seven consecutive input edges match after saved redirects'],'limits':['not runtime tested','orientation slots not verified','direction gestures not verified','conditional redirects are display normalization, not unconditional runtime reachability']}
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
layout_path = ROOT / 'inventory/vault-layout.json'
layout = json.loads(layout_path.read_text(encoding='utf-8'))
page = '03配置/玩家攻击/徒手招式板小样.md'
if page not in layout['documents']:
    layout['documents'].append(page)
    layout_path.write_text(json.dumps(layout,ensure_ascii=False,indent=2),encoding='utf-8')
print(OUT/'player-board-prototype.html')
