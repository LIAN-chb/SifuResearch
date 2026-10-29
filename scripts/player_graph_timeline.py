"""Evidence-backed animation coordinates and attack-order permissions.

This model deliberately does not claim complete runtime cancel availability.
"""
from copy import deepcopy
import math

OPERATIONS = {
    'AttackLight': ('轻击', 'Light'), 'AttackHeavy': ('重击', 'Heavy'),
    'AttackLightAlt': ('轻击·变体分支', 'LightAlt'),
    'AttackHeavyAlt': ('重击·变体分支', 'HeavyAlt'),
    'AttackLightHold': ('长按轻击', 'LightHold'),
    'AttackHeavyHold': ('蓄力重击', 'HeavyHold'),
    'AttackLightFrontFront': ('前前轻击', 'LightFrontFront'),
    'AttackHeavyFrontFront': ('前前重击', 'HeavyFrontFront'),
    'AttackLightBackFront': ('后前轻击', 'LightBackFront'),
    'AttackHeavyBackFront': ('后前重击', 'HeavyBackFront'),
    'AttackLightGuard': ('防御轻击', None),
    'AttackHeavyGuard': ('防御重击', None),
    'AttackLightFront': ('前轻击', 'LightFront'),
    'AttackHeavyFront': ('前重击', 'HeavyFront'),
    'AttackKnockdown': ('倒地攻击', 'AttackKnockdown'),
    'AttackKnockdownHold': ('长按倒地攻击', 'AttackKnockdownHold'),
    'AttackGrab': ('抓取', 'Grab'),
    'LightRushAttack': ('奔跑轻击', 'LightRushAttack'),
    'HeavyRushAttack': ('奔跑重击', 'HeavyRushAttack'),
    'Disengage': ('拉开距离', 'Disengage'),
    'Dodge': ('闪避', None), 'Avoid': ('原地闪避', None),
    'Guard': ('防御', None), 'Parry': ('招架', None),
    'MoveInterrupt': ('移动打断', None), 'Rush': ('奔跑', None),
    'GuardInterrupt': ('防御打断', None),
    'GuardInterruptNoParry': ('防御打断·不招架', None),
}


def bound(raw):
    kind = raw.get('Type[0]')
    if kind == 'ERangeBoundTypes::Open':
        return {'value': None, 'type': 'open'}
    value = raw.get('Value[0]')
    if kind not in ('ERangeBoundTypes::Inclusive', 'ERangeBoundTypes::Exclusive') or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'Unresolved range bound: {raw}')
    return {'value': value, 'type': kind.split('::')[-1].lower()}


def frame_range(window):
    frame = window.get('m_FrameRange[0]', {})
    anim = frame.get('m_Anim[0]')
    if not anim:
        return None
    return {'start': bound(anim['LowerBound[0]']), 'end': bound(anim['UpperBound[0]']),
            'raw': deepcopy(frame)}


def merge_intervals(rows):
    """Union only identical guards; retain all layer/window provenance."""
    groups = {}
    for row in rows:
        key = (row['action'], row['hitConditions'])
        groups.setdefault(key, []).append(deepcopy(row))
    result = []
    for group in groups.values():
        group.sort(key=lambda r: -math.inf if r['start']['value'] is None else r['start']['value'])
        merged = []
        for row in group:
            if not merged:
                merged.append(row)
                continue
            prev = merged[-1]
            end, start = prev['end']['value'], row['start']['value']
            overlaps = end is None or start is None or start < end or (start == end and (prev['end']['type'] == 'inclusive' or row['start']['type'] == 'inclusive'))
            if not overlaps:
                merged.append(row)
                continue
            prev['sources'].extend(row['sources'])
            if end is not None and (row['end']['value'] is None or row['end']['value'] > end):
                prev['end'] = row['end']
            elif end == row['end']['value'] and row['end']['type'] == 'inclusive':
                prev['end'] = row['end']
            if start == prev['start']['value'] and row['start']['type'] == 'inclusive':
                prev['start'] = row['start']
        result.extend(merged)
    return result


