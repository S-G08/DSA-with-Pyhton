from os import *
from sys import *
from collections import *
from math import *

ans=[]
def is_valid(row,col,arr,visited,n):
    if row<0 or row>= n or col<0 or col>= n or arr[row][col] == 0 or visited[row][col]:
        return False
    return True

def explore(row, col, arr, visited, n, pathTaken):
    global ans
    if arr[row][col]==0:
        return
    if row==n-1 and col==n-1:
        ans.append(pathTaken)
        return
    
    drow=[1,0,0,-1]
    dcol=[0,-1,1,0]
    dpath=["D","L","R","U"]

    for i in range(4):
        next_row=row+drow[i]
        next_col=col+dcol[i]

        if is_valid(next_row,next_col,arr,visited,n):
            visited[next_row][next_col]=True  
            pathTaken+=dpath[i]
            explore(next_row,next_col,arr,visited,n,pathTaken)

            #Backtrack
            visited[next_row][next_col]=False
            pathTaken=pathTaken[:-1]
      

def searchMaze(arr, n):
    global ans
    ans=[]
    visited=[[False for _ in range(n)]for _ in range(n)]
    visited[0][0]=True
    explore(0,0,arr,visited,n,"")
    return ans

def main():
    n = 2
 
    m = [
        [1, 1],
        [0, 1]
        
    ]
 
    
    result=searchMaze(m, n)
 
    if not result:
        print(-1)
    else:
        for path in result:
            print(path, end=" ")
        print()
 
 
if __name__ == "__main__":
    main()