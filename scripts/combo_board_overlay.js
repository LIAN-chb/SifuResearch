/* 连招编排覆盖层：复用徒手招式板的 SVG 图，接管交互（单一高亮源），只做路径与详情。 */
(function () {
  const QG = (typeof DATA !== 'undefined' && DATA && DATA.graph);
  if (!QG) { console.warn('no DATA.graph'); return; }
  const QE = window.QENEMIES || [];
  const NODE = {}; QG.nodes.forEach(n => { NODE[n.id] = n; });
  const C2D = QG.canonicalToDisplay || {};
  const d2 = c => (C2D[String(c)] !== undefined ? C2D[String(c)] : Number(c));

  const OUT = {};
  (QG.edges || []).forEach(e => {
    const ins = [...new Set(e.variants.map(v => v.input))];
    const cond = e.variants.every(v => v.conditional);
    (OUT[e.source] = OUT[e.source] || []).push({ t: e.target, ins, cond });
  });

  const ENTRY = {
    active: { label: '主动进攻', roots: [44, 48], hint: '轻击 / 重击起手。方向攻击不在起手之列，它们是连段里的输入。' },
    dodge:  { label: '闪避后',   roots: [55], hint: '斗转星移换位；鹰击长空需敌人出招前摇，未纳入。' },
    parry:  { label: '招架反击', roots: [2, 19, 21], hint: '招架成功后的三个入口：闪电击 / 奔雷手 / 使绊子。' },
    down:   { label: '倒地起身', roots: [0], hint: '被击倒后起身攻击。' }
  };
  const GOAL = { overall: '综合', dizzy: '眩晕窗口', struct: '破防', damage: '高伤害', knockdown: '击倒收尾' };
  const CMDS = [['前前轻', 39], ['前前重', 36], ['后前轻', 32], ['后前重', 31], ['长按轻', 33], ['长按重', 56], ['闪避攻击', 55], ['拉开', 52]];
  const S = { enemy: 0, entry: 'active', goal: 'overall', wt: { dmg: 34, struct: 26, sdiz: 20, len: 12, fin: 8, risk: 22 } };

  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const nm = id => (NODE[id] ? NODE[id].label : '#' + id);
  const num = id => { const s = (window.QSTATS || {})[id] || {}; return { dmg: s.dmg || 0, struct: s.struct || 0, hits: s.hits || 0, kd: !!s.kd }; };
  const stats = e => ({ dmg: e.dizzy_dmg || 100, hits: e.dizzy_hits || 4, down: e.down_hits || 2, trig: e.mem_trigger || 99, prob: e.prob || 0 });

  // ---------- 路径枚举 ----------
  function collect(root, depth) {
    const out = [];
    (function walk(id, ids, ins, hits, dmg, struct, conds) {
      const n = num(id);
      const cur = { ids: ids.concat([id]), ins: ins.slice(), hits: hits + n.hits, dmg: dmg + n.dmg, struct: struct + n.struct, conds };
      out.push(cur);
      const outs = OUT[id] || [];
      if (cur.ids.length >= depth || !outs.length) return;
      for (const e of outs) {
        if (cur.ids.includes(e.t)) continue;
        walk(e.t, cur.ids, ins.concat([e.ins[0]]), cur.hits, cur.dmg, cur.struct, conds + (e.cond ? 1 : 0));
      }
    })(root, [], [], 0, 0, 0, 0);
    return out;
  }

  function score(c, e) {
    const st = stats(e), W = S.wt, sum = Math.max(1, W.dmg + W.struct + W.sdiz + W.len + W.fin);
    const eff = Math.min(c.hits, st.hits);
    const effD = c.hits ? c.dmg * (eff / c.hits) : 0;
    const risk = c.hits >= st.trig ? Math.min(1, (st.prob || 0.6) + 0.12 * (c.hits - st.trig)) : 0;
    const isTail = !(OUT[c.ids[c.ids.length - 1]] || []).length;
    const base = (W.dmg * Math.min(effD / 180, 1.5) + W.struct * Math.min(c.struct / 260, 1.5) +
      W.sdiz * Math.min(eff / 8, 1.5) + W.len * (1 - c.conds * 0.15) + W.fin * (isTail ? 1 : 0)) / sum * 100;
    c.risk = risk; c.eff = eff; c.tail = isTail;
    return base * (1 - (W.risk / 100) * risk);
  }

  // ---------- 高亮（唯一来源） ----------
  function clearHl() { document.querySelectorAll('.q-hl').forEach(n => n.classList.remove('q-hl')); }
  function hl(ids) {
    clearHl();
    ids.forEach(id => { const g = document.querySelector('#nodes .node[data-node="' + id + '"]'); if (g) g.classList.add('q-hl'); });
    for (let i = 0; i < ids.length - 1; i++) {
      const s = ids[i], t = ids[i + 1];
      document.querySelectorAll('#edges path[data-members]').forEach(p => {
        const mm = p.getAttribute('data-members').split('-').map(Number);
        if (d2(mm[0]) === s && d2(mm[1]) === t) p.classList.add('q-hl');
      });
    }
  }

  let top = [], lastIds = null;

  function renderRows() {
    const e = QE[S.enemy] || {}, res = document.getElementById('qres');
    if (!top.length) { res.innerHTML = '<p class="qhint">该入口没有配置内后续。</p>'; return; }
    res.innerHTML = top.map((c, i) => {
      const st = stats(e);
      const hitTxt = c.hits > st.hits ? ('有效 ' + st.hits + ' 击 / 全链 ' + c.hits) : (c.hits + ' 击');
      const loop = c.tail ? CMDS.filter(([, t]) => NODE[t]).map(([l]) => l).join(' / ') : '';
      return '<div class="qrow" data-i="' + i + '"><b>' + c.score.toFixed(1) + '</b>' +
        c.ids.map(id => esc(nm(id))).join(' → ') +
        '<i>' + hitTxt + ' · ' + Math.round(c.dmg) + ' 伤 · ' + Math.round(c.struct) + ' 结' + (c.tail ? ' · 收尾' : '') +
        (c.risk > 0 ? ' · 末端风险 ' + Math.round(c.risk * 100) + '%' : '') + '</i>' +
        (loop ? '<i class="qloop">↻ 尾招后可用指令接回：' + loop + '</i>' : '') + '</div>';
    }).join('');
    if (top[0]) { lastIds = top[0].ids; hl(lastIds); }
  }

  // ---------- 侧栏 ----------
  function buildPanel() {
    const archs = [...new Set(QE.map(e => e.archetype))];
    const box = document.createElement('div');
    box.id = 'qpanel';
    box.innerHTML =
      '<div class="qh">徒手连招图</div>' +
      '<div class="qb"><label>敌人 · 原型</label><select id="qarch">' +
      archs.map(a => '<option>' + esc(a) + '</option>').join('') + '</select>' +
      '<label style="margin-top:8px">敌人 · 版本</label><select id="qver"></select>' +
      '<div id="qthr" class="qthr"></div></div>' +
      '<div class="qb"><label>入口</label><div class="qtabs" id="qentry">' +
      Object.keys(ENTRY).map(k => '<button data-k="' + k + '">' + ENTRY[k].label + '</button>').join('') + '</div>' +
      '<div id="qehint" class="qhint"></div></div>' +
      '<div class="qb"><label>目标</label><div class="qtabs" id="qgoal">' +
      Object.keys(GOAL).map(k => '<button data-k="' + k + '">' + GOAL[k] + '</button>').join('') + '</div></div>' +
      '<div class="qb"><label>权重</label><div id="qwt"></div></div>' +
      '<div class="qb"><label>推荐路径（点击高亮）</label><div id="qres"></div></div>' +
      '<div class="qb"><label>节点详情</label><div id="qnode" class="qhint">点击图中任意节点查看它的数值与后继。</div></div>';
    document.body.appendChild(box);

    const META = [['dmg', '伤害'], ['struct', '结构'], ['sdiz', '命中'], ['len', '长度'], ['fin', '收尾'], ['risk', '风险']];
    document.getElementById('qwt').innerHTML = META.map(([k, l]) =>
      '<div class="qwr"><span>' + l + '</span><input type="range" min="0" max="60" value="' + S.wt[k] + '" data-k="' + k + '"><b>' + S.wt[k] + '</b></div>').join('');
    document.getElementById('qwt').oninput = ev => {
      const k = ev.target.dataset.k; if (!k) return;
      S.wt[k] = +ev.target.value; ev.target.nextElementSibling.textContent = S.wt[k]; draw();
    };
    document.getElementById('qarch').onchange = () => { fillVers(); draw(); };
    document.getElementById('qver').onchange = () => { S.enemy = +document.getElementById('qver').value; draw(); };
    document.getElementById('qentry').onclick = ev => { const b = ev.target.closest('button'); if (!b) return; S.entry = b.dataset.k; draw(); };
    document.getElementById('qgoal').onclick = ev => { const b = ev.target.closest('button'); if (!b) return; S.goal = b.dataset.k; draw(); };
    document.getElementById('qres').onclick = ev => {
      const r = ev.target.closest('.qrow'); if (!r) return;
      lastIds = top[+r.dataset.i].ids; hl(lastIds);
      document.querySelectorAll('#qres .qrow').forEach(x => x.classList.toggle('on', x === r));
    };
    fillVers();
  }

  function fillVers() {
    const a = document.getElementById('qarch').value;
    const list = QE.map((e, i) => [e, i]).filter(([e]) => e.archetype === a);
    const sel = document.getElementById('qver');
    sel.innerHTML = list.map(([e, i]) => '<option value="' + i + '">' + esc(e.version || '标准') + '</option>').join('');
    S.enemy = list.length ? list[0][1] : 0;
    sel.value = S.enemy;
  }

  function draw() {
    const e = QE[S.enemy] || {};
    document.getElementById('qthr').innerHTML =
      '<b>' + esc(e.name) + '</b><br>眩晕窗口 ' + (e.dizzy_dmg || '—') + ' 伤害 / ' + (e.dizzy_hits || '—') + ' 命中' +
      ' · 倒地最多 ' + (e.down_hits || 2) + ' 击' + (e.mem_trigger ? ' · 防御记忆 ' + e.mem_trigger + ' 击' : '');
    document.querySelectorAll('#qentry button').forEach(b => b.classList.toggle('on', b.dataset.k === S.entry));
    document.querySelectorAll('#qgoal button').forEach(b => b.classList.toggle('on', b.dataset.k === S.goal));
    document.getElementById('qehint').textContent = ENTRY[S.entry].hint;

    let all = [];
    ENTRY[S.entry].roots.filter(r => NODE[r]).forEach(r => { all = all.concat(collect(r, 7)); });
    all.forEach(c => { c.score = score(c, e); });
    all.sort((a, b) => b.score - a.score);
    const seen = new Set(); top = [];
    for (const c of all) { const k = c.ids.join(','); if (seen.has(k)) continue; seen.add(k); top.push(c); if (top.length >= 8) break; }
    renderRows();
  }

  // ---------- 节点详情（接管点击，避免与基座选中态打架） ----------
  function showNode(id) {
    const n = NODE[id] || {}, s = num(id), outs = OUT[id] || [];
    document.getElementById('qnode').innerHTML =
      '<b>' + esc(nm(id)) + '</b>' +
      (n.official && n.official.length ? '<br><span class="qoff">' + esc(n.official.map(o => o.name).join(' / ')) + '</span>' : '') +
      '<br>' + s.dmg + ' 伤 · ' + s.struct + ' 结 · ' + s.hits + ' 击' + (s.kd ? ' · 击倒' : '') +
      '<br>' + (outs.length
        ? outs.map(o => '<span class="qedge">' + esc(o.ins.join('/')) + ' → ' + esc(nm(o.t)) + (o.cond ? '（条件）' : '') + '</span>').join('')
        : '<span class="qhint">无配置内后继（收尾型）</span>') +
      '<div class="qact"><button id="qstart">以它为起点</button></div>';
    document.getElementById('qstart').onclick = () => {
      const list = collect(id, 6);
      list.forEach(c => { c.score = score(c, QE[S.enemy] || {}); });
      list.sort((a, b) => b.score - a.score);
      const seen = new Set(); top = [];
      for (const c of list) { const k = c.ids.join(','); if (seen.has(k)) continue; seen.add(k); top.push(c); if (top.length >= 8) break; }
      renderRows();
    };
    hl([id]);
  }

  // ---------- 启动 ----------
  const css = document.createElement('style');
  css.textContent = `
  body{padding-left:306px}
  #clear,#audit,#help-toggle,.page-brand #page-switch{display:none!important}
  #qpanel{position:fixed;left:0;top:0;bottom:0;width:306px;background:#f4f2ec;border-right:1px solid #d8d4c6;z-index:90;overflow:auto;font:13px/1.5 -apple-system,"Segoe UI","Microsoft YaHei",sans-serif;color:#25372d;padding:14px 14px 40px}
  #qpanel .qh{font-size:17px;font-weight:700;margin-bottom:12px;color:#1d3a2b}
  #qpanel .qb{margin-bottom:14px}
  #qpanel label{display:block;font-size:11px;letter-spacing:2px;color:#6f7a6d;margin-bottom:6px}
  #qpanel select{width:100%;padding:6px 8px;border:1px solid #bdcdb9;border-radius:8px;background:#fffef9;color:#25372d;font-size:13px}
  #qpanel .qthr{font-size:11.5px;color:#5f6f5c;margin-top:8px;line-height:1.6;background:#fffef9;border:1px solid #e0dccd;border-radius:8px;padding:7px 9px}
  #qpanel .qtabs{display:flex;flex-wrap:wrap;gap:6px}
  #qpanel .qtabs button{border:1px solid #bdcdb9;background:#fffef9;border-radius:999px;padding:4px 11px;font-size:12px;color:#3d5344;cursor:pointer}
  #qpanel .qtabs button.on{background:#2e5740;border-color:#2e5740;color:#f4f2ec}
  #qpanel .qhint{font-size:11.5px;color:#7b8578;margin-top:6px;line-height:1.55}
  #qpanel .qwr{display:flex;align-items:center;gap:8px;margin:4px 0}
  #qpanel .qwr span{width:34px;font-size:12px;color:#4d5f4e}
  #qpanel .qwr input{flex:1}
  #qpanel .qwr b{width:24px;text-align:right;font-weight:600;font-size:12px;color:#2e5740}
  #qpanel .qrow{border:1px solid #dcd8ca;background:#fffef9;border-radius:9px;padding:7px 9px;margin-bottom:6px;cursor:pointer;font-size:12px;line-height:1.5}
  #qpanel .qrow:hover{border-color:#9fb79c;background:#f7fbf5}
  #qpanel .qrow.on{border-color:#c0392b;box-shadow:0 0 0 1px #c0392b inset}
  #qpanel .qrow b{color:#2e5740;margin-right:6px}
  #qpanel .qrow i{display:block;color:#8a9587;font-style:normal;font-size:11px;margin-top:2px}
  #qpanel .qrow .qloop{color:#a06a2c}
  #qpanel .qoff{color:#8a6a3c;font-size:11px}
  #qpanel .qedge{display:inline-block;background:#f0f4e9;border-radius:5px;padding:1px 6px;margin:2px 4px 0 0;font-size:11px;color:#3d5344}
  #qpanel .qact{margin-top:8px}
  #qpanel .qact button{border:1px solid #2e5740;background:#2e5740;color:#f4f2ec;border-radius:7px;padding:4px 10px;font-size:12px;cursor:pointer}
  #nodes .node.q-hl rect{fill:#eef6ea;stroke:#c0392b;stroke-width:3}
  #edges path.q-hl{stroke:#c0392b!important;stroke-width:3!important;opacity:1!important}
  `;
  document.head.appendChild(css);
  buildPanel();
  draw();

  // 接管节点交互：基座自带的悬停/选中高亮让位给路径高亮
  document.querySelectorAll('header .tools button, header .tools span').forEach(el => {
    const t = el.textContent.trim();
    if (/编辑布局|默认布局|覆盖与待核|说明|取消选择/.test(t)) el.style.display = 'none';
  });
  const nodesG = document.getElementById('nodes');
  if (nodesG) {
    ['click', 'pointerdown', 'mouseover', 'pointerover', 'focusin'].forEach(t =>
      nodesG.addEventListener(t, ev => {
        const g = ev.target.closest && ev.target.closest('.node');
        if (!g) return;
        ev.stopPropagation();
        if (t === 'click') showNode(+g.dataset.node);
      }, true));
  }
  setInterval(() => { if (lastIds) hl(lastIds); }, 600);
})();
