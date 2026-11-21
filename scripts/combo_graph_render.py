# -*- coding: utf-8 -*-
"""连招图渲染：把连招树画成有向图（共享前缀 = 同一节点），前端做路径评分。"""

CSS = r"""
:root{
  --paper:#f4f2ec; --card:#fffef9; --ink:#25372d; --ink2:#5c6b5f; --line:#c9d4c3;
  --accent:#2e5740; --config:#44875d; --state:#7b6aa8; --cmd:#5c7baf; --warn:#b4553f;
}
*{box-sizing:border-box}
html,body{height:100%}
body{margin:0;background:var(--paper);color:var(--ink);
  font:13.5px/1.5 -apple-system,"Segoe UI","Microsoft YaHei",sans-serif;overflow:hidden}
h1,h2,h3{font-family:"Noto Serif SC","Songti SC",Georgia,serif;font-weight:600;margin:0}
.app{display:flex;height:100vh}
.side{width:296px;flex:0 0 296px;height:100vh;overflow-y:auto;background:var(--paper);
  border-right:1px solid var(--line);padding:0 0 24px}
.side .top{background:var(--accent);color:#f2f5ee;padding:16px 16px 18px;margin-bottom:12px}
.side .top h1{font-size:15px;letter-spacing:.05em}
.side .top p{margin:6px 0 0;font-size:10.5px;opacity:.85;line-height:1.45}
.box{background:var(--card);border:1px solid var(--line);border-radius:8px;margin:0 12px 10px;padding:10px 12px}
.box h2{font-size:12px;letter-spacing:.14em;color:var(--ink2);margin-bottom:8px}
label{display:block;font-size:11px;color:var(--ink2);margin:6px 0 3px}
select{width:100%;padding:5px 6px;border:1px solid var(--line);border-radius:6px;background:#fff;color:var(--ink);font-size:12.5px}
.tabs{display:flex;flex-wrap:wrap;gap:6px}
.tab{padding:4px 10px;border:1px solid var(--line);border-radius:14px;background:#fff;
  font-size:12px;color:var(--ink2);cursor:pointer;user-select:none}
.tab.on{background:var(--accent);border-color:var(--accent);color:#fff}
.hint{font-size:11px;color:var(--ink2);margin:6px 0 0;line-height:1.45}
.kv{display:flex;justify-content:space-between;font-size:12px;padding:3px 0;border-bottom:1px dotted #e2e6dd}
.kv:last-child{border-bottom:0}
.kv b{font-weight:600}
.wt{display:flex;align-items:center;gap:6px;font-size:11.5px;margin:3px 0}
.wt span{width:56px;color:var(--ink2);flex:0 0 auto}
.wt input{flex:1;accent-color:var(--accent)}
.wt b{width:22px;text-align:right}
.main{flex:1;height:100vh;overflow:auto;position:relative}
.canvas{position:relative}
svg{display:block}
.node{cursor:pointer}
.node rect{fill:#fffef9;stroke:var(--line);stroke-width:1.2;rx:7}
.node.sel rect{stroke:var(--accent);stroke-width:2.4;fill:#f1f6ef}
.node.root rect{stroke:var(--accent);stroke-width:1.8;fill:#f6faf4}
.node.entry rect{stroke-dasharray:0}
.node text{font-size:11.5px;fill:var(--ink);pointer-events:none}
.node text.sub{font-size:10px;fill:var(--ink2)}
.node .inp{font-size:10px;fill:var(--ink2)}
.edge{fill:none;stroke:var(--config);stroke-width:1.4;opacity:.55}
.edge.state{stroke:var(--state);stroke-dasharray:5 3}
.edge.cmd{stroke:var(--cmd);stroke-dasharray:2 3;opacity:.45}
.edge.best{stroke-width:2.6;opacity:.95}
.edge text{font-size:9.5px;fill:var(--ink2);opacity:.9}
.panel{position:sticky;bottom:0;background:var(--card);border-top:1px solid var(--line);
  padding:10px 16px;font-size:12px;min-height:120px;max-height:38vh;overflow:auto}
.panel h3{font-size:13px;margin-bottom:6px}
.chips{display:flex;flex-wrap:wrap;gap:4px;margin:4px 0}
.chip{font-size:11px;padding:1px 7px;border-radius:10px;border:1px solid var(--line);background:#fff}
.chip.kd{color:var(--warn);border-color:#e2c4bb}
.chip.push{color:#8a6a3c;border-color:#e0d3b8}
.chip.ground{color:#3f6f8a;border-color:#c3d6e2}
.badge{display:inline-block;font-size:10px;padding:0 5px;border-radius:3px;margin-left:4px;vertical-align:1px}
.b-稳{background:#dcecdf;color:#2e5740}
.b-紧{background:#f3edd6;color:#7a6420}
.b-需状态{background:#f6e2d8;color:#8a4a30}
.b-待核{background:#e8e8e8;color:#666}
.legend{display:flex;gap:12px;font-size:11px;color:var(--ink2);padding:8px 16px;background:var(--card);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:3}
.legend i{display:inline-block;width:14px;height:0;border-top:2px solid var(--config);vertical-align:3px;margin-right:4px}
.legend .s{border-top:2px dashed var(--state)}
.legend .c{border-top:2px dotted var(--cmd)}
.warn{color:var(--warn)}
"""

