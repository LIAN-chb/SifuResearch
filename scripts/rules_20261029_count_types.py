"""Read-only CodeView TPI layout reader for selected Sifu combat types.

Consumes index_pdb.Msf and reads only the exact Epic Sifu PDB selected by
index_pdb.py. Produces no executables, extraction files, or game modifications.
CodeView record definitions: https://llvm.org/docs/PDB/CodeViewTypes.html
"""
import sys, json, re, struct
from pathlib import Path
sys.dont_write_bytecode = True
ROOT = Path(r'E:\ProgrameFiles\SifuResearch')
sys.path.insert(0, str(ROOT / 'scripts'))
from index_pdb import Msf, PDB

TARGET_NAMES = {'AFightingCharacter','UCharacterHealthComponent','UHealthComponent','UHitComponent','UDefenseComponent','FFightingStateElement','FHitDescription','FHitRequest','FAttackRequest','FDamageInfos'}
RELEVANT = re.compile(r'^(AFightingCharacter|UCharacterHealthComponent|UHealthComponent|UHitComponent|UDefenseComponent|FFightingStateElement|FHitDescription|FHitRequest|FAttackRequest|FDamageInfos)$')
SKIP_GENERIC = ('TIs', 'TCall', 'TEnum', 'TArray<', 'TSet<', 'TMap<', 'TBase', 'TShared', 'TUnique', 'TDefault', 'BaseKey', 'TPair', 'TFunction', 'TMulticast', 'TWeak', 'TCpp', 'UE4Is', 'TPromise', 'TRefCount', 'FArchive', 'FProperty', 'Z_Construct', 'UScriptStruct::', 'TStructOps', 'UE4Tuple_Private', 'std::')

LF_CLASS, LF_STRUCTURE, LF_UNION, LF_ENUM = 0x1504, 0x1505, 0x1506, 0x1507
LF_FIELDLIST, LF_MODIFIER, LF_POINTER, LF_ARRAY, LF_BITFIELD, LF_ALIAS = 0x1203, 0x1001, 0x1002, 0x1503, 0x1205, 0x150a
LF_MEMBER, LF_STMEMBER, LF_ENUMERATE = 0x150d, 0x150e, 0x1502
LF_BCLASS, LF_INDEX, LF_VFUNCTAB, LF_NESTTYPE = 0x1400, 0x1404, 0x1409, 0x1510


def cstr(buf, p):
    e = buf.find(b'\0', p)
    return buf[p:e].decode('utf-8', 'replace') if e >= 0 else ''


def cvnum(buf, p):
    leaf = struct.unpack_from('<H', buf, p)[0]
    if leaf < 0x8000:
        return p + 2, leaf
    fmts = {0x8000: '<b', 0x8001: '<h', 0x8002: '<H', 0x8003: '<i', 0x8004: '<I', 0x8009: '<d', 0x800a: '<Q'}
    fmt = fmts.get(leaf)
    if fmt:
        return p + 2 + struct.calcsize(fmt), struct.unpack_from(fmt, buf, p + 2)[0]
    if leaf in (0x8005, 0x8006):
        return p + 10, int.from_bytes(buf[p+2:p+10], 'little', signed=(leaf == 0x8005))
    if leaf in (0x8007, 0x8008):
        return p + 14, int.from_bytes(buf[p+2:p+14], 'little', signed=(leaf == 0x8007))
    if leaf == 0x800b: return p + 18, buf[p+2:p+18].hex()
    return p + 2, {'unsupported_numeric_leaf': hex(leaf)}


def simple_name(ti):
    base = ti & 0xff
    names = {0x00:'<no-type>',0x03:'void',0x08:'HRESULT',0x10:'char',0x20:'unsigned char',0x11:'short',0x21:'unsigned short',0x12:'int',0x22:'unsigned int',0x13:'int64',0x23:'uint64',0x30:'bool8',0x31:'bool16',0x32:'bool32',0x40:'float',0x41:'double'}
    n = names.get(base, f'cv_simple_{base:02x}')
    ptr = (ti >> 8) & 0xf
    return n + ('*' if ptr else '')


def main():
    msf = Msf(PDB)
    raw = msf.stream(2)
    hdr_size, first, end, rec_bytes = struct.unpack_from('<4I', raw, 4)
    pos, idx = hdr_size, first
    records, type_names, type_kinds, type_sizes, array_meta = {}, {}, {}, {}, {}
    udts_by_name = {}
    while pos + 4 <= len(raw) and idx < end:
        length, kind = struct.unpack_from('<HH', raw, pos)
        rec = raw[pos+4:pos+length+2]
        records[idx] = (kind, rec)
        type_kinds[idx] = kind
        if kind in (LF_CLASS, LF_STRUCTURE) and len(rec) >= 18:
            name = cstr(rec, cvnum(rec, 16)[0])
            size_pos, size = cvnum(rec, 16)
            fieldlist = struct.unpack_from('<I', rec, 4)[0]
            udt = {'type_index':hex(idx),'leaf':hex(kind),'name':name,'size_bytes':size,'field_list_index':hex(fieldlist),'declared_member_count':struct.unpack_from('<H',rec,0)[0],'properties':hex(struct.unpack_from('<H',rec,2)[0]),'record_bytes':len(rec)}
            type_names[idx] = name
            type_sizes[idx] = size if isinstance(size,int) else None
            if name: udts_by_name.setdefault(name, []).append(udt)
        elif kind == LF_UNION and len(rec) >= 10:
            size_pos, size = cvnum(rec, 8)
            fieldlist = struct.unpack_from('<I', rec, 4)[0]
            name = cstr(rec, size_pos)
            udt = {'type_index':hex(idx),'leaf':hex(kind),'name':name,'size_bytes':size,'field_list_index':hex(fieldlist),'declared_member_count':struct.unpack_from('<H',rec,0)[0],'properties':hex(struct.unpack_from('<H',rec,2)[0]),'record_bytes':len(rec)}
            type_names[idx] = name
            type_sizes[idx] = size if isinstance(size,int) else None
            if name: udts_by_name.setdefault(name, []).append(udt)
        elif kind == LF_ENUM and len(rec) >= 12:
            fieldlist = struct.unpack_from('<I',rec,4)[0]
            name = cstr(rec,12)
            udt = {'type_index':hex(idx),'leaf':hex(kind),'name':name,'size_bytes':None,'underlying_type_index':hex(struct.unpack_from('<I',rec,4)[0]),'field_list_index':hex(fieldlist),'declared_member_count':struct.unpack_from('<H',rec,0)[0],'properties':hex(struct.unpack_from('<H',rec,2)[0]),'record_bytes':len(rec)}
            # Enum layout: count, props, underlying type, field list, name.
            udt['underlying_type_index'] = hex(struct.unpack_from('<I',rec,4)[0])
            udt['field_list_index'] = hex(struct.unpack_from('<I',rec,8)[0])
            udt['underlying_type_index'] = hex(struct.unpack_from('<I',rec,4)[0])
            udt['field_list_index'] = hex(struct.unpack_from('<I',rec,8)[0])
            type_names[idx] = name
            type_sizes[idx] = None
            if name: udts_by_name.setdefault(name, []).append(udt)
        elif kind == LF_ALIAS and len(rec) >= 5:
            name = cstr(rec,4)
            type_names[idx] = name
        elif kind == LF_MODIFIER and len(rec) >= 6:
            underlying = struct.unpack_from('<I',rec,0)[0]
            type_names[idx] = f'{hex(underlying)} (cv modifier {hex(struct.unpack_from("<H",rec,4)[0])})'
        elif kind == LF_POINTER and len(rec) >= 8:
            underlying, attrs = struct.unpack_from('<II',rec,0)
            type_names[idx] = f'{type_names.get(underlying, simple_name(underlying))}* [attrs={hex(attrs)}]'
        elif kind == LF_ARRAY and len(rec) >= 10:
            elem, _ = struct.unpack_from('<II',rec,0); npos, nval = cvnum(rec,8)
            type_names[idx] = f'{type_names.get(elem, simple_name(elem))}[{nval}B]'
            array_meta[idx] = (elem, nval)
            type_sizes[idx] = nval
        pos += length + 2
        idx += 1
    # Prefer full definitions with actual nonzero size; forward refs are typically size 0.
    chosen = {}
    for name, variants in udts_by_name.items():
        full = [x for x in variants if x['size_bytes'] not in (0,None)]
        chosen[name] = max(full or variants, key=lambda x:(x['size_bytes'] or 0, int(x['type_index'],16)))

    # Resolve forward declarations to complete same-name UDTs for sizeof(array element).
    for ti, name in type_names.items():
        if name in chosen and chosen[name].get('size_bytes'):
            type_sizes[ti] = chosen[name]['size_bytes']
    def type_desc(ti):
        if ti < first:
            return {'type_index':hex(ti),'name':simple_name(ti),'leaf':None}
        kind, rec = records.get(ti,(None,b''))
        if kind == 0x1009 and len(rec)>=24:
            return {'type_index':hex(ti),'name':'member-function','leaf':hex(kind),'return_type':type_desc(struct.unpack_from('<I',rec)[0]),'param_count':struct.unpack_from('<H',rec,14)[0]}
        name = type_names.get(ti)
        if kind == LF_POINTER and len(rec)>=8:
            underlying, attrs = struct.unpack_from('<II',rec,0)
            return {'type_index':hex(ti),'name':type_names.get(ti,f'{type_desc(underlying)["name"]}*'),'leaf':hex(kind),'underlying_type':type_desc(underlying),'attrs':hex(attrs)}
        if kind == LF_MODIFIER and len(rec)>=6:
            underlying, attr=struct.unpack_from('<IH',rec,0)
            return {'type_index':hex(ti),'name':type_names.get(ti,'modifier'),'leaf':hex(kind),'underlying_type':type_desc(underlying),'attrs':hex(attr)}
        if kind == LF_BITFIELD and len(rec)>=6:
            under, bits, shift=struct.unpack_from('<IBB',rec,0)
            return {'type_index':hex(ti),'name':f'{type_desc(under)["name"]}:{bits}','leaf':hex(kind),'underlying_type':type_desc(under),'bit_length':bits,'bit_position':shift}
        if kind == LF_ARRAY and len(rec)>=10:
            elem, _ = struct.unpack_from('<II',rec,0); _, byte_length = cvnum(rec,8)
            elem_size = type_sizes.get(elem)
            if elem < first:
                elem_size = {0x10:1,0x20:1,0x11:2,0x21:2,0x12:4,0x22:4,0x13:8,0x23:8,0x30:1,0x31:2,0x32:4,0x40:4,0x41:8,0x74:4,0x75:4,0x72:2,0x73:2}.get(elem & 0xff, elem_size)
            count = byte_length // elem_size if isinstance(byte_length,int) and elem_size and byte_length % elem_size == 0 else None
            suffix = f'[{count}]' if count is not None else f'[{byte_length}B]'
            return {'type_index':hex(ti),'name':f'{type_desc(elem)["name"]}{suffix}','leaf':hex(kind),'byte_length':byte_length,'element_type':type_desc(elem),'element_size_bytes':elem_size,'element_count':count}
        return {'type_index':hex(ti),'name':name or simple_name(ti),'leaf':hex(kind) if kind is not None else None}

    def parse_fieldlist(fidx, seen=None):
        seen = seen or set()
        if fidx in seen: return []
        seen.add(fidx)
        entry=records.get(fidx)
        if not entry or entry[0]!=LF_FIELDLIST: return []
        _, data=entry; p=0; out=[]
        while p+2<=len(data):
            if data[p]>=0xf0 and (data[p]&0xf0)==0xf0:
                pad=data[p]&0x0f
                if 0<pad<=len(data)-p: p+=pad; continue
            leaf=struct.unpack_from('<H',data,p)[0]
            start=p
            try:
                if leaf==LF_MEMBER and p+8<=len(data):
                    attrs=struct.unpack_from('<H',data,p+2)[0]; ti=struct.unpack_from('<I',data,p+4)[0]; q,offset=cvnum(data,p+8); name=cstr(data,q)
                    if not name: break
                    out.append({'kind':'member','name':name,'offset_bytes':offset,'type':type_desc(ti),'attributes':hex(attrs)})
                    p=q+len(name.encode('utf-8','replace'))+1
                elif leaf==LF_STMEMBER and p+8<=len(data):
                    attrs=struct.unpack_from('<H',data,p+2)[0]; ti=struct.unpack_from('<I',data,p+4)[0]; name=cstr(data,p+8)
                    if not name: break
                    out.append({'kind':'static_member','name':name,'offset_bytes':None,'type':type_desc(ti),'attributes':hex(attrs)})
                    p=p+8+len(name.encode('utf-8','replace'))+1
                elif leaf==LF_ENUMERATE and p+4<=len(data):
                    attrs=struct.unpack_from('<H',data,p+2)[0]; q,value=cvnum(data,p+4); name=cstr(data,q)
                    if not name: break
                    out.append({'kind':'enumerator','name':name,'value':value,'attributes':hex(attrs)})
                    p=q+len(name.encode('utf-8','replace'))+1
                elif leaf==LF_BCLASS and p+8<=len(data):
                    attrs=struct.unpack_from('<H',data,p+2)[0]; ti=struct.unpack_from('<I',data,p+4)[0]; q,offset=cvnum(data,p+8)
                    out.append({'kind':'base_class','name':type_desc(ti)['name'],'offset_bytes':offset,'type':type_desc(ti),'attributes':hex(attrs)})
                    p=q
                elif leaf==LF_INDEX and p+8<=len(data):
                    continuation=struct.unpack_from('<I',data,p+4)[0]
                    out.extend(parse_fieldlist(continuation,seen)); p+=8
                elif leaf == LF_VFUNCTAB:
                    if p+8>len(data): break
                    out.append({'kind':'vfunctab','type':type_desc(struct.unpack_from('<I',data,p+4)[0])});p+=8
                elif leaf == 0x1511 and p+8<=len(data):  # LF_ONEMETHOD
                    attrs=struct.unpack_from('<H',data,p+2)[0]; ti=struct.unpack_from('<I',data,p+4)[0]
                    q=p+8
                    virtual_offset = struct.unpack_from('<I',data,q)[0] if ((attrs >> 2) & 0x7) in (4,6) else None
                    if virtual_offset is not None: q+=4
                    name=cstr(data,q)
                    if not name: break
                    out.append({'kind':'method','name':name,'type':type_desc(ti),'attributes':hex(attrs),'vtable_offset':virtual_offset})
                    p=q+len(name.encode('utf-8','replace'))+1
                elif leaf == 0x150f and p+8<=len(data):  # LF_METHOD
                    count=struct.unpack_from('<H',data,p+2)[0]; ti=struct.unpack_from('<I',data,p+4)[0]; name=cstr(data,p+8)
                    if not name: break
                    out.append({'kind':'overloaded_methods','name':name,'count':count,'method_list_type_index':hex(ti)})
                    p=p+8+len(name.encode('utf-8','replace'))+1
                elif leaf==LF_NESTTYPE and p+8<=len(data):
                    ti=struct.unpack_from('<I',data,p+4)[0];name=cstr(data,p+8)
                    out.append({'kind':'nested_type','name':name,'type':type_desc(ti)});p=p+8+len(name.encode('utf-8','replace'))+1
                else:
                    # Preserve the stop reason; keep preceding fields, do not guess the unknown record length.
                    out.append({'kind':'unparsed_field_record','leaf':hex(leaf),'position_bytes':p,'remaining_prefix_hex':data[p:min(p+32,len(data))].hex()})
                    break
                if p<=start: break
            except (IndexError,struct.error,ValueError):
                break
        return out

    def layout_for(name):
        type_rec=chosen.get(name)
        if not type_rec: return {'name':name,'found':False}
        if type_rec['leaf']=='0x1507':
            underlying=int(type_rec['underlying_type_index'],16)
            underlying_desc=type_desc(underlying)
        else: underlying_desc=None
        fi=int(type_rec['field_list_index'],16)
        return {**type_rec,'found':True,'underlying_type':underlying_desc,'fields':parse_fieldlist(fi)}

    wanted=[]
    for name in sorted(chosen):
        if name in TARGET_NAMES or (RELEVANT.search(name) and name[:1] in 'FAUE' and not name.startswith(SKIP_GENERIC) and '<' not in name and '::' not in name and '_Parms' not in name and not name.startswith('Z_Construct')):
            item=layout_for(name)
            if (item.get('size_bytes') or 0)>0 or item.get('leaf')=='0x1507': wanted.append(item)
    # Include any requested spelling that is an enum/scoped alias.
    missing=[n for n in sorted(TARGET_NAMES) if n not in chosen]
    # Enumerations used beneath requested structures are recovered by name/index if recorded as UDTs.
    enum_values={x['name']:x['fields'] for x in wanted if x.get('leaf')=='0x1507'}
    output={'target_pdb':str(PDB),'target_pdb_bytes':PDB.stat().st_size,'tpi_header':{'header_bytes':hdr_size,'type_index_begin':hex(first),'type_index_end':hex(end),'record_bytes':rec_bytes,'stream_bytes':len(raw)},'record_leaf_counts':{'UDT_definitions':sum(1 for i in records if type_kinds[i] in (LF_CLASS,LF_STRUCTURE,LF_UNION,LF_ENUM)),'field_lists':sum(1 for i in records if type_kinds[i]==LF_FIELDLIST)},'target_names_found':sorted([n for n in TARGET_NAMES if n in chosen]),'target_names_missing':missing,'layouts':wanted,'interpretation_limits':['This file reads CodeView TPI declarations and compiler-emitted layouts only. A member name/type/offset does not prove which code reads or writes it, its runtime value, or its behavioral meaning.','Base-class fields are represented as base subobjects and are not flattened into inherited member offsets.','Unknown FieldList subrecord kinds stop decoding of that list; fields emitted before the stop remain visible with their direct offsets.','Some requested source spellings may be aliases or nested/scoped names and can be reported as unresolved until matched through symbols or cross-references.']}
    out=ROOT/'inventory'/'rules-20261029-count-target-layouts.json'
    out.write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'output':str(out),'bytes':out.stat().st_size,'target_names_found':output['target_names_found'],'target_names_missing':missing,'layouts':len(wanted),'header':output['tpi_header']},ensure_ascii=False,indent=2))
    msf.close()

if __name__=='__main__': main()







