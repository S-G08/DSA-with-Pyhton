class Edge:
    def __init__(self,src,dest,wt):
        self.src = src
        self.dest = dest
        self.wt = wt

def getParent(v,parent):
    if v == parent[v]:
        return v
    return getParent(parent[v],parent)

def minimumSpanningTree(edges,n,E):
    edges = sorted(edges,key = lambda edge:edge.wt)
    output = []

    
    parent = [i for i in range(n)]
    count = 0
    i = 0
    while count < (n-1):
        currentEdge = edges[i]
        srcParent = getParent(currentEdge.src,parent)
        destParent = getParent(currentEdge.dest,parent)
        
        if srcParent != destParent:
            output.append(currentEdge)
            count+=1
            parent[srcParent] = destParent
        i+=1
    total_weight=0
    for ele in output:
        total_weight+=ele.wt
    return total_weight


li = [int(ele) for ele in input().split()]
n = li[0]
E = li[1]
edges = []
for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    src = curr_input[0]
    dest = curr_input[1]
    wt = curr_input[2]
    edge = Edge(src,dest,wt)
    edges.append(edge)

output = minimumSpanningTree(edges,n,E)

print(output)