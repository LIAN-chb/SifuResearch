"""Incremental readable Hitted configuration catalog. Does not regenerate older catalogs."""
import json,hashlib,datetime
from pathlib import Path
R=Path(r'E:\ProgrameFiles\SifuResearch');V=R/'Sifu'
a=json.loads((R/'inventory/followup-hitted-assets.json').read_text(encoding='utf-8'))
def flat(ps,p=''):
 out={}
 for f in ps:
  k=p+f['name'];v=f['value']
  if isinstance(v,list):out.update(flat(v,k+'.'))
  else:out[k]=f.get('reference',v)
 return out
def cell(v):
 if v is None:return '空引用'
 if v is True:return '是'
 if v is False:return '否'
 if isinstance(v,float):return f'{v:.8g}'
 if isinstance(v,dict):return '未解码（保留原始摘要）'
 return str(v).replace('|','\\|').replace('\n',' ')
def short(v):return cell(v).split('/')[-1].split('.')[-1] if v else '无'
def bound(f,p):
 t=f.get(p+'Type');v=f.get(p+'Value');label=str(t).split('::')[-1]
 return '无界（保存'+cell(v)+'）' if label=='Open' else label+':'+cell(v)
lines=['# Hitted订单与服务配置','', '[[03配置/订单与服务/索引|返回订单索引]] · [[01机制/连续受击与反击追击的系统链|综合机制]] · [[02实现/连续受击与反击追击的系统链|执行证据]]','',
'这里只列本机构建这两份订单默认对象及其全部33条服务；保存值不等于每次受击都激活。父类、条件、动画通知和实例引用需要分别核对。序号保留原始数组下标。','',
'## 本层订单设置','', '| 订单 | 类型 | 父类 | 启动动作状态 | 停止时弹出动作状态 | 是否标记硬直订单 | 进入／订单间／退出混合时长配置 |','|---|---|---|---|---|---|---|']
rows=[]
for o in a['objects']:
 if not o['export'].startswith('Default__'):continue
 f=flat(o['properties']);stem=o['asset'].split('/')[-1].removesuffix('.uasset');pkg=next(p for p in a['packages'] if p['path']==o['asset']);cl=pkg['exports'][0];parent=o['references'].get(str(cl['superIndex']))
 lines.append('| '+' | '.join(map(cell,[stem,f.get('m_eOrderType'),parent,f.get('m_ePushFightingStateOnStart','未保存'),f.get('m_bPopFightingStateOnStop','未保存'),f.get('m_bIsStunOrder','未保存'),str([f.get(x+'.m_fDuration','未保存') for x in ['m_LocoToOrderBlendSettings','m_OrderToOrderBlendSettings','m_OrderToLocoBlendSettings']])]))+' |')
lines+=['','`EFightingActionState::Hit`是此字段的准确枚举类型；不要直接视作持续状态`EFightingState::Dizzy`。未保存字段不补成false或0。','']
for o in a['objects']:
 if not o['export'].startswith('Default__'):continue
 stem=o['asset'].split('/')[-1].removesuffix('.uasset');elements=next(f for f in o['properties'] if f['name']=='m_OrderServices')['value'][0]['arrayElements']
 lines+=['## '+stem+'：全部服务','', '| 下标 | 服务类 | 实例覆写 | 禁用 | 按帧区间启动 | 动画缺少该服务时启动 | 激活条件／反转 | 保存范围／绑定动画 | 冻结处理 |','|---|---|---|---|---|---|---|---|---|']
 for i,e in enumerate(elements):
  f=flat(e);cls=f.get('m_OrderServiceInstance.m_DefaultClassObject');inst=f.get('m_OrderServiceInstance.m_Instance');ran='m_FrameRangeInfos.m_FrameRange.'
  row={'order':stem,'index':i,'fields':f};rows.append(row)
  vals=[i,short(cls),short(inst),cell(f.get('m_bDisabled')),cell(f.get('m_bActivateFromFrameRange')),cell(f.get('m_bActivateWhenMissingFromAnim')),short(f.get('m_ActivationCondition'))+'／反转='+cell(f.get('m_bInvertCondition')),bound(f,ran+'LowerBound.')+' → '+bound(f,ran+'UpperBound.')+'；绑定='+cell(f.get('m_FrameRangeInfos.m_bBoundToAnim')),f.get('m_eFreezeFrameHandling')]
  lines.append('| '+' | '.join(cell(v) for v in vals)+' |')
 lines+=['']
lines+=['## 订单内的实例覆写','', '| 订单／实例 | 本层字段（中文） | 原字段 | 保存值或引用 |','|---|---|---|---|']
labels={'m_availabilityLayerData':'动作许可层数据','m_eOperation':'许可层组合运算','m_bRemoveOnOrderServiceStop':'服务停止时移除','m_BoneMask':'骨骼遮罩','m_EnumLayer.m_Value':'变量权重层枚举','m_fEnterLeaveSlopeHitActivationDelay':'进入／离开斜坡命中激活延迟','m_bHasHitOnEnterSlope':'进入斜坡时有命中','m_bHasHitOnLeaveSlope':'离开斜坡时有命中','m_ComboStartName':'连招起始状态名','m_eDropReason':'掉落原因'}
for o in a['objects']:
 if o['export'].startswith('Default__'):continue
 for k,v in flat(o['properties']).items():lines.append('| '+' | '.join(map(cell,[o['asset'].split('/')[-1]+':'+o['export'],labels.get(k,'其他保存字段'),k,v]))+' |')
lines+=['','## 来源与覆盖','', '`inventory/followup-hitted-assets.json`保存完整路径、引用、边界和源文件SHA；`inventory/followup-hitted-catalog-table.json`保留上表每行字段及完整引用。提取副本在`logs/followup-hitted/extracted/`。两份类导出含native后缀，未伪称其字节码已经解析；8份默认／子对象的tagged边界已完整核对。','', '配置里的禁用、帧范围启动、缺动画时启动和激活条件是不同开关。范围无界时保存的0不是有效端点；按帧启动为否也不等于服务永不执行，需继续看动画通知／订单服务生命周期。']
def put(rel,text):
 p=V/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.strip()+'\n',encoding='utf-8',newline='\n')
put('03配置/订单与服务/Hitted订单与服务.md','\n'.join(lines))
put('03配置/订单与服务/索引.md','''# 订单与服务配置

[[03配置/配置索引|配置索引]] · [[00索引/系统线索与关系图|系统线索]]

| 集合 | 读取内容 | 覆盖与边界 |
|---|---|---|
| [[03配置/订单与服务/Hitted订单与服务]] | 普通／通用受击订单默认值、全部33条服务及实例覆写 | 本机定向提取；服务实际触发另核对 |

订单描述执行生命周期；服务可在条件、帧范围或动画通知下附加作用。已提取、已解析、已接通逻辑和已实战验证分开记录，不能用资源名字补因果。
''')
(R/'inventory/followup-hitted-catalog-table.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
lp=R/'inventory/vault-layout.json';layout=json.loads(lp.read_text(encoding='utf-8'))
for rel in ['03配置/订单与服务/Hitted订单与服务.md','03配置/订单与服务/索引.md']:
 if rel not in layout['documents']:layout['documents'].append(rel)
lp.write_text(json.dumps(layout,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
print(json.dumps({'new_notes':2,'service_rows':len(rows)},ensure_ascii=True))