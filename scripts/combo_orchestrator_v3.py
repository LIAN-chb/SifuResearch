# -*- coding: utf-8 -*-
"""徒手连招编排器 v3 —— 按「敌人 × 入口 × 目标」推导可选连段，输出单文件交互式 HTML。

设计依据（全部来自本项目解包数据）：
1) 连招树边 = 设计层保证的衔接（配置内），帧余量不作为可行性判据；
2) 指令攻击（前前轻/前前重/后前轻/后前重/长按/闪避/拉开）是独立输入能力，
   由可用性层的 FollowUp 排除集决定哪些可在收招窗口内重入；
3) 状态入口（招架反击 / 击倒起身 / 推击 / 奔跑）来自 starts 条件入口；
4) 敌人阈值来自 state-reaction-settings.csv：眩晕窗口内累计伤害/命中达到上限即脱离，
   倒地窗口最多再吃 2 击，破防窗口 3.0 秒。

用法：
    D:\\Programes\\PY\\python.exe scripts\\combo_orchestrator_v3.py
输出：
    exports/20261119-连招编排-02/连招编排器.html
    exports/20261119-连招编排-02/chains-v3.json
    exports/20261119-连招编排-02/README.md
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORTS = os.path.join(ROOT, "exports")
BOARD_PATH = os.path.join(EXPORTS, "20261029-招式时间轴-14", "board-data.json")
MOVE_PATH = os.path.join(EXPORTS, "20261119-连招编排-01", "move-table.json")
ENEMY_PATH = os.path.join(EXPORTS, "20261119-连招编排-01", "enemies.json")
LAYER_PATH = os.path.join(EXPORTS, "20261029-招式时间轴-14", "availability-layers.json")
AVAIL_PATH = os.path.join(EXPORTS, "mainchar-availability-windows.json")
HITBOX_PATH = os.path.join(EXPORTS, "mainchar-hitbox-windows.json")
OUT_DIR = os.path.join(EXPORTS, "20261119-连招编排-02")

FPS = 60.0

# 衔接时序判定：gap = 前段最后一击命中帧 → 下一段首判定帧之间的间隔
# 上界来自连招树自身的标定：无条件树边的 gap 实测最大 29 帧（44→45=25、14→7=27、39→9=29），
# 条件边（推击/击倒等特殊状态）可放宽到 45 帧。
GAP_OK = 29        # 无条件衔接（普通受击硬直）可接受的最大间隔
GAP_TIGHT = 24     # 余量充足线：≤24 视为「稳」，25–29 视为「紧」
GAP_COND = 45      # 条件边（敌人处于推击/击倒/破防等较长状态）可接受的最大间隔

# ---------------------------------------------------------------- 常量

GRADE_LABEL = {
    "config": "配置衔接",
    "cond": "条件衔接",
    "cmd": "指令衔接",
    "state": "状态入口",
}

# 可在收招窗口内重入的指令输入（依据 FollowUp 层的排除集：Alt/Rush/Grab/同招被排除）
CMD_INPUTS = [
    ("LightFrontFront", "前前轻"),
    ("LightBackFront", "后前轻"),
    ("HeavyFrontFront", "前前重"),
    ("HeavyBackFront", "后前重"),
    ("LightHold", "长按轻"),
    ("HeavyHold", "长按重"),
    ("DodgeAttack", "闪避攻击"),
    ("Disengage", "拉开"),
    ("Light", "轻击"),
    ("Heavy", "重击"),
]
CMD_LABEL = dict(CMD_INPUTS)

ENTRY_SPECS = {
    "active": {
        "label": "主动进攻",
        "hint": "中性起手：轻击 / 重击起手，命中后才进入连段。方向攻击（前前、后前、长按）不是起手，它们在连段里以指令重入出现。",
        "starts": ["44", "48"],
    },
    "dodge": {
        "label": "闪避后攻击",
        "hint": "闪避/换位后追打：斗转星移（换位）是收尾型招式，之后接自由起手。鹰击长空（拉开距离）只有敌方出招前摇才命中，单列为特殊招式，不参与连段推导。",
        "starts": ["55"],
    },
    "parry": {
        "label": "招架反击",
        "hint": "招架成功（BP_TargetIsParryVictim）后进入：轻击三连打（配置里 2/17/18 是同一招的三个随机变体，页面按一招展示）/ 重击奔雷手 / 长按重击使绊子。",
        "starts": ["2", "19", "21"],
    },
    "down": {
        "label": "倒地起身",
        "hint": "被击倒后起身反击（KnockedDown 状态入口），起身瞬间有霸体判定差异，注意使用时机。",
        "starts": ["0"],
    },
}

ENTRY_NODE_LABEL = {
    "2": "招架反击·轻（三连打）",
    "17": "招架反击·轻（变体甲）",
    "18": "招架反击·轻（变体乙）",
    "19": "招架反击·重（奔雷手）",
    "21": "招架反击·长按重（使绊子）",
    "55": "闪避攻击·换位（斗转星移）",
    "52": "拉开距离",
    "0": "倒地起身攻击",
}

# 社区常见路线（人工整理，由引擎逐步校验后注入，保证不被搜索剪枝遗漏）
CURATED_COMBOS = [
    {"entry": "parry", "title": "社区主流·招架处决线",
     "seq": [("19", "重击"), ("48", "重击"), ("4", "重击"), ("39", "前前轻"), ("32", "后前轻"), ("26", "重击")]},
    {"entry": "parry", "title": "招架轻·三连打接重链",
     "seq": [("2", "招架反击·轻（三连打）"), ("4", "重击"), ("5", "重击"), ("10", "重击")]},
    {"entry": "active", "title": "轻击五连（疾风连环）",
     "seq": [("44", "轻击"), ("45", "轻"), ("14", "轻"), ("7", "轻"), ("8", "轻")]},
    {"entry": "active", "title": "重击四连（碎背肘）",
     "seq": [("48", "重击"), ("4", "重击"), ("5", "重击"), ("10", "重击")]},
    {"entry": "active", "title": "破防接扫腿",
     "seq": [("33", "长按轻"), ("31", "后前重")]},
    {"entry": "dodge", "title": "换位后接重链",
     "seq": [("55", "闪避攻击"), ("48", "重击"), ("4", "重击"), ("5", "重击")]},
]

GOALS = [
    ("overall", "综合"),
    ("dizzy", "眩晕窗口"),
    ("struct", "破防"),
    ("damage", "高伤害"),
    ("knockdown", "击倒收尾"),
]

PROFILE_PATH = os.path.join(EXPORTS, "enemy-defense-profiles.json")

# 训练场「原型 / 版本」两级目录：中文名取自本地化 General_* / ArchetypeVersion_*。
# 不是每个原型都有 基础/高级/小Boss 三档（闪电踢只有标准、首领只有阶段），照实列出。
ENEMY_TABLE = [
    # (原型, 版本, 抗性资产键)
    ("帮派成员", "基础", "Grunt_Base_ResistanceDB"),
    ("帮派成员", "高级", "Grunt_Adv_ResistanceDB"),
    ("帮派成员", "小Boss", "Grunt_Miniboss_ResistanceDb"),
    ("巨无霸", "基础", "BigGuy_Base_ResistanceDB"),
    ("巨无霸", "高级", "BigGuy_Advanced_ResistanceDB"),
    ("巨无霸", "小Boss", "BigGuy_MiniBossResistanceDB"),
    ("闪电踢", "标准", "FlashKick_ResistanceDB"),
    ("弟子", "基础", "FireDisciple_Base_ResistanceDB"),
    ("弟子", "高级", "FireDisciple_Adv_ResistanceDB"),
    ("弟子", "小Boss", "FireDisciple_MiniBoss_ResistanceDB"),
    ("保镖", "基础", "Bodyguard_Base_ResistanceDB"),
    ("保镖", "标准", "Bodyguard_ResistanceDB"),
    ("保镖", "小Boss", "Bodyguard_MiniBoss_ResistanceDB"),
    ("法贾", "", "Fajar_ResistanceDb"),
    ("肖恩", "", "Sean_ResistanceDB"),
    ("黑木", "", "Kuroki_ResistanceDB"),
    ("扬", "", "Yang_ResistanceDB"),
    ("凤姐", "", "Fengjie_ResistanceDB"),
    ("师父", "", "Sifu_ResistanceDB"),
    ("仆人", "", "Servant_ResistanceDB"),
]

# 版本名归一（防御图文件名里的版本片段 → 训练场里的版本名）
_VER_ALIAS = {
    "": "标准", "ContextualDefense": "标准", "标准": "标准",
    "Base": "基础", "Advanced": "高级", "Adv": "高级", "AdvStaff": "高级（长棍）",
    "MiniBoss": "小Boss", "Miniboss": "小Boss", "H0": "训练场", "NoAttack": "无攻击",
}

# 会把敌人打到地上的收尾招：之后只有下段/追击类（39 袭裆拳、40 追击、26 追亡逐北）还能命中
KNOCK_NODES = {"26", "31", "15", "16", "54", "21"}
GROUND_NODES = {"39", "40", "26"}
# 鹰击长空（拉开距离攻击，节点 52）：判定只在敌方出招前摇时成立，不能作为普通入口/衔接
ENEMY_ATTACK_NODES = {"52"}
# 推击后（PushInstigator）可用的招式：轻→14/25、重→26/4（board-data starts start=5）
PUSH_OK = {"14", "25", "26", "4"}
PUSH_INPUT = {"14": "轻", "25": "轻", "26": "重", "4": "重"}


def _norm_ver(v):
    v = str(v or "").strip()
    if v in _VER_ALIAS:
        return _VER_ALIAS[v]
    if v.startswith("P") and v[1:].isdigit():
        return f"第{v[1:]}阶段"
    return v


def _reaction_index():
    """原型×版本 → 防御反应画像（由 *_ContextualDefense 影响图汇总）。"""
    try:
        profs = load_json(PROFILE_PATH)
    except OSError:
        return {}
    out = {}
    for p in profs:
        key = (p.get("arch_cn") or "", _norm_ver(p.get("version")))
        cur = out.setdefault(key, {
            "mem_hits": set(), "prob": None,
            "parry": 0, "dodge": 0, "avoid": 0, "guard": 0, "counter": 0,
            "structure": None,
        })
        for h, _w in p.get("hit_memory") or []:
            if h:
                cur["mem_hits"].add(int(h))
        for pr in p.get("probabilities") or []:
            if pr is not None and (cur["prob"] is None or pr > cur["prob"]):
                cur["prob"] = round(float(pr), 2)
        has = p.get("has") or {}
        mapping = {"parry": "parry_deflect", "dodge": "dodge", "avoid": "avoid",
                   "guard": "guard", "counter": "counter"}
        for k, src in mapping.items():
            cur[k] = max(cur[k], int(has.get(src) or 0))
        for st in p.get("structure_tests") or []:
            if st.get("max") is not None:
                cur["structure"] = st.get("max")
    for key, cur in out.items():
        hits = sorted(cur["mem_hits"])
        cur["mem_min"] = hits[0] if hits else None
        cur["mem_trigger"] = hits[-1] if hits else None
        cur["mem_hits"] = hits
    return out


def load_json(path):
    with open(path, encoding="utf-8-sig") as f:
        return json.load(f)


def norm_input(raw):
    """'EComboTransition::Light' -> 'Light'"""
    if not raw:
        return ""
    return str(raw).split("::")[-1]


# ---------------------------------------------------------------- 载入

def _asset_base(p):
    return os.path.basename(p or "").strip()


def _official_labels(board):
    """节点 → 官方中文名（含连招段号）；无官方名时回退到节点名。"""
    out = {}
    for nid, node in (board.get("nodes") or {}).items():
        label = None
        for off in node.get("official") or []:
            nm = (off.get("name") or "").strip()
            if not nm:
                continue
            m = re.search(r"第(\d+)段", off.get("scope") or "")
            label = f"{nm}·{m.group(1)}" if m else nm
            break
        name = node.get("name") or nid
        if not label:
            label = name
        elif "变体" in name:
            label = label + "（变体）"
        out[str(nid)] = label
    return out


def _build_link(table, avail):
    """每节点的收招窗口起始帧 / 首判定帧 / 末判定帧 / 硬直 / 冻结。

    优先取连段 FollowUp 层（该层允许的输入才可能接续）；
    某些收尾技只在 GenericAll（全局通用层）登记窗口，此时退回 GenericAll，
    它代表"最早可以做出任何动作"的帧，可作为下次出手的最早时刻。
    """
    follow, generic = {}, {}
    for a in avail or []:
        base = _asset_base(a.get("attack_db"))
        props = a.get("properties") or {}
        fr = (props.get("m_FrameRange[0]") or {}).get("m_Anim[0]") or {}
        lo = fr.get("LowerBound[0]") or {}
        if lo.get("Type[0]") == "ERangeBoundTypes::Open":
            continue
        try:
            v = float(lo.get("Value[0]"))
        except (TypeError, ValueError):
            continue
        layer = ((props.get("m_Layer[0]") or {}).get("reference") or "").split(".")[-1]
        if layer.startswith("GenericAll"):
            generic[base] = min(generic.get(base, 1e9), v)
        else:
            follow[base] = min(follow.get(base, 1e9), v)
    link = {}
    for nid, node in table.items():
        agg = node.get("agg") or {}
        fr = agg.get("frame") or [0, 0]
        base = _asset_base(node.get("rep_variant_asset"))
        src = "follow"
        win = follow.get(base)
        if win is None:
            win = generic.get(base)
            src = "generic"
        if win is None:
            continue
        link[nid] = {
            "win": win,
            "first": float(fr[0] or 0),
            "last": float(fr[1] or 0),
            "stun": float(agg.get("stun") or 0),
            "freeze": float(agg.get("freeze") or 0),
            "src": src,
        }
    return link


def transition_gap(ctx, a, b):
    """前段最后一击 → 下一段首判定的间隔帧数（越小越稳）。"""
    la = ctx.get("link", {}).get(a)
    lb = ctx.get("link", {}).get(b)
    if not la or not lb:
        return None
    return la["win"] + lb["first"] - la["last"]


def gap_tier(gap):
    if gap is None:
        return "待核"
    if gap <= GAP_TIGHT:
        return "稳"
    if gap <= GAP_OK:
        return "紧"
    if gap <= GAP_COND:
        return "需状态"
    return "超界"


def _attack_props():
    """资产基名 → AttackDB.m_AttackProperties 标签（招式行为属性：推击/击倒/打下段/破防等）。"""
    import gzip
    path = os.path.join(ROOT, "inventory", "tagged-objects.json.gz")
    if not os.path.exists(path):
        return {}
    objs = json.load(gzip.open(path, "rt", encoding="utf-8"))
    out = {}
    for o in objs:
        if not o["class"].endswith("AttackDB"):
            continue
        base = os.path.basename(o["asset"])[: -len(".uasset")]
        for p in o["properties"]:
            if p.get("name") != "m_Attack":
                continue
            for q in p.get("value") or []:
                if q.get("name") == "m_AttackProperties" and "tagNames" in q:
                    out.setdefault(base, set()).update(q["tagNames"])
    return out


def build_context():
    board = load_json(BOARD_PATH)
    table = load_json(MOVE_PATH)
    enemies_raw = load_json(ENEMY_PATH)
    layers = load_json(LAYER_PATH)

    # 招式行为属性（来自攻击资产 AttackDB.m_AttackProperties）：决定敌人被打成什么状态
    aprops = _attack_props()
    # 判定高度带（High / Mid_1 / Mid_2 / Low）：倒地目标的受击盒贴地，只有 Low 带够得着
    band_of = {}
    for e in load_json(HITBOX_PATH):
        base = e["attack_db"].split("/")[-1].rsplit(".", 1)[0]
        band = (e["properties"].get("m_eHitTarget[0]") or "").split("::")[-1]
        if band:
            band_of.setdefault(base, set()).add(band)
    for nid, node in table.items():
        assets = [((v.get("asset") or "").split("/")[-1].rsplit(".", 1)[0]) for v in (node.get("variants") or [])]
        if node.get("rep_variant_asset"):
            assets.append(node["rep_variant_asset"].split("/")[-1].rsplit(".", 1)[0])
        tags = set()
        bands = set()
        for a in assets:
            tags |= aprops.get(a, set())
            bands |= band_of.get(a, set())
        node["props"] = sorted(tags)
        node["bands"] = sorted(bands)
        node["push"] = "Attack.HitProperties.PushBack" in tags
        node["kd"] = ("Attack.HitProperties.KnockDown" in tags
                      or "Attack.Specific.SkillFollowKD" in tags
                      or nid in {"26"})
        # 能打倒地目标 = 该招存在贴地（Low）判定带；不再用 AvoidProperties.Grounded 标签推断
        node["ground"] = "Low" in bands
        node["pursuit"] = any(t.startswith("Attack.Specific.SkillFollow") for t in tags)
        node["unblockable"] = "Attack.Defense.Unblockable" in tags
        node["need_enemy_attack"] = nid in ENEMY_ATTACK_NODES

    defaults = {}
    default_label = {}
    for d in board.get("defaults", []):
        tgt = d.get("target")
        if tgt in (None, -1, "-1"):
            continue
        # fallback=True 表示该输入会退回到该节点，仍视为有效入口
        defaults[norm_input(d.get("rawInput"))] = str(tgt)
        default_label.setdefault(str(tgt), d.get("input") or norm_input(d.get("rawInput")))

    starts = board.get("starts", [])

    # 可用性层：汇总 FollowUp 排除集
    layer_info = {}
    for key, val in (layers.get("layers") or {}).items():
        short = key.split("/")[-1].split(".")[0]
        layer_info[short] = {
            "invert": bool(val.get("invert")),
            "actions": list(val.get("listedActions") or []),
            "meaning": val.get("listMeaning"),
        }
    blocked = set()
    for short, info in layer_info.items():
        if short.endswith("FollowUp") and info["invert"]:
            blocked.update(info["actions"])

    # 指令输入 → 默认目标节点
    cmd_map = {}
    for inp, label in CMD_INPUTS:
        tgt = defaults.get(inp)
        if tgt and tgt in table:
            cmd_map[inp] = tgt

    return {
        "board": board,
        "table": table,
        "enemies_raw": enemies_raw,
        "defaults": defaults,
        "default_label": default_label,
        "starts": starts,
        "layers": layer_info,
        "blocked": blocked,
        "cmd_map": cmd_map,
        "labels": _official_labels(board),
        "link": _build_link(table, load_json(AVAIL_PATH)),
        "reactions": _reaction_index(),
    }


# ---------------------------------------------------------------- 连段搜索

def node_links(ctx, nid, used_inputs, used_nodes, prev_cmd):
    """返回当前节点在「敌人当前姿态」下可衔接的步骤。

    姿态由上一招的行为属性决定：
    - 击倒（HitProperties.KnockDown）→ 敌人倒地，普通招式从倒地目标上方挥空，连段在此终止；
    - 推击（HitProperties.PushBack）→ 敌人被击退，只有推击后专用招式可用；
    - 其余按站立处理（站立时任何命中型招式都成立）。
    """
    node = ctx["table"][nid]
    knocked = bool(node.get("kd"))
    pushed = bool(node.get("push"))
    links = []
    edge_inputs = set()
    for e in node.get("edges") or []:
        if e.get("to") not in ctx["table"]:
            continue
        inp = e.get("input") or ""
        raw = norm_input(e.get("rawInput"))
        if raw:
            edge_inputs.add(raw)
        gap = transition_gap(ctx, nid, e["to"])
        limit = GAP_COND if e.get("conditional") else GAP_OK
        if gap is not None and gap > limit:
            continue  # 敌人会在下一击命中前脱离，不能算连招
        if e.get("conditional"):
            ref = e.get("condition_ref") or ""
            if "CheatComboCheck" in ref:
                # 偷招检查：验证玩家输入时机，不是敌人状态，输入对了就成立
                links.append({
                    "to": e["to"], "input": inp, "grade": "config", "cond": None,
                    "note": "设计内连段（需输入时机）", "gap": gap,
                })
                continue
            links.append({
                "to": e["to"],
                "input": inp,
                "grade": "cond",
                "cond": e.get("condition_ref"),
                "note": "需敌人状态（条件边）",
                "gap": gap,
            })
        else:
            links.append({
                "to": e["to"],
                "input": inp,
                "grade": "config",
                "cond": None,
                "note": "设计内连段",
                "gap": gap,
            })
    # 指令重入：该输入在当前节点没有对应树边时才走重入
    for inp, label in CMD_INPUTS:
        if inp in edge_inputs or inp in used_inputs or inp == prev_cmd:
            continue
        tgt = ctx["cmd_map"].get(inp)
        if not tgt or tgt in used_nodes:
            continue
        if inp in ctx["blocked"]:
            continue
        gap = transition_gap(ctx, nid, tgt)
        if gap is not None and gap > GAP_OK:
            continue
        links.append({
            "to": tgt,
            "input": label,
            "grade": "cmd",
            "cond": None,
            "note": "收招窗口内指令重入",
            "cmd_input": inp,
            "gap": gap,
        })
    # 特殊招式（鹰击长空）只在敌方出招前摇成立，不参与常规连段
    links = [l for l in links if not ctx["table"].get(l["to"], {}).get("need_enemy_attack")]
    if knocked:
        # 敌人倒地：受击盒贴地，站立的 Mid/High 判定一律挥空，连段终止
        # （工具里没有可确证的「倒地追击」招式，故不做任何衔接，避免推荐打不中的链）
        links = []
    elif pushed:
        # 敌人被击退：推击后专用招式由 PushInstigator 状态入口保证命中（不是条件推断）
        keep = []
        for l in links:
            if l["to"] in PUSH_OK:
                l = dict(l)
                l["grade"] = "state"
                l["cond"] = None
                l["note"] = "推击状态入口（必中）"
                keep.append(l)
        have = {l["to"] for l in keep}
        for tgt in sorted(PUSH_OK):
            if tgt in have or tgt in used_nodes or tgt not in ctx["table"]:
                continue
            gap = transition_gap(ctx, nid, tgt)
            if gap is not None and gap > GAP_COND:
                continue
            keep.append({
                "to": tgt,
                "input": PUSH_INPUT.get(tgt, "重"),
                "grade": "state",
                "cond": None,
                "note": "推击状态入口（必中）",
                "gap": gap,
            })
        links = keep
    return links


def _new_state(start_id):
    return {
        "chain": [start_id],
        "inputs": [],
        "grades": [],
        "conds": [],
        "step_conds": [],
        "gaps": [],
        "cmd_count": 0,
        "cond_count": 0,
        "used_inputs": set(),
        "used_nodes": {start_id},
        "prev_cmd": None,
    }


def _partial_score(ctx, st):
    steps, tot = chain_stats(ctx, st)
    return (0.6 * tot["dmg"] + 0.5 * tot["struct"] + 0.4 * tot["sdiz"]
            + (10.0 if steps and steps[-1].get("finisher") else 0.0)
            + 8.0 * tot["config_ratio"])


def search_chains(ctx, start_ids, max_depth=6, beam=700, max_cmd=3, max_cond=2):
    """宽度优先 + 打分剪枝：保证不同分支（含指令重入）都能被展开到，不会因深挖单支而漏链。"""
    level = [_new_state(s) for s in start_ids if s in ctx["table"]]
    out = []
    for depth in range(1, max_depth):
        for st in level:
            if len(st["chain"]) >= 2:
                out.append(st)
        nxt = []
        for st in level:
            node_id = st["chain"][-1]
            for l in node_links(ctx, node_id, st["used_inputs"], st["used_nodes"], st["prev_cmd"]):
                if l["to"] in st["used_nodes"]:
                    continue
                if l["grade"] == "cmd" and st["cmd_count"] >= max_cmd:
                    continue
                if l["grade"] == "cond" and st["cond_count"] >= max_cond:
                    continue
                ns = {
                    "chain": st["chain"] + [l["to"]],
                    "inputs": st["inputs"] + [l["input"]],
                    "grades": st["grades"] + [l["grade"]],
                    "conds": st["conds"] + ([l["cond"]] if l["grade"] == "cond" else []),
                    "step_conds": st["step_conds"] + [l["cond"]],
                    "gaps": st["gaps"] + [l.get("gap")],
                    "cmd_count": st["cmd_count"] + (1 if l["grade"] == "cmd" else 0),
                    "cond_count": st["cond_count"] + (1 if l["grade"] == "cond" else 0),
                    "used_inputs": set(st["used_inputs"]),
                    "used_nodes": set(st["used_nodes"]) | {l["to"]},
                    "prev_cmd": l.get("cmd_input"),
                }
                if l["grade"] == "cmd":
                    ns["used_inputs"].add(l.get("cmd_input"))
                nxt.append(ns)
        if not nxt:
            break
        # 去重（同节点序列 + 同输入序列）
        seen, uniq = set(), []
        for st in nxt:
            key = (tuple(st["chain"]), tuple(st["inputs"]))
            if key in seen:
                continue
            seen.add(key)
            uniq.append(st)
        uniq.sort(key=lambda s: _partial_score(ctx, s), reverse=True)
        # 每个起点保留配额，避免高分长链挤掉其他入口分支（如 19→48 支路）
        quota = max(80, beam // max(len(set(s["chain"][0] for s in uniq)), 1))
        by_start = {}
        for st in uniq:
            by_start.setdefault(st["chain"][0], []).append(st)
        level = []
        for sid, group in by_start.items():
            level.extend(group[:quota])
        level.sort(key=lambda s: _partial_score(ctx, s), reverse=True)
        level = level[:beam]
    for st in level:
        if len(st["chain"]) >= 2:
            out.append(st)
    return out


def chain_stats(ctx, st):
    table = ctx["table"]
    labels = ctx.get("labels") or {}
    steps = []
    tot = {"dmg": 0.0, "struct": 0.0, "sdiz": 0.0, "hits": 0, "stun": 0, "kb": 0.0,
           "frames": 0.0, "min_gap": None, "gaps": []}
    for i, nid in enumerate(st["chain"]):
        node = table[nid]
        agg = node.get("agg") or {}
        if i == 0:
            grade = "state" if st.get("entry_key") in ("parry", "down") else "input"
            cond, gap = None, None
            label = (ENTRY_NODE_LABEL.get(nid)
                     or ctx.get("default_label", {}).get(nid)
                     or node.get("name") or nid)
        else:
            grade = st["grades"][i - 1]
            cond = st["step_conds"][i - 1] if i - 1 < len(st["step_conds"]) else None
            gap = st["gaps"][i - 1] if i - 1 < len(st.get("gaps") or []) else None
            label = st["inputs"][i - 1]
        fr = agg.get("frame") or [0, 0]
        step = {
            "id": nid,
            "name": labels.get(nid) or node.get("name") or nid,
            "rawName": node.get("rawName"),
            "input": label,
            "grade": grade,
            "tier": gap_tier(gap) if i > 0 else "入口",
            "gap": gap,
            "cond": cond,
            "dmg": agg.get("dmg") or 0,
            "struct": agg.get("struct") or 0,
            "sdiz": agg.get("sdiz") or 0,
            "hits": agg.get("hits") or 0,
            "stun": agg.get("stun") or 0,
            "frame": fr,
            "finisher": bool(node.get("is_finisher")),
        }
        steps.append(step)
        if gap is not None:
            tot["gaps"].append(gap)
            tot["min_gap"] = gap if tot["min_gap"] is None else min(tot["min_gap"], gap)
        tot["dmg"] += step["dmg"]
        tot["struct"] += step["struct"]
        tot["sdiz"] += step["sdiz"]
        tot["kb"] = max(tot["kb"], step["dmg"] and (agg.get("kb") or 0) or 0)
        tot["hits"] += step["hits"]
        tot["stun"] = max(tot["stun"], step["stun"])
        tot["frames"] += max(float(fr[1] or 0), 0.0)
    tot["frames"] = round(tot["frames"], 1)
    tot["dmg"] = round(tot["dmg"], 1)
    tot["struct"] = round(tot["struct"], 1)
    tot["sdiz"] = round(tot["sdiz"], 1)
    tot["kb"] = round(tot["kb"], 1)
    grades = [s["grade"] for s in steps[1:]] or ["state"]
    tot["config_ratio"] = round(grades.count("config") / max(len(grades), 1), 3)
    tot["cmd_count"] = grades.count("cmd")
    tot["cond_count"] = grades.count("cond")
    tot["all_ok"] = all(s["tier"] in ("入口", "稳", "紧") for s in steps)
    tot["tiers"] = [s["tier"] for s in steps[1:]]
    return steps, tot


# ---------------------------------------------------------------- 敌人与评分

def enemy_record(key, raw, arch=None, ver=None, reaction=None):
    dz = raw.get("dizzy") or {}
    dn = raw.get("down") or {}
    st = raw.get("structure_broken") or {}
    sd = raw.get("super_dizzy") or {}
    name = f"{arch}·{ver}" if (arch and ver) else (arch or key)
    if arch and not ver:
        name = arch
    return {
        "key": key,
        "name": name,
        "archetype": arch or key,
        "version": ver or "",
        "dizzy_dmg": dz.get("threshold_damage"),
        "dizzy_hits": dz.get("threshold_hits"),
        "down_hits": dn.get("threshold_hits"),
        "struct_duration": st.get("duration"),
        "struct_coef": st.get("guard_coef"),
        "super_duration": sd.get("duration"),
        "super_mandatory": sd.get("mandatory"),
        "mem_trigger": (max(reaction.get("mem_hits") or []) if reaction.get("mem_hits") else None),
        "mem_min": reaction.get("mem_min"),
        "prob": reaction.get("prob"),
        "reaction": reaction or {},
    }


def reaction_risk(enemy, hits):
    """敌人连续挨打后的防御反应概率（来自 *_ContextualDefense 影响图的攻击记忆测试）。

    记忆测试 = 「在 m_fMemoryLimit 秒内挨了 m_uiHitsCount 次同类命中 → 触发防御反应」。
    取该敌人所有记忆测试里最大的命中数作为触发点：低于它不触发，超过后概率随超量上升。
    返回 (风险 0~1, 反应类型中文)。
    """
    r = enemy.get("reaction") or {}
    trig = r.get("mem_trigger")
    if not trig or hits < trig:
        return 0.0, ""
    p = r.get("prob")
    p = 1.0 if p is None else float(p)
    over = hits - trig
    rate = min(1.0, p + 0.12 * over)
    kinds = []
    if r.get("parry"):
        kinds.append("弹反")
    if r.get("guard"):
        kinds.append("格挡")
    if r.get("dodge") or r.get("avoid"):
        kinds.append("闪避")
    return round(rate, 2), "/".join(kinds[:2])


def score_chain(goal, steps, tot, enemy):
    """按目标给连段打分。

    有效输出只算「敌人脱离之前」的部分：命中数达到眩晕窗口预算后，
    后续招式随时会被弹反/格挡/闪避，不再计入有效伤害，只保留为末端风险。
    """
    budget_hits = enemy.get("dizzy_hits") or 999
    eff_dmg = eff_struct = eff_sdiz = 0.0
    eff_hits = 0
    cut = None
    for i, s in enumerate(steps):
        if eff_hits >= budget_hits:
            cut = i
            break
        sh = s["hits"] or 1
        room = budget_hits - eff_hits
        if sh > room:
            # 该段只能吃到预算内的那部分命中，敌人随即脱离
            frac = room / sh
            eff_dmg += s["dmg"] * frac
            eff_struct += s["struct"] * frac
            eff_sdiz += s["sdiz"] * frac
            eff_hits = budget_hits
            cut = i + 1
            break
        eff_dmg += s["dmg"]
        eff_struct += s["struct"]
        eff_sdiz += s["sdiz"]
        eff_hits += sh
    tot["eff_dmg"] = round(eff_dmg, 1)
    tot["eff_struct"] = round(eff_struct, 1)
    tot["eff_sdiz"] = round(eff_sdiz, 1)
    tot["eff_hits"] = eff_hits
    tot["cut_index"] = cut
    dmg = eff_dmg
    fin_bonus = 12.0 if steps and steps[-1].get("finisher") else 0.0
    # 衔接可信度：全部落在官方连段树时序区间内（稳/紧）不扣分；
    # 依赖长状态（需状态）或窗口数据缺失（待核）逐步降低可信度。
    tiers = [s.get("tier") for s in steps[1:]]
    doubt = 1.0
    doubt -= 0.10 * tiers.count("需状态")
    doubt -= 0.06 * tiers.count("待核")
    doubt = max(0.45, doubt)
    # 敌人差异化：连续挨打超过该敌人的记忆阈值后，末端有概率被弹反/格挡/闪避
    risk, kind = reaction_risk(enemy, tot["hits"])
    tot["reaction_risk"] = risk
    tot["reaction_kind"] = kind
    doubt *= (1.0 - 0.22 * risk)
    if goal == "dizzy":
        s = dmg + 18.0 * (eff_hits <= budget_hits) + 0.35 * eff_sdiz + fin_bonus
        return round(s * doubt, 1)
    if goal == "struct":
        frames = tot["frames"] or 0
        over = max(0.0, frames - 180.0)
        s = eff_struct * (1.0 - min(0.45, over / 400.0)) + fin_bonus
        return round(s * doubt, 1)
    if goal == "damage":
        return round((dmg + fin_bonus + 0.1 * eff_sdiz) * doubt, 1)
    if goal == "knockdown":
        last = steps[-1] if steps else {}
        s = 0.55 * tot["kb"] + 0.45 * dmg + fin_bonus
        if last.get("finisher"):
            s += 15.0
        if last.get("frame") and last.get("stun", 0) >= 20:
            s += 6.0
        return round(s * doubt, 1)
    # overall
    s = (
        0.34 * min(dmg / 180.0, 1.5)
        + 0.26 * min(eff_struct / 260.0, 1.5)
        + 0.20 * min(eff_sdiz / 220.0, 1.5)
        + 0.12 * tot["config_ratio"]
        + 0.08 * fin_bonus / 12.0
    )
    return round(s * 100 * doubt, 1)


def risk_tags(entry_key, steps, tot, enemy):
    tags = []
    if entry_key == "active":
        tags.append("起手可能被抢/被格挡")
    if tot["cmd_count"]:
        tags.append("含指令重入（需收招窗口）")
    if tot["cond_count"]:
        tags.append("含条件衔接（需敌人状态）")
    if tot["frames"] and enemy.get("struct_duration") and tot["frames"] > enemy["struct_duration"] * FPS:
        tags.append("动作时长超破防窗口")
    if enemy.get("dizzy_hits") and tot["hits"] > enemy["dizzy_hits"]:
        tags.append("命中数超眩晕预算")
    if steps and not steps[-1].get("finisher"):
        tags.append("非收尾节点，收招留破绽")
    if tot.get("reaction_risk"):
        tags.append(f"末端有 {round(tot['reaction_risk']*100)}% 被{tot.get('reaction_kind') or '防御'}风险")
    return tags


def build_curated(ctx, spec):
    """按显式序列逐步走一遍引擎判定，确认每一步在配置/输入层成立。"""
    chain = [spec["seq"][0][0]]
    if chain[0] not in ctx["table"]:
        return None
    inputs, grades, conds, step_conds, gaps = [], [], [], [], []
    used_inputs, used_nodes = set(), {chain[0]}
    prev_cmd, cmd, condc = None, 0, 0
    for nid, _label in spec["seq"][1:]:
        links = node_links(ctx, chain[-1], used_inputs, used_nodes, prev_cmd)
        link = next((l for l in links if l["to"] == nid), None)
        if link is None:
            return None
        chain.append(nid)
        inputs.append(link["input"])
        grades.append(link["grade"])
        gaps.append(link.get("gap"))
        if link["grade"] == "cond":
            conds.append(link["cond"])
            condc += 1
        step_conds.append(link["cond"])
        used_nodes.add(nid)
        if link["grade"] == "cmd":
            used_inputs.add(link.get("cmd_input"))
            cmd += 1
        prev_cmd = link.get("cmd_input")
    return {
        "chain": chain, "inputs": inputs, "grades": grades, "conds": conds,
        "step_conds": step_conds, "gaps": gaps, "cmd_count": cmd,
        "cond_count": condc, "used_inputs": used_inputs,
        "used_nodes": used_nodes, "prev_cmd": prev_cmd,
    }


def build_chain_pool(ctx):
    """连段与敌人无关：按入口枚举一次，保留全部可行链（去重后交给前端筛选）。"""
    pool = {}
    for ekey, spec in ENTRY_SPECS.items():
        seen = set()
        chains = []
        for st in search_chains(ctx, spec["starts"], max_depth=6, beam=2600):
            if len(st["chain"]) < 2:
                continue
            key = (tuple(st["chain"]), tuple(st["inputs"]))
            if key in seen:
                continue
            seen.add(key)
            steps, tot = chain_stats(ctx, st)
            chains.append({
                "steps": steps,
                "totals": tot,
                "entry_key": ekey,
                "entry_label": ENTRY_NODE_LABEL.get(st["chain"][0])
                or ctx["default_label"].get(st["chain"][0])
                or ctx["table"][st["chain"][0]].get("name"),
                "entry_node": st["chain"][0],
                "curated": False,
            })
        # 注入人工整理的社区路线（引擎校验通过才保留）
        for spec in CURATED_COMBOS:
            if spec["entry"] != ekey:
                continue
            st = build_curated(ctx, spec)
            if not st:
                print("  [跳过] 社区路线未通过引擎校验:", spec["title"])
                continue
            steps, tot = chain_stats(ctx, st)
            chains.append({
                "steps": steps,
                "totals": tot,
                "entry_key": ekey,
                "entry_label": ENTRY_NODE_LABEL.get(st["chain"][0])
                or ctx["default_label"].get(st["chain"][0])
                or ctx["table"][st["chain"][0]].get("name"),
                "entry_node": st["chain"][0],
                "curated": True,
                "title": spec["title"],
            })
        uniq = {}
        for ch in chains:
            k = tuple(s["id"] for s in ch["steps"])
            if k not in uniq or ch.get("curated"):
                uniq[k] = ch
        pool[ekey] = list(uniq.values())
    return pool


def pick_top(goal, chains, enemy, n=6):
    """排序时把「窗口内可执行」的连段排前面：眩晕窗口按命中预算过滤；社区路线保证入选。

    totals 必须按敌人复制一份再评分：同一份连段池会被所有敌人复用，
    敌人相关的字段（有效输出、末端反应）不能写回共享对象。
    """
    band = []
    out_band = []
    for ch in chains:
        tot = dict(ch["totals"])
        s = score_chain(goal, ch["steps"], tot, enemy)
        item = (s, ch, tot)
        if goal == "dizzy":
            bh = enemy.get("dizzy_hits")
            if bh and tot["hits"] > bh:
                out_band.append(item)
                continue
        band.append(item)
    band.sort(key=lambda x: -x[0])
    out_band.sort(key=lambda x: -x[0])
    picked = band + out_band

    def _key(ch):
        return (tuple(st["id"] for st in ch["steps"]), tuple(st["input"] for st in ch["steps"]))

    def _norm(n):
        for suf in ("（变体甲）", "（变体乙）", "（三连打）", "变体甲", "变体乙", "（）"):
            n = n.replace(suf, "")
        return n

    def _sig(ch):
        # 同一组招式换个顺序重入不算新思路：按招式集合去重（每种集合最多留 2 条不同起手）
        return tuple(sorted((_norm(st["name"]), _norm(st["input"])) for st in ch["steps"]))

    chosen = []
    keys = set()
    sigs = {}
    for s, ch, tot in picked:
        if len(chosen) >= n:
            break
        if _key(ch) in keys:          # 完全同序同输入的链只留一条
            continue
        sig = _sig(ch)
        if sigs.get(sig, 0) >= 2:
            continue
        chosen.append((s, ch, tot))
        keys.add(_key(ch))
        sigs[sig] = sigs.get(sig, 0) + 1
    # 社区路线保证入选：未进前 n 时追加到末尾（不打断按分排序）
    for s, ch, tot in picked:
        if not ch.get("curated"):
            continue
        k = _key(ch)
        if k in keys:
            continue
        chosen.append((s, ch, tot))
        keys.add(k)

    out = []
    for s, ch, tot in chosen:
        out.append({
            "score": s,
            "entry": ch["entry_label"],
            "entry_node": ch["entry_node"],
            "title": ch.get("title"),
            "curated": bool(ch.get("curated")),
            "steps": ch["steps"],
            "totals": tot,
            "risks": risk_tags(ch["entry_key"], ch["steps"], tot, enemy),
            "over_budget": bool(goal == "dizzy" and enemy.get("dizzy_hits")
                                and tot["hits"] > enemy["dizzy_hits"]),
        })
    return out


# ---------------------------------------------------------------- 主流程

def _compact(ctx, ch):
    """压缩连段记录（与敌人无关，前端按敌人/目标即时评分）。"""
    steps = ch["steps"]
    return {
        "ids": [s["id"] for s in steps],
        "ins": [s["input"] for s in steps],
        "gr": [s["grade"] for s in steps],
        "gap": [None if s.get("gap") is None else round(s["gap"], 1) for s in steps],
        "entry": ch["entry_label"],
        "entry_node": ch["entry_node"],
        "cur": 1 if ch.get("curated") else 0,
        "title": ch.get("title") or "",
        "steps": [[s["dmg"], s["struct"], s["sdiz"], s["hits"], s["stun"],
                   s.get("frame"), 1 if s.get("finisher") else 0, s.get("cond") or ""]
                  for s in steps],
    }


def build_graph(ctx):
    """把每个节点的可衔接步骤汇成一张有向图：节点=招式，边=一次输入。

    边只来自两类游戏内依据：
    - 连招树无条件边（board-data edges，设计内连段）；
    - 状态入口（starts 的 PushInstigator 推击后衔接）。
    指令重入单独标 grade=cmd，前端默认隐藏。
    """
    edges = []
    seen = set()
    for nid in ctx["table"]:
        for l in node_links(ctx, nid, set(), {nid}, None):
            key = (nid, l["to"], l.get("input"))
            if key in seen:
                continue
            seen.add(key)
            edges.append({
                "s": nid,
                "t": l["to"],
                "inp": l.get("input") or "",
                "grade": l.get("grade"),
                "gap": l.get("gap"),
                "tier": gap_tier(l.get("gap")),
                "note": l.get("note"),
            })
    return edges


def main():
    ctx = build_context()
    edges = build_graph(ctx)
    print("连招图:", len(ctx["table"]), "节点", len(edges), "条衔接")

    enemies = []
    for arch, ver, key in ENEMY_TABLE:
        if key not in ctx["enemies_raw"]:
            continue
        reaction = ctx["reactions"].get((arch, ver or "标准")) or {}
        e = enemy_record(key, ctx["enemies_raw"][key], arch, ver, reaction)
        enemies.append(e)

    data = {
        "meta": {
            "title": "师父 · 徒手连招编排器",
            "built_from": "board-data.json / move-table.json / state-reaction-settings.csv / availability-layers.json / 攻击资产属性",
            "note": "全部数值为解包配置静态估算，非游戏内实测；衔接为配置/输入层证据，命中与时机仍需实战校验。",
        },
        "entries": {k: {"label": v["label"], "hint": v["hint"], "starts": v["starts"]} for k, v in ENTRY_SPECS.items()},
        "goals": [{"key": k, "label": l} for k, l in GOALS],
        "archetypes": list(dict.fromkeys(e["archetype"] for e in enemies)),
        "enemies": enemies,
        "nodes": {
            nid: {
                "name": ctx["labels"].get(nid) or node.get("name"),
                "rawName": node.get("rawName"),
                "agg": node.get("agg"),
                "finisher": bool(node.get("is_finisher")),
                "kd": bool(node.get("kd")),
                "ground": bool(node.get("ground")),
                "push": bool(node.get("push")),
                "pursuit": bool(node.get("pursuit")),
                "need_enemy_attack": bool(node.get("need_enemy_attack")),
                "props": node.get("props") or [],
            }
            for nid, node in ctx["table"].items()
        },
        "graph": {"edges": edges},
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    json_path = os.path.join(OUT_DIR, "combo-graph.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

    from combo_graph_render import render_html as render_graph_html
    html_path = os.path.join(OUT_DIR, "连招编排器.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(render_graph_html(data))

    readme_path = os.path.join(OUT_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(render_readme(data, {"edges": edges}))

    print("已输出:", html_path)
    print("已输出:", json_path)
    print("已输出:", readme_path)


HTML_TPL = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>师父 · 徒手连招编排器</title>
<style>
:root{
  --paper:#f4f2ec; --card:#fffef9; --ink:#25372d; --ink2:#5c6b5f; --line:#c9d4c3;
  --accent:#2e5740; --config:#44875d; --cmd:#5c7baf; --cond:#ac8650; --state:#7b6aa8; --warn:#b4553f;
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
  font:14px/1.55 -apple-system,"Segoe UI","Microsoft YaHei",sans-serif;}
h1,h2,h3{font-family:"Noto Serif SC","Songti SC",Georgia,serif;font-weight:600;margin:0}
.top{display:flex;justify-content:space-between;align-items:center;gap:16px;
  padding:18px 26px;background:var(--accent);color:#f2f5ee}
.brand{display:flex;gap:14px;align-items:center}
.mark{width:42px;height:42px;border:1px solid rgba(255,255,255,.5);border-radius:10px;
  display:grid;place-items:center;font-family:serif;font-size:22px}
.top h1{font-size:19px;letter-spacing:.06em}
.sub{margin:2px 0 0;font-size:12px;opacity:.82}
.top-note{font-size:12px;opacity:.85;border:1px solid rgba(255,255,255,.35);
  padding:6px 10px;border-radius:999px;white-space:nowrap}
main{display:grid;grid-template-columns:300px minmax(0,1fr);gap:22px;padding:22px 26px 40px;
  align-items:start;max-width:1440px;margin:0 auto}
.panel{position:sticky;top:18px;display:flex;flex-direction:column;gap:16px}
section.panel-box{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 15px}
.panel h2{font-size:13px;letter-spacing:.14em;color:var(--ink2);margin-bottom:10px}
label{display:block;font-size:12px;color:var(--ink2);margin-bottom:8px}
select{width:100%;margin-top:4px;padding:7px 9px;border:1px solid var(--line);border-radius:9px;
  background:#fff;color:var(--ink);font-size:13px}
.tabs{display:flex;flex-wrap:wrap;gap:6px}
.tab{border:1px solid var(--line);background:#fff;border-radius:999px;padding:5px 11px;
  font-size:12.5px;cursor:pointer;color:var(--ink2);transition:.15s}
.tab:hover{border-color:var(--accent);color:var(--accent)}
.tab.on{background:var(--accent);border-color:var(--accent);color:#f5f7f2}
.hint{font-size:12px;color:var(--ink2);margin:10px 0 0;line-height:1.6}
.enemy-card .en-name{font-size:15px;font-weight:600}
.enemy-card .en-arch{font-size:11.5px;color:var(--ink2);letter-spacing:.1em;margin-bottom:10px}
.kv{display:flex;justify-content:space-between;gap:10px;font-size:12.5px;
  padding:5px 0;border-top:1px dashed var(--line)}
.kv:first-of-type{border-top:0}
.kv b{font-weight:600}
.kv span{color:var(--ink2)}
.results{min-width:0}
.results-head{display:flex;justify-content:space-between;align-items:baseline;
  gap:12px;margin-bottom:14px;flex-wrap:wrap}
.results-head h2{font-size:17px}
.results-head p{font-size:12.5px;color:var(--ink2);margin:0}
.chain{background:var(--card);border:1px solid var(--line);border-radius:14px;
  padding:14px 16px;margin-bottom:14px;box-shadow:0 1px 0 rgba(46,87,64,.04)}
.chain.is-best{border-color:var(--accent);box-shadow:0 0 0 1px rgba(46,87,64,.18)}
.chain-head{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.idx{font-family:serif;font-size:13px;color:var(--ink2)}
.entry-chip{font-size:11.5px;color:var(--accent);background:rgba(46,87,64,.08);
  border:1px solid rgba(46,87,64,.25);border-radius:999px;padding:3px 9px}
.tag-curated{font-size:11.5px;color:#8a6a3c;background:rgba(172,134,80,.12);
  border:1px solid rgba(172,134,80,.45);border-radius:999px;padding:3px 9px}
.score{margin-left:auto;font-family:serif;font-size:15px;color:var(--accent)}
.flow{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin:12px 0 10px}
.step{border:1px solid var(--line);border-radius:9px;padding:5px 9px;background:#fff;
  font-size:12.5px;line-height:1.3;display:inline-flex;flex-direction:column;gap:1px}
.step b{font-weight:600}
.step i{font-style:normal;font-size:10.5px;color:var(--ink2);letter-spacing:.04em}
.step i.tier{display:inline-block;margin-left:4px;padding:0 4px;border-radius:3px;font-size:10px;letter-spacing:.02em}
.wt{display:flex;align-items:center;gap:6px;font-size:11.5px;margin:3px 0}
.wt span{width:56px;color:#5b6b62;flex:0 0 auto}
.wt input{flex:1;accent-color:#2e5740}
.wt b{width:22px;text-align:right;color:#25372d;font-weight:600}
.t-稳{background:rgba(68,135,93,.16);color:#2e6b46}
.t-紧{background:rgba(190,150,60,.2);color:#8a6a1c}
.t-需状态{background:rgba(178,92,62,.16);color:#9a4a2f}
.t-待核{background:rgba(0,0,0,.07);color:#6b6b6b}
.step.g-config{border-color:rgba(68,135,93,.55);background:rgba(68,135,93,.07)}
.step.g-cmd{border-color:rgba(92,123,175,.55);background:rgba(92,123,175,.07)}
.step.g-cond{border-color:rgba(172,134,80,.6);background:rgba(172,134,80,.09)}
.step.g-state{border-color:rgba(123,106,168,.55);background:rgba(123,106,168,.07)}
.step.g-input{border-color:rgba(37,55,45,.35);background:rgba(37,55,45,.04)}
.arrow{color:var(--ink2);font-size:13px}
.stats{display:flex;flex-wrap:wrap;gap:14px;font-size:12.5px;color:var(--ink2);
  border-top:1px dashed var(--line);padding-top:10px}
.stats b{color:var(--ink);font-weight:600}
.bars{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px;margin-top:10px}
.bar{font-size:11.5px;color:var(--ink2)}
.bar .track{height:6px;border-radius:99px;background:rgba(37,55,45,.1);margin-top:3px;overflow:hidden}
.bar .fill{height:100%;border-radius:99px;background:var(--config)}
.bar .fill.over{background:var(--warn)}
.risks{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.risk{font-size:11px;color:var(--warn);border:1px solid rgba(180,85,63,.35);
  background:rgba(180,85,63,.06);border-radius:999px;padding:2px 8px}
details{margin-top:10px}
summary{cursor:pointer;font-size:12px;color:var(--ink2)}
table{width:100%;border-collapse:collapse;margin-top:8px;font-size:12px}
th,td{text-align:left;padding:6px 7px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--ink2);font-weight:600;font-size:11px;letter-spacing:.06em}
td.num{font-variant-numeric:tabular-nums;white-space:nowrap}
.more-wrap{display:flex;justify-content:center;margin:18px 0 8px}
.more{background:#fffef9;border:1px solid #bdcdb9;color:#2e5740;border-radius:999px;padding:8px 22px;font-size:13px;cursor:pointer}
.more:hover{background:#eef2ea}
.empty{color:var(--ink2);font-size:13px;padding:30px;text-align:center;border:1px dashed var(--line);border-radius:14px}
.foot{margin-top:18px;font-size:11.5px;color:var(--ink2);line-height:1.7;border-top:1px solid var(--line);padding-top:12px}
.legend{display:flex;gap:14px;flex-wrap:wrap;font-size:11.5px;color:var(--ink2);margin-top:2px}
.legend i{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:5px}
@media(max-width:900px){main{grid-template-columns:1fr}.panel{position:static}}
</style>
</head>
<body>
<header class="top">
  <div class="brand">
    <span class="mark">師</span>
    <div><h1>徒手连招编排器</h1><p class="sub">敌人 × 入口 × 目标 → 由解包配置推导的可选连段</p></div>
  </div>
  <div class="top-note">静态配置推导 · 非实测 · 命中与时机需实战校验</div>
</header>
<main>
  <aside class="panel">
    <section class="panel-box">
      <h2>敌 人</h2>
      <label>原型<select id="arch"></select></label>
      <label>具体<select id="enemy"></select></label>
    </section>
    <section class="panel-box enemy-card" id="enemyCard"></section>
    <section class="panel-box">
      <h2>入 口</h2>
      <div class="tabs" id="entryTabs"></div>
      <p class="hint" id="entryHint"></p>
    </section>
    <section class="panel-box">
      <h2>筛 选</h2>
      <label style="display:flex;align-items:center;gap:6px;font-size:12px;margin-bottom:6px">
        <input type="checkbox" id="strict" style="width:auto"> 只看设计内衔接（配置边 + 状态入口，不含指令重入）
      </label>
      <label>起点招式<select id="startNode"></select></label>
      <p class="hint" style="margin-top:6px">选某个招式后只保留以它为起点的连段；留空则按入口筛选。</p>
    </section>
    <section class="panel-box">
      <h2>权 重</h2>
      <div class="tabs" id="presetTabs"></div>
      <div id="wtBox"></div>
    </section>
    <section class="panel-box">
      <h2>目 标</h2>
      <div class="tabs" id="goalTabs"></div>
      <div class="legend">
        <span><i style="background:#44875d"></i>配置衔接</span>
        <span><i style="background:#5c7baf"></i>指令重入</span>
        <span><i style="background:#ac8650"></i>条件衔接</span>
        <span><i style="background:#7b6aa8"></i>状态入口</span>
      </div>
    </section>
  </aside>
  <section class="results">
    <div class="results-head">
      <h2 id="resultTitle"></h2>
      <p id="resultSub"></p>
    </div>
    <div id="list"></div>
    <div class="more-wrap"><button id="moreBtn" class="more">显示更多</button></div>
    <footer class="foot">
      <b>口径</b>：连段树边＝设计层保证的衔接；指令重入＝可用性层 FollowUp 允许的输入（Alt / Rush / 抓取 / 同招重入被排除）；
      状态入口＝starts 条件入口。阈值语义为<b>窗口内累计上限</b>——眩晕窗口累计命中达到上限、累计伤害超过上限即脱离；
      倒地窗口最多再吃 2 击；破防窗口 3.0 秒。所有数值取自解包的命中判定表与状态反应表，属静态估算，不代表实战命中结果。
      <br>衔接档位：<b>稳</b>（间隔≤24帧）/ <b>紧</b>（≤29帧，与官方连段同档）/ <b>需状态</b>（30–45帧，需敌人处于推击等长状态）/ <b>待核</b>（该招式缺窗口数据）。间隔 = 前段收招窗口帧 + 后段首判定帧 − 前段末判定帧，用于判断敌人受击硬直是否还够；它不刻画格挡与闪避的 AI 决策。
    </footer>
  </section>
</main>
<script>
const DATA = /*__DATA__*/;
const S = {arch:null, enemy:null, entry:null, goal:"overall", limit:20, total:0, strict:false, start:"",
           wt:{dmg:34,struct:26,sdiz:20,len:12,fin:8,risk:22}};
const WT_KEY="sifu.combo.weights.v7";
const WT_META=[["dmg","伤害"],["struct","结构"],["sdiz","特殊眩晕"],["len","连段长度"],["fin","收尾质量"],["risk","风险惩罚"]];
const PRESETS=[
  ["均衡",{dmg:34,struct:26,sdiz:20,len:12,fin:8,risk:22}],
  ["眩晕压制",{dmg:20,struct:10,sdiz:50,len:10,fin:10,risk:24}],
  ["破防",{dmg:10,struct:55,sdiz:15,len:10,fin:10,risk:18}],
  ["爆伤",{dmg:55,struct:10,sdiz:10,len:15,fin:10,risk:20}],
  ["处决",{dmg:25,struct:25,sdiz:20,len:15,fin:15,risk:25}]
];
try{const w=JSON.parse(localStorage.getItem(WT_KEY)||"null"); if(w) Object.assign(S.wt,w);}catch(e){}

function el(id){return document.getElementById(id)}
function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]))}
const GRADE_NAME = {config:"配置", cmd:"指令", cond:"条件", state:"状态", input:"输入"};
const GAP_TIGHT=24, GAP_OK=29, GAP_COND=45;
const FPS=60;

function tierOf(g){ if(g==null) return "待核"; if(g<=GAP_TIGHT) return "稳"; if(g<=GAP_OK) return "紧"; if(g<=GAP_COND) return "需状态"; return "超界"; }

function saveWt(){ try{localStorage.setItem(WT_KEY, JSON.stringify(S.wt));}catch(e){} }
function renderWeights(){
  el("wtBox").innerHTML = WT_META.map(([k,label])=>
    `<div class="wt"><span>${label}</span><input type="range" min="0" max="60" value="${S.wt[k]}" data-k="${k}"><b>${S.wt[k]}</b></div>`).join("");
  el("wtBox").querySelectorAll("input").forEach(inp=>{
    inp.oninput=()=>{S.wt[inp.dataset.k]=+inp.value; inp.nextElementSibling.textContent=inp.value; saveWt(); render();};
  });
  el("presetTabs").innerHTML = PRESETS.map(([n])=>`<span class="tab" data-n="${n}">${n}</span>`).join("");
  el("presetTabs").onclick=e=>{const t=e.target.closest(".tab"); if(!t)return;
    const p=PRESETS.find(x=>x[0]===t.dataset.n); if(p){Object.assign(S.wt,p[1]); saveWt(); renderWeights(); render();}};
}

function hydrate(ch){
  // 把压缩链展开成渲染用的对象（招式名/数值/时序档位）
  const steps = ch.ids.map((id,i)=>{
    const n = DATA.nodes[id] || {};
    const v = ch.steps[i] || [];
    return {id, name:n.name||id, input:ch.ins[i], grade:ch.gr[i], gap:ch.gap[i], tier:tierOf(ch.gap[i]),
            dmg:v[0]||0, struct:v[1]||0, sdiz:v[2]||0, hits:v[3]||0, stun:v[4]||0,
            frame:v[5], finisher:!!v[6], cond:v[7]||"", kd:n.kd, ground:n.ground, push:n.push};
  });
  const tot = {dmg:0,struct:0,sdiz:0,hits:0,stun:0,kb:0,frames:0,config_ratio:0,cmd_count:0,cond_count:0,min_gap:null,all_ok:true};
  steps.forEach((s,i)=>{
    tot.dmg+=s.dmg; tot.struct+=s.struct; tot.sdiz+=s.sdiz; tot.hits+=s.hits;
    tot.stun=Math.max(tot.stun,s.stun);
    if(s.frame) tot.frames+=Math.round(s.frame[1]-s.frame[0]);
    if(i>0){
      if(s.grade==="config") tot.config_ratio++;
      if(s.grade==="cmd") tot.cmd_count++;
      if(s.grade==="cond") tot.cond_count++;
      if(s.gap!=null) tot.min_gap = tot.min_gap==null?s.gap:Math.min(tot.min_gap,s.gap);
      if(s.tier && s.tier!=="稳" && s.tier!=="紧") tot.all_ok=false;
    }
  });
  tot.dmg=Math.round(tot.dmg); tot.struct=Math.round(tot.struct); tot.sdiz=Math.round(tot.sdiz);
  const denom = Math.max(1, steps.length-1);
  tot.config_ratio = tot.config_ratio/denom;
  return {steps, totals:tot, entry:ch.entry, curated:!!ch.cur, title:ch.title, entry_node:ch.entry_node, ids:ch.ids, ins:ch.ins};
}

function reactionRisk(e, hits){
  const r = e.reaction||{};
  if(!r.mem_trigger || hits < r.mem_trigger) return [0,""];
  const p = (r.prob==null)?1:r.prob;
  const rate = Math.min(1, p + 0.12*(hits-r.mem_trigger));
  const kinds=[]; if(r.parry)kinds.push("弹反"); if(r.guard)kinds.push("格挡"); if(r.dodge||r.avoid)kinds.push("闪避");
  return [Math.round(rate*100)/100, kinds.slice(0,2).join("/")];
}

function scoreChain(ch, e, goal){
  const t=ch.totals, budget=e.dizzy_hits||999;
  let ed=0, es=0, ez=0, used=0, cut=null, segs=0;
  for(let i=0;i<ch.steps.length;i++){
    const s=ch.steps[i];
    let bud=budget;
    if(i>0){
      const prev=ch.steps[i-1];
      if(prev.kd || prev.push || prev.grade==="state"){ used=0; segs++; }
      if(prev.kd) bud=e.down_hits||2;
    }
    if(used>=bud){ cut=i; break; }
    const sh=s.hits||1, room=bud-used;
    if(sh>room){ const f=room/sh; ed+=s.dmg*f; es+=s.struct*f; ez+=s.sdiz*f; used=bud; cut=i+1; break; }
    ed+=s.dmg; es+=s.struct; ez+=s.sdiz; used+=sh;
  }
  t.eff_dmg=Math.round(ed*10)/10; t.eff_struct=Math.round(es*10)/10; t.eff_sdiz=Math.round(ez*10)/10;
  t.eff_hits=used; t.cut_index=cut; t.segments=segs+1;
  t.hits_all=ch.steps.reduce((a,s)=>a+(s.hits||1),0);
  const fin = ch.steps.length && ch.steps[ch.steps.length-1].finisher ? 12 : 0;
  let doubt=1;
  ch.steps.slice(1).forEach(s=>{ if(s.tier==="需状态") doubt-=0.10; else if(s.tier==="待核") doubt-=0.06; });
  doubt=Math.max(0.45,doubt);
  const [risk,kind]=reactionRisk(e,t.eff_hits);
  t.reaction_risk=risk; t.reaction_kind=kind;
  doubt*=(1-(S.wt.risk/100)*risk);
  const dmg=ed;
  let s;
  if(goal==="dizzy") s = dmg + 18*(eh<=budget?1:0) + 0.35*ez + fin;
  else if(goal==="struct"){ const over=Math.max(0,(t.frames||0)-180); s = es*(1-Math.min(0.45,over/400)) + fin; }
  else if(goal==="damage") s = dmg + fin + 0.1*ez;
  else if(goal==="knockdown"){
    const last=ch.steps[ch.steps.length-1]||{};
    s = 0.55*(t.kb||0) + 0.45*dmg + fin + (last.finisher?15:0) + (last.frame && last.stun>=20 ? 6 : 0);
  } else {
    const W=S.wt, sum=Math.max(1,W.dmg+W.struct+W.sdiz+W.len+W.fin);
    s = (W.dmg*Math.min(dmg/180,1.5) + W.struct*Math.min(es/260,1.5) + W.sdiz*Math.min(ez/220,1.5)
        + W.len*t.config_ratio + W.fin*(fin/12))/sum*100;
  }
  t.score = Math.round(s*doubt*10)/10;
  // 风险标签
  const tags=[];
  if(t.cmd_count) tags.push("含指令重入（需收招窗口）");
  if(t.cond_count) tags.push("含条件衔接（需敌人状态）");
  if(t.frames && e.struct_duration && t.frames > e.struct_duration*FPS) tags.push("动作时长超破防窗口");
  if(t.cut_index!=null) tags.push("超出当前状态窗口的命中预算");
  if(ch.steps.length && !ch.steps[ch.steps.length-1].finisher) tags.push("非收尾节点，收招留破绽");
  if(t.reaction_risk) tags.push("末端有 "+Math.round(t.reaction_risk*100)+"% 被"+(t.reaction_kind||"防御")+"风险");
  if(ch.steps.some(x=>x.kd)) tags.push("含击倒（击倒后连段终止）");
  if(ch.steps.some(x=>x.push)) tags.push("含推击（后续接追打）");
  ch.risks = tags;
  return t.score;
}

function init(){
  const archSel=el("arch");
  DATA.archetypes.forEach(a=>{const o=document.createElement("option");o.value=a;o.textContent=a;archSel.appendChild(o)});
  S.arch=DATA.archetypes[0];
  archSel.onchange=()=>{S.arch=archSel.value;fillEnemies()};
  fillEnemies();
  el("strict").checked=S.strict;
  el("strict").onchange=()=>{S.strict=el("strict").checked;S.limit=20;render()};
  const sn=el("startNode");
  sn.innerHTML='<option value="">（不限）</option>'+Object.keys(DATA.nodes).map(id=>
    `<option value="${id}">${esc(DATA.nodes[id].name||id)}</option>`).join("");
  sn.onchange=()=>{S.start=sn.value;S.limit=20;render()};
  renderWeights();
  el("entryTabs").innerHTML=Object.entries(DATA.entries).map(([k,v])=>
    `<span class="tab" data-k="${k}">${esc(v.label)}</span>`).join("");
  el("entryTabs").onclick=e=>{const t=e.target.closest(".tab");if(!t)return;S.entry=t.dataset.k;S.limit=20;render()};
  el("goalTabs").innerHTML=DATA.goals.map(g=>`<span class="tab" data-k="${g.key}">${esc(g.label)}</span>`).join("");
  el("goalTabs").onclick=e=>{const t=e.target.closest(".tab");if(!t)return;S.goal=t.dataset.k;S.limit=20;render()};
}

function fillEnemies(){
  const list=DATA.enemies.filter(e=>e.archetype===S.arch);
  const sel=el("enemy");
  sel.innerHTML=list.map(e=>`<option value="${e.key}">${esc(e.name)}</option>`).join("");
  S.enemy=list[0]?list[0].key:null;
  sel.onchange=()=>{S.enemy=sel.value;S.limit=20;render()};
  if(!S.entry) S.entry=Object.keys(DATA.entries)[0];
  render();
}

function enemyCard(){
  const e=DATA.enemies.find(x=>x.key===S.enemy); if(!e)return "";
  const row=(k,v)=>`<div class="kv"><span>${k}</span><b>${v}</b></div>`;
  const r=e.reaction||{};
  let react="—";
  if(r.mem_trigger){
    const p=r.prob==null?"必触发":Math.round(r.prob*100)+"%";
    const kinds=[];
    if(r.parry)kinds.push("弹反"); if(r.guard)kinds.push("格挡");
    if(r.dodge||r.avoid)kinds.push("闪避");
    react=`连续 ${r.mem_trigger} 击后 ${p} ${kinds.join("/")||"防御"}`;
  }
  return `<div class="en-arch">${esc(e.archetype)}${e.version?" · "+esc(e.version):""}</div>
    <div class="en-name">${esc(e.name)}</div>
    ${row("眩晕窗口预算", `${e.dizzy_dmg==null?"—":e.dizzy_dmg+" 伤害"} / ${e.dizzy_hits==null?"—":e.dizzy_hits+" 命中"}`)}
    ${row("倒地窗口", `${e.down_hits==null?"—":"最多 "+e.down_hits+" 击"}`)}
    ${row("破防窗口", `${e.struct_duration==null?"—":e.struct_duration+" s"}`)}
    ${row("特殊眩晕", `${e.super_duration==null?"—":e.super_duration+" s"}`)}
    ${row("防御反应", react)}`;
}

function stepChip(st,i){
  const cls="g-"+st.grade;
  const inl = i===0 ? (st.grade==="state"?"入场":st.input) : st.input;
  const tip = [
    st.name,
    i===0 ? "入口：" + (st.grade==="state"?"敌人状态触发":"默认输入起手") : "衔接：" + (GRADE_NAME[st.grade]||""),
    i===0 ? "" : ("衔接间隔：" + (st.gap==null?"待核":Math.round(st.gap)+"f（"+(st.tier||"待核")+"）")),
    i===0 ? "" : ("伤害 " + st.dmg + " · 结构 " + st.struct + " · 特殊眩晕 " + st.sdiz),
    i===0 ? ("判定窗口 " + (st.frame?Math.round(st.frame[0])+"–"+Math.round(st.frame[1])+"f":"—")) : ("命中 " + st.hits + " · 硬直 " + st.stun + "f" + (st.finisher?" · 收尾":""))
  ].filter(Boolean).join("\n");
  return `<span class="step ${cls}" title="${esc(tip)}"><b>${esc(st.name)}</b><i>${esc(inl)}</i></span>`;
}

function bars(tot,e){
  const b=(label,val,max,noOver)=>{
    const p=Math.max(0,Math.min(1,val/(max||1)));
    const over=(!noOver)&&val>max;
    return `<div class="bar"><div>${label} <b>${val}</b>${max?` / ${max}`:""}</div>
      <div class="track"><div class="fill ${over?"over":""}" style="width:${(p*100).toFixed(0)}%"></div></div></div>`;
  };
  let out="";
  const seg=tot.segments||1;
  const segTag=seg>1?` · 跨 ${seg} 段窗口`:"";
  if(e.dizzy_hits) out+=b(seg>1?`命中（全链）vs 每段预算`:`命中 vs 眩晕预算`, seg>1?tot.hits_all:tot.eff_hits, e.dizzy_hits, seg>1);
  if(e.dizzy_dmg) out+=b(`伤害 vs 眩晕预算${segTag}`, Math.round(tot.eff_dmg), e.dizzy_dmg, seg>1);
  if(e.down_hits) out+=`<div class="bar"><div>倒地窗口 <b>最多 ${e.down_hits} 击</b> · 仅对倒地追击生效</div></div>`;
  return out?`<div class="bars">${out}</div>`:"";
}

function detailTable(ch){
  const rows = ch.steps.map((s,i)=>{
    const fr = s.frame?`${Math.round(s.frame[0])}–${Math.round(s.frame[1])}f`:"—";
    const cond = s.cond?`<div style="font-size:10.5px;color:#8a6a3c">${esc(String(s.cond).split(".").pop().split("_C_")[0])}</div>`:"";
    return `<tr>
      <td class="num">${i+1}</td>
      <td><b>${esc(s.name)}</b>${cond}</td>
      <td>${esc(s.input)}</td>
      <td style="white-space:nowrap">${GRADE_NAME[s.grade]||"-"}</td>
      <td class="num" style="white-space:nowrap">${i===0?"—":`${esc(s.tier||"待核")}${s.gap!=null?" "+Math.round(s.gap)+"f":""}`}</td>
      <td class="num">${s.dmg}</td>
      <td class="num">${s.struct}</td>
      <td class="num">${s.sdiz}</td>
      <td class="num">${s.hits}</td>
      <td class="num">${s.stun}f</td>
      <td class="num">${fr}</td>
    </tr>`;
  }).join("");
  return `<details><summary>逐步明细（含判定窗口与逐段数值）</summary>
    <table><thead><tr><th>#</th><th>招式</th><th>输入</th><th>衔接</th><th>衔接间隔</th><th>伤害</th><th>结构</th><th>特殊眩晕</th><th>命中</th><th>硬直</th><th>判定窗口</th></tr></thead>
    <tbody>${rows}</tbody></table></details>`;
}

function chainCard(ch,i,best){
  const t=ch.totals;
  const risks=(ch.risks||[]).map(r=>`<span class="risk">${esc(r)}</span>`).join("");
  return `<article class="chain ${best?"is-best":""}">
    <div class="chain-head">
      <span class="idx">${String(i+1).padStart(2,"0")}</span>
      <span class="entry-chip">入口 · ${esc(ch.entry)}</span>
      ${ch.curated?`<span class="tag-curated">${esc(ch.title||"社区路线")}</span>`:""}
      <span class="score">${ch.totals.score}</span>
    </div>
    <div class="flow">${ch.steps.map(stepChip).join('<span class="arrow">›</span>')}</div>
    <div class="stats">
      <span>伤害 <b>${t.dmg}</b></span><span>结构 <b>${t.struct}</b></span>
      <span>特殊眩晕 <b>${t.sdiz}</b></span><span>命中 <b>${t.hits}</b></span>
      <span>最大硬直 <b>${t.stun}f</b></span><span>动作帧 <b>${t.frames}</b></span>
      <span>最紧衔接 <b>${t.min_gap==null?"—":Math.round(t.min_gap)+"f"}</b></span>
      <span>连招判定 <b>${t.all_ok?"时序可达":"含状态依赖"}</b></span>
      <span>末端反应 <b>${t.reaction_risk?Math.round(t.reaction_risk*100)+"% "+(t.reaction_kind||""):"—"}</b></span>
      ${t.cut_index!=null?`<span>有效输出 <b>伤害 ${t.eff_dmg} · 结构 ${t.eff_struct} · 命中 ${t.eff_hits}</b>（第 ${t.cut_index+1} 段起可能已脱离）</span>`:""}
      <span>衔接口径 <b>配置 ${Math.round(t.config_ratio*100)}% · 指令 ${t.cmd_count} · 条件 ${t.cond_count}</b></span>
    </div>
    ${bars(t, DATA.enemies.find(x=>x.key===S.enemy)||{})}
    ${risks?`<div class="risks">${risks}</div>`:""}
    ${detailTable(ch)}
  </article>`;
}

function render(){
  el("entryTabs").querySelectorAll(".tab").forEach(t=>t.classList.toggle("on",t.dataset.k===S.entry));
  el("goalTabs").querySelectorAll(".tab").forEach(t=>t.classList.toggle("on",t.dataset.k===S.goal));
  const ent=DATA.entries[S.entry]; if(ent) el("entryHint").textContent=ent.hint;
  el("enemyCard").innerHTML=enemyCard();
  const e=DATA.enemies.find(x=>x.key===S.enemy);
  const pool=DATA.pool[S.entry]||[];
  let list=pool.map(hydrate);
  if(S.strict) list=list.filter(c=>c.steps.every(s=>s.grade!=="cmd"&&s.grade!=="cond"));
  if(S.start) list=list.filter(c=>c.ids[0]===S.start);
  list.forEach(c=>scoreChain(c,e,S.goal));
  list.sort((a,b)=>b.totals.score-a.totals.score);
  S.total=list.length;
  const shown=list.slice(0,S.limit);
  el("resultTitle").textContent=e?`${e.name} · ${ent?ent.label:""} · ${(DATA.goals.find(g=>g.key===S.goal)||{}).label||""}`:"";
  el("resultSub").textContent=list.length
    ? `共 ${list.length} 条可连带（按「${(DATA.goals.find(g=>g.key===S.goal)||{}).label||""}」评分排序，已显示前 ${shown.length} 条）`
    : "该组合下没有可推导的连段：尝试切换入口或目标。";
  el("list").innerHTML = shown.length
    ? shown.map((c,i)=>chainCard(c,i,i===0)).join("")
    : `<div class="empty">该组合下没有可推导的连段：尝试切换入口或目标。</div>`;
  const btn=el("moreBtn");
  btn.style.display = list.length>S.limit ? "inline-block" : "none";
  btn.textContent = `显示更多（还有 ${list.length-S.limit} 条）`;
  btn.onclick=()=>{S.limit+=30;render()};
}

init();
</script>
</body>
</html>
"""


