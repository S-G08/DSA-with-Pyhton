from collections import deque

def dfs(node, parent, adj, visi, n):
    visi[node] = True

    for i in adj[node]:
        if not visi[i]:
            if dfs(i, node, adj, visi, n):
                return True
        elif parent != i:
            return True
    
    return False

def cycleDetection(edges, n, m):
    adj = [[] for _ in range(n+1)]
    for i in range(m):
        adj[edges[i][0]].append(edges[i][1])
        adj[edges[i][1]].append(edges[i][0])

    visi = [False] * (n+1)
    for i in range(1, n+1):
        if not visi[i]:
            if dfs(i, -1, adj, visi, n):
                return "Yes"
    
    return "No"

def cycle_detection_bfs(edges, n, m):
    adj = [[] for _ in range(n+1)]
    for i in range(len(edges)):
        adj[edges[i][0]].append(edges[i][1])
        adj[edges[i][1]].append(edges[i][0])

    visi = [False] * (n+1)

    for node in range(1, n+1):
        if not visi[node]:
            q = deque([(node, -1)])
            visi[node] = True

            while q:
                front, parent = q.popleft()
                for i in adj[front]:
                    if i == parent:
                        continue
                    elif visi[i]:
                        return "Yes"
                    else:
                        q.append((i, front))
                        visi[i] = True

    return "No"

