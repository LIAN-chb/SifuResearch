"""Focused, bounded decoding for Sifu Grunt order DB defaults and Avoided/Deflected services."""
import gzip
import hashlib
import json
import struct
import sys
from pathlib import Path

ROOT = Path(r"E:\ProgrameFiles\SifuResearch")
sys.path.insert(0, str(ROOT / "tools"))
import local_bounded_packages as q

PACKAGES = {
    "OrderAvoided": ROOT / "logs/followup-order-services/extracted/Sifu/Content/Animations/System/Orders/Attacks/OrderAvoided.uasset",
    "OrderDeflected": ROOT / "logs/followup-order-services/extracted/Sifu/Content/Animations/System/Orders/Attacks/OrderDeflected.uasset",
    "BP_OrderDB": ROOT / "logs/followup-order-services/extracted/Sifu/Content/Animations/System/Orders/BP_OrderDB.uasset",
    "OrderServiceIsPlayerCondition": ROOT / "logs/followup-order-services/extracted/Sifu/Content/Animations/System/Orders/Services/OrderServiceIsPlayerCondition.uasset",
    "DeflectedParryCancelAvailabilityOrderService": ROOT / "logs/followup-order-services/extracted/Sifu/Content/Animations/System/Orders/Services/Parry/DeflectedParryCancelAvailabilityOrderService.uasset",
    "Grunt_OrderDB": ROOT / "extracted/Sifu/Content/DB/AI/Archetypes/Grunt/Grunt_OrderDB.uasset",
    "BP_Grunt_Base": ROOT / "extracted/Sifu/Content/Blueprints/AI/Grunt/BP_Grunt_Base.uasset",
    "GenericNone": ROOT / "extracted/Sifu/Content/DB/Inputs/Availability/LayerData/GenericNone.uasset",
    "AllDefensiveOptions": ROOT / "extracted/Sifu/Content/DB/Inputs/Availability/LayerData/Guard/AllDefensiveOptions.uasset",
    "DeflectedParryCancelAL": ROOT / "extracted/Sifu/Content/DB/Inputs/Availability/LayerData/DeflectedParryCancelAL.uasset",
}

def refname(pkg, index, seen=None):
    if index == 0:
        return None
    seen = set() if seen is None else set(seen)
    if index in seen:
        return "<cycle>"
    seen.add(index)
    if index < 0:
        if -index > len(pkg["imports"]):
            return "<bad-import>"
        item = pkg["imports"][-index - 1]
        outer = refname(pkg, item["outer"], seen)
    else:
        if index > len(pkg["exports"]):
            return "<bad-export>"
        item = pkg["exports"][index - 1]
        outer = refname(pkg, item["outerIndex"], seen)
    return (outer + "." if outer else "") + item["name"]

def enrich(props, raw, pkg):
    for prop in props:
        val = prop["value"]
        chunk = raw[prop["valueOffset"]:prop["valueOffset"] + prop["size"]]
        if isinstance(val, list):
            enrich(val, chunk, pkg)
        elif prop["type"] == "ObjectProperty" and isinstance(val, int):
            prop["reference"] = refname(pkg, val)
        elif prop["type"] == "ArrayProperty" and len(chunk) >= 4:
            count = struct.unpack_from("<i", chunk)[0]
            if not 0 <= count <= 10000:
                continue
            inner = prop.get("inner")
            if inner == "ObjectProperty" and len(chunk) == 4 + 4 * count:
                prop["arrayValues"] = list(struct.unpack_from("<" + "i" * count, chunk, 4))
                prop["arrayReferences"] = [refname(pkg, v) for v in prop["arrayValues"]]
            elif inner in ("EnumProperty", "NameProperty") and len(chunk) == 4 + 8 * count:
                rr = q.Reader(chunk, pkg["names"], 4)
                prop["arrayValues"] = [rr.name() for _ in range(count)]
            elif inner == "StructProperty":
                try:
                    # UObject's tagged struct-array encoding uses one bounded tagged struct per element.
                    pos, elements = 4, []
                    for _ in range(count):
                        subprops, consumed = q.tags(chunk[pos:], pkg["names"])
                        if consumed <= 0:
                            raise ValueError("empty array element")
                        enrich(subprops, chunk[pos:pos + consumed], pkg)
                        elements.append(subprops)
                        pos += consumed
                    if pos != len(chunk):
                        raise ValueError("array element bounds do not consume payload")
                    prop["arrayElements"] = elements
                except (ValueError, struct.error, UnicodeError) as ex:
                    prop["arrayDecodeError"] = str(ex)