def enrich(data, layers, timings, conditions):
    transition_map = {x['input']: x['transition'] for x in layers['inputTransitionMapping'] if x['inverse_matches']}
    attacks = {**data['outsideAttacks'], **data['attacks']}
    for asset, a in attacks.items():
        timing = timings['attacks'][asset]
        hits = []
        for i, w in enumerate(a['windows']):
            r = frame_range(w['window'])
            if r:
                hits.append({**r, 'segment': i + 1, 'table': w['table'], 'row': w['row'],
                             'activationCondition': w['window'].get('m_activationCondition[0]'),
                             'specialAction': w.get('action')})
        permissions, unresolved = [], []
        for i, w in enumerate(a['raw'].get('m_AvailabilityLayerWindows[0]', [])):
            r, ref = frame_range(w), w.get('m_Layer[0]')
            layer = layers['layers'].get(ref)
            if not r or not layer:
                unresolved.append({'index': i, 'raw': w, 'reason': '未接通动画帧范围或许可层'})
                continue
            for action, (label, transition) in OPERATIONS.items():
                included = action in layer['listedActions']
                if included == layer['invert']:
                    continue
                permissions.append({**r, 'action': action, 'label': label, 'transition': transition_map.get(action),
                    'hitConditions': w.get('m_uiHitConditions[0]'),
                    'sources': [{'index': i, 'layer': ref, 'asset': layer['asset'], 'range': deepcopy(r)}]})
        permissions = merge_intervals(permissions)
        finite = [b['value'] for r in hits + permissions for b in (r['start'], r['end']) if b['value'] is not None]
        markers = []
        for key, label in [('lastBuildupFrame', '动画前摇末标记'), ('hitMarkerFrame', '动画命中标记')]:
            if isinstance(timing.get(key), (int, float)):
                markers.append({'frame': timing[key], 'label': label})
                finite.append(timing[key])
        extent = max(finite, default=0)
        # Padding is exclusively a viewport margin, never an inferred animation end.
        view_end = max(1, extent * 1.08)
        a['timeline'] = {'asset': asset, 'coordinate': 'animation-frames', 'timing': timing,
            'hits': hits, 'permissions': permissions, 'unresolved': unresolved, 'markers': markers,
            'viewStart': min([0] + finite), 'viewEnd': view_end,
            'animationEnd': timing.get('animationEndFrame'), 'stage': 'static-attack-order-permission',
            'rule': '攻击窗口进入时OR叠加，退出时移除各自句柄；当前轴只展示攻击订单提供的许可。',
            'missing': '当前轨道为静态许可；输入选择、运行时上下文、移动及Ability启动/打断条件仍限制实际执行。',
            'evidence': ['notes/player-timeline-14-availability.md', 'notes/player-timeline-14-timing.md']}
    by_node = {x['node']: x['entries'] for x in conditions['nodes']}
    for key, node in data['nodes'].items():
        node['conditionalVariants'] = [
            {'tag': entry['tag'], 'variants': deepcopy(entry['variants'])}
            for entry in by_node.get(int(key), [])]
    data['timelineResearch'] = {'version': 1, 'operation': layers['attackWindowOperation'],
        'selectionRule': '同组候选先经过玩家当前许可过滤，再按攻击Ability输入优先表选取并检查目标；普通与变体同时有效且无更高优先候选时，变体先于对应普通。后继还经节点有效性、条件及回退选择。',
        'missing': '尚缺完整Ability激活/打断守卫、部分输入条件蓝图、实际context栈、特殊移动掩码和节点fallback内部；因此没有标最终有效取消。',
        'notes': ['notes/player-timeline-14-availability.md', 'notes/player-timeline-14-timing.md'],
        'browserValidation': '未完成：浏览器安全策略拒绝本地file协议并禁止绕过',
        'runtimeValidation': '未进行游戏实测'}
