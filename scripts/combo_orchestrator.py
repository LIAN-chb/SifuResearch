#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
徒手连招编排器 (BareHands Combo Orchestrator)
=================================================
基于《师父》静态解包数据装配"统一招式表", 并按敌人原型与目标状态编排推荐连招链。

数据输入 (relative to workspace root E:\\ProgrameFiles\\SifuResearch):
  exports/20261029-招式时间轴-14/board-data.json      徒手连招树 (57 节点/边/入口/组)
  exports/mainchar-hitbox-windows.json                判定窗口 (攻击资产 -> 判定行 + 帧区间)
  exports/hit-impact-values.csv                       判定冲击值 (OnHit/OnGuard/OnDeflect)
  exports/20261029-招式时间轴-14/timing-data.json     招式时序 (预备段/命中帧)
  exports/state-reaction-settings.csv                 敌人状态反应阈值 (眩晕/倒地/破防)
  exports/state-resistance-matrices.csv               状态抗性矩阵
  exports/20261029-招式时间轴-14/availability-layers.json  输入可用性层 (参考)

数据输出 (exports/20261119-连招编排-01/):
  move-table.json     统一招式表 (每节点: 入口/出边/收尾/命中汇总/时序/判定窗口)
  enemies.json        敌人原型阈值 (眩晕/倒地/破防)
  chains.json         编排结果 (按 敌人原型 x 目标 分组)
  推荐连招表.md       Markdown 推荐表
  README.md           说明文档

声明:
  - 全部数值来自静态配置, 未游戏实测; 命中数值为按配置累加/取最值的静态估计。
  - 连招树只证明"配置衔接" (100% 概率边), 不保证敌人不格挡/不闪避。
  - 眩晕/破防阈值口径未实测, 命中数与结构伤害仅作静态参考。
