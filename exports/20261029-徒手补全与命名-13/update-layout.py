from pathlib import Path
R=Path(__file__).resolve().parents[2]
p=R/'scripts/build_player_board.py';s=p.read_text(encoding='utf-8').replace("data['page']='barehands'", "data['page']='barehands'\ndata['legacyNodeIds']=[n['id'] for n in data['graph']['nodes']]");p.write_text(s,encoding='utf-8')
p=R/'scripts/player_graph_editor.js';s=p.read_text(encoding='utf-8')
s=s.replace("KEY='sifu.barehands.layout.v1'", "KEY=DATA.page==='focus'?'sifu.focus.layout.v1':'sifu.barehands.layout.v1',GRAPH=DATA.page==='focus'?'sifu-barehands-focus':'sifu-barehands'")
s=s.replace('migrationPending=false;',"migrationPending=false,migrationMessage='旧布局已就近入格，原布局可导出备份';")
s=s.replace("function validPositions(p){const ids=G.nodes.map(n=>n.id);", "function validPositions(p,ids=G.nodes.map(n=>n.id)){")
s=s.replace("graph:'sifu-barehands'", "graph:GRAPH")
start=s.index('  function importObject(');end=s.index('\n  const defaultGrid=',start)
s=s[:start]+'''  function prepareLayout(value){
    if(!value||value.schema!==SCHEMA||value.graph!==GRAPH)throw Error('布局页面不匹配，未导入');
    const all=G.nodes.map(n=>n.id),old=DATA.legacyNodeIds||[],expanded=value.signature!==sig&&value.signature===old.join(',')&&old.length>0,ids=expanded?old:all;
    if((!expanded&&value.signature!==sig)||!validPositions(value.nodes,ids))throw Error('节点集合或位置不匹配，未导入');
    const sourceModel=globalThis.createPlayerGraphCellLayout(ids);
    if(value.mode==='cells-v1'){if(!sourceModel.validate(value.nodes)||!value.cells)throw Error('格位无效，未导入');const cs=sourceModel.cells(value.nodes);if(ids.some(id=>!value.cells[id]||cs[id].col!==value.cells[id].col||cs[id].row!==value.cells[id].row))throw Error('行列与位置不一致，未导入');}
    const p={...value.nodes};if(expanded)for(const id of all)if(!p[id])p[id]={...defaults.get(id)};
    const result=cellModel.project(p);if(expanded&&value.mode==='cells-v1'&&old.some(id=>JSON.stringify(result.positions[id])!==JSON.stringify(value.nodes[id])))throw Error('无法保留旧节点格位，未导入');
    return {...result,expanded};
  }
  function preserveExpansion(value){try{localStorage.setItem(KEY+'.before-completion13',JSON.stringify(value));}catch{}backupOriginal(value);}
  function importObject(value){const projected=prepareLayout(value),before=snapshot();restore(projected.positions);snap=true;const changed=JSON.stringify(before)!==JSON.stringify(snapshot());if(changed&&!commit(before))throw Error('布局的连接空间不足，未更改当前布局');if(projected.expanded)preserveExpansion(value);else if(projected.changed)backupOriginal(value);if(save())status(projected.expanded?'已保留旧节点位置，并补入新节点':'已导入格子布局并自动保存');}
''' + s[end:]
start=s.index('  try{const oldBackup=');end=s.index('\n  // Node-sized',start)
s=s[:start]+'''  try{const oldBackup=localStorage.getItem(KEY+'.before-cells');if(oldBackup){legacyBackup=JSON.parse(oldBackup);$('export-original').disabled=false;}const stored=localStorage.getItem(KEY);if(stored){const value=JSON.parse(stored),projected=prepareLayout(value);if(projected.expanded){preserveExpansion(value);migrationPending=true;migrationMessage='已恢复旧节点位置，新动作已放入空格';}else if(projected.changed){backupOriginal(value);migrationPending=true;}restore(projected.positions);snap=true;status(projected.expanded?'已恢复旧节点位置并补入新动作':projected.changed?'旧布局已就近入格，原布局已保留备份':'已恢复上次编辑的格子布局');}}catch{status('未读取到匹配布局；原浏览器记录未覆盖，可导入备份',true);}
''' + s[end:]
s=s.replace("if(save())status('旧布局已就近入格，原布局可导出备份')", "if(save())status(migrationMessage)")
s=s.replace("function setEditing(value){editing=", "function setEditing(value){hideTooltip();editing=")
s=s.replace("a.download='sifu-barehands-layout.json'", "a.download=DATA.page==='focus'?'sifu-barehands-focus-layout.json':'sifu-barehands-layout.json'")
p.write_text(s,encoding='utf-8')
