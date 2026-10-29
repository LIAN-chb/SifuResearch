"""Decode the two resilience service CDOs and two Grunt animation notify windows."""
import hashlib, json, struct, sys
from pathlib import Path
ROOT = Path(r"E:\ProgrameFiles\SifuResearch")
sys.path.insert(0, str(ROOT / "tools"))
import local_bounded_packages as q
EXTRACTED = ROOT / "logs/case-resilience/extracted"

def refname(pkg, index, seen=None):
    if index == 0: return None
    seen = set() if seen is None else set(seen)
    if index in seen: return "<cycle>"
    seen.add(index)
    if index < 0:
        item = pkg["imports"][-index - 1]
        outer = refname(pkg, item["outer"], seen)
    else:
        item = pkg["exports"][index - 1]
        outer = refname(pkg, item["outerIndex"], seen)
    return (outer + "." if outer else "") + item["name"]

def decode_array_struct(raw, names, field_name, meta):
    rr = q.Reader(raw, names)
    count = rr.number("i")
    inner_name, inner_type = rr.name(), rr.name()
    size, array_index = rr.number("i"), rr.number("i")
    struct_name = rr.name()
    rr.take(16)  # struct GUID
    has_guid = rr.number("B")
    if has_guid == 1: rr.take(16)
    elif has_guid != 0: raise ValueError("invalid inner array GUID flag")
    if inner_name != field_name or inner_type != "StructProperty" or array_index != 0:
        raise ValueError(f"unexpected inner array tag {inner_name}/{inner_type}/{array_index}")
    if size != len(raw) - rr.position or not 0 <= count <= 10000:
        raise ValueError("inner array size/count out of bounds")
    elements = []
    for _ in range(count):
        payload = raw[rr.position:]
        props, consumed = q.tags(payload, names)
        if consumed <= 0: raise ValueError("empty array struct")
        enrich(props, payload[:consumed], meta)
        elements.append(props)
        rr.position += consumed
    if rr.position != len(raw): raise ValueError("array elements do not consume payload")
    return struct_name, elements

def enrich(props, raw, meta):
    for prop in props:
        chunk = raw[prop["valueOffset"]:prop["valueOffset"] + prop["size"]]
        if isinstance(prop.get("value"), list):
            enrich(prop["value"], chunk, meta)
        elif prop["type"] == "ObjectProperty" and isinstance(prop.get("value"), int):
            prop["reference"] = refname(meta, prop["value"])
        elif prop["type"] == "ArrayProperty" and prop.get("inner") == "StructProperty":
            try:
                struct_name, elements = decode_array_struct(chunk, meta["names"], prop["name"], meta)
                prop["arrayStruct"] = struct_name
                prop["arrayElements"] = elements
            except (ValueError, struct.error) as error:
                prop["arrayDecodeError"] = str(error)

def parse_exports(path):
    meta = q.read_package(path, EXTRACTED)
    body = path.with_suffix(".uexp").read_bytes()
    header_size = path.stat().st_size
    result = []
    for ordinal, export in enumerate(meta["exports"], 1):
        start = export["serialOffset"] - header_size
        raw = body[start:start + export["serialSize"]]
        try:
            props, consumed = q.tags(raw, meta["names"])
            enrich(props, raw, meta)
            result.append({"ordinal": ordinal, "name": export["name"], "classIndex": export["classIndex"],
                           "superIndex": export["superIndex"], "serialSize": export["serialSize"],
                           "properties": props, "propertyBytes": consumed,
                           "suffixBytes": len(raw) - consumed})
        except (ValueError, struct.error) as error:
            result.append({"ordinal": ordinal, "name": export["name"], "classIndex": export["classIndex"],
                           "superIndex": export["superIndex"], "serialSize": export["serialSize"],
                           "decodeError": str(error), "rawHead": raw[:32].hex()})
    return meta, body, result

