"""Display topology only; inputs/conditions and source edge identity remain intact."""
import collections

def build_graph(data):
    nodes=data['nodes']; canonical=sorted({n['target'] for n in nodes.values()})
    groups={i:{i} for i in canonical}; representative={i:i for i in canonical}; audit=[]
    node_edges=[(n['target'],e) for n in nodes.values() for e in n['edges']]
    def signature(i):
        incoming=set();outgoing=set()
        for s,e in node_edges:
            if e['target'] is None:continue
            a,b=representative[s],representative[e['target']]
            if b==i:incoming.add('N'+str(a))
            if a==i:outgoing.add('N'+str(b))
        for e in data['starts']:
            if e['target'] is not None and representative[e['target']]==i:incoming.add('S'+str(e['start']))
        # Empty adjacency is unknown position, not evidence of equivalence.
        if not incoming and not outgoing:return ('isolated',i)
        return (tuple(sorted(incoming)),tuple(sorted(outgoing)))
    while True:
        buckets=collections.defaultdict(list)
        for i in sorted(groups):buckets[signature(i)].append(i)
        merges=[ids for ids in buckets.values() if len(ids)>1]
        if not merges:break
        for ids in merges:
            root=min(ids);sig=signature(root)
            audit.append({'kind':'equal-neighbours','members':sorted(set().union(*(groups[i] for i in ids))),'incoming':list(sig[0]),'outgoing':list(sig[1]),'inputAndConditionIgnored':True})
            for i in ids[1:]:
                groups[root]|=groups.pop(i)
            for member in groups[root]:representative[member]=root
    # Routing-only conduit is not another playable attack; retain its routing evidence.
    for i in list(groups):
        members=groups[i]
        if any(nodes[str(m)]['variants'] for m in members):continue
        successors={representative[e['target']] for s,e in node_edges if representative[s]==i and e['target'] is not None and representative[e['target']]!=i}
        if len(successors)==1:
            target=next(iter(successors));audit.append({'kind':'routing-only','members':sorted(members),'target':target})
            groups[target]|=groups.pop(i)
            for member in members:representative[member]=target
    labels={0:'起身攻击',2:'招架反击·轻击',4:'重击第2段',5:'重击第3段',7:'轻击第4段',8:'轻击第5段',9:'轻击连打收尾',10:'重击第4段',11:'重重轻',12:'重重轻重',14:'轻击第3段',15:'轻轻轻重',16:'重击后·变体重击',19:'招架反击·重击',21:'招架反击·长按重击',22:'奔跑攻击',25:'推击后追击',30:'轻轻重',31:'后前重',32:'后前轻',33:'长按轻击',36:'前前重',39:'前前轻',40:'前前轻后·轻击',44:'轻击第1段',45:'轻击第2段',48:'重击第1段',50:'重击后·变体连按',51:'防御重击',52:'拉开距离攻击',54:'拉开后·重击',55:'闪避攻击',56:'蓄力重击'}
    positions={0:(150,110),22:(390,110),55:(630,110),51:(870,110),52:(1110,110),54:(1350,110),2:(260,230),19:(500,230),21:(740,230),33:(1040,230),56:(1280,230),39:(390,355),36:(630,355),32:(870,355),31:(1110,355),40:(1350,355),44:(390,505),45:(630,505),14:(870,505),7:(1110,505),8:(1350,505),48:(390,665),4:(630,665),5:(870,665),10:(1110,665),50:(1350,665),16:(150,825),11:(390,825),12:(630,825),9:(870,825),15:(1110,825),30:(1350,825),25:(1110,955)}
    labels[50]='重击后·变体攻击'
    assert set(groups)==set(positions),(set(groups)-set(positions),set(positions)-set(groups))
    display=[]
    for i,members in sorted(groups.items()):
        raw=sorted(n['id'] for n in nodes.values() if representative[n['target']]==i)
        display.append({'id':i,'label':labels[i],'configs':sorted(members),'rawNodes':raw,'x':positions[i][0],'y':positions[i][1],'direction':i in (31,32,36,39)})
    edges=collections.defaultdict(list);internal=[]
    for s,e in node_edges:
        a=representative[s];b=representative[e['target']] if e['target'] is not None else None
        record={**e,'sourceConfig':s}
        if a==b:internal.append({'display':a,**record})
        else:edges[(a,b)].append(record)
    display_edges=[{'source':a,'target':b,'variants':es,'sourceEdgeIndices':[e['index'] for e in es]} for (a,b),es in sorted(edges.items(),key=lambda x:(x[0][0],x[0][1] if x[0][1] is not None else -1))]
    for e in display_edges:
        e['id']=str(e['source'])+'-'+str(e['target'])
    return {'width':1540,'height':1045,'nodes':display,'edges':display_edges,'internalEdges':internal,'merges':audit,'canonicalToDisplay':{str(k):v for k,v in representative.items()},'rawToDisplay':{k:representative[n['target']] for k,n in nodes.items()},'starts':[{**s,'displayTarget':representative[s['target']] if s['target'] is not None else None} for s in data['starts']],'reportedCommonInput':{'targets':[31,32,36,39],'provenance':'用户观察：方向招式通常可在多种动作后接入；不作为逐源节点已证实边，限制待核'}}
