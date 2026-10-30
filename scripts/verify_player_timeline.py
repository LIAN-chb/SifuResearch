"""Check source ranges, conditional coverage and OR interval equivalence.

No browser rendering or runtime gameplay is asserted by this check.
"""
from pathlib import Path
import hashlib
import json
from player_graph_timeline import bound, frame_range, merge_intervals, OPERATIONS

R = Path(__file__).resolve().parents[1]
O = R/'exports/20261029-时间轴精简-15'
read = lambda p: json.loads(p.read_text(encoding='utf-8'))
d = read(O/'board-data.json')
layers = read(R/'exports/20261029-招式时间轴-14/availability-layers.json')
conditions = read(R/'exports/20261029-徒手补全与命名-13/conditional-attacks.json')
checks = []


def check(name, ok):
    checks.append({'name': name, 'passed': bool(ok)})


def contains(row, x):
    lo, hi = row['start'], row['end']
    return (lo['value'] is None or x > lo['value'] or (x == lo['value'] and lo['type'] == 'inclusive')) and (hi['value'] is None or x < hi['value'] or (x == hi['value'] and hi['type'] == 'inclusive'))


attacks = {**d['outsideAttacks'], **d['attacks']}
for asset, a in attacks.items():
    t = a['timeline']
    check(asset+' identity', t['asset'] == asset)
    check(asset+' every hit range including indexed bound keys',
          len(t['hits']) == len(a['windows']) and all(
              {k: h[k] for k in ('start', 'end', 'raw')} == frame_range(w['window']) and h['segment'] == i+1
              for i, (w, h) in enumerate(zip(a['windows'], t['hits']))))
    check(asset+' no invented action end', t['animationEnd'] is None)
    check(asset+' all source windows decoded', not t['unresolved'])
    windows = a['raw'].get('m_AvailabilityLayerWindows[0]', [])
    points = sorted({b['value'] for row in t['permissions'] for b in [row['start'], row['end']] if b['value'] is not None})
    probes = set(points)
    if points:
        probes.update((a+b)/2 for a, b in zip(points, points[1:]))
        probes.update([points[0]-1, points[-1]+1])
    # Compare independent raw layer membership at every cell and exact endpoint.
    equivalent = True
    for action in OPERATIONS:
        masks = {w.get('m_uiHitConditions[0]') for w in windows}
        for mask in masks:
            source = [w for w in windows if w.get('m_uiHitConditions[0]') == mask and
                      ((action in layers['layers'][w['m_Layer[0]']]['listedActions']) != layers['layers'][w['m_Layer[0]']]['invert'])]
            rows = [r for r in t['permissions'] if r['action'] == action and r['hitConditions'] == mask]
            for x in probes:
                if any(contains(frame_range(w), x) for w in source) != any(contains(row, x) for row in rows):
                    equivalent = False
    check(asset+' OR membership equivalent at boundaries and cells', equivalent)
    check(asset+' viewport contains finite evidence', all(t['viewStart'] <= b['value'] <= t['viewEnd'] for row in t['hits']+t['permissions'] for b in [row['start'],row['end']] if b['value'] is not None))
    check(asset+' all merged windows retain source identity', all(
        s['layer'] == windows[s['index']]['m_Layer[0]'] and s['range'] == frame_range(windows[s['index']])
        for row in t['permissions'] for s in row['sources']))

for n in d['nodes'].values():
    expected = next(x['entries'] for x in conditions['nodes'] if x['node'] == n['id'])
    check('node '+str(n['id'])+' every conditional configuration represented',
          n['conditionalVariants'] == [{'tag':e['tag'],'variants':e['variants']} for e in expected])
    check('node '+str(n['id'])+' all displayed variants have independent action model',
          all(v['asset'] in attacks and attacks[v['asset']]['timeline']['asset'] == v['asset']
              for v in n['variants']+[v for e in n['conditionalVariants'] for v in e['variants']]))
    check('node '+str(n['id'])+' successors have existing graph identities', all(
          str(e['target']) in d['graph']['canonicalToDisplay'] for e in n['edges'] if e['target'] is not None))

jab = next(a for p,a in d['attacks'].items() if p.endswith('/MainChar_Jab_FR.uasset'))
check('jab exact hit 22 to 23', [(r['start']['value'],r['end']['value']) for r in jab['timeline']['hits']] == [(22,23)])
check('jab overlapping light union starts 25 and has open end', any(
    r['action']=='AttackLight' and r['start']['value']==25 and r['end']['type']=='open' and len(r['sources'])>=2 for r in jab['timeline']['permissions']))
check('multi-hit and charge represented', any(len(a['timeline']['hits'])>1 for a in attacks.values()) and any(v['tier']!='基础' for n in d['nodes'].values() for v in n['variants']))
check('no guessed inverse map for three unsupported transitions', not any(
    r['transition'] in ('LightGuard','HeavyGuard','DodgeAttack') for a in attacks.values() for r in a['timeline']['permissions']))


def row(start, end, mask=31):
    return {'action':'test','hitConditions':mask,'start':{'value':start,'type':'exclusive'},
            'end':{'value':end,'type':'exclusive'},'sources':[]}


check('exclusive shared point remains a hole', len(merge_intervals([row(0,2),row(2,4)]))==2)
r1,r2=row(0,2),row(2,4);r1['end']['type']='inclusive'
check('included shared point joins intervals', len(merge_intervals([r1,r2]))==1)
check('distinct condition masks never collapse', len(merge_intervals([row(0,3,1),row(1,4,2)]))==2)
check('open bound ignores serialized zero', bound({'Type[0]':'ERangeBoundTypes::Open','Value[0]':0})=={'type':'open','value':None})
try:
    bound({'Type[0]':'ERangeBoundTypes::Inclusive'})
except ValueError:
    check('missing finite bound rejected', True)
else:
    check('missing finite bound rejected', False)

errors = [x['name'] for x in checks if not x['passed']]
report = {'status':'failed' if errors else 'passed','checks':checks,'errors':errors,
          'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'data_sha256':hashlib.sha256((O/'board-data.json').read_bytes()).hexdigest(),
          'not_verified':['browser layout or interactions','runtime action execution','actual action end and elapsed time']}
(O/'timeline-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':report['status'],'checks':len(checks),'errors':errors},ensure_ascii=True))
raise SystemExit(bool(errors))
