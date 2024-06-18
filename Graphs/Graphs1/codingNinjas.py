from typing import List
from sys import stdin

def solve(Graph: List[str], N: int, M: int) -> int:
    searching_string = "CODINGNINJA"
    visited = [[False for _ in range(len(Graph[i]))] for i in range(len(Graph))]

    for i in range(len(Graph)):
        for j in range(len(Graph[i])):
            if Graph[i][j] == 'C':
                if dfs(Graph, visited, searching_string[1:], i, j):
                    return 1
        
    return 0

def dfs(graph: List[str], visited: List[List[bool]], search_string: str, i: int, j: int) -> bool:
    if not search_string:
        visited[i][j] = True
        return True

    visited[i][j] = True
    x_dir = [-1, 1, 0, 0, 1, -1, 1, -1]
    y_dir = [0, 0, -1, 1, 1, -1, -1, 1]

    for k in range(len(x_dir)):
        x = i + x_dir[k]
        y = j + y_dir[k]

        if 0 <= x < len(graph) and 0 <= y < len(graph[x]) and graph[x][y] == search_string[0] and not visited[x][y]:
            if dfs(graph, visited, search_string[1:], x, y):
                return True

    visited[i][j] = False
    return False














def takeInput():
    #To take fast I/O
    n,m=list(map(int,stdin.readline().strip().split( )))
    arr = [stdin.readline().strip() for i in range(n)]
    return arr,n,m




# Main 
arr,n,m=takeInput()
print(solve(arr,n,m)) 