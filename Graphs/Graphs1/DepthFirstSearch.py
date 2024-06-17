class Graph:
    def __init__(self,n) -> None:
        self.graph=[]
        self.visited=[]
        for _ in range(n+1):
            self.graph.append([])
            self.visited.append(False)
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def print(self):
        print(self.graph)

    def dfs(self,s):
        self.visited[s]=True
        print("Visited:",s)
        for v in self.graph[s]:
            if not self.visited[v]:               
                self.dfs(v)

g=Graph(5)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(3,5)
g.dfs(1)

