import io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = os.path.join(ROOT, 'exports', '20261119-连招编排-02', '连招编排器.html')
dst = os.path.join(ROOT, 'exports', '20261119-连招编排-03', '连招编排器.html')
js_path = os.path.join(HERE, 'overlay-v3.js')
full_path = os.path.join(ROOT, 'exports', '20261119-连招编排-02', 'combo-graph.json')

html = io.open(src, encoding='utf-8').read()
lines = html.split('\n')
print('src lines:', len(lines), 'bytes:', len(html.encode('utf-8')))

assert lines[330].strip() == '<script>', repr(lines[330][:60])
assert lines[566].strip() == '</script>', repr(lines[566][:60])
assert lines[567].strip() == '</html>', repr(lines[567][:60])

js = io.open(js_path, encoding='utf-8').read()
assert '(function () {' in js
assert js.strip().endswith('})();')

patch_path = os.path.join(HERE, 'overlay-v32-patch.js')
if os.path.exists(patch_path):
    patch = io.open(patch_path, encoding='utf-8').read()
    idx = js.rstrip().rfind('init();')
    assert idx > 0, 'init() call not found'
    js = js[:idx] + patch + '\n  init();\n})();\n'
    print('patch merged before init():', len(patch), 'chars')

full = json.load(io.open(full_path, encoding='utf-8'))
payload = {
    'nodes': full.get('nodes') or {},
    'edges': (full.get('graph') or {}).get('edges') or [],
    'enemies': full.get('enemies') or [],
    'entries': full.get('entries') or {},
    'goals': full.get('goals') or [],
}
qfull = 'window.QFULL=' + json.dumps(payload, ensure_ascii=False, separators=(',', ':')) + ';'
print('full graph:', len(payload['nodes']), 'nodes', len(payload['edges']), 'edges', len(qfull), 'bytes')

moves_path = os.path.join(HERE, 'moves-table.json')
assert os.path.exists(moves_path), 'missing build/moves-table.json: run build/make_moves_table.py first'
moves = json.load(io.open(moves_path, encoding='utf-8'))
qmoves = 'window.QMOVES=' + json.dumps(moves, ensure_ascii=False, separators=(',', ':')) + ';'
print('moves table:', len(moves), 'nodes', len(qmoves), 'bytes')

head = lines[:330]
tail = lines[567:]
out = head + ['<script>', qfull, '</script>', '<script>', qmoves, '</script>', '<script>', js.rstrip('\n'), '</script>'] + tail
io.open(dst, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('dst written:', dst, os.path.getsize(dst), 'bytes')

io.open(os.path.join(HERE, 'overlay-check.js'), 'w', encoding='utf-8', newline='\n').write(js)
print('check file written -> build/overlay-check.js')
