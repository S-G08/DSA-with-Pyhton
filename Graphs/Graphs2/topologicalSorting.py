from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)
        self.visited=[]
        self.st=[]

        for i in range(V+1):
            self.visited.append(False)
    def addEdge(self, v, w):
        self.adj[v].append(w)


def dfs(g,s):
    for v in g.adj[s]:
        if not g.visited[v]:
            g.visited[v]=True
            dfs(g,v)
    g.st.append(s)
def topologicalSort(g):
    for i in range(g.V):
        if not g.visited[i]:
            g.visited[i]=True
            dfs(g,i)
    
    while len(g.st)>0:
        print(g.st[-1],end=" ")
        g.st.pop()
    

    



    
    
if __name__ == "__main__":
    n = int(input())
    e = int(input())

    g = Graph(n)
    for _ in range(e):
        a, b = map(int, input().split())
        g.addEdge(a, b)

    topologicalSort(g)
