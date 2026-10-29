// Direction- and endpoint-aware orthogonal routes. One geometry for overview and focus.
globalThis.createPlayerGraphRouter = function () {
  const EPS=1e-6,HALF_W=94,HALF_H=29,ESCAPE=24,LANE=12;
  class Queue {
    constructor(){this.a=[];}
    push(v){const a=this.a;let i=a.length;a.push(v);while(i){const p=(i-1)>>1;if(a[p][0]<=v[0])break;a[i]=a[p];i=p;}a[i]=v;}
    pop(){const a=this.a,v=a[0],last=a.pop();if(a.length){let i=0;while(i*2+1<a.length){let j=i*2+1;if(j+1<a.length&&a[j+1][0]<a[j][0])j++;if(a[j][0]>=last[0])break;a[i]=a[j];i=j;}a[i]=last;}return v;}
    get size(){return this.a.length;}
  }
  function segment(a,b,e){const horizontal=Math.abs(a[1]-b[1])<EPS;return {horizontal,fixed:horizontal?a[1]:a[0],from:Math.min(a[horizontal?0:1],b[horizontal?0:1]),to:Math.max(a[horizontal?0:1],b[horizontal?0:1]),direction:Math.sign(b[horizontal?0:1]-a[horizontal?0:1]),source:e.source,target:e.target,id:e.id};}
  function compatible(a,b){return a.direction===b.direction&&(a.source===b.source||a.target===b.target);}
  function overlaps(a,b){return Math.min(a.to,b.to)>Math.max(a.from,b.from)+EPS;}
  function conflicts(a,b){if(a.horizontal!==b.horizontal||!overlaps(a,b))return false;const distance=Math.abs(a.fixed-b.fixed);return distance<LANE-EPS&&!(distance<EPS&&compatible(a,b));}
  function simplify(ps){const out=[];for(const p of ps){if(out.length&&Math.abs(p[0]-out.at(-1)[0])<EPS&&Math.abs(p[1]-out.at(-1)[1])<EPS)continue;while(out.length>=2){const a=out.at(-2),b=out.at(-1);if((a[0]===b[0]&&b[0]===p[0])||(a[1]===b[1]&&b[1]===p[1]))out.pop();else break;}out.push(p);}return out;}
  function touches(a,b,n,pad=4){return a[0]===b[0]?a[0]>n.x-HALF_W-pad&&a[0]<n.x+HALF_W+pad&&Math.max(a[1],b[1])>n.y-HALF_H-pad&&Math.min(a[1],b[1])<n.y+HALF_H+pad:a[1]>n.y-HALF_H-pad&&a[1]<n.y+HALF_H+pad&&Math.max(a[0],b[0])>n.x-HALF_W-pad&&Math.min(a[0],b[0])<n.x+HALF_W+pad;}
  function mergeSegments(routes){
    const buckets=new Map();
    for(const r of routes)for(let i=1;i<r.points.length;i++){const s=segment(r.points[i-1],r.points[i],r.e);if(s.to-s.from<EPS)continue;const key=(s.horizontal?'h':'v')+s.fixed+':'+s.direction;if(!buckets.has(key))buckets.set(key,[]);buckets.get(key).push(s);}
    const out=[];
    for(const entries of buckets.values()){
      const cuts=[...new Set(entries.flatMap(s=>[s.from,s.to]))].sort((a,b)=>a-b);
      for(let i=1;i<cuts.length;i++){const from=cuts[i-1],to=cuts[i],middle=(from+to)/2,cover=entries.filter(s=>s.from<middle&&s.to>middle);if(!cover.length)continue;
        // Pairwise compatible membership prevents transitive false buses.
        const sets=[];for(const s of cover){const match=sets.find(xs=>xs.every(x=>compatible(x,s)));if(match)match.push(s);else sets.push([s]);}
        for(const xs of sets){const first=xs[0];out.push({...first,from,to,ids:[...new Set(xs.map(s=>s.id))],members:xs.map(s=>({id:s.id,source:s.source,target:s.target,direction:s.direction}))});}
      }
    }
    return out;
  }
  function routeAll(nodes,edges,basePairs,priority=[],attempt=0){
    const xs=new Set([0]),ys=new Set([0]),byId=new Map(nodes.map(n=>[n.id,n]));
    for(const n of nodes){for(const dx of [0,-LANE,LANE,-HALF_W-ESCAPE,HALF_W+ESCAPE,-HALF_W-ESCAPE-LANE,HALF_W+ESCAPE+LANE])xs.add(n.x+dx);for(const dy of [0,-LANE,LANE,-HALF_H-ESCAPE,HALF_H+ESCAPE,-HALF_H-ESCAPE-LANE,HALF_H+ESCAPE+LANE])ys.add(n.y+dy);}
    const extent={w:Math.max(1540,...nodes.map(n=>n.x+170)),h:Math.max(1045,...nodes.map(n=>n.y+120))};xs.add(extent.w);ys.add(extent.h);
    const X=[...xs].filter(x=>x>=0).sort((a,b)=>a-b),Y=[...ys].filter(y=>y>=0).sort((a,b)=>a-b),XM=new Map(X.map((x,i)=>[x,i])),YM=new Map(Y.map((y,i)=>[y,i]));
    const blocked=new Set();for(let i=0;i<X.length;i++)for(let j=0;j<Y.length;j++)if(nodes.some(n=>Math.abs(X[i]-n.x)<HALF_W+7&&Math.abs(Y[j]-n.y)<HALF_H+7))blocked.add(i+','+j);
    const reserved=[],routes=[],failures=[],failureDetails=[],opposite={1:2,2:1,3:4,4:3},exit={r:1,l:2,b:3,t:4},entry={r:2,l:1,b:4,t:3};
    const guards=[];for(const n of nodes)for(const [a,b] of [[[n.x-HALF_W,n.y],[n.x-HALF_W-ESCAPE,n.y]],[[n.x+HALF_W,n.y],[n.x+HALF_W+ESCAPE,n.y]],[[n.x,n.y-HALF_H],[n.x,n.y-HALF_H-ESCAPE]],[[n.x,n.y+HALF_H],[n.x,n.y+HALF_H+ESCAPE]]])guards.push({...segment(a,b,{source:n.id,target:n.id,id:'port'}),node:n.id,end:b});
    function forbidden(s){return reserved.some(r=>conflicts(s,r))||guards.some(g=>g.node!==s.source&&g.node!==s.target&&g.horizontal===s.horizontal&&Math.abs(g.fixed-s.fixed)<EPS&&overlaps(g,s));}
    function ports(n,e,incoming=false){const result=[],sideChoices=basePairs.has(e.id)?(incoming?['l']:['r']):(incoming?['t']:['b']);for(const side of sideChoices){const horizontal=side==='r'||side==='l',sign=side==='r'||side==='b'?1:-1,a=horizontal?[n.x+sign*HALF_W,n.y]:[n.x,n.y+sign*HALF_H],p=horizontal?[n.x+sign*(HALF_W+ESCAPE),n.y]:[n.x,n.y+sign*(HALF_H+ESCAPE)];if(p[0]<0||p[1]<0||nodes.some(other=>other.id!==n.id&&touches(a,p,other))||forbidden(segment(incoming?p:a,incoming?a:p,e)))continue;result.push({a,p,side});}return result;}
    function search(start,end,e,startDir,endDir){
      const sx=XM.get(start[0]),sy=YM.get(start[1]),tx=XM.get(end[0]),ty=YM.get(end[1]);if(sx===undefined||sy===undefined||tx===undefined||ty===undefined)return null;
      const q=new Queue(),dist=new Map(),prev=new Map(),key=(x,y,d)=>x+','+y+','+d,first=key(sx,sy,startDir);dist.set(first,0);q.push([0,sx,sy,startDir,0]);
      while(q.size){const [,x,y,dir,cost]=q.pop(),k=key(x,y,dir);if(dist.get(k)!==cost)continue;
        if(x===tx&&y===ty&&dir!==opposite[endDir]){const ps=[[X[x],Y[y]]];let at=k;while(prev.has(at)){const p=prev.get(at);ps.push([X[p.x],Y[p.y]]);at=p.key;}return {points:ps.reverse(),cost};}
        for(const [dx,dy,nd] of [[1,0,1],[-1,0,2],[0,1,3],[0,-1,4]]){const nx=x+dx,ny=y+dy;if(nd===opposite[dir]||nx<0||ny<0||nx>=X.length||ny>=Y.length||blocked.has(nx+','+ny))continue;const a=[X[x],Y[y]],b=[X[nx],Y[ny]],s=segment(a,b,e);if(forbidden(s))continue;const nc=cost+(Math.abs(b[0]-a[0])+Math.abs(b[1]-a[1]))/20+(dir===nd?0:8),nk=key(nx,ny,nd);if(nc<(dist.get(nk)??Infinity)){dist.set(nk,nc);prev.set(nk,{x,y,key:k});q.push([nc+(Math.abs(X[tx]-X[nx])+Math.abs(Y[ty]-Y[ny]))/20,nx,ny,nd,nc]);}}
      }return null;
    }
    const backwards=e=>byId.get(e.target).y<byId.get(e.source).y;
    const rank=e=>priority.includes(e.id)?priority.indexOf(e.id):1000;
    const sorted=edges.filter(e=>e.target!==null).sort((a,b)=>Number(basePairs.has(b.id))-Number(basePairs.has(a.id))||rank(a)-rank(b)||Number(backwards(b))-Number(backwards(a))||a.id.localeCompare(b.id));
    for(const e of sorted){const a=byId.get(e.source),b=byId.get(e.target);let points=null;
      if(a.y===b.y||a.x===b.x){const horizontal=a.y===b.y,sign=Math.sign(horizontal?b.x-a.x:b.y-a.y),ps=horizontal?[[a.x+sign*HALF_W,a.y],[b.x-sign*HALF_W,b.y]]:[[a.x,a.y+sign*HALF_H],[b.x,b.y-sign*HALF_H]];if(!nodes.some(n=>n.id!==a.id&&n.id!==b.id&&touches(ps[0],ps[1],n))&&!forbidden(segment(ps[0],ps[1],e)))points=ps;}
      if(!points){const pairs=[];for(const s of ports(a,e))for(const t of ports(b,e,true))pairs.push({s,t,c:Math.abs(s.p[0]-t.p[0])+Math.abs(s.p[1]-t.p[1])});pairs.sort((a,b)=>a.c-b.c);let best=null;for(const pair of pairs){const found=search(pair.s.p,pair.t.p,e,exit[pair.s.side],entry[pair.t.side]);if(!found)continue;const ps=simplify([pair.s.a,...found.points,pair.t.a]),score=found.cost+ps.length*2;if(!best||score<best.score)best={points:ps,score};if(best&&pair.c/20>best.score)break;}points=best?.points;}
      if(!points){failures.push(e.id);failureDetails.push({id:e.id,sourcePorts:ports(a,e),targetPorts:ports(b,e,true),near:reserved.filter(r=>conflicts(segment([a.x,a.y+HALF_H],[a.x,a.y+HALF_H+ESCAPE],e),r)||conflicts(segment([b.x,b.y-HALF_H-ESCAPE],[b.x,b.y-HALF_H],e),r))});continue;}const route={e,points};routes.push(route);for(let i=1;i<points.length;i++)reserved.push(segment(points[i-1],points[i],e));
    }
    if(failures.length&&attempt<3)return routeAll(nodes,edges,basePairs,[...new Set([...failures,...priority])],attempt+1);
    return {routes,failures,extent,failureDetails,attempts:attempt+1};
  }
  return {routeAll,mergeSegments,compatible,conflicts};
};
