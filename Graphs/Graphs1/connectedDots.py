from sys import stdin
import sys

sys.setrecursionlimit(10 ** 8)

from typing import List


def solve(board: List[str], n: int, m: int) -> int:
        
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if has_cycle(board, -1, -1, i, j, visited) == 1:
                    return 1
    return 0

def has_cycle(board: List[str], from_x: int, from_y: int, i: int, j: int, visited: List[List[bool]]) -> int:
    if visited[i][j]:
        return 1

    x_dir = [1, 0, 0, -1]
    y_dir = [0, 1, -1, 0]
    visited[i][j] = True
    for l in range(len(x_dir)):
        x = x_dir[l] + i
        y = y_dir[l] + j
        if x == from_x and y == from_y:
            continue

        if 0 <= x < len(board) and 0 <= y < len(board[x]) and board[x][y] == board[i][j]:
            ans = has_cycle(board, i, j, x, y, visited)
            if ans == 1:
                return 1

    return 0









def takeInput():
    #To take fast I/O
    n,m=list(map(int,stdin.readline().strip().split( )))
    arr = [stdin.readline().strip() for i in range(n)]
    return arr,n,m




# Main 
arr,n,m = takeInput()

ans = solve(arr,n,m)

if(ans) :
    print('true')
else :
    print('false')