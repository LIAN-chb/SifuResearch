# -*- coding: utf-8 -*-
"""生成 moves-table.json：57 个 canonical 节点的招式属性注解。
数据源：02 连招编排器.html 的 DATA（official/attacks）+ combo-graph.json（agg/flags/edges）。
"""
import json, re, io, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
HTML02 = os.path.join(ROOT, 'exports', '20261119-连招编排-02', '连招编排器.html')
GRAPH = os.path.join(ROOT, 'exports', '20261119-连招编排-03', 'combo-graph.json')
OUT = os.path.join(HERE, 'moves-table.json')

TARGET = {'High': '高', 'Mid_1': '中1', 'Mid_2': '中2', 'Low': '低'}

PROP_LABEL = [
    ('Attack.Combo.Entry', '连招起手'),
    ('Attack.Combo.Filler', '连招填充'),
    ('Attack.Combo.Finisher', '连招收尾'),
    ('Attack.HitProperties.Stun', '眩晕型命中'),
    ('Attack.BreakDoors', '可破门/破防'),
    ('Attack.Specific.RushAttack', '奔跑攻击'),
    ('Attack.Specific.BackFrontKD', '后前派生击倒'),
    ('Attack.Specific.SkillFollowKD', '技能追击击倒'),
    ('Attack.Specific.PostPushback', '推击后专用'),
    ('Attack.Specific.EngageGroundPunch', '可攻击倒地'),
    ('Attack.Specific.InvertPosition', '换位'),
    ('Attack.Type.Hit', '普通命中'),
    ('Attack.Speed.Fast', '快'),
    ('Attack.Speed.Normal', '中速'),
    ('Attack.Speed.Slow', '慢'),
]


def load_data_json(path):
    lines = io.open(path, encoding='utf-8').read().split('\n')
    raw = lines[30]  # 行31：const DATA={...};
    s = raw[raw.index('{'):]
    if s.endswith(';'):
        s = s[:-1]
    return json.loads(s)


def main():
    data = load_data_json(HTML02)
    g = json.load(io.open(GRAPH, encoding='utf-8'))
    nodes = {str(k): v for k, v in g['nodes'].items()}
    edges = g['graph']['edges']
    dnodes = {str(n['id']): n for n in data['graph']['nodes']}

    indeg, outdeg = {}, {}
    for e in edges:
        s, t = str(e['s']), str(e['t'])
        outdeg[s] = outdeg.get(s, 0) + 1
        indeg[t] = indeg.get(t, 0) + 1

    # 同一 rawName 视为同一招式（不同上下文节点）
    by_raw = {}
    for i, n in nodes.items():
        by_raw.setdefault(n.get('rawName') or n.get('name'), []).append(i)

    # 官方名：展示节点合并后 official 列表会混入相邻招式，按名字精确回填
    all_offs = []
    for dn in dnodes.values():
        for o in (dn.get('official') or []):
            all_offs.append(o)
    def off_names_for(nm):
        res, seen = [], set()
        for o in all_offs:
            on = o.get('name') or ''
            if on and (on == nm or on.startswith(nm + '·') or nm.startswith(on)):
                k = (on, o.get('en'))
                if k in seen:
                    continue
                seen.add(k)
                res.append({'name': on, 'en': o.get('en'), 'scope': o.get('scope'),
                            'key': o.get('key'), 'namespace': o.get('namespace')})
        return res

    out = {}
    for i, n in sorted(nodes.items(), key=lambda kv: int(kv[0])):
        agg = n.get('agg') or {}
        dn = dnodes.get(i) or {}
        offs = off_names_for(n.get('name') or '')
        if not offs and dn.get('official'):
            # 展示节点的主 canonical 且名字与展示标签一致时才沿用
            if str((data['graph'].get('canonicalToDisplay') or {}).get(i, i)) == i:
                offs = [{'name': dn['official'][0].get('name'), 'en': dn['official'][0].get('en'),
                         'scope': dn['official'][0].get('scope'), 'key': dn['official'][0].get('key'),
                         'namespace': dn['official'][0].get('namespace')}]
        props = []
        for p in (n.get('props') or []):
            lab = dict(PROP_LABEL).get(p)
            if lab:
                props.append(lab)
        tgt = [TARGET.get(str(t).split('::')[-1], str(t).split('::')[-1]) for t in (agg.get('targets') or [])]
        fr = agg.get('frame') or [None, None]
        entry_inputs = [e.get('inp') for e in edges if str(e['s']) == i and e.get('grade') == 'config']
        state_inputs = [{'inp': e.get('inp'), 'from': str(e['s']), 'gap': e.get('gap'),
                         'tier': e.get('tier'), 'note': e.get('note')}
                        for e in edges if str(e['t']) == i and e.get('grade') == 'state']
        out[i] = {
            'id': int(i),
            'name': n.get('name'),
            'raw': n.get('rawName'),
            'aliases': [x for x in by_raw.get(n.get('rawName') or n.get('name'), []) if x != i],
            'display': dn.get('canonical') if dn else None,
            'isAlias': bool(n.get('name') is None),
            'stats': {'hits': agg.get('hits'), 'dmg': agg.get('dmg'), 'struct': agg.get('struct'),
                      'sdiz': agg.get('sdiz'), 'stun': agg.get('stun'), 'kb': agg.get('kb'),
                      'freeze': agg.get('freeze'), 'frame': fr},
            'targets': tgt,
            'flags': {k: bool(n.get(k)) for k in ('kd', 'ground', 'push', 'pursuit', 'finisher', 'need_enemy_attack')},
            'props': props,
            'official': offs,
            'indeg': indeg.get(i, 0),
            'outdeg': outdeg.get(i, 0),
            'configInputs': sorted(set(x for x in entry_inputs if x)),
            'stateEntryFrom': state_inputs,
        }
    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
    print('wrote', OUT, 'nodes', len(out))


if __name__ == '__main__':
    main()
