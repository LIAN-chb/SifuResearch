"""Report rule-layer wording: each prohibition needs a default action or a checked boundary."""
import datetime
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / 'inventory/rule-style-verification.json'

# Full rule-layer scope; retrospectives is reported as backlog.
ENFORCED = [
    'AGENTS.md',
    'PROJECT.md',
    'notes/research-workflow.md',
    'notes/rule-maintenance.md',
    'notes/workspace-layout.md',
    'notes/mechanism-writing.md',
    'notes/capability-discovery.md',
    'notes/version-control.md',
    'notes/tool-capabilities.md',
    'notes/handoffs/README.md',
    'adr/README.md',
]
ADVISORY = [
    'notes/retrospectives/README.md',
]

PROHIBITION = re.compile(
    '禁止|严禁|不得|不要|不能|不可|不应|避免|勿|永不|'
    '不出现|不混入|不覆盖|不改|不写|不凭|不机械|不直接|不把|不另|'
    '不重复|不虚构|不用|不要求|不预设|不宣称'
)
ANCHOR = re.compile(
    '默认|改为|应先|须|必须|优先|只写|只暂存|只作|记录|核对|备份|检查|'
    '输出|写入|询问|标为|合并|删除|运行|使用|保留|转为|停止|复制|列出|写明|写清'
)
MAX_RATIO = 0.2
MIN_DUPLICATE_LEN = 12


def units(text):
    """Split markdown into rule-sized units: table rows, bullets, or paragraphs."""
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    out = []
    for block in re.split(r'\n\s*\n', text):
        lines = [line.rstrip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        if all(line.lstrip().startswith('|') for line in lines):
            for line in lines:
                if not re.fullmatch(r'\|[\s:|-]+\|', line.strip()):
                    out.append(line.strip())
        elif all(line.lstrip().startswith(('#', '-', '*')) or re.match(r'\s*\d+\.', line) for line in lines):
            current = []
            for line in lines:
                if line.lstrip().startswith(('#', '-', '*')) or re.match(r'\s*\d+\.', line):
                    if current:
                        out.append(' '.join(current).strip())
                    current = [line.strip()]
                else:
                    current.append(line.strip())
            if current:
                out.append(' '.join(current).strip())
        else:
            out.append(' '.join(line.strip() for line in lines).strip())
    return [u for u in out if not u.startswith('#')]


def normalize(unit):
    return re.sub(r'\s+', '', re.sub(r'^[\|\-\*\d.、\s]+', '', unit))


def scan(path):
    text = (ROOT / path).read_text(encoding='utf-8-sig')
    found = []
    duplicated_units = []
    all_units = units(text)
    for unit in all_units:
        # "能不能" asks about possibility and is not a prohibition.
        probe = unit.replace('能不能', '能否')
        if PROHIBITION.search(probe) and not ANCHOR.search(probe):
            found.append(unit)
        if PROHIBITION.search(probe):
            duplicated_units.append(normalize(unit))
    prohibited = len(duplicated_units)
    ratio = prohibited / len(all_units) if all_units else 0.0
    return {
        'path': path,
        'units': len(all_units),
        'prohibited_units': prohibited,
        'ratio': round(ratio, 4),
        'unpaired': found,
        'prohibited_texts': duplicated_units,
    }


def main():
    results = []
    for path in ENFORCED + ADVISORY:
        scope = 'enforced' if path in ENFORCED else 'advisory'
        item = scan(path)
        item['scope'] = scope
        results.append(item)

    duplicates = []
    seen = {}
    for item in results:
        for norm in item['prohibited_texts']:
            if len(norm) < MIN_DUPLICATE_LEN:
                continue
            seen.setdefault(norm, []).append(item['path'])
    for norm, paths in seen.items():
        if len(paths) > 1:
            duplicates.append({'text': norm, 'files': sorted(set(paths))})

    errors = []
    for item in results:
        if item['scope'] != 'enforced':
            continue
        if item['ratio'] > MAX_RATIO:
            errors.append(f"{item['path']}: prohibited ratio {item['ratio']:.0%} exceeds {MAX_RATIO:.0%}")
        for unit in item['unpaired']:
            errors.append(f"{item['path']}: prohibition without default action: {unit}")

    report = {
        'checked_at': datetime.datetime.now().astimezone().isoformat(),
        'status': 'passed' if not errors else 'failed',
        'rule': 'Each prohibition states a default action or a checked hard boundary.',
        'thresholds': {'max_prohibited_ratio': MAX_RATIO, 'min_duplicate_len': MIN_DUPLICATE_LEN},
        'enforced_scope': ENFORCED,
        'advisory_scope': ADVISORY,
        'files': results,
        'duplicates_across_files': duplicates,
        'errors': errors,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"{report['status']}: {len(errors)} issue(s); report={REPORT}")
    for item in results:
        flag = 'ENFORCED' if item['scope'] == 'enforced' else 'backlog'
        print(f"  [{flag}] {item['path']}: {item['prohibited_units']}/{item['units']} units "
              f"({item['ratio']:.0%}), unpaired={len(item['unpaired'])}")
    return 0 if not errors else 1


if __name__ == '__main__':
    raise SystemExit(main())
