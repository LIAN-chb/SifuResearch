"""把连招图数据注入「徒手招式板」基座，生成连招编排器页面。

基座：exports/20261029-时间轴精简-15/徒手招式板.html（保留其 SVG 正交路由、节点坐标、抽屉与时间轴）
只注入三样东西：window.QENEMIES / window.QSTATS / 覆盖层脚本（侧栏 + 路径高亮）。
"""
import io
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "exports", "20261029-时间轴精简-15", "徒手招式板.html")
GRAPH = os.path.join(ROOT, "exports", "20261119-连招编排-02", "combo-graph.json")
OVERLAY = os.path.join(ROOT, "scripts", "combo_board_overlay.js")
OUT = os.path.join(ROOT, "exports", "20261119-连招编排-02", "连招编排器.html")


def main():
    html = io.open(BASE, encoding="utf-8").read()
    data = json.load(io.open(GRAPH, encoding="utf-8"))
    overlay = io.open(OVERLAY, encoding="utf-8").read()

    enemies = []
    for e in data["enemies"]:
        enemies.append({
            "key": e.get("key"),
            "name": e.get("name"),
            "archetype": e.get("archetype"),
            "version": e.get("version"),
            "dizzy_dmg": e.get("dizzy_dmg"),
            "dizzy_hits": e.get("dizzy_hits"),
            "down_hits": e.get("down_hits"),
            "mem_trigger": e.get("mem_trigger"),
            "prob": e.get("prob"),
        })

    # 配置节点 -> 显示节点：显示节点 id 即 canonicalToDisplay 的值
    board = json.load(io.open(os.path.join(ROOT, "exports", "20261029-招式时间轴-14", "board-data.json"),
                              encoding="utf-8-sig"))
    c2d = {}
    for n in board["nodes"].values():
        c2d[str(n["id"])] = n["id"]
    # 显示节点里出现的 id（含 1001/1002/1003 这类虚拟节点）
    disp_ids = set()
    for m in data["graph"]["edges"]:
        disp_ids.add(m["s"]); disp_ids.add(m["t"])

    stats = {}
    for nid, rec in data["nodes"].items():
        agg = rec.get("agg") or {}
        stats[str(nid)] = {
            "dmg": agg.get("dmg") or 0,
            "struct": agg.get("struct") or 0,
            "sdiz": agg.get("sdiz") or 0,
            "hits": agg.get("hits") or 0,
            "kd": bool(rec.get("kd")),
            "push": bool(rec.get("push")),
        }

    payload = (
        "<script>window.QENEMIES=" + json.dumps(enemies, ensure_ascii=False) + ";\n"
        "window.QSTATS=" + json.dumps(stats, ensure_ascii=False) + ";</script>\n"
        "<script>\n" + overlay + "\n</script>\n"
    )
    assert "</html>" in html
    html = html.replace("</html>", payload + "</html>", 1)
    io.open(OUT, "w", encoding="utf-8").write(html)
    print("enemies:", len(enemies), "stats:", len(stats))
    print("out:", OUT, len(html), "bytes")


if __name__ == "__main__":
    main()