HTML = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>师父 · 徒手连招图</title>
<style>__CSS__</style>
</head>
<body>
<div class="app">
  <aside class="side">
    <div class="top">
      <h1>徒手连招图</h1>
    </div>
    <div class="box">
      <h2>敌 人</h2>
      <label>原型</label><select id="arch"></select>
      <label>具体</label><select id="enemy"></select>
      <div id="enemyCard" style="margin-top:8px"></div>
    </div>
    <div class="box">
      <h2>入 口</h2>
      <div class="tabs" id="entryTabs"></div>
      <p class="hint" id="entryHint"></p>
    </div>
    <div class="box">
      <h2>目 标</h2>
      <div class="tabs" id="goalTabs"></div>
      <p class="hint">目标只改变高亮路径的评分，不改变图结构。</p>
    </div>
    <div class="box">
      <h2>权 重</h2>
      <div class="tabs" id="presetTabs"></div>
      <div id="wtBox"></div>
    </div>
    <div class="box">
      <h2>显 示</h2>
      <label style="display:flex;gap:6px;align-items:center;color:var(--ink)">
        <input type="checkbox" id="showCmd"> 显示指令重入（可用性层允许，非连招树边）
      </label>
      <label style="display:flex;gap:6px;align-items:center;color:var(--ink)">
        <input type="checkbox" id="showLabels" checked> 显示连线输入标签
      </label>
    </div>
    <p class="hint" style="margin:10px 12px 0">节点＝招式，连线＝一次输入；同一起手共用节点，分叉即分支，任一前缀都成立。</p>
  </aside>
  <main class="main">
    <div class="legend">
      <span><i></i>配置衔接（连招树）</span>
      <span><i class="s"></i>状态入口（击退后）</span>
      <span><i class="c"></i>指令重入</span>
      <span id="stat"></span>
    </div>
    <div class="canvas" id="canvas"><svg id="map"></svg></div>
    <div class="panel" id="panel"><h3>点选节点查看</h3><p class="hint">图中每条路径都是可连段；点击节点查看该点最优先的路径与招式数值。</p></div>
  </main>
</div>
<script>
const DATA = /*__DATA__*/;
const S = {arch:null, enemy:null, entry:"active", goal:"overall", showCmd:false, showLabels:true,
           wt:{dmg:34,struct:26,sdiz:20,len:12,fin:8,risk:22}, sel:null};
