import sys

def solve(graph, n):
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == True:
                for k in range(n):
                    if k != i and graph[k][j] == True and graph[i][k] == True:
                        count += 1
    return count // 6

def take_input():
    n, m = map(int, input().split())
    graphs = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        first_vertex, second_vertex = map(int, input().split())
        graphs[first_vertex][second_vertex] = True
        graphs[second_vertex][first_vertex] = True
    return graphs

if __name__ == "__main__":
    graphs = take_input()
    ans = solve(graphs, len(graphs))
    print(ans)