"""Bounded LocRes v1-v3 reader. Layout cross-checked against CUE4Parse primary code."""
from pathlib import Path
import struct,json,hashlib,collections,sys
O=Path(__file__).resolve().parent
SOURCES=['https://raw.githubusercontent.com/FabianFG/CUE4Parse/master/CUE4Parse/UE4/Localization/FTextLocalizationResource.cs','https://raw.githubusercontent.com/FabianFG/CUE4Parse/master/CUE4Parse/UE4/Objects/Core/i18N/FTextKey.cs']
class Reader:
 def __init__(self,p):self.data=p.read_bytes();self.at=0
 def take(self,n):
  assert n>=0 and self.at+n<=len(self.data),(self.at,n)
  b=self.data[self.at:self.at+n];self.at+=n;return b
 def integer(self,fmt):return struct.unpack('<'+fmt,self.take(struct.calcsize('<'+fmt)))[0]
 def text(self):
  n=self.integer('i');assert abs(n)<1000000
  if not n:return ''
  b=self.take(abs(n)*(2 if n<0 else 1));assert b.endswith(b'\0\0' if n<0 else b'\0')
  return b[:-2].decode('utf-16-le') if n<0 else b[:-1].decode('utf-8')
def parse(p):
 r=Reader(p);assert r.take(16)==struct.pack('<4I',0x7574140e,0xfc034a67,0x9d90154a,0x1b7f37c3)
 v=r.integer('B');assert v in [1,2,3]
 pool_offset=r.integer('q');assert 25<=pool_offset<len(r.data)
 entries_start=r.at;r.at=pool_offset;pool=[]
 for _ in range(r.integer('i')):
  text=r.text();refs=r.integer('i') if v>=2 else None;pool.append({'text':text,'refs':refs})
 assert r.at==len(r.data),'unparsed bytes after pool'
 r.at=entries_start;total=r.integer('I') if v>=2 else None;rows=[]
 def key():
  h=r.integer('I') if v>=2 else None
  return r.text(),h
 for _ in range(r.integer('I')):
  ns,nh=key()
  for _ in range(r.integer('I')):
   offset=r.at;k,kh=key();source_hash=r.integer('I');idx=r.integer('i');assert 0<=idx<len(pool)
   rows.append({'namespace':ns,'key':k,'source_hash':source_hash,'text':pool[idx]['text'],'entry_offset':offset,'pool_index':idx})
 assert r.at==pool_offset,('entry table not consumed',r.at,pool_offset)
 assert total is None or total==len(rows)
 assert len({(x['namespace'],x['key']) for x in rows})==len(rows)
 return rows,{'version':v,'entries':len(rows),'pool_strings':len(pool),'bytes':len(r.data),'sha256':hashlib.sha256(r.data).hexdigest(),'tables_fully_consumed':True}
records={};meta={}
for lang in ['en','zh-Hans']:
 rows,report=parse(O/'extracted/Sifu/Content/Localization/Game'/lang/'Game.locres');records[lang]=rows;meta[lang]=report
 (O/(lang+'.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
en={(r['namespace'],r['key']):r for r in records['en']};zh={(r['namespace'],r['key']):r for r in records['zh-Hans']}
pairs=[]
for key,e in en.items():
 if key not in zh:continue
 z=zh[key]
 if e['source_hash']!=z['source_hash']:continue
 pairs.append({'namespace':key[0],'key':key[1],'en':e['text'],'zh-Hans':z['text'],'source_hash':e['source_hash'],'en_entry_offset':e['entry_offset'],'zh_entry_offset':z['entry_offset']})
(O/'paired-texts.json').write_text(json.dumps(pairs,ensure_ascii=False,indent=2),encoding='utf-8')
(O/'localization-verification.json').write_text(json.dumps({'status':'passed','locales':meta,'paired_entries':len(pairs),'paired_only_when_key_and_source_hash_match':True,'en_only':[list(k) for k in sorted(set(en)-set(zh))],'zh_only':[list(k) for k in sorted(set(zh)-set(en))],'source_hash_mismatches':[list(k) for k in sorted(set(en)&set(zh)) if en[k]['source_hash']!=zh[k]['source_hash']],'reader_sources':SOURCES,'python':sys.version,'reader_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(meta));print(collections.Counter(r['namespace'] for r in pairs));
for r in pairs:
 if any(t in (r['en']+' '+r['zh-Hans']).lower() for t in ['chasing','追亡','palm strike','snap kick','flowing claw','charged backfist']):print(json.dumps(r,ensure_ascii=True))
