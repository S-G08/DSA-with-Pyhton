from collections import deque

def topologicalSort(edges, n, m):
    # Step 1: Initialize graph and in-degree array
    graph = {i: [] for i in range(1, n + 1)}
    in_degree = {i: 0 for i in range(1, n + 1)}
    
    # Step 2: Build the graph and fill in-degrees
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Step 3: Find all nodes with in-degree 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topological_order = []
    
    # Step 4: Process the nodes
    while queue:
        current = queue.popleft()
        topological_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Step 5: Check if we processed all nodes
    if len(topological_order) == n:
        return topological_order
    else:
        return []  # This case should not happen as the graph is guaranteed to be a DAG

