class Graph:
    def __init__(self,n) -> None:
        self.graph=[]
        self.visited=[]
        self.n=n
        for _ in range(n+1):
            self.graph.append([])
            self.visited.append(False)
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def print(self):
        print(self.graph)

    def clear(self):
        for i in range(len(self.visited)):
            self.visited[i]=False
            

    def dfs(self,s):
        self.visited[s]=True
        print("Visited:",s)
        for v in self.graph[s]:
            if not self.visited[v]:               
                self.dfs(v)
    
    def _dfs(self,s):
        self.clear()
        for i in range(1,self.n+1):
            if not self.visited[i]:
                self.dfs(i)
g=Graph(7)  
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(6,7)

g._dfs(1)