"""

import json
import os
import sys
from collections import defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOARD = os.path.join(ROOT, "exports", "20261029-招式时间轴-14", "board-data.json")
HITBOX = os.path.join(ROOT, "exports", "mainchar-hitbox-windows.json")
IMPACT = os.path.join(ROOT, "exports", "hit-impact-values.csv")
TIMING = os.path.join(ROOT, "exports", "20261029-招式时间轴-14", "timing-data.json")
REACTION = os.path.join(ROOT, "exports", "state-reaction-settings.csv")
RESIST = os.path.join(ROOT, "exports", "state-resistance-matrices.csv")
AVAIL = os.path.join(ROOT, "exports", "20261029-招式时间轴-14", "availability-layers.json")

OUT_DIR = os.path.join(ROOT, "exports", "20261119-连招编排-01")

# ---------------------------------------------------------------------------
# 显示映射
# ---------------------------------------------------------------------------
EDGE_INPUT_LABEL = {
    "EComboTransition::Light": "轻",
    "EComboTransition::Heavy": "重",
    "EComboTransition::LightAlt": "轻(Alt)",
    "EComboTransition::HeavyAlt": "重(Alt)",
}
ENTRY_LABEL = {
    "Light": "轻击", "Heavy": "重击",
    "LightHold": "长按轻(破防)", "HeavyHold": "长按重(蓄力)",
    "LightFront": "前轻", "HeavyFront": "前重",
    "LightFrontFront": "前前轻(冲刺)", "HeavyFrontFront": "前前重(冲刺)",
    "LightBackFront": "后前轻(掌推)", "HeavyBackFront": "后前重(扫腿)",
    "LightAlt": "轻(交替)", "HeavyAlt": "重(交替)",
    "DodgeAttack": "闪避攻击", "Disengage": "后撤拉开",
    "HeavyGuard": "格挡重击", "AttackKnockdown": "击倒追击",
    "AttackKnockdownHold": "长按追击(沉重击)",
}
GROUP_LABEL = {
    "light": "轻击组", "heavy": "重击组", "mixed": "混合组",
    "direction": "方向组", "charge": "蓄力组", "situation": "情境组",
}

# 中文输入标签 -> rawInput (用于连段验证/渲染)
LABEL_RAW = {v: k for k, v in ENTRY_LABEL.items()}
LABEL_RAW.update({
    "轻": "Light", "重": "Heavy", "轻(Alt)": "LightAlt", "重(Alt)": "HeavyAlt",
    "前前轻": "LightFrontFront", "前前重": "HeavyFrontFront",
    "后前轻": "LightBackFront", "后前重": "HeavyBackFront",
    "长按轻": "LightHold", "长按重": "HeavyHold",
    "闪避攻击": "DodgeAttack", "后撤拉开": "Disengage",
    # starts 里的中文输入标签
    "轻击": "Light", "重击": "Heavy", "长按重击": "HeavyHold",
    "奔跑轻击": "LightRushAttack", "奔跑重击": "HeavyRushAttack",
})
# board 全局缓存(验证函数使用)
BOARD_CACHE = {}

# 击倒/收尾约定: 无出边节点 + 已知击倒类技能标签
KNOWN_KNOCKDOWN_SKILLS = (
    "MultiHit", "SpinHighKick", "CrookedFoot", "InvertPosition",
    "DizzyPunch", "Disengage",
)
FINISHER_NAMES = set()  # 由构建填充: 无无条件出边的节点


# ---------------------------------------------------------------------------
# 装载
# ---------------------------------------------------------------------------
def load_json(path, default=None):
    for enc in ("utf-8-sig", "utf-8"):
        try:
            with open(path, encoding=enc) as f:
                return json.load(f)
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    if default is not None:
        return default
    raise RuntimeError("cannot load json: " + path)


def load_csv_rows(path):
    import csv
    with open(path, encoding="utf-8-sig", newline="") as f:
        rd = csv.reader(f)
        hdr = next(rd)
        return hdr, list(rd)


def ref_to_asset(ref):
    """/Game/DB/.../TableName.TableName -> Sifu/Content/DB/.../TableName.uasset"""
    if not ref or not ref.startswith("/Game/"):
        return None
    stem = ref[len("/Game/"):].split(".")[0]
    return "Sifu/Content/" + stem + ".uasset"


def fval(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return 0.0


def ival(s):
    try:
        return int(float(s))
    except (TypeError, ValueError):
        return 0


# ---------------------------------------------------------------------------
# 冲击值索引
# ---------------------------------------------------------------------------
def build_impact_index():
    """{(asset, row, outcome): {dmg, struct, sdiz, stun, kb, freeze}}"""
    hdr, rows = load_csv_rows(IMPACT)
    idx = {}
    # columns: 0 asset 1 row 2 outcome 3 useDmg 4 dmg 5 useStruct 6 struct
    # 7 useSdiz 8 sdiz 9 useStun 10 stun 11 useKb 12 kb 13 useFreeze 14 freeze
    for r in rows:
        key = (r[0], r[1], r[2])
        idx[key] = {
            "dmg": fval(r[4]) if r[3] == "True" else 0.0,
            "struct": fval(r[6]) if r[5] == "True" else 0.0,
            "sdiz": fval(r[8]) if r[7] == "True" else 0.0,
            "stun": ival(r[10]) if r[9] == "True" else 0,
            "kb": fval(r[12]) if r[11] == "True" else 0.0,
            "freeze": ival(r[14]) if r[13] == "True" else 0,
        }
    return idx


# ---------------------------------------------------------------------------
# 敌人原型阈值
# ---------------------------------------------------------------------------
def build_enemies():
    hdr, rows = load_csv_rows(REACTION)
    per = defaultdict(dict)
    for r in rows:
        asset, reaction = r[0], r[1]
        per[asset][reaction] = {
            "max_dmg": fval(r[6]),
            "max_hits": ival(r[7]),
            "persistent": r[9] == "True" if len(r) > 9 else False,
            "priority": ival(r[10]) if len(r) > 10 else 0,
            "super_layer": ival(r[11]) if len(r) > 11 and r[11] else None,
            "duration": fval(r[15]) if len(r) > 15 and r[15] else None,
        }

    # 抗性矩阵: 每 asset 各状态 抗性列
    hdr2, rows2 = load_csv_rows(RESIST)
    resist = defaultdict(dict)
    for r in rows2:
        if len(r) < 5:
            continue
        resist[r[0]][r[2]] = {
            "knockdown": ival(r[3]), "push": ival(r[4]), "dizzy": ival(r[5]),
        }

    enemies = {}
    order = []
    for asset, d in sorted(per.items()):
        short = asset.split("/")[-1].replace(".uasset", "")
        dz = d.get("m_DizzyReaction", {})
        dn = d.get("m_DownReaction", {})
        sb = d.get("m_StructureBrokenReaction", {})
        sdz = d.get("m_SuperDizzyReaction", {})
        entry = {
            "asset": asset,
            "name": short,
            "dizzy": {
                "threshold_damage": dz.get("max_dmg"),
                "threshold_hits": dz.get("max_hits"),
                "persistent": dz.get("persistent"),
                "super_layer": dz.get("super_layer"),
            },
            "down": {
                "threshold_hits": dn.get("max_hits"),
                "threshold_damage": dn.get("max_dmg"),
            },
            "structure_broken": {
                "duration": sb.get("duration"),
            },
            "super_dizzy": {
                "duration": sdz.get("duration"),
            },
            "resistance": resist.get(asset, {}),
        }
        enemies[asset] = entry
        order.append((short, asset, entry))
    return enemies, order


# ---------------------------------------------------------------------------
# 统一招式表
# ---------------------------------------------------------------------------
def build_move_table(board, impact_idx, timing):
    nodes = board["nodes"]
    defaults = board.get("defaults", [])
    starts = board.get("starts", [])
    groups = board.get("groups", {})

    # entry inputs by node
    entry_by_node = defaultdict(list)
    for d in defaults:
        if d.get("target") is not None and not d.get("fallback"):
            entry_by_node[str(d["target"])].append(d)
    entry_by_state = defaultdict(list)
    for s in starts:
        entry_by_state[str(s.get("target"))].append(s)

    hw_index = defaultdict(list)
    for h in load_json(HITBOX, default=[]):
        hw_index[h["attack_db"]].append(h)

    t_attacks = timing.get("attacks", {}) if isinstance(timing, dict) else {}
    t_special = timing.get("specialHitActions", []) if isinstance(timing, dict) else []

    node_group = defaultdict(list)
    for gname, ids in groups.items():
        for nid in ids:
            node_group[str(nid)].append(gname)

    table = {}
    hit_counts = defaultdict(int)

    for nid, nd in nodes.items():
        raw = nd.get("rawName", "")
        official = None
        if nd.get("official"):
            official = nd["official"][0].get("name") or nd["official"][0].get("en")
        # 渲染层 name 字段(中文)优先于 rawName
        disp = nd.get("name") or raw

        variants = []
        var_used = None
        for v in nd.get("variants", []):
            asset = v.get("asset", "")
            var_used = var_used or (asset or None)
            hbx = hw_index.get(asset, [])
            tim = t_attacks.get(asset)
            rows = []
            for h in hbx:
                p = h.get("properties", {})
                hr = (p.get("m_HitRow[0]") or {})
                row_name = (hr.get("RowName[0]") or "")
                ref = (hr.get("DataTable[0]") or {}).get("reference")
                tbl = ref_to_asset(ref)
                fr = ((p.get("m_FrameRange[0]") or {}).get("m_Anim[0]") or {})
                lo = fr.get("LowerBound[0]") or {}
                hi = fr.get("UpperBound[0]") or {}
                frange = [
                    lo.get("Value[0]") if lo.get("Type[0]") != "ERangeBoundTypes::Open" else None,
                    hi.get("Value[0]") if hi.get("Type[0]") != "ERangeBoundTypes::Open" else None,
                ]
                row_data = {
                    "row": row_name,
                    "table": tbl,
                    "frame": frange,
                    "target": p.get("m_eHitTarget[0]"),
                }
                if tbl and row_name:
                    onhit = impact_idx.get((tbl, row_name, "m_OnHitImpact"))
                    onguard = impact_idx.get((tbl, row_name, "m_OnGuardImpact"))
                    ondeflect = impact_idx.get((tbl, row_name, "m_OnDeflectImpact"))
                    row_data["impacts"] = {
                        "hit": onhit, "guard": onguard, "deflect": ondeflect,
                    }
                rows.append(row_data)
                hit_counts[(tbl, row_name)] += 1
            variants.append({
                "asset": asset,
                "timing": {
                    "wanted_buildup": (tim or {}).get("wantedBuildupFrames"),
                    "last_buildup": (tim or {}).get("lastBuildupFrame"),
                    "hit_marker": (tim or {}).get("hitMarkerFrame"),
                    "anim_row": (tim or {}).get("animationRow"),
                } if tim else None,
                "hitboxes": rows,
            })

        # 汇总: 首个含命中数据的变体为准; 若首个无数据则取第一个有数据的
        rep = None
        for v in variants:
            if v["hitboxes"]:
                rep = v
                break
        if rep is None:
            rep = variants[0] if variants else None
        agg = {"hits": 0, "dmg": 0.0, "struct": 0.0, "sdiz": 0.0,
               "stun": 0, "kb": 0.0, "freeze": 0, "targets": [], "frame": [None, None]}
        if rep:
            for hb in rep["hitboxes"]:
                imp = ((hb.get("impacts") or {}).get("hit")) or {}
                if imp:
                    agg["hits"] += 1
                    agg["dmg"] += imp.get("dmg", 0.0)
                    agg["struct"] += imp.get("struct", 0.0)
                    agg["sdiz"] += imp.get("sdiz", 0.0)
                    agg["stun"] = max(agg["stun"], imp.get("stun", 0))
                    agg["kb"] = max(agg["kb"], imp.get("kb", 0.0))
                    agg["freeze"] = max(agg["freeze"], imp.get("freeze", 0))
                if hb.get("target"):
                    agg["targets"].append(hb["target"])
                fr = hb.get("frame") or []
                if len(fr) == 2:
                    if agg["frame"][0] is None or (fr[0] is not None and fr[0] < agg["frame"][0]):
                        agg["frame"][0] = fr[0]
                    if agg["frame"][1] is None or (fr[1] is not None and fr[1] > agg["frame"][1]):
                        agg["frame"][1] = fr[1]

        edges = []
        has_uncond = False
        for e in nd.get("edges", []):
            cond = bool(e.get("conditional"))
            if not cond:
                has_uncond = True
            edges.append({
                "to": str(e.get("target")),
                "input": EDGE_INPUT_LABEL.get(e.get("rawInput"), e.get("rawInput")),
                "rawInput": e.get("rawInput"),
                "conditional": cond,
                "condition_ref": (e.get("condition") or {}).get("reference"),
            })

        entry = []
        for d in entry_by_node.get(nid, []):
            entry.append({"kind": "input", "label": ENTRY_LABEL.get(d.get("rawInput"), d.get("rawInput")), "rawInput": d.get("rawInput")})
        for s in entry_by_state.get(nid, []):
            entry.append({"kind": "state", "state": s.get("rawState"), "label": ENTRY_LABEL.get(s.get("input", ""), s.get("input")), "condition_ref": (s.get("condition") or {}).get("reference")})

        table[nid] = {
            "id": nid,
            "rawName": raw,
            "name": disp or raw,
            "official": official,
            "groups": [GROUP_LABEL.get(g, g) for g in node_group.get(nid, [])],
            "groupKeys": list(node_group.get(nid, [])),
            "tags": [str(t) for t in nd.get("tags", [])],
            "charge": nd.get("charge") or [],
            "entry": entry,
            "edges": edges,
            "has_uncond_edge": has_uncond,
            "is_finisher": not has_uncond,
            "agg": agg,
            "rep_variant_asset": rep["asset"] if rep else None,
            "variants": variants,
        }

    return table


# ---------------------------------------------------------------------------
# 编排: 链枚举
# ---------------------------------------------------------------------------
# --- v2: 指令攻击重入 -----------------------------------------------------
# v1 只沿连招树无条件边枚举(同键续按), 漏掉了两类真实衔接:
#   A. 指令攻击重入: 方向攻击(前前轻/前前重/后前轻/后前重)/蓄力/闪避攻击/拉开距离
#      是独立输入能力(defaults 入口), 与普通轻/重并列在全局输入优先级栈
#      (availability.attackAbilityInputsInPriorityOrder), 各 *_FollowUp 层排除集
#      不含方向攻击 -> 任意攻击收招窗口内可重新输入, 作为新段起手。
#   B. 状态触发衔接: 条件边(招架反击 BP_TargetIsParryVictim / 推击后
#      BP_TargetPlaysOrder / CheatCombo 等) 依赖敌人状态, 单独成节给出。
# walk_chains_v2 以"按键序列"驱动: 每步先查当前节点是否存在该输入的
# 无条件出边(边衔接), 否则若是命令键则重入 defaults 目标(命令段),
# 否则 Light/Heavy 重入 44/48 重新起手 —— 与游戏输入解析一致。

# 命令重入键(方向/蓄力/闪避/拉开/防御/起身/奔跑): 每条链中最多出现一次
COMMAND_INPUTS = [
    "LightFrontFront", "LightBackFront", "HeavyFrontFront", "HeavyBackFront",
    "LightHold", "HeavyHold", "DodgeAttack", "Disengage", "HeavyGuard",
    "AttackKnockdown", "AttackKnockdownHold", "LightRushAttack", "HeavyRushAttack",
]
COMMAND_SET = set(COMMAND_INPUTS)


def build_command_map(board):
    """defaults -> {rawInput: target_node_id_str}; 排除 fallback/无效目标"""
    cm = {}
    for d in board.get("defaults", []):
        t = d.get("target")
        if t is not None and not d.get("fallback"):
            cm[d.get("rawInput")] = str(t)
    return cm


def walk_chains_v2(table, command_map, start_id, max_depth=8,
                   max_reentries=3, max_chains=300, max_cond=2,
                   first_inputs_override=None):
    """按键序列驱动链枚举: 边衔接优先, 命令键重入开新段, Light/Heavy 兜底重入 44/48.

    三类衔接(与玩家实际输入一致):
      - edge: 无条件出边(连招树内衔接)
      - cond: 条件出边(敌人状态触发衔接, 如 BP_TargetPlaysOrder → 追亡逐北)
      - reentry: 指令攻击重入(前前轻/前前重/后前轻/重/蓄力/闪避/拉开等)

    返回链列表, 每链 {'chain':[node_id...], 'inputs':[按键label...],
      'raw_inputs':[rawInput...], 'reentries':[重入步下标...],
      'conds':[{'step':i,'ref':条件引用,'input':rawInput,...}]}
    约束: 指令重入 ≤ max_reentries; 条件边 ≤ max_cond; 单链节点不重复; 每起点 ≤ max_chains.
    """
    chains = []
    start_str = str(start_id)

    first_inputs = [(ri, ENTRY_LABEL.get(ri, ri))
                    for ri, tgt in command_map.items() if tgt == start_str]
    if first_inputs_override is not None:
        first_inputs = list(first_inputs_override)
    if not first_inputs:
        return chains

    base_keys = [("Light", "轻"), ("Heavy", "重")]
    # 命令键优先遍历(方向/蓄力/闪避), 使含指令穿插的链更早进入枚举
    all_keys = [(k, ENTRY_LABEL.get(k, k)) for k in COMMAND_INPUTS] + base_keys

    def step(node_id, raw_input):
        """优先无条件边, 其次条件边, 最后命令键重入. 输入名统一去 EComboTransition:: 前缀."""
        n = table[str(node_id)]
        want = raw_input.split("::")[-1]
        for e in n.get("edges", []):
            if not e.get("conditional") and e.get("rawInput", "").split("::")[-1] == want:
                return ("edge", e["to"], None)
        for e in n.get("edges", []):
            if e.get("conditional") and e.get("rawInput", "").split("::")[-1] == want:
                ref = e.get("condition_ref") or (e.get("condition") or {}).get("reference")
                return ("cond", e["to"], ref)
        if raw_input in command_map:
            return ("reentry", command_map[raw_input], None)
        # 命令键也可带 EComboTransition:: 前缀
        for k, v in command_map.items():
            if k.split("::")[-1] == want:
                return ("reentry", v, None)
        return None

    def record(path, seq_in, seq_label, conds):
        if path not in [c["chain"] for c in chains]:
            chains.append({"chain": list(path), "inputs": list(seq_label),
                           "raw_inputs": list(seq_in),
                           "reentries": [i for i, ri in enumerate(seq_in)
                                         if ri in COMMAND_SET and i > 0],
                           "conds": list(conds)})

    def dfs(node, seq_in, seq_label, used_cmds, path, n_reentry, conds):
        if len(chains) >= max_chains:
            return
        if len(path) >= max_depth:
            record(path, seq_in, seq_label, conds)
            return
        progressed = False
        for ri, lab in all_keys:
            if ri in used_cmds:
                continue
            nxt = step(node, ri)
            if nxt is None:
                if ri in ("Light", "Heavy") and ri in command_map:
                    t = command_map[ri]
                    if str(t) not in path and n_reentry < max_reentries:
                        nxt = ("reentry", t, None)
                    else:
                        continue
                else:
                    continue
            kind, to, ref = nxt
            if kind == "reentry" and n_reentry >= max_reentries:
                continue
            if kind == "cond" and len(conds) >= max_cond:
                continue
            if kind == "cond" and not ref:
                continue  # 无引用的条件边不采信
            if str(to) in path:
                continue
            new_used = set(used_cmds)
            if ri in COMMAND_SET:
                new_used.add(ri)
            new_conds = conds + ([{"step": len(path), "ref": ref,
                                   "input": ri, "label": lab}] if kind == "cond" else [])
            progressed = True
            dfs(str(to), seq_in + [ri], seq_label + [lab], new_used,
                path + [str(to)], n_reentry + (1 if kind == "reentry" else 0),
                new_conds)
            if len(chains) >= max_chains:
                return
        if not progressed and path:
            record(path, seq_in, seq_label, conds)

    for ri, lab in first_inputs:
        dfs(start_str, [ri], [lab], {ri} if ri in COMMAND_SET else set(),
            [start_str], 0, [])
        if len(chains) >= max_chains:
            break
    return chains


# 旧版: 仅沿无条件边(保留用于对比)
def walk_chains(table, start_id, max_depth=8):
    """从 start 沿无条件出边走, 生成所有简单链 (不重复节点)."""
    chains = []

    def dfs(nid, path):
        n = table[str(nid)]
        nxt = [e for e in n["edges"] if not e["conditional"]]
        if not nxt:
            chains.append(list(path))
            return
        cont = False
        for e in nxt:
            to = e["to"]
            if to in path:
                continue
            if len(path) >= max_depth:
                continue
            cont = True
            dfs(to, path + [(to, e["input"])])
        if not cont:
            chains.append(list(path))

    dfs(start_id, [(str(start_id), None)])
    return chains


def chain_stats_v2(table, chain_rec):
    """v2 链: {'chain':[ids], 'inputs':[...], 'raw_inputs':[...], 'reentries':[idx]}"""
    tot = {"hits": 0, "dmg": 0.0, "struct": 0.0, "sdiz": 0.0,
           "stun": 0, "kb": 0.0, "freeze": 0, "buildup": 0}
    steps = []
    ids = chain_rec["chain"]
    inputs = chain_rec["inputs"]
    for i, nid in enumerate(ids):
        n = table[str(nid)]
        agg = n["agg"]
        for k in ("hits", "dmg", "struct", "sdiz", "kb"):
            tot[k] += agg[k]
        tot["stun"] = max(tot["stun"], agg["stun"])
        tot["freeze"] = max(tot["freeze"], agg["freeze"])
        b = 0
        if n["rep_variant_asset"]:
            for v in n["variants"]:
                if v["asset"] == n["rep_variant_asset"] and v["timing"]:
                    b = v["timing"].get("wanted_buildup") or 0
                    break
        tot["buildup"] += b
        inp = inputs[i] if i < len(inputs) else None
        steps.append({
            "id": nid, "input": inp,
            "name": n["name"], "raw": n["rawName"], "official": n["official"],
            "groups": n["groupKeys"], "is_finisher": n["is_finisher"],
            "hits": agg["hits"], "dmg": agg["dmg"], "struct": agg["struct"],
            "sdiz": agg["sdiz"], "stun": agg["stun"], "kb": agg["kb"],
            "freeze": agg["freeze"], "frame": agg["frame"],
            "tags": n["tags"], "reentry": i in chain_rec["reentries"],
        })
    return tot, steps


def score_chains_v2(chains, table, enemy, goal):
    scored = []
    for ch in chains:
        tot, steps = chain_stats_v2(table, ch)
        first = steps[0]
        if goal == "dizzy":
            th_d = enemy["dizzy"].get("threshold_damage") or 0
            th_h = enemy["dizzy"].get("threshold_hits") or 0
            hit_ratio = 0.0
            if th_h > 0:
                hit_ratio = tot["hits"] / th_h
            score = (0.0 if (th_h > 0 and tot["hits"] >= th_h) else -10.0) \
                + hit_ratio * 5.0 \
                + min(tot["sdiz"] / max(th_d, 1), 2.0) + tot["dmg"] / 100.0
        elif goal == "struct":
            score = tot["struct"] * 2.0 + tot["dmg"] / 50.0
        elif goal == "damage":
            score = tot["dmg"] * 2.0 + tot["sdiz"] / 10.0
        elif goal == "knockdown":
            score = 0.0
            last = steps[-1]
            if last["is_finisher"]:
                score += 8.0 + tot["kb"] / 50.0 + last["kb"] / 100.0
            score += tot["kb"] / 200.0
        else:
            score = tot["dmg"] + tot["struct"]
        # 重入步小加分(指令穿插是玩家常用技能)
        score += 0.5 * len(ch["reentries"])
        scored.append({
            "chain": [s["id"] for s in steps],
            "inputs": ch["inputs"],
            "raw_inputs": ch["raw_inputs"],
            "reentries": ch["reentries"],
            "conds": ch.get("conds") or [],
            "steps": steps,
            "totals": tot,
            "entry_state": None,
            "entry_input": first.get("input"),
            "finisher": steps[-1]["name"] if steps[-1]["is_finisher"] else None,
            "has_conditional": any(e["conditional"] for s in steps for e in table[s["id"]]["edges"] if not s["is_finisher"]),
            "score": round(score, 2),
            "goal": goal,
        })
    scored.sort(key=lambda x: -x["score"])
    return scored


def state_chains_v2(table, starts, max_depth=8):
    """状态入口链: 从每个 starts 目标节点沿线枚举(带状态标签), 供状态衔接节使用.

    返回 {state_name: [ (entry_node, inputs_label, chain_ids) ... ]}
    """
    out = defaultdict(list)
    for s in starts:
        tgt = s.get("target")
        if tgt is None:
            continue
        state = s.get("rawState") or s.get("start") or "?"
        node = table.get(str(tgt))
        if not node:
            continue
        # 从该节点沿无条件边枚举简单链
        chains = []
        def dfs(nid, path):
            n = table[str(nid)]
            nxt = [e for e in n["edges"] if not e["conditional"]]
            if not nxt or len(path) >= max_depth:
                chains.append(list(path))
                return
            for e in nxt:
                to = e["to"]
                if to in path:
                    continue
                dfs(to, path + [to])
        dfs(str(tgt), [str(tgt)])
        for ch in chains:
            out[state].append({
                "start": node["name"],
                "start_input": s.get("input"),
                "sequence": ch,
            })
    return dict(out)


# 旧版: 仅沿无条件边(保留用于对比 v1)
def chain_stats(table, chain, fictive=None):
    """累加链上各节点代表变体命中汇总."""
    tot = {"hits": 0, "dmg": 0.0, "struct": 0.0, "sdiz": 0.0,
           "stun": 0, "kb": 0.0, "freeze": 0, "buildup": 0}
    steps = []
    for i, (nid, inp) in enumerate(chain):
        n = table[str(nid)]
        agg = n["agg"]
        for k in ("hits", "dmg", "struct", "sdiz", "kb"):
            tot[k] += agg[k] if k != "kb" else agg[k]
        tot["stun"] = max(tot["stun"], agg["stun"])
        tot["freeze"] = max(tot["freeze"], agg["freeze"])
        b = 0
        if n["rep_variant_asset"]:
            for v in n["variants"]:
                if v["asset"] == n["rep_variant_asset"] and v["timing"]:
                    b = v["timing"].get("wanted_buildup") or 0
                    break
        tot["buildup"] += b
        steps.append({
            "id": nid, "input": inp or (n["entry"][0]["label"] if n["entry"] else None),
            "name": n["name"], "raw": n["rawName"], "official": n["official"],
            "groups": n["groupKeys"], "is_finisher": n["is_finisher"],
            "hits": agg["hits"], "dmg": agg["dmg"], "struct": agg["struct"],
            "sdiz": agg["sdiz"], "stun": agg["stun"], "kb": agg["kb"],
            "freeze": agg["freeze"], "frame": agg["frame"],
            "tags": n["tags"],
        })
    return tot, steps


# ---------------------------------------------------------------------------
# 目标评分与推荐
# ---------------------------------------------------------------------------
def score_chains(chains, table, enemy, goal):
    scored = []
    for ch in chains:
        tot, steps = chain_stats(table, ch)
        first = steps[0]
        entry_kind = first.get("groups", [])[:1]
        # 目标相关指标
        if goal == "dizzy":
            th_d = enemy["dizzy"].get("threshold_damage") or 0
            th_h = enemy["dizzy"].get("threshold_hits") or 0
            reach_d = (th_d > 0 and tot["struct"] + tot["sdiz"] >= th_d)
            reach_h = (th_h > 0 and tot["hits"] >= th_h)
            hit_ratio = 0.0
            if th_h > 0:
                hit_ratio = tot["hits"] / th_h
            # 分: 优先少命中数到达; 命中数占比高; 其次特殊眩晕总量; 再次伤害
            score = (0.0 if reach_h else -10.0) + hit_ratio * 5.0 \
                + min(tot["sdiz"] / max(th_d, 1), 2.0) + tot["dmg"] / 100.0
        elif goal == "struct":
            score = tot["struct"] * 2.0 + tot["dmg"] / 50.0
        elif goal == "damage":
            score = tot["dmg"] * 2.0 + tot["sdiz"] / 10.0
        elif goal == "knockdown":
            score = 0.0
            last = steps[-1]
            if last["is_finisher"]:
                score += 8.0 + tot["kb"] / 50.0 + last["kb"] / 100.0
            score += tot["kb"] / 200.0
        else:
            score = tot["dmg"] + tot["struct"]

        scored.append({
            "chain": [s["id"] for s in steps],
            "steps": steps,
            "totals": tot,
            "entry_state": None,
            "entry_input": first.get("input"),
            "finisher": steps[-1]["name"] if steps[-1]["is_finisher"] else None,
            "has_conditional": any(e["conditional"] for s in steps for e in table[s["id"]]["edges"] if not s["is_finisher"]),
            "score": round(score, 2),
            "goal": goal,
        })
    scored.sort(key=lambda x: -x["score"])
    return scored


def main():
    global BOARD_CACHE
    print("== 徒手连招编排器 ==")
    os.makedirs(OUT_DIR, exist_ok=True)
    board = load_json(BOARD)
    BOARD_CACHE = board
    impact_idx = build_impact_index()
    timing = load_json(TIMING, default={})
    print("board nodes:", len(board["nodes"]), " edges:", sum(len(n.get("edges", [])) for n in board["nodes"].values()))

    table = build_move_table(board, impact_idx, timing)
    enemies, enemy_order = build_enemies()

    # 覆盖报告
    n_with_data = sum(1 for n in table.values() if n["agg"]["hits"] > 0)
    n_finisher = sum(1 for n in table.values() if n["is_finisher"])
    print(f"moves: {len(table)} | with hit data: {n_with_data} | finishers: {n_finisher}")
    no_data = [n["id"] for n in table.values() if n["agg"]["hits"] == 0]
    print("nodes without hit data:", no_data)

    # 起始入口: 默认输入 (target 有效) 与 状态入口
    starts = board.get("starts", [])
    defaults = board.get("defaults", [])
    start_nodes = {}
    for d in defaults:
        t = d.get("target")
        if t is not None and not d.get("fallback"):
            start_nodes.setdefault(str(t), {"kind": "input", "label": ENTRY_LABEL.get(d.get("rawInput"), d.get("rawInput"))})
    for s in starts:
        t = s.get("target")
        if t is not None:
            start_nodes.setdefault(str(t), {"kind": "state", "state": s.get("rawState"),
                                            "label": ENTRY_LABEL.get(s.get("input", ""), s.get("input"))})

    # 敌人档案输出
    enemies_out = {}
    for e in enemies.values():
        enemies_out[e["name"]] = e
    with open(os.path.join(OUT_DIR, "enemies.json"), "w", encoding="utf-8") as f:
        json.dump(enemies_out, f, ensure_ascii=False, indent=1)

    # 招式表输出
    with open(os.path.join(OUT_DIR, "move-table.json"), "w", encoding="utf-8") as f:
        json.dump({k: {kk: vv for kk, vv in v.items() if kk != "variants"} for k, v in table.items()},
                  f, ensure_ascii=False, indent=1)

    # 编排 (v2: 按键序列 + 指令重入 + 状态条件衔接)
    goals = ["dizzy", "struct", "damage", "knockdown"]
    result = {"notice": "静态配置估计, 未实测", "chains": {}, "state_chains": {}}
    cmd_map = build_command_map(board)
    state_chains = state_chains_v2(table, starts)
    result["state_chains"] = state_chains

    # 参与评分的起始节点: 默认输入可达节点(输入入口) + 状态入口
    label_to_raw = {v: k for k, v in ENTRY_LABEL.items()}
    start_nodes_input = {str(d["target"]): d["rawInput"]
                         for d in defaults if d.get("target") is not None and not d.get("fallback")}
    state_entries = []
    seen_state_entry = set()
    for s in starts:
        tgt = s.get("target")
        if tgt is None:
            continue
        lab = s.get("input") or ""
        raw = label_to_raw.get(lab, lab)
        k = (str(tgt), raw, s.get("rawState"))
        if k in seen_state_entry:
            continue
        seen_state_entry.add(k)
        state_entries.append({"node": str(tgt), "raw": raw, "label": lab,
                              "state": s.get("rawState"),
                              "condition_ref": (s.get("condition") or {}).get("reference")})

    for short, asset, enemy in enemy_order:
        result["chains"][short] = {}
        for goal in goals:
            all_scored = []
            for sid, raw_inp in start_nodes_input.items():
                chains = walk_chains_v2(table, cmd_map, sid)
                sc = score_chains_v2(chains, table, enemy, goal)
                for c in sc:
                    c["entry_raw"] = raw_inp
                    c["entry_kind"] = "input"
                all_scored.extend(sc)
            for se in state_entries:
                chains = walk_chains_v2(table, cmd_map, se["node"],
                                        first_inputs_override=[(se["raw"], se["label"])])
                sc = score_chains_v2(chains, table, enemy, goal)
                for c in sc:
                    c["entry_raw"] = se["raw"]
                    c["entry_kind"] = "state"
                    c["entry_state"] = se["state"]
                    if se["condition_ref"]:
                        c["conds"] = ([{"step": -1, "ref": se["condition_ref"],
                                        "input": se["raw"], "label": se["label"]}]
                                      + (c.get("conds") or []))
                all_scored.extend(sc)
            # 去重: 相同 (chain, inputs)
            seen = set()
            uniq = []
            for c in all_scored:
                k = (tuple(c["chain"]), tuple(c.get("inputs") or []))
                if k in seen:
                    continue
                seen.add(k)
                uniq.append(c)
            uniq.sort(key=lambda x: -x["score"])
            # 注入经逐步验证的社区主流链(保证出现在推荐里且带验证标记)
            injected = []
            seen_keys = {(tuple(c["chain"]), tuple(c.get("inputs") or [])) for c in uniq}
            for title, entry_spec, seq in COMMUNITY_COMBOS:
                rec = sequence_chain(table, seq)
                if not rec:
                    continue
                sc2 = score_chains_v2([rec], table, enemy, goal)
                if not sc2:
                    continue
                c = sc2[0]
                c["title"] = title
                c["curated"] = True
                ek, _, ev = entry_spec.partition(":")
                c["entry_kind"] = ek
                c["entry_state"] = ev if ek == "state" else None
                c["entry_input"] = rec["inputs"][0] if rec["inputs"] else None
                k2 = (tuple(c["chain"]), tuple(c.get("inputs") or []))
                if k2 in seen_keys:
                    continue
                seen_keys.add(k2)
                injected.append(c)
            uniq = injected + uniq
            uniq.sort(key=lambda x: -x["score"])
            # 保证社区链一定出现在推荐前 8 条内(其余按分数)
            top = [c for c in uniq if c.get("curated")][:3]
            rest = [c for c in uniq if not c.get("curated")]
            result["chains"][short][goal] = (top + rest)[:8]

    result["stats"] = {
        "v1_chains_only_edges": True,
        "v2_input_sequence_with_reentry": True,
        "command_inputs": COMMAND_INPUTS,
    }
    with open(os.path.join(OUT_DIR, "chains.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print("chains written:", os.path.join(OUT_DIR, "chains.json"))

    # Markdown 推荐表
    md = render_markdown(table, result, enemy_order)
    with open(os.path.join(OUT_DIR, "推荐连招表.md"), "w", encoding="utf-8") as f:
        f.write(md)
    readme = render_readme()
    with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)
    print("done. outputs under", OUT_DIR)


GOAL_TITLE = {
    "dizzy": "眩晕积累 (Dizzy)",
    "struct": "结构破坏/破防 (Structure)",
    "damage": "高伤害 (Damage)",
    "knockdown": "击倒收尾 (Knockdown)",
}


def sequence_chain(table, seq):
    """按显式 (node_id, input_label) 序列构造一条链记录(用于社区主流链注入).

    返回 walk_chains_v2 同构的 dict, 或 None(某步不可达)。
    """
    chain_ids, inputs, raws, conds, reentries = [], [], [], [], []
    prev = None
    for i, (nid, lab) in enumerate(seq):
        n = table.get(str(nid))
        if not n:
            return None
        want = LABEL_RAW.get(lab, lab).split("::")[-1]
        if prev is not None:
            p = table[str(prev)]
            kind = None
            for e in p.get("edges", []):
                if not e.get("conditional") and e.get("rawInput", "").split("::")[-1] == want:
                    kind, to = "edge", e["to"]
                    break
            if kind is None:
                for e in p.get("edges", []):
                    if e.get("conditional") and e.get("rawInput", "").split("::")[-1] == want:
                        kind, to = "cond", e["to"]
                        ref = e.get("condition_ref") or (e.get("condition") or {}).get("reference")
                        break
                if kind == "cond" and ref:
                    conds.append({"step": i, "ref": ref, "input": want, "label": lab})
            if kind is None:
                cm = build_command_map(BOARD_CACHE)
                for k, v in cm.items():
                    if k.split("::")[-1] == want:
                        kind, to = "reentry", v
                        break
                if kind == "reentry":
                    reentries.append(i)
            if kind is None or str(to) != str(nid):
                return None
        chain_ids.append(str(nid))
        inputs.append(lab)
        raws.append(want)
        prev = str(nid)
    return {"chain": chain_ids, "inputs": inputs, "raw_inputs": raws,
            "reentries": reentries, "conds": conds, "curated": True}


# 社区主流连段(人工整理, 由引擎逐步验证后注入推荐; 验证结果见第三节)
COMMUNITY_COMBOS = [
    ("社区主流·杂兵处决线", "state:Default",
     [(19, "重击"), (48, "重击"), (4, "重击"), (39, "前前轻"), (32, "后前轻"), (26, "重击")]),
    ("社区主流·轻5收尾", "input:轻击",
     [(44, "轻击"), (45, "轻"), (14, "轻"), (7, "轻"), (8, "轻")]),
    ("社区主流·重4碎背肘", "input:重击",
     [(48, "重击"), (4, "重击"), (5, "重击"), (10, "重击")]),
    ("破防接扫腿", "input:长按轻",
     [(33, "长按轻"), (31, "后前重")]),
]


def canonical_chains(table):
    """通用基础链: 节点序列 + 输入序列 + 官方名备注(数据驱动计算数值)."""
    # (标题, 入口标签, [(node_id, input_label)...], 备注)
    return [
        ("轻击五连 (疾风连环)", "轻击", [(44, "轻"), (45, "轻"), (14, "轻"), (7, "轻"), (8, "轻")],
         "轻4后按轻=升龙爪(条件), 按重=回旋踢击倒"),
        ("重击四连 (碎背肘)", "重击", [(48, "重"), (4, "重"), (5, "重"), (10, "重")],
         "重4收尾为双肘/合击(碎背肘), 条件边需 CheatCombo 检查"),
        ("重击→扫腿", "重击", [(48, "重"), (4, "后前重")],
         "重2后直接接后前重(扫腿), 指令重入"),
        ("破防→轻连", "长按轻", [(33, "长按轻"), (7, "轻")],
         "破防(避短扬长)后接轻4派生"),
        ("前前轻 (袭裆拳)", "前前轻", [(39, "前前轻"), (40, "轻")],
         "袭裆拳命中后按轻接追击"),
        ("前前重 (上步重踢)", "前前重", [(36, "前前重"), (5, "重")],
         "上步重踢后按重接重3"),
        ("后前轻 (推掌/推踢)", "后前轻", [(32, "后前轻")],
         "推掌命中会把敌人推入硬直, 是追亡逐北的入口"),
        ("后前重 (扫腿)", "后前重", [(31, "后前重")],
         "扫腿直接击倒, 无后续"),
        ("招架反击·轻 (闪电击)", "招架(默认态)", [(2, "轻")],
         "招架成功(目标处于招架受击态)后轻三连"),
        ("招架反击·重 (奔雷手)", "招架(默认态)", [(19, "重")],
         "招架成功后重击(2Hits), 可接轻重入连战"),
        ("闪避攻击 (斗转星移)", "闪避", [(55, "闪避攻击")],
         "闪避攻击换位, 收尾"),
        ("倒地起身攻击", "倒地起身", [(0, "轻")],
         "倒地状态(KnockedDown)起身攻击"),
    ]


def render_markdown(table, result, enemy_order):
    lines = []
    lines.append("# 徒手连招推荐表 (基于静态配置)")
    lines.append("")
    lines.append("> 数据来源: board-data.json / hitbox-windows / hit-impact-values / timing-data / state-reaction-settings / availability-layers。")
    lines.append("> **均为静态配置估计, 未经游戏实测**。数值为按配置累加(命中)或取最值(硬直/击退/冻结)的参考,**不代表实战保证**;")
    lines.append("> 连招树只证明配置衔接, 敌人可能格挡/闪避/反制。眩晕与破防阈值为配置口径, 仅作预判参考。")
    lines.append("")
    lines.append("> 编排模型(三条衔接通道): **①树内边** 连招树保存的无条件出边; **②指令重入** 任意收招窗口内重按方向/蓄力/闪避指令(前前轻、前前重、后前轻、后前重、长按轻/重、闪避攻击、拉开), 依据 availability-layers 的输入优先栈; **③状态条件边** 敌人处于特定状态时触发的条件分支(如推掌命中后 `BP_TargetPlaysOrder` → 追亡逐北)。")
    lines.append("")

    # ---- 通用基础链条 (官方名对照, 数值数据驱动) ----
    lines.append("## 一、通用基础连段（入口 → 衔接 → 收尾）")
    lines.append("")
    lines.append("| 连段 | 入口 | 输入序列 | 伤害 | 结构 | 特殊眩晕 | 命中 | 最大硬直 | 备注 |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for title, entry_lab, steps, note in canonical_chains(table):
        tot = {"hits": 0, "dmg": 0.0, "struct": 0.0, "sdiz": 0.0, "stun": 0}
        for nid, _lab in steps:
            n = table.get(str(nid))
            if not n:
                continue
            for k in ("hits", "dmg", "struct", "sdiz"):
                tot[k] += n["agg"][k]
            tot["stun"] = max(tot["stun"], n["agg"]["stun"])
        seq = " → ".join(lab for _nid, lab in steps)
        lines.append("| {} | {} | {} | {:.0f} | {:.0f} | {:.0f} | {} | {}f | {} |".format(
            title, entry_lab, seq, tot["dmg"], tot["struct"], tot["sdiz"],
            tot["hits"], tot["stun"], note))
    lines.append("")
    lines.append("> 数值为配置累加(命中/伤害/结构/特殊眩晕)与取最大值(硬直); 未登记命中数据的节点按 0 计。")
    lines.append("")

    # ---- 二、按敌人原型 x 目标推荐链 ----
    lines.append("## 二、按敌人状态与目标的推荐连招链")
    lines.append("")
    lines.append("> 目标: **眩晕积累 / 结构破坏 / 高伤害 / 击倒收尾**。")
    lines.append("> 链格式: `节点[本次输入]`, 其中 **★**=指令重入(方向/蓄力/闪避键), **◆**=状态条件边; 收尾=无后继节点。")
    lines.append("> 数值为静态累加估计(命中)与取最值(硬直/击退/冻结)。")
    lines.append("")
    for short, asset, enemy in enemy_order:
        lines.append(f"### {short}")
        lines.append("")
        dz = enemy.get("dizzy") or {}
        sb = enemy.get("structure_broken") or {}
        dn = enemy.get("down") or {}
        lines.append(
            f"- 眩晕阈值: 伤害 {dz.get('threshold_damage') or '?'} / 命中 {dz.get('threshold_hits') or '?'}"
            f"{' (持续型)' if dz.get('persistent') else ''}; 破防持续 {sb.get('duration') or '?'}s;"
            f" 倒地阈值: 命中 {dn.get('threshold_hits') or '?'}"
        )
        lines.append("")
        for goal in ("dizzy", "struct", "damage", "knockdown"):
            lines.append(f"**{GOAL_TITLE[goal]}**")
            lines.append("")
            chs = (result.get("chains") or {}).get(short, {}).get(goal, [])
            if not chs:
                lines.append("- (无可编排链)")
                lines.append("")
                continue
            for c in chs[:5]:
                steps = c.get("steps") or []
                reentries = set(c.get("reentries") or [])
                conds = {x.get("step") for x in (c.get("conds") or [])}
                parts = []
                for i, s in enumerate(steps):
                    mark = "★" if i in reentries else ("◆" if i in conds else "")
                    parts.append("{}[{}]{}".format(s.get("name"), s.get("input") or "?", mark))
                seq = " → ".join(parts) or "(空)"
                t = c.get("totals") or {}
                fin = c.get("finisher") or "无收尾节"
                entry = c.get("entry_input") or "?"
                if c.get("entry_kind") == "state":
                    entry = "{}·{}".format(c.get("entry_state") or "状态", entry)
                title = c.get("title")
                prefix = ("**[{}]** ".format(title)) if title else ""
                lines.append(
                    "- {}[得分 {}] 入口 **{}** → `{}` | 收尾 **{}** | 伤害 {:.0f} · 结构 {:.0f}"
                    " · 特殊眩晕 {:.0f} · 命中 {} · 最大硬直 {}f · 击退 {:.0f}".format(
                        prefix, c.get("score"), entry, seq, fin,
                        t.get("dmg", 0), t.get("struct", 0), t.get("sdiz", 0),
                        t.get("hits", 0), t.get("stun", 0), t.get("kb", 0),
                    )
                )
            lines.append("")
    lines.append("")

    # ---- 三、社区连段验证 ----
    lines.append("## 三、社区主流连段验证")
    lines.append("")
    lines.append("> 把人工整理的社区连段拆成逐步输入, 用引擎逐段判定衔接通道(树内边/指令重入/状态条件边)。")
    lines.append("")
    verify_list = verify_community_combo(table)
    for vr in verify_list:
        lines.append("### {}".format(vr.get("title")))
        lines.append("")
        if vr.get("ok"):
            lines.append("| 步 | 节点 | 本次输入 | 衔接类型 | 条件引用 | 判定 |")
            lines.append("|---|---|---|---|---|---|")
            for i, st in enumerate(vr["steps"], 1):
                cond = st.get("ref") or "—"
                if cond and len(cond) > 48:
                    cond = cond[:45] + "…"
                lines.append("| {} | {} | {} | {} | {} | {} |".format(
                    i, st.get("name"), st.get("input") or "—", st.get("kind"),
                    cond, st.get("verdict")))
            t = vr.get("totals") or {}
            lines.append("")
            lines.append("- 合计: 伤害 {:.0f} · 结构 {:.0f} · 特殊眩晕 {:.0f} · 命中 {} · 最大硬直 {}f".format(
                t.get("dmg", 0), t.get("struct", 0), t.get("sdiz", 0),
                t.get("hits", 0), t.get("stun", 0)))
        else:
            lines.append("- 无法完全走通: {}".format(vr.get("reason")))
        lines.append("")

    # ---- 四、状态入口与状态触发衔接 ----
    lines.append("## 四、状态触发衔接（starts 状态入口）")
    lines.append("")
    lines.append("> 入口=敌人处于该状态时, 玩家按对应键进入的节点; 后续沿用同一套衔接通道。")
    lines.append("")
    state_entries = defaultdict(list)
    for nid, n in table.items():
        for e in n.get("entry", []):
            if e.get("kind") == "state":
                state_entries.setdefault(e.get("state"), []).append(
                    "{}({})".format(n.get("name"), e.get("label") or ""))
    if state_entries:
        for state in sorted(state_entries):
            lines.append("- **{}**: {}".format(state, " / ".join(sorted(set(state_entries[state])))))
    else:
        lines.append("- (无)")
    lines.append("")
    sc = result.get("state_chains") or {}
    if sc:
        lines.append("**从状态入口展开的可用后继链**")
        lines.append("")
        for state in sorted(sc):
            arr = sc[state]
            seen = set()
            shown = 0
            for item in arr:
                seq = item.get("sequence") or []
                k = tuple(seq)
                if k in seen:
                    continue
                seen.add(k)
                names = " → ".join(table.get(s, {}).get("name", s) for s in seq[:6])
                lines.append("- {}: `{}`".format(state, names))
                shown += 1
                if shown >= 4:
                    break
        lines.append("")

    # ---- 五、收尾节点索引 ----
    lines.append("## 五、收尾节点索引")
    lines.append("")
    fins = [n for n in table.values() if n.get("is_finisher")]
    if fins:
        lines.append("| id | 名称 | 组 | 标签 |")
        lines.append("|---|---|---|---|")
        for n in fins:
            lines.append("| {} | {} | {} | {} |".format(
                n.get("id"), n.get("name"),
                ",".join(n.get("groups") or []), ",".join(n.get("tags") or [])))
    else:
        lines.append("- (无)")
    lines.append("")
    lines.append("---")
    lines.append("> 生成: exports/20261119-连招编排-01/ · 全静态配置, 未实测。")
    return "\n".join(lines)


def verify_community_combo(table):
    """逐条验证 COMMUNITY_COMBOS 的每一步, 返回列表."""
    results = []
    for title, entry_spec, seq in COMMUNITY_COMBOS:
        r = _verify_sequence(table, seq)
        r["title"] = title
        r["entry"] = entry_spec
        ek, _, ev = entry_spec.partition(":")
        if r.get("steps"):
            r["steps"][0]["kind"] = "state" if ek == "state" else "input"
            r["steps"][0]["state"] = ev if ek == "state" else None
        results.append(r)
    return results


def _verify_sequence(table, seq):
    """按给定 (node_id, input_label) 逐步验证衔接通道."""
    steps = []
    ok = True
    reason = None
    prev = None
    for item in seq:
        if len(item) == 3:
            nid, lab, expected = item
        else:
            nid, lab = item
            expected = None
        n = table.get(str(nid))
        if not n:
            ok = False
            reason = f"节点 {nid} 不存在"
            break
        step = {"node": str(nid), "name": n["name"], "input": lab, "kind": "?", "ref": None}
        if prev is None:
            step["kind"] = "state" if expected == "state" else "input"
            step["verdict"] = "入口"
        else:
            p = table[str(prev["node"])]
            want = LABEL_RAW.get(lab, lab).split("::")[-1]
            kind, ref, to = None, None, None
            for e in p.get("edges", []):
                if not e.get("conditional") and e.get("rawInput", "").split("::")[-1] == want:
                    kind, to = "edge", e["to"]
                    break
            if kind is None:
                for e in p.get("edges", []):
                    if e.get("conditional") and e.get("rawInput", "").split("::")[-1] == want:
                        kind, to = "cond", e["to"]
                        ref = e.get("condition_ref") or (e.get("condition") or {}).get("reference")
                        break
            if kind is None:
                cm = build_command_map(BOARD_CACHE)
                for k, v in cm.items():
                    if k.split("::")[-1] == want:
                        kind, to = "reentry", int(v)
                        break
            if kind is None:
                step["kind"] = "x"
                step["verdict"] = "不可达(无该输入边/指令)"
                ok = False
                reason = f"{p['name']} 无法通过「{lab}」衔接"
                steps.append(step)
                break
            if str(to) != str(nid):
                step["kind"] = kind
                step["verdict"] = f"实际去向={table.get(str(to), {}).get('name', to)}"
                ok = False
                reason = f"期望 {n['name']}, 实际 {to}"
            else:
                step["kind"] = kind
                step["ref"] = ref
                step["verdict"] = "通过" if kind != "cond" else "通过(需状态条件)"
        steps.append(step)
        if not ok:
            break
        prev = step

    totals = {"dmg": 0.0, "struct": 0.0, "sdiz": 0.0, "hits": 0, "stun": 0}
    if ok:
        for st in steps:
            n = table.get(st["node"])
            if not n:
                continue
            for k in ("dmg", "struct", "sdiz", "hits"):
                totals[k] += n["agg"][k]
            totals["stun"] = max(totals["stun"], n["agg"]["stun"])
    conds = [s["ref"] for s in steps if s.get("ref")]
    conclusion = ("链全部走通: 入口为招架状态; 第2步(重击→重击)与第4/5步(袭裆拳/推掌)依赖指令重入; "
                  "收尾追亡逐北依赖 `BP_TargetPlaysOrder` 条件边(敌人被推掌/推击命中后的状态)。" if ok
                  else None)
    return {"ok": ok, "reason": reason, "steps": steps, "totals": totals,
            "cond_refs": conds, "conclusion": conclusion}


def render_readme():
    lines = []
    lines.append("# 连招编排器 (combo_orchestrator.py) 说明")
    lines.append("")
    lines.append("## 运行")
    lines.append("```")
    lines.append("D:\\Programes\\PY\\python.exe scripts\\combo_orchestrator.py")
    lines.append("```")
    lines.append("")
    lines.append("## 输入数据")
    lines.append("- `exports/20261029-招式时间轴-14/board-data.json`: 徒手连招树(57 节点/边/默认入口/状态入口/官方名/组)")
    lines.append("- `exports/mainchar-hitbox-windows.json`: 攻击资产 -> 判定行 + 帧区间(命中窗口)")
    lines.append("- `exports/hit-impact-values.csv`: 判定行 -> OnHit/OnGuard/OnDeflect 冲击值")
    lines.append("  - 注意: 判定行名跨 25 张表共用, 必须经 hitbox 的 DataTable reference 精确选表")
    lines.append("- `exports/20261029-招式时间轴-14/timing-data.json`: 招式时序(预备段/命中帧)")
    lines.append("- `exports/state-reaction-settings.csv`: 敌人状态反应阈值(眩晕伤害/命中/持续/破防时长)")
    lines.append("- `exports/state-resistance-matrices.csv`: 状态抗性矩阵(击倒/推击/眩晕抗性)")
    lines.append("- `exports/20261029-招式时间轴-14/availability-layers.json`: 输入可用性层(全局输入优先栈 + 各 FollowUp 层排除集, 是指令重入通道的依据)")
    lines.append("")
    lines.append("## 输出")
    lines.append("- `move-table.json`: 统一招式表(每节点: 入口/出边/收尾标记/命中汇总/时序/判定窗口)")
    lines.append("- `enemies.json`: 敌人原型阈值")
    lines.append("- `chains.json`: 每敌人 x 4 目标 的 top8 推荐链(含 steps 明细/总计)")
    lines.append("- `推荐连招表.md`: 人类可读推荐表")
    lines.append("")
    lines.append("## 编排口径与边界 (v2)")
    lines.append("- **三类衔接通道**: (1) 树内边 = 连招树保存的无条件出边; (2) 指令重入 = 任意收招窗口重按方向/蓄力/闪避指令(前前轻/前前重/后前轻/后前重/长按轻/长按重/闪避攻击/拉开), 依据 availability-layers 的 `attackAbilityInputsInPriorityOrder` 全局输入栈, 以及各 `*_FollowUp` 层排除集从不排除方向攻击; (3) 状态条件边 = 敌人处于特定状态才触发的条件分支(如推击命中后 BP_TargetPlaysOrder → 追亡逐北), 带 condition_ref 标注")
    lines.append("- **入口**: 默认输入类(defaults) + 状态入口(starts: 招架/奔跑/推击/倒地起身/Idle), 两者都参与编排")
    lines.append("- **收尾**: 无出边的节点(is_finisher); 击倒类由 KB/收尾加分体现")
    lines.append("- **社区链**: `COMMUNITY_COMBOS` 为人工整理的社区主流链, 由同一引擎逐步验证后注入推荐(带【社区主流】标记与第三节逐步验证表)")
    lines.append("- **数值**: 命中累加、硬直/击退/冻结取最大; 均为静态配置估计, 非实测")
    lines.append("- **边界**: 连招树只证明配置衔接, 不保证敌人不格挡/不闪避/不反制; 方向指令能否在该窗口重入属静态推断")
    lines.append("- **阈值**: 眩晕/倒地/破防阈值来自状态反应配置, 只是预测参考")
    lines.append("")
    lines.append("## 扩展")
    lines.append("- 目标函数在 `score_chains_v2`; 可加新目标(如 破防后追击)")
    lines.append("- 新增社区链: 在 `COMMUNITY_COMBOS` 加 (标题, 入口, [(节点id, 输入标签)...])")
    lines.append("- 数据连接: 节点 variants.asset -> hitbox attack_db -> (DataTable reference, RowName) -> impact 键 (asset,row,outcome)")
    return "\n".join(lines)


if __name__ == "__main__":
    main()