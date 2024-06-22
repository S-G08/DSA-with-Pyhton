from sys import stdin
import sys
sys.setrecursionlimit(10 ** 8)
def DFS(arr, visited, n, sv):
    visited[sv] = 1

    for i in range(n):
        if i == sv:
            continue
        if arr[sv][i] == 1 and visited[i] == 0:
            DFS(arr, visited, n, i)

def solve(n, m, u, v):
    arr = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(m):
        arr[u[i] - 1][v[i] - 1] = 1
        arr[v[i] - 1][u[i] - 1] = 1

    visited = [0 for _ in range(n)]

    count = 0
    for i in range(n):
        if visited[i] == 0:
            count += 1
            DFS(arr, visited, n, i)

    return count

if __name__ == "__main__":
    li = stdin.readline().strip().split()
    V = int(li[0])
    E = int(li[1])
    u=[]
    v=[]
    for i in range(E):
        li = stdin.readline().strip().split()
        u.append(int(li[0]))
        v.append(int(li[1])) 
    
    print(solve(V, E, u, v))