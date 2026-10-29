from pathlib import Path
import ast
p=Path(r'E:\ProgrameFiles\SifuResearch\scripts\build_player_readable.py');s=p.read_text(encoding='utf-8')
old="def literal(s):\n parts=re.findall(r'[A-Z]+(?=[A-Z][a-z]|\\d|\\b)|[A-Z]?[a-z]+|\\d+',s)\n return '·'.join(WORDS.get(x,x) for x in parts if WORDS.get(x,x)) or s"
new="""def literal(s):
 phrases={'MainChar':'','Mainchar':'','MC':'','FollowUp':'后续','GetUp':'起身','GetUpAttack':'起身攻击','Backturned':'背向','BareHands':'徒手','PostParry':'招架后','KnockDown':'击倒','Knockdown':'击倒','ChargedPunch':'蓄力拳','GroundedPunch':'倒地目标拳击','GroundPunches':'地面连续拳'}
 parts=[]
 for chunk in re.split(r'[_\\s]+',s):
  if chunk in phrases:parts.append(phrases[chunk]);continue
  words=re.findall(r'[A-Z]+(?=[A-Z][a-z]|\\d|\\b)|[A-Z]?[a-z]+|\\d+',chunk)
  parts.extend(WORDS.get(x,x) for x in words)
 return '·'.join(x for x in parts if x) or s"""
if old not in s:raise ValueError('literal block missing')
s=s.replace(old,new)
marker="def graphtext(tree,subset=None,default_indices=None,with_starts=True):"
helper="""def node_damage_summary(node):
 life=set();structure=set()
 for key,ref in node.get('m_AttackInfos[0]',{}).items():
  if not key.startswith('m_Attacks['):continue
  for w in windows(local(ref)):
   ha,hn,hr=gethit(w)
   if not hr:continue
   ps=nested(hr['properties'],'m_OnHitImpact')
   if val(ps,'m_bUseDamage') is True:life.add(val(ps,'m_fDamage'))
   if val(ps,'m_bUseStructureDamage') is True:structure.add(val(ps,'m_fStructureDamage'))
 def show(values):return '/'.join(fmt(x) for x in sorted(values)) if len(values)<=4 else '多种，见表'
 return '命中段生命配置:'+show(life)+'；架势配置:'+show(structure) if life or structure else ''
"""
s=s.replace(marker,helper+'\n'+marker)
s=s.replace("label='N'+str(i)+' '+node_label(ns[i])","label='N'+str(i)+' '+node_label(ns[i])\n  damage=node_damage_summary(ns[i])\n  if damage:label+='<br/>'+damage")
s=s.replace("for group,items in groups.items():\n p=BASE", "for group,items in groups.items():\n items.sort(key=lambda o:('/_old/' in o['asset'],'/_Special' in o['asset'],o['asset']))\n p=BASE")
s=s.replace("['连续命中保证','连招树只证明配置衔接", "['图中生命／架势配置','标注基本动作各命中段的保存值集合，不求和，不是最终伤害或同一输入的累计值'],['连续命中保证','连招树只证明配置衔接")
ast.parse(s);p.write_text(s,encoding='utf-8',newline=chr(10))