services = []
for stem in ("BP_ResilienceOrderService", "BP_SuperResilienceOrderService"):
    path = EXTRACTED / f"Sifu/Content/Animations/System/Orders/Services/Attack/{stem}.uasset"
    meta, body, exports = parse_exports(path)
    cdo = next(e for e in exports if e["name"].startswith("Default__"))
    bonus = next((p["value"] for p in cdo.get("properties", []) if p["name"] == "m_iBonus"), None)
    services.append({"path": meta["path"], "uassetSha256": meta["uassetSha256"],
                     "uexpSha256": hashlib.sha256(body).hexdigest(),
                     "classExport": next(e for e in exports if not e["name"].startswith("Default__")),
                     "cdoName": cdo["name"], "cdoProperties": cdo.get("properties"),
                     "m_iBonus": bonus, "allExports": exports,
                     "classParentImports": meta["imports"][:3]})

animations = []
for folder, stem in (("KneeStrike", "Grunt_Attack_Barehands_KneeStrike"),
                     ("SpinKick", "Grunt_Attack_Barehands_SpinKick")):
    path = EXTRACTED / f"Sifu/Content/Animations/Grunt/Attacks/Barehands/{folder}/{stem}.uasset"
    meta, body, exports = parse_exports(path)
    main = next(e for e in exports if e["name"] == stem)
    notify_array = next(p for p in main["properties"] if p["name"] == "Notifies")
    events = []
    for ordinal, event in enumerate(notify_array.get("arrayElements", [])):
        by_name = {p["name"]: p for p in event}
        if by_name.get("NotifyName", {}).get("value") != "OrderServiceNotifyState": continue
        end_link = by_name.get("EndLink", {}).get("value", [])
        end_value = next((p["value"] for p in end_link if p["name"] == "LinkValue"), None)
        events.append({"eventOrdinal": ordinal, "notifyName": by_name["NotifyName"]["value"],
                       "notifyStateClass": by_name.get("NotifyStateClass", {}).get("reference"),
                       "triggerTimeOffset": by_name.get("TriggerTimeOffset", {}).get("value"),
                       "startLinkValue": by_name.get("LinkValue", {}).get("value"),
                       "endTriggerTimeOffset": by_name.get("EndTriggerTimeOffset", {}).get("value"),
                       "endLinkValue": end_value,
                       "duration": by_name.get("Duration", {}).get("value"),
                       "trackIndex": by_name.get("TrackIndex", {}).get("value"),
                       "notifyTriggerChance": by_name.get("NotifyTriggerChance", {}).get("value"),
                       "bTriggerOnDedicatedServer": by_name.get("bTriggerOnDedicatedServer", {}).get("value"),
                       "m_ServiceClassRef": next((p.get("reference") for e in exports if "OrderServiceNotifyState" in e["name"] for p in e.get("properties", []) if p["name"] == "m_ServiceClass"), None)})
    main_props = {p["name"]: p for p in main["properties"]}
    animations.append({"path": meta["path"], "uassetSha256": meta["uassetSha256"],
                       "uexpSha256": hashlib.sha256(body).hexdigest(), "mainExport": stem,
                       "numFrames": main_props["NumFrames"]["value"],
                       "sequenceLengthSeconds": main_props["SequenceLength"]["value"],
                       "notifyArrayStruct": notify_array.get("arrayStruct"),
                       "notifyEventCount": notify_array.get("arrayNum", len(notify_array.get("arrayElements", []))),
                       "notifyArrayDecodeError": notify_array.get("arrayDecodeError"),
                       "orderServiceNotifyEvents": events,
                       "note": "LinkValue/EndLink.LinkValue are absolute sequence-time values in this AnimLinkableElement; offsets are recorded separately."})

output = {"batch": "case-resilience-20261028", "sourcePakSha256": "497e7e81fc3bba196d19f7f9fd84597c506fd4dc547905f6989847b1510ff2be",
          "reader": "tools/local_bounded_packages.py q.tags plus bounded AnimNotifyEvent StructProperty array decoder in this script",
          "services": services, "animations": animations,
          "limits": ["Static package data only; animation execution/runtime gate not observed.",
                     "AnimNotifyEvent absolute times are package values, not guarantees that gameplay selected the animation or fired its notify."]}
path = ROOT / "inventory/case-resilience-notifies-20261028.json"
path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"output": str(path), "serviceBonuses": {s["cdoName"]: s["m_iBonus"] for s in services},
                  "windows": [{"animation": a["mainExport"], **a["orderServiceNotifyEvents"][0]} for a in animations]}, ensure_ascii=False, indent=2))
