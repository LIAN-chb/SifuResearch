"""扫描批次交接中的“规则信号”，按类型与标签聚合，输出规则候选。

只读 notes/handoffs/*.md，只写 inventory/rule-signals.json；不改任何规则文件，
不自动生成 ADR。没有“规则信号”节的批次按未记录处理，不回填。
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HANDOFFS = ROOT / "notes" / "handoffs"
OUT = ROOT / "inventory" / "rule-signals.json"

TYPES = ("重复要求", "agent偏差", "未覆盖情形")
SKIP_FILES = {"README.md", "TEMPLATE.md"}
SECTION = "## 规则信号"
THRESHOLD = 2


def read_section(text: str) -> list[str]:
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.strip() == SECTION:
            start = index + 1
            break
    if start is None:
        return []
    body: list[str] = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        body.append(line)
    return body


def parse_line(line: str, source: str) -> dict | None:
    raw = line.strip()
    if not raw.startswith("- "):
        return None
    content = raw[2:].strip()
    if not content or content.startswith("<") or "本批无" in content:
        return None
    parts = [part.strip() for part in content.split("｜")]
    head = parts[0]
    signal_type = None
    time_text = ""
    for candidate in TYPES:
        if candidate in head:
            signal_type = candidate
            time_text = head.replace(candidate, "").strip()
            break
    if signal_type is None:
        return None
    tag = ""
    detail_parts = []
    for part in parts[1:]:
        if part.startswith("标签="):
            tag = part[len("标签="):].strip()
        elif part.startswith(("摘句=", "描述=", "位置=")):
            detail_parts.append(part)
    return {
        "source": source,
        "time": time_text,
        "type": signal_type,
        "tag": tag or "未标注",
        "detail": "；".join(detail_parts),
    }


def main() -> int:
    signals: list[dict] = []
    scanned = 0
    with_signals = 0

    if HANDOFFS.is_dir():
        for path in sorted(HANDOFFS.glob("*.md")):
            if path.name in SKIP_FILES:
                continue
            scanned += 1
            try:
                text = path.read_text(encoding="utf-8")
            except OSError as exc:
                print(f"skip {path.name}: {exc}")
                continue
            body = read_section(text)
            if not body:
                continue
            found = [item for item in (parse_line(line, path.name) for line in body) if item]
            if found:
                with_signals += 1
                signals.extend(found)

    groups: dict[tuple[str, str], list[dict]] = {}
    for signal in signals:
        groups.setdefault((signal["type"], signal["tag"]), []).append(signal)

    candidates = []
    for (signal_type, tag), items in groups.items():
        if len(items) < THRESHOLD:
            continue
        per_batch: dict[str, int] = {}
        for item in items:
            per_batch[item["source"]] = per_batch.get(item["source"], 0) + 1
        candidates.append({
            "type": signal_type,
            "tag": tag,
            "count": len(items),
            "batches": sorted(per_batch),
            "same_batch": any(count >= THRESHOLD for count in per_batch.values()),
            "priority": "immediate" if any(count >= THRESHOLD for count in per_batch.values()) else "normal",
            "items": items,
        })
    candidates.sort(key=lambda item: (-item["count"], item["type"], item["tag"]))

    report = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "scanned_batches": scanned,
        "batches_with_signals": with_signals,
        "signals": signals,
        "candidates": candidates,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"scanned={scanned} with_signals={with_signals} signals={len(signals)} candidates={len(candidates)}")
    for item in candidates:
        print(f"  [{item['priority']}] {item['type']}／{item['tag']}: {item['count']} 次 · {', '.join(item['batches'])}")
    print(f"report={OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
