from pathlib import Path
p=Path(__file__).resolve().parents[2]/'scripts/player_graph_editor.js';s=p.read_text(encoding='utf-8')
s=s.replace("save();status(projected.changed?", "if(save())status(projected.changed?")
s=s.replace("{save();status('旧布局已就近入格，原布局可导出备份');}", "{if(save())status('旧布局已就近入格，原布局可导出备份');}")
s=s.replace("restore(g.preview.positions);if(!commit(g.before))status('仍在原格');", "const moved=JSON.stringify(g.before)!==JSON.stringify(g.preview.positions);restore(g.preview.positions);if(!commit(g.before)&&!moved)status('仍在原格');")
p.write_text(s,encoding='utf-8')
