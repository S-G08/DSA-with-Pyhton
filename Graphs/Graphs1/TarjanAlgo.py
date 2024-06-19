def stronglyConnectedComponents(n, edges):
    # Initialize empty adjacency lists for the graph and its reverse
    graph = [[] for _ in range(n)]  # Graph
    rev_graph = [[] for _ in range(n)]  # Reverse graph

    # Construct the graph and its reverse
    for edge in edges:
        u, v = edge
        graph[u].append(v)  # Add edge from u to v
        rev_graph[v].append(u)  # Add edge from v to u in the reverse graph

    # Define DFS function to fill the stack with nodes
    def dfs(node, visited, stack, graph):
        visited[node] = True  # Mark node as visited
        for neighbour in graph[node]:
            if not visited[neighbour]:  # If neighbour is not visited
                dfs(neighbour, visited, stack, graph)  # Recursively call DFS
        stack.append(node)  # Add node to the stack

    # Define DFS function to find SCCs (Strongly Connected Components)
    def dfs_scc(node, visited, scc, rev_graph):
        visited[node] = True  # Mark node as visited
        scc.append(node)  # Add node to the SCC
        for neighbour in rev_graph[node]:
            if not visited[neighbour]:  # If neighbour is not visited
                dfs_scc(neighbour, visited, scc, rev_graph)  # Recursively call DFS

    # Perform DFS on the graph to fill the stack
    visited = [False] * n  # Initialize visited array for graph
    stack = []  # Initialize stack
    for i in range(n):
        if not visited[i]:  # If node is not visited
            dfs(i, visited, stack, graph)  # Call DFS to fill the stack

    # Reset visited array for second DFS
    visited = [False] * n

    # Initialize list to store SCCs
    scc_list = []

    # Perform DFS on the reverse graph to find SCCs
    while stack:
        node = stack.pop()  # Pop a node from the stack
        if not visited[node]:  # If node is not visited
            scc = []  # Initialize a new SCC
            dfs_scc(node, visited, scc, rev_graph)  # Call DFS to find SCC
            scc_list.append(scc)  # Add SCC to the list of SCCs

    return scc_list
