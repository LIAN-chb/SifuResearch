import ast,datetime,hashlib,json,re,shutil
from pathlib import Path
ROOT=Path(r'E:\ProgrameFiles\SifuResearch');VAULT=ROOT/'Sifu'
MAPPING=json.loads(r'''{"受击硬直与脱离":[["受击与抗性","各资产的累计限制、状态矩阵与完整保存字段"],["敌人原型","不同敌人变体的本层属性、父类和配置引用"],["受击恢复","各 HittedDB 与恢复动作层"]],"敌人如何选择防御":[["AI防御","38 套情境图的全部已解析测试、节点与参数"],["敌人原型","不同原型实际保存的防御图引用"]],"防反与闪避反击后的追击":[["玩家攻击","逐条查看 Parry／Avoid 相关标志和命中结果"],["敌人攻击","对照原攻击者各命中行的配置"],["受击与抗性","核对状态持续与累计限制；不据配置提前认定窗口成因"]],"攻击冲击力韧性与伤害":[["玩家攻击","313 条玩家 HitBox 行，分别列命中／格挡／弹开配置"],["敌人攻击","492 条敌人 HitBox 行"],["共享攻击","50 条共享／Focus／通用 HitBox 行"],["动作与时序","553 个动作资源与600条动画行，以及命中／许可窗口"]],"群体AI与状态反馈":[["群体票据","50 个攻击票据的数量、角色掩码和冷却配置"],["敌人原型","各原型本层保存的群体／动作配置"]]}''')
changes={}
home=VAULT/'00索引/首页.md';s=home.read_text(encoding='utf-8')
s=s.replace('知识库分为三个目录；按主题阅读机制，再跳转到对应的简要实现。','知识库分为索引、机制、实现和配置四层；先读规则，再查对应实现与不同配置。')
s=s.replace('| 02实现 | 对应数据与执行逻辑、简短证据定位 | 下表的实现篇 |','| 02实现 | 对应数据与执行逻辑、简短证据定位 | 下表的实现篇 |'+chr(10)+'| 03配置 | 每种基础机制下的不同角色、武器、动作与 AI 配置 | [[03配置/配置索引]] |')
block='\n## 配置差异与全量查表\n\n原机制篇中的攻击数值是解释用样本；系统配置现在另行展开。入口：[[03配置/配置索引]]、[[03配置/覆盖范围与读表说明]]。\n\n| 已解析集合 | 当前收录 |\n|---|---|\n| 玩家／敌人／共享 HitBox 行 | 313／492／50，共 855 行，分别保存三种命中结果 |\n| 动作资源／动画行 | 553／600；保留旧资源与测试标记，不当作独立实战招式数 |\n| 受击与抗性／敌人原型 | 52 套／245 个父类链已核对的原型；原型值是本层保存配置 |\n| AI 情境防御／攻击票据 | 38 套图／50 个票据 |\n\n尚未解码、缺省继承、未对上引用和未验证的实战效果均在覆盖说明中单列。更新：2026-10-28。\n'
if '## 配置差异与全量查表' not in s:s+=block
changes[home]=s
for directory in ['01机制','02实现']:
 for topic,items in MAPPING.items():
  p=VAULT/directory/(topic+'.md');s=p.read_text(encoding='utf-8')
  block='\n## 不同配置查表\n\n本篇解释基础规则。不同角色、武器、动作与状态的保存配置单独维护，不再只靠正文少量例子表达覆盖范围。\n\n| 配置集合 | 查找内容 |\n|---|---|\n'
  for category,desc in items:block+='| [[03配置/'+category+'/索引]] | '+desc+' |\n'
  block+='\n统一边界见 [[03配置/覆盖范围与读表说明]]。保存值、最终实战值和未解码项分别标记。\n'
  if '## 不同配置查表' not in s:s+=block
  changes[p]=s
for name in ['术语与证据说明','研究进度与问题']:
 p=VAULT/'00索引'/(name+'.md');s=p.read_text(encoding='utf-8')
 if '## 配置目录补充' not in s:
  s+='\n## 配置目录补充\n\n已新增 [[03配置/配置索引]]，在原三个基础目录外专门收录配置差异。当前集合、完整性边界与未对上引用见 [[03配置/覆盖范围与读表说明]]。原型配置是本层覆盖值；动作资源、动画行和 HitBox 行分开计数。后续新增具体机制时，同步记录其不同配置，不再只列少数样本。\n'
 changes[p]=s
# Wiki alias pipes inside Markdown tables must be escaped for Obsidian.
for p,s in list(changes.items()):
 lines=[]
 for line in s.splitlines():
  if line.startswith('|'):
   line=re.sub(r'\[\[([^\]]+)\]\]',lambda m:'[['+m.group(1).replace(chr(92)+'|','|').replace('|',chr(92)+'|')+']]',line)
  lines.append(line)
 changes[p]='\n'.join(lines)+'\n'
backup=ROOT/'notes/vault-backups'/('config-catalog-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S'));backup.mkdir(parents=True,exist_ok=False)
for p,s in changes.items():
 dest=backup/p.relative_to(VAULT);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
 p.write_text(s,encoding='utf-8',newline=chr(10))
layoutpath=ROOT/'inventory/vault-layout.json';layout=json.loads(layoutpath.read_text(encoding='utf-8'))
if '03配置' not in layout['directories']:layout['directories'].append('03配置')
layout['documents']=sorted(p.relative_to(VAULT).as_posix() for p in VAULT.rglob('*.md') if '.obsidian' not in p.parts)
layout['configuration_catalog']='03配置/配置索引.md'
layoutpath.write_text(json.dumps(layout,ensure_ascii=False,indent=2),encoding='utf-8',newline=chr(10))
checker=ROOT/'scripts/verify_knowledge_vault.py';s=checker.read_text(encoding='utf-8')
s=s.replace("ref=target.split('|',1)[0]","ref=target.split('|',1)[0].rstrip(chr(92))")
s=s.replace("'Note outside three directories: '","'Note outside configured directories: '")
s=s.replace("if '[['+target+'/'+topic not in docs.get(source+'/'+topic,''):","if '[['+target+'/'+topic not in docs.get(source+'/'+topic,''):")
ast.parse(s);checker.write_text(s,encoding='utf-8',newline=chr(10))
print(json.dumps({'navigation_notes_updated':len(changes),'total_notes':len(layout['documents']),'backup':str(backup)},ensure_ascii=True))
