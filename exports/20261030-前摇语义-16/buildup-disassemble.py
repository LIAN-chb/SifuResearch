from pathlib import Path
import sys
R=Path('E:/ProgrameFiles/SifuResearch');sys.path.insert(0,str(R/'scripts'))
s=(R/'scripts/disassemble_research.py').read_text()
s=s.replace("ROOT/'logs'/group", "ROOT/'logs'/'20261030-前摇语义-16'/group")
s=s.replace("ROOT/'inventory'/(group+'-disassembly.json')", "ROOT/'exports'/'20261030-前摇语义-16'/(group+'-disassembly.json')")
ns={'__name__':'adapted'};exec(compile(s,'adapted-disassemble','exec'),ns)
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--group',required=True);parser.add_argument('--name',action='append',required=True)
a=parser.parse_args();ns['disassemble'](a.name,a.group)