const WT_KEY="{{SECRET_a7k2m9qd}}";
const WT_META=[["dmg","伤害"],["struct","结构"],["sdiz","特殊眩晕"],["len","连段长度"],["fin","收尾"],["risk","风险"]];
const PRESETS=[["均衡",{dmg:34,struct:26,sdiz:20,len:12,fin:8,risk:22}],
  ["眩晕",{dmg:20,struct:10,sdiz:50,len:10,fin:10,risk:24}],
  ["破防",{dmg:10,struct:55,sdiz:15,len:10,fin:10,risk:18}],
  ["爆伤",{dmg:55,struct:10,sdiz:10,len:15,fin:10,risk:20}],
  ["处决",{dmg:25,struct:25,sdiz:20,len:15,fin:15,risk:25}]];
try{const w=JSON.parse(localStorage.getItem(WT_KEY)||"null");if(w)Object.assign(S.wt,w);}catch(e){}

const el=id=>document.getElementById(id);
const esc=s=>String(s==null?"":s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const NW=168, NH=48, DX=206, DY=74;

function tierOf(g){if(g==null)return "待核";if(g<=24)return "稳";if(g<=29)return "紧";if(g<=45)return "需状态";return "超界";}

function saveWt(){try{localStorage.setItem(WT_KEY,JSON.stringify(S.wt))}catch(e){}}
function renderWeights(){
  el("wtBox").innerHTML=WT_META.map(([k,l])=>
    `<div class="wt"><span>${l}</span><input type="range" min="0" max="60" value="${S.wt[k]}" data-k="${k}"><b>${S.wt[k]}</b></div>`).join("");
  el("wtBox").querySelectorAll("input").forEach(i=>{i.oninput=()=>{S.wt[i.dataset.k]=+i.value;i.nextElementSibling.textContent=i.value;saveWt();render();};});
  el("presetTabs").innerHTML=PRESETS.map(([n])=>`<span class="tab" data-n="${n}">${n}</span>`).join("");
  el("presetTabs").onclick=e=>{const t=e.target.closest(".tab");if(!t)return;
    const p=PRESETS.find(x=>x[0]===t.dataset.n);if(p){Object.assign(S.wt,p[1]);saveWt();renderWeights();render();}};
}

function edgesFor(){
  return DATA.graph.edges.filter(e=>S.showCmd||e.grade!=="cmd");
}
function rootsFor(){
  const spec=DATA.entries[S.entry];
  return (spec.starts||[]).filter(id=>DATA.nodes[id]);
}

function reachable(roots,edges){
  const out={},seen=new Set(roots);
  edges.forEach(e=>{(out[e.s]=out[e.s]||[]).push(e)});
  const q=[...roots];
  while(q.length){const n=q.shift();for(const e of out[n]||[]){if(!seen.has(e.t)){seen.add(e.t);q.push(e.t)}}}
  return {out,seen};
}

function layout(roots,out,seen){
  const depth={},order=[...seen];
  roots.forEach(r=>depth[r]=0);
  let changed=true,guard=0;
  while(changed&&guard++<20){
    changed=false;
    for(const n of order){
      if(depth[n]==null)continue;
      for(const e of out[n]||[]){
        const d=depth[n]+1;
        if(depth[e.t]==null){depth[e.t]=d;changed=true;}
        else if(depth[e.t]<d){depth[e.t]=d;}
      }
    }
  }
  const par={};
  for(const n of order){for(const e of out[n]||[]){(par[e.t]=par[e.t]||[]).push(n);}}
  const byDepth={};
  for(const n of order){const d=depth[n]??0;(byDepth[d]=byDepth[d]||[]).push(n);}
  const idx={};
  const maxD=Math.max(...Object.keys(byDepth).map(Number),0);
  for(let d=0;d<=maxD;d++){
    const arr=byDepth[d]||[];
    if(d===0){arr.sort((a,b)=>+a-+b);}
    else{
      arr.sort((a,b)=>{
        const pa=par[a]||[],pb=par[b]||[];
        const ma=pa.length?pa.reduce((s,p)=>s+(idx[p]??0),0)/pa.length:1e6;
        const mb=pb.length?pb.reduce((s,p)=>s+(idx[p]??0),0)/pb.length:1e6;
        return ma-mb||(+a-+b);
      });
    }
    arr.forEach((n,i)=>{idx[n]=i;});
  }
  const pos={};
  for(let d=0;d<=maxD;d++){
    (byDepth[d]||[]).forEach((n,i)=>{pos[n]={x:30+d*DX,y:24+i*DY,d};});
  }
  return pos;
}

function nodeStats(id){
  const n=DATA.nodes[id]||{}, a=n.agg||{};
  return {hits:a.hits||1,dmg:a.dmg||0,struct:a.struct||0,sdiz:a.sdiz||0,stun:a.stun||0,kb:a.kb||0,fin:n.finisher?1:0,kd:n.kd,push:n.push,ground:n.ground};
}
function scoreOf(t){
  const W=S.wt,sum=Math.max(1,W.dmg+W.struct+W.sdiz+W.len+W.fin);
  let s=(W.dmg*Math.min(t.dmg/180,1.5)+W.struct*Math.min(t.struct/260,1.5)+W.sdiz*Math.min(t.sdiz/220,1.5)
        +W.len*t.ratio+W.fin*t.fin)/sum*100;
  const e=DATA.enemies.find(x=>x.key===S.enemy)||{};
  const risk=e.mem_trigger?Math.min(1,(e.prob||0.7)+0.12*Math.max(0,t.hits-(e.mem_trigger||99))):0;
  s*= (1-(S.wt.risk/100)*risk);
  t.risk=risk;
  return s;
}
function budgetOf(){const e=DATA.enemies.find(x=>x.key===S.enemy)||{};return {hits:e.dizzy_hits||999,dmg:e.dizzy_dmg||9999,down:e.down_hits||2};}
function initAcc(id){
  const st=nodeStats(id),b=budgetOf();
  const hits=Math.min(st.hits,b.hits);
  const t={dmg:st.dmg*hits/st.hits,struct:st.struct*hits/st.hits,sdiz:st.sdiz*hits/st.hits,
           hits,ratio:1,fin:st.fin,used:hits,segs:1,path:[id]};
  t.score=scoreOf(t);t.cut=hits<st.hits;
  return t;
}
function extend(acc,e){
  const st=nodeStats(e.t),b=budgetOf(),prev=DATA.nodes[acc.path[acc.path.length-1]]||{};
  let used=acc.used,segs=acc.segs;
  if(prev.kd||prev.push||e.grade==="state"){used=0;segs++;}
  const bud=prev.kd?b.down:b.hits;
  if(used>=bud) return null;
  const sh=Math.min(st.hits,bud-used),frac=sh/st.hits;
  const t={dmg:acc.dmg+st.dmg*frac,struct:acc.struct+st.struct*frac,sdiz:acc.sdiz+st.sdiz*frac,
           hits:acc.hits+sh,ratio:acc.ratio*0+0,fin:acc.fin+st.fin,used:used+sh,segs,
           path:acc.path.concat([e.t])};
  const cfg=acc.cfg||1;const n=acc.path.length; t.ratio=( (acc.ratio*(n-1)||0) + (e.grade==="config"?1:0) )/n;
  t.score=scoreOf(t);
  return t;
}
function analyze(){
  const roots=rootsFor(),edges=edgesFor(),{out,seen}=reachable(roots,edges);
  const pos=layout(roots,out,seen);
  const order=Object.keys(pos).sort((a,b)=>pos[a].d-pos[b].d);
  const best={};
  roots.forEach(r=>{if(pos[r])best[r]=initAcc(r)});
  for(const id of order){
    const b=best[id];if(!b)continue;
    for(const e of out[id]||[]){
      const c=extend(b,e);
      if(!c)continue;
      if(!best[e.t]||c.score>best[e.t].score)best[e.t]=c;
    }
  }
  return {roots,edges,out,seen,pos,best};
}

function render(){
  const A=analyze();
  const vis=A.edges.filter(e=>A.pos[e.s]&&A.pos[e.t]);
  el("stat").textContent=`${Object.keys(A.pos).length} 个节点 · ${vis.length} 条衔接`;
  const W=Math.max(900, Math.max(...Object.values(A.pos).map(p=>p.x),0)+NW+60);
  const H=Math.max(400, Math.max(...Object.values(A.pos).map(p=>p.y),0)+NH+40);
  const svg=el("map");svg.setAttribute("width",W);svg.setAttribute("height",H);
  let h="";
  const bestPath=new Set();
  const sel=A.best[S.sel];
  if(sel) sel.path.forEach((id,i)=>{if(i)bestPath.add(sel.path[i-1]+">"+id)});
  for(const e of vis){
    const a=A.pos[e.s],b=A.pos[e.t];if(!a||!b)continue;
    const x1=a.x+NW,y1=a.y+NH/2,x2=b.x,y2=b.y+NH/2,dx=(x2-x1)/2;
    const cls=["edge",e.grade==="state"?"state":"",e.grade==="cmd"?"cmd":"",bestPath.has(e.s+">"+e.t)?"best":""].join(" ");
    h+=`<path class="${cls}" d="M${x1},${y1} C${x1+dx},${y1} ${x2-dx},${y2} ${x2},${y2}"></path>`;
    if(S.showLabels){
      const mx=(x1+x2)/2,my=(y1+y2)/2-3;
      h+=`<text x="${mx}" y="${my}" text-anchor="middle">${esc(e.inp)}</text>`;
    }
  }
  for(const id of Object.keys(A.pos)){
    const p=A.pos[id],n=DATA.nodes[id]||{},b=A.best[id];
    const cls=["node",A.roots.includes(id)?"root":"",S.sel===id?"sel":""].join(" ");
    h+=`<g class="${cls}" data-id="${id}" transform="translate(${p.x},${p.y})">
      <rect width="${NW}" height="${NH}" rx="7"></rect>
      <text x="10" y="18">${esc(n.name||id)}</text>
      <text class="sub" x="10" y="33">${b?`${Math.round(b.dmg)}伤 · ${Math.round(b.struct)}结 · ${b.hits}击`:"不可达"}</text>
    </g>`;
  }
  svg.innerHTML=h;
  svg.querySelectorAll(".node").forEach(g=>g.onclick=()=>{S.sel=g.dataset.id;render();showDetail(A);});
  if(!vis.length){
    el("panel").innerHTML=`<h3>${esc((DATA.entries[S.entry]||{}).label||"")}</h3>
      <p class="hint">该入口招式本身没有配置内的后续衔接（收尾型招式）。可打开左侧「显示指令重入」查看收招窗口内还能接什么。</p>`;
  }
  showDetail(A);
}

function showDetail(A){
  const id=S.sel; if(!id){return;}
  const n=DATA.nodes[id]||{},b=A.best[id],e=DATA.enemies.find(x=>x.key===S.enemy)||{};
  const st=nodeStats(id);
  const chips=[];
  if(n.kd)chips.push('<span class="chip kd">击倒</span>');
  if(n.push)chips.push('<span class="chip push">击退</span>');
  if(n.ground)chips.push('<span class="chip ground">贴地判定</span>');
  if(n.finisher)chips.push('<span class="chip">收尾</span>');
  (n.props||[]).slice(0,4).forEach(p=>chips.push(`<span class="chip">${esc(p.replace(/^Attack\./,""))}</span>`));
  let path="—";
  if(b){path=b.path.map(x=>(DATA.nodes[x]||{}).name||x).join(" → ");}
  const outs=(A.out[id]||[]).map(x=>{
    const t=DATA.nodes[x.t]||{};
    return `<div class="kv"><span>${esc(x.inp)} → ${esc(t.name||x.t)}<i class="badge b-${tierOf(x.gap)}">${tierOf(x.gap)}${x.gap!=null?x.gap+"f":""}</i></span><b>${x.grade==="state"?"状态入口":x.grade==="cmd"?"指令重入":"配置"}</b></div>`;
  }).join("")||'<p class="hint">无后续（收尾）</p>';
  el("panel").innerHTML=`
    <h3>${esc(n.name||id)} <span class="hint">${esc(n.rawName||"")}</span></h3>
    <div class="chips">${chips.join("")}</div>
    <div class="kv"><span>本招 伤害/结构/特殊眩晕</span><b>${st.dmg} / ${st.struct} / ${st.sdiz}</b></div>
    <div class="kv"><span>命中 / 硬直 / 击退</span><b>${st.hits} 击 · ${st.stun}f · ${st.kb}</b></div>
    <div class="kv"><span>最优路径累计（${e.name||""}）</span><b>${b?`${Math.round(b.dmg)} / ${Math.round(b.struct)} / ${Math.round(b.sdiz)} · ${b.hits} 击`: "—"}</b></div>
    <p class="hint" style="margin:6px 0 2px">最优路径：${esc(path)}</p>
    <p class="hint" style="margin:0 0 4px">后继衔接：</p>${outs}`;
}

function fillEnemies(){
  const list=DATA.enemies.filter(e=>e.archetype===S.arch);
  el("enemy").innerHTML=list.map(e=>`<option value="${e.key}">${esc(e.name)}</option>`).join("");
  S.enemy=list[0]&&list[0].key;
  el("enemy").onchange=()=>{S.enemy=el("enemy").value;S.sel=null;render()};
  render();
}
function enemyCard(){
  const e=DATA.enemies.find(x=>x.key===S.enemy);if(!e)return "";
  return `<div class="kv"><span>眩晕窗口</span><b>${e.dizzy_dmg||"—"} 伤 / ${e.dizzy_hits||"—"} 击</b></div>
    <div class="kv"><span>倒地窗口</span><b>最多 ${e.down_hits||2} 击</b></div>
    <div class="kv"><span>破防窗口</span><b>3.0 s</b></div>
    <div class="kv"><span>防御反应</span><b>${e.mem_trigger?`连续 ${e.mem_trigger} 击后 ${Math.round((e.prob||0)*100)}%`:"—"}</b></div>`;
}
function init(){
  el("arch").innerHTML=DATA.archetypes.map(a=>`<option>${esc(a)}</option>`).join("");
  S.arch=DATA.archetypes[0];
  el("arch").onchange=()=>{S.arch=el("arch").value;fillEnemies()};
  el("entryTabs").innerHTML=Object.entries(DATA.entries).map(([k,v])=>`<span class="tab" data-k="${k}">${esc(v.label)}</span>`).join("");
  el("entryTabs").onclick=e=>{const t=e.target.closest(".tab");if(!t)return;S.entry=t.dataset.k;S.sel=null;sync();render();};
  el("goalTabs").innerHTML=DATA.goals.map(g=>`<span class="tab" data-k="${g.key}">${esc(g.label)}</span>`).join("");
  el("goalTabs").onclick=e=>{const t=e.target.closest(".tab");if(!t)return;S.goal=t.dataset.k;sync();render();};
  el("showCmd").onchange=()=>{S.showCmd=el("showCmd").checked;render()};
  el("showLabels").onchange=()=>{S.showLabels=el("showLabels").checked;render()};
  renderWeights();
  const orig=render; window.render=()=>{orig();sync();};
  sync();
  fillEnemies();
}
function sync(){
  el("entryTabs").querySelectorAll(".tab").forEach(t=>t.classList.toggle("on",t.dataset.k===S.entry));
  el("goalTabs").querySelectorAll(".tab").forEach(t=>t.classList.toggle("on",t.dataset.k===S.goal));
  el("entryHint").textContent=(DATA.entries[S.entry]||{}).hint||"";
  el("enemyCard").innerHTML=enemyCard();
}
init();
</script>
</body>
</html>
"""


def render_html(data, css=None, html=None):
    import json
    c = css if css is not None else CSS
    h = html if html is not None else HTML
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    return h.replace("__CSS__", c).replace("/*__DATA__*/", blob)
