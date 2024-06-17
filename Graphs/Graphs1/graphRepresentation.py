class Graph:
    def __init__(self, n:int) -> None:
        self.graph=[]
        # for adjacency matrix and edge lis
        for i in range(n+1):
            temp=[0 for _ in range(n+1)]
            self.graph.append(temp)
        
        # for adjacency list
        for _ in range(n+1):
            self.graph.append([])

    def add_edge(self,u, v)-> None:
        #for adjacency matrix
        self.graph[u][v]=1
        self.graph[v][u]=1

        #for edge list
        self.graph.append((u,v))

        #for adjacency list
        self.graph[u].append[v]
        self.graph[v].append[u]


    def print(self):
        print(self.graph)