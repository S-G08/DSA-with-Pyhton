import heapq

def networkDelayTime(edges, n, k):
    # Step 1: Create an adjacency list
    adj_list = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        adj_list[u].append((v, w))
    
    # Step 2: Initialize distances and priority queue
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0
    min_heap = [(0, k)]  # (distance, node)
    
    # Step 3: Dijkstra's algorithm
    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        
        if current_distance > dist[current_node]:
            continue
        
        for neighbor, weight in adj_list[current_node]:
            distance = current_distance + weight
            
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    
    # Step 4: Find the maximum distance
    max_distance = max(dist.values())
    return max_distance if max_distance != float('inf') else -1