def metadata_for(path):
    # Package parser requires relative paths under the extraction root and reads paired .uexp.
    if ROOT / "extracted" in path.parents:
        base = ROOT / "extracted"
    else:
        base = ROOT / "logs/followup-order-services/extracted"
    meta = q.read_package(path, base)
    uexp = path.with_suffix(".uexp").read_bytes()
    header_size = path.stat().st_size
    parsed = []
    for i, export in enumerate(meta["exports"], 1):
        start = export["serialOffset"] - header_size
        stop = start + export["serialSize"]
        if not 0 <= start <= stop <= len(uexp):
            continue
        raw = uexp[start:stop]
        try:
            props, consumed = q.tags(raw, meta["names"])
            suffix = raw[consumed:]
            if suffix not in (b"", b"\0\0\0\0"):
                continue
            enrich(props, raw, meta)
            parsed.append({"exportIndex": i, "name": export["name"], "class": refname(meta, export["classIndex"]),
                           "serialOffset": export["serialOffset"], "serialSize": export["serialSize"],
                           "propertyBytes": consumed, "tail": suffix.hex(), "properties": props})
        except (ValueError, struct.error, UnicodeError):
            continue
    meta["uexpSha256"] = hashlib.sha256(uexp).hexdigest()
    return meta, parsed

def main():
    results = []
    for label, path in PACKAGES.items():
        if not path.is_file() or not path.with_suffix(".uexp").is_file():
            results.append({"label": label, "path": str(path), "status": "missing"})
            continue
        meta, exports = metadata_for(path)
        results.append({"label": label, "path": meta["path"], "status": "parsed", "uassetSha256": meta["uassetSha256"],
                        "uexpSha256": meta.get("uexpSha256"), "imports": meta["imports"], "exports": exports})

    # The nested service list on OrderAvoided/OrderDeflected is a bounded tagged StructProperty array.
    for package in results:
        if package.get("label") not in ("OrderAvoided", "OrderDeflected"):
            continue
        for export in package.get("exports", []):
            if not export["name"].startswith("Default__"):
                continue
            services = next((p for p in export["properties"] if p["name"] == "m_OrderServices"), None)
            if not services or not isinstance(services["value"], list):
                continue
            service_array = next((p for p in services["value"] if p["name"] == "m_Services"), None)
            if not service_array:
                continue
            # Locate the property's raw bytes from the package's serialized property offsets.
            source_path = ROOT / "logs/followup-order-services/extracted" / package["path"]
            meta = q.read_package(source_path, ROOT / "logs/followup-order-services/extracted")
            e = meta["exports"][export["exportIndex"] - 1]
            blob = source_path.with_suffix(".uexp").read_bytes()
            raw_start = e["serialOffset"] - source_path.stat().st_size
            raw = blob[raw_start:raw_start + e["serialSize"]]
            array_offset = services["valueOffset"] + service_array["valueOffset"]
            arr = raw[array_offset:array_offset + service_array["size"]]
            count = struct.unpack_from("<i", arr)[0]
            # Struct array data is an inner property tag followed by `count` tagged OrderServiceInfos.
            rr = q.Reader(arr, meta["names"], 4)
            inner_name, inner_type = rr.name(), rr.name()
            inner_size, inner_index = rr.number("i"), rr.number("i")
            struct_name = rr.name()
            rr.take(16)  # struct GUID
            has_guid = rr.number("B")
            if has_guid == 1:
                rr.take(16)
            elif has_guid != 0:
                raise ValueError("invalid inner array property GUID flag")
            if inner_name != "m_Services" or inner_type != "StructProperty" or inner_index != 0 or struct_name != "OrderServiceInfos":
                raise ValueError("unexpected order-service array inner tag")
            struct_payload = rr.take(inner_size)
            if rr.position != len(arr):
                raise ValueError("order-service array inner tag bounds")
            pos, parsed_services = 0, []
            for ordinal in range(count):
                props, consumed = q.tags(struct_payload[pos:], meta["names"])
                enrich(props, struct_payload[pos:pos + consumed], meta)
                parsed_services.append({"ordinal": ordinal, "properties": props, "serializedBytes": consumed})
                pos += consumed
            if pos != len(struct_payload):
                raise ValueError("order-service struct elements do not consume payload")
            service_array.pop("arrayDecodeError", None)
            service_array["arrayStruct"] = struct_name
            service_array["arrayElements"] = parsed_services
            service_array["arrayCount"] = count
            service_array["arrayConsumedBytes"] = rr.position
            service_array["arrayDecodeValid"] = rr.position == len(arr)

    out = ROOT / "inventory/followup-order-services-packages.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"packages": len(results), "parsed": sum(x.get("status") == "parsed" for x in results),
                      "missing": [x["label"] for x in results if x.get("status") != "parsed"], "output": str(out)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
