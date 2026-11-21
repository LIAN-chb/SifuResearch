"""导出敌人档案：原型/版本中文名、防御反应图（反击/弹反/闪避/格挡）与攻击记忆阈值。

数据来源：
- 本地化 zh-Hans.json（General_* 与 ArchetypeVersion_*）
- inventory/tagged-objects.json.gz 中的 *_ContextualDefense.uasset（AIContextualDefense 影响图）
- exports/state-reaction-settings.csv（眩晕/倒地/破防阈值）

输出：exports/enemy-defense-profiles.json
"""
import gzip
import json
import os
import re
import sys
import csv

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARCH_CN = {
    "Grunt": "喽啰",
    "BigGuy": "巨无霸",
    "FlashKick": "闪电踢",
    "FireDisciple": "弟子",
    "Bodyguard": "保镖",
    "Fajar": "法贾",
    "Sean": "肖恩",
    "Kuroki": "黑木",
    "Yang": "扬",
    "Sifu": "师父",
    "Fengjie": "凤姐",
    "Servant": "仆人",
}
VER_CN = {"Base": "基础", "Advanced": "高级", "MiniBoss": "小Boss", "Miniboss": "小Boss"}


def simple(ps):
    out = {}
    for p in ps:
        name = p["name"] + "[" + str(p.get("arrayIndex", 0)) + "]"
        v = p["value"]
        if isinstance(v, list):
            out[name] = simple(v)
        elif "arrayElements" in p:
            out[name] = [simple(e) for e in p["arrayElements"]]
        elif "tagNames" in p:
            out[name] = p["tagNames"]
        elif "reference" in p:
            out[name] = {"index": v, "reference": p["reference"]}
        elif "arrayReferences" in p:
            out[name] = p["arrayReferences"]
        elif "arrayValues" in p:
            out[name] = p["arrayValues"]
        else:
            out[name] = v
    return out


def arch_of(stem):
    for k in sorted(ARCH_CN, key=len, reverse=True):
        if stem.startswith(k):
            return k
    return None


def version_of(stem, arch):
    rest = stem[len(arch):].lstrip("_")
    for k, cn in VER_CN.items():
        if rest.startswith(k):
            return cn
    m = re.match(r"Phase(\d)", rest)
    if m:
        return f"第{m.group(1)}阶段"
    if rest:
        return rest.split("_")[0]
    return "默认"


def main():
    objs = json.load(gzip.open(os.path.join(R, "inventory/tagged-objects.json.gz"), "rt", encoding="utf-8"))
    graphs = {}
    for o in objs:
        if not o["asset"].endswith("ContextualDefense.uasset"):
            continue
        graphs.setdefault(o["asset"], []).append(o)

    profiles = []
    for asset, items in sorted(graphs.items()):
        stem = os.path.basename(asset)[: -len(".uasset")]
        arch = arch_of(stem)
        if arch is None:
            continue
        mem, struct, diff, probs, nodes = [], [], [], [], {}
        for x in items:
            cls = x["class"].split(".")[-1]
            nodes[cls] = nodes.get(cls, 0) + 1
            p = simple(x["properties"])
            if cls == "AttackMemoryInfluenceTest":
                mem.append({
                    "props": p.get("m_AttackProperties[0]") or [],
                    "hits": p.get("m_uiHitsCount[0]"),
                    "memory": p.get("m_fMemoryLimit[0]"),
                    "types": p.get("m_HitTypes[0]"),
                    "inverted": bool(p.get("m_bInverted[0]")),
                })
            elif cls == "StructureInfluenceTest":
                struct.append({"test": p.get("m_eTestType[0]"), "max": p.get("m_fValueMax[0]")})
            elif cls in ("DifficultyInfluenceTest", "GameDifficultyInfluenceTest"):
                diff.append({"test": p.get("m_eTestType[0]"), "min": p.get("m_fValueMin[0]")})
            elif cls == "AIInfluence_TestSequence" and "m_fProbability[0]" in p:
                probs.append(p["m_fProbability[0]"])
        # 纯命中记忆（Attack.Type.Hit）＝重复连打触发的防御反应
        hitmem = [m for m in mem if "Attack.Type.Hit" in (m["props"] or []) and not m["inverted"]]
        profiles.append({
            "asset": asset,
            "stem": stem,
            "arch": arch,
            "arch_cn": ARCH_CN.get(arch, arch),
            "version": version_of(stem, arch),
            "nodes": nodes,
            "has": {
                "parry_deflect": nodes.get("DefenseInfluenceNodeParryDeflect", 0),
                "dodge": nodes.get("DefenseInfluenceNodeDodge", 0),
                "avoid": nodes.get("DefenseInfluenceNodeAvoid", 0),
                "guard": nodes.get("DefenseInfluenceNodeGuard", 0),
                "counter": nodes.get("BP_AiLaunchCounterCombo_C", 0) + nodes.get("BP_AiLaunchCounterCombo_Parry_C", 0),
            },
            "hit_memory": sorted(
                {(m["hits"], m["memory"]) for m in hitmem if m["hits"] is not None},
                key=lambda t: (t[0], t[1]),
            ),
            "memory_tests": mem,
            "probabilities": sorted({round(p, 2) for p in probs}),
            "structure_tests": struct,
            "difficulty_tests": diff,
        })

    out = os.path.join(R, "exports", "enemy-defense-profiles.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(profiles, f, ensure_ascii=False, indent=2)
    print("profiles", len(profiles), "->", out)
    agg = {}
    for p in profiles:
        agg.setdefault(p["arch_cn"], []).append(p["version"])
    for k, v in agg.items():
        print(k, sorted(set(v)))


if __name__ == "__main__":
    main()