def render_html(data):
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return HTML_TPL.replace("/*__DATA__*/", js)


def render_readme(data, pool):
    lines = []
    lines.append("# 徒手连招图 v8（单文件 HTML）\n")
    lines.append("工具把招式画成**有向图**：同一招只有一个节点，后续分支从它分出；一条完整路径成立，它的任一前缀也成立。\n")
    lines.append("## 运行\n")
    lines.append("```\nD:\\Programes\\PY\\python.exe scripts\\combo_orchestrator_v3.py\n```\n")
    lines.append("输出到本目录：`连招编排器.html`（自包含，双击即用）、`combo-graph.json`（图数据）、`README.md`。\n")
    lines.append("## 入口的定义（用户口径）\n")
    for k, spec in ENTRY_SPECS.items():
        lines.append(f"- **{spec['label']}**：{spec['hint']}")
    lines.append("\n## 衔接的三类证据\n")
    lines.append("| 等级 | 含义 | 数据依据 |")
    lines.append("|---|---|---|")
    lines.append("| 配置 | 设计层保证的连招树边 | board-data.json edges（100% 概率、无条件） |")
    lines.append("| 指令 | 收招窗口内的指令攻击重入 | availability-layers.json 各 FollowUp 层排除集 |")
    lines.append("| 条件 | 需敌人状态的树边 | edges.conditional + condition_ref |")
    lines.append("\n帧余量（前段硬直 − 下段首判定帧）不作为可行性判据：实测该差值在游戏自带连段边上分布于 −17…+17 帧，"
                 "说明连段内下一段并非从动画第 0 帧起手，帧推演无法断言真连；v4 改用「收招窗口帧 + 首判定帧 − 末判定帧」的衔接间隔判定：间隔 ≤24 帧记「稳」、≤29 帧记「紧」（与官方连段同档）、30–45 帧记「需状态」（仅条件边成立），>45 帧直接剪掉。\n")
    lines.append("## 敌人目录（训练场「原型 / 版本」两级）\n")
    lines.append("原型名取自本地化 `General_*`（如 `General_Grunt=帮派成员`、`General_BigGuy=巨无霸`、"
                 "`General_Flashkick=闪电踢`、`General_Disciple=弟子`、`General_Bodyguard=保镖`，侦探板里帮派成员另称「帮派分子」）；"
                 "版本名取自 `ArchetypeVersion_*`（基础 / 高级 / 小Boss）。**并非每类都有三档**：闪电踢只有「标准」，"
                 "首领（法贾/肖恩/黑木/扬/凤姐/师父）只有阶段或无版本，弟子/保镖另有「易化」难度档但不作为版本列出。\n")
    lines.append("## 敌人防御反应（脱离机制的一部分）\n")
    lines.append("每个原型×版本的 `*_ContextualDefense.uasset` 里有一张 `AIContextualDefense` 影响图，其中的 "
                 "`AttackMemoryInfluenceTest` 记录了「多久之内挨了几次同类命中就触发防御反应」：")
    lines.append("- 帮派成员 基础：1 击 / 2 秒、5 击 / 5 秒，触发概率 0.7；高级多一条 2 击 / 4 秒；")
    lines.append("- 巨无霸：2 击 / 5–6 秒（无概率节点，视为必触发）；")
    lines.append("- 保镖：1–2 击 / 5 秒 + 概率 0.5/0.7；闪电踢：1 击 / 3 秒、4 击 / 2 秒、5 击 / 5 秒；")
    lines.append("- 黑木 1 击 / 7 秒、8 击 / 5 秒；肖恩 2 击 / 3 秒、4 击 / 10 秒；扬 1 击 / 3 秒、2 击 / 10 秒；师父 1–2 击 / 10–15 秒。")
    lines.append("工具取该敌人**最大的命中阈值**作为「看穿点」：连段命中数不到它 → 不触发；超过后按 "
                 "`概率 + 0.12×(超出次数)` 估算末端被弹反/格挡/闪避的风险，并扣减评分。"
                 "这正是「连招打到末端被格挡、砍掉前几段就收得住」的来源。\n")
    lines.append("## 倒地约束\n")
    lines.append("追亡逐北、扫腿、回旋踢、旋转高踢、使绊子等收尾会把敌人打倒在地；倒地窗口最多再吃 2 击，"
                 "且**只有下段/追击招式（袭裆拳、其追击、追亡逐北）还能命中**。因此这类收尾之后，"
                 "引擎只保留指向这几招的衔接，其余衔接一律剪掉，不会出现「放倒后还接着打站立招式」的假连段。\n")
    lines.append("## 阈值口径（易误读）\n")
    lines.append("m_fMaxAccumulatedDamage / m_iMaxAccumatedHits 是**状态退出阈值**，不是触发阈值：\n")
    lines.append("- 眩晕窗口内累计命中达到上限、累计伤害超过上限，敌人即脱离；")
    lines.append("- 倒地窗口最多再吃 2 击；")
    lines.append("- 破防窗口 3.0 秒（结束恢复 30% 格挡系数）。\n")
    lines.append("因此「眩晕窗口」目标下，工具优先推荐**命中预算内伤害最高**的连段，命中数超出预算会被折损。\n")
    lines.append("## 有效输出（为什么长连段不一定是好连段）\n")
    lines.append("眩晕窗口预算（如帮派成员 4 击 / 100 伤害）是敌人脱离条件，所以工具在计分时只统计**敌人脱离之前**的输出："
                 "命中数累计到预算为止，超出部分按比例折算或不计入，并单独标「有效输出」。"
                 "这正是「砍掉前几段就能收尾」的量化：比预算更长的连段，末尾几段在实战中大概率被弹反/格挡/闪避。\n")
    lines.append("## 敌人姿态状态（v6 新增）\n")
    lines.append("引擎不再假定敌人永远站着。每招的行为属性取自攻击资产 `AttackDB.m_AttackProperties`，由它决定敌人被打成什么状态：\n")
    lines.append("| 属性 | 含义 | 代表招式 |")
    lines.append("|---|---|---|")
    lines.append("| `Attack.HitProperties.KnockDown` | 击倒 | 扫腿、回旋踢、旋转高踢、拉开后重击追打、抓击后肘击 |")
    lines.append("| `Attack.HitProperties.PushBack` | 推击（敌人被击退） | 推掌（后前轻）、向前踢击衔接 |")
    lines.append("| 判定高度带 `EAttackTarget` | High/Mid_1/Mid_2/Low，描述该招的判定高度；倒地目标贴地，Mid 以上判定挥空 | 袭裆拳=Mid_1、扫腿=Low |")
    lines.append("| `Attack.Specific.SkillFollowKD` / `SkillFollowDmg` | 推击后专用追打 | 追亡逐北、乘胜追击 |")
    lines.append("| `Attack.Defense.Unblockable` | 破防（不可格挡） | 避短扬长（长按轻） |")
    lines.append("\n状态转换：站立 →（击倒）→ 倒地，**连段终止**——倒地目标的受击盒贴地，站立的 Mid/High 判定从其上方挥空，"
                 "因此击倒类收尾之后不再推荐任何后续招式（早期版本曾据 `Attack.AvoidProperties.Grounded` 标签推断「袭裆拳可打倒地」，"
                 "该推断未经证实且与实际不符，已移除）；站立 →（推击）→ 被击退，此时**只允许推击后专用招式**"
                 "（轻→轻击第3段/乘胜追击，重→追亡逐北/重击第2段）；其余情况回到站立。\n")
    lines.append("**鹰击长空（拉开距离攻击，节点 52）单列**：判定只在敌方出招前摇时成立，普通闪避后打不到人，"
                 "因此不进入任何连段、也不作为入口。\n")
    lines.append("## 权重与筛选（v7 新增）\n")
    lines.append("- 六个权重滑块：伤害 / 结构 / 特殊眩晕 / 连段长度 / 收尾质量 / 风险惩罚；前五项归一化后加权，风险惩罚直接乘在总分上；预设「均衡 / 眩晕压制 / 破防 / 爆伤 / 处决」，改动保存在浏览器本地；")
    lines.append("- 起点招式下拉：只保留以该招为第一段的链，用来反向查「这招后面能接什么」；")
    lines.append("- 「只看设计内衔接」勾选后剔除含指令重入的链，只留配置边与状态入口。\n")
    lines.append("## 状态切换会重置命中预算（v7 修正）\n")
    lines.append("- 眩晕窗口的命中上限只在**同一姿态**内累计：推掌把敌人打进击退姿态、追亡逐北把敌人打倒，预算随姿态切换重新计算，倒地后再给 2 击的额度；")
    lines.append("- 推击后的衔接按 PushInstigator 状态入口处理（轻→疾风连环·3 / 乘胜追击，重→追亡逐北 / 重击·2），属状态保证的必中，不再是「条件分支」；")
    lines.append("- 偷招检查（BP_ComboTransition_CheatComboCheck）归为「需输入时机」的设计内连段，不当作敌人状态条件。\n")
    lines.append("## 全量输出与前端评分\n")
    lines.append("- 引擎只做与敌人无关的枚举：每条链给出招式序列、输入、衔接等级与间隔、逐段数值；")
    lines.append("- 前端按当前敌人 + 目标即时计算：眩晕预算内的**有效输出**、末端防御反应概率、目标分与风险标签，再排序显示；")
    lines.append("- 列表默认显示前 20 条，底部「显示更多」每次追加 30 条，直到全部；")
    lines.append("- 连段池规模见文末。\n")
    lines.append("## 搜索与排序\n")
    lines.append("- 引擎按「输入键序列」做逐层 beam 搜索：每层按起点分配配额，避免长链把短而关键的支路挤掉；")
    lines.append("- 每条链最多 8 段、指令重入最多 3 次、条件边最多 2 次，且同一段不重复；")
    lines.append("- 打分 = 0.6×有效伤害 + 0.5×有效结构 + 0.4×有效特殊眩晕 + 10×收尾奖励 + 8×配置衔接占比，"
                 "再乘「衔接可信度」与「敌人末端反应」系数；")
    lines.append("- 同一组招式换个重入顺序不算新思路：完全同序同输入的链只留一条，同一招式集合最多保留 2 条不同起手；")
    lines.append("- 人工整理的社区路线（全部经引擎逐步校验）标注「社区路线」，与推导链一起排序展示。\n")
    lines.append("## 结果怎么读\n")
    lines.append("连段卡里每个招式节点只显示「招式名 + 输入」，鼠标悬停可看到该段的衔接类型、衔接间隔、伤害/结构/特殊眩晕/命中/硬直与判定窗口；")
    lines.append("下方数值行给出累计伤害/结构/特殊眩晕/命中/最大硬直/动作帧、最紧衔接、连招判定与衔接口径（配置占比 · 指令数 · 条件数）。")
    lines.append("风险标签含义：起手可能被抢/被格挡（仅主动进攻）、含指令重入、含条件衔接、"
                 "命中数超眩晕预算、动作时长超破防窗口、非收尾节点、末端被弹反/格挡/闪避的概率。\n")
    lines.append("## 图规模\n")
    edges = (pool or {}).get("edges") or []
    cfg = [e for e in edges if e.get("grade") == "config"]
    stt = [e for e in edges if e.get("grade") == "state"]
    cmd = [e for e in edges if e.get("grade") == "cmd"]
    lines.append(f"- 节点 {len(data.get('nodes') or {})} 个；衔接 {len(edges)} 条（配置边 {len(cfg)} · 状态入口 {len(stt)} · 指令重入 {len(cmd)}）")
    for k, spec in ENTRY_SPECS.items():
        lines.append(f"- {spec['label']}：起点 {'、'.join(spec['starts'])}")
    lines.append("\n## 边界\n")
    lines.append("- 全部数值为静态配置估算，未做游戏内实测；")
    lines.append("- 连招树只证明配置衔接，不保证敌人不出手、不格挡；")
    lines.append("- 起手（主动进攻）是否被抢先属对手 AI 行为，本工具只能提示风险；")
    lines.append("- 后续验证建议：从「招架反击」入口挑 2–3 条，在训练/低难度场景按步骤复现。\n")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
