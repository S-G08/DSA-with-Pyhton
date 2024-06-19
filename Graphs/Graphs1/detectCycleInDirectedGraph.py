def isCyclicUtil(graph, v, visited, recStack):
    visited[v] = True
    recStack[v] = True
    
    for neighbour in graph[v]:
        if not visited[neighbour]:
            if isCyclicUtil(graph, neighbour, visited, recStack):
                return True
        elif recStack[neighbour]:
            return True
    
    recStack[v] = False
    return False

def isCyclic(edges, num_vertices, num_edges):
    graph = [[] for _ in range(num_vertices)]
    
    for u, v in edges:
        graph[u].append(v)
    
    visited = [False] * num_vertices
    recStack = [False] * num_vertices
    
    for node in range(num_vertices):
        if not visited[node]:
            if isCyclicUtil(graph, node, visited, recStack):
                return True
    return False


