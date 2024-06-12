from typing import List


def findWays(arr: List[int], k: int) -> int:
    n=len(arr)
    mod=1000000007
    tab = [[0] * (k + 1) for i in range(n + 1)]
    
    for i in range(1, k + 1):
        tab[0][i] = 0
    for i in range(0,n+1):
        tab[i][0]=1
     
    for i in range(1, n+1):
        for j in range(k + 1):
            if arr[i-1] <= j:
                tab[i][j] = tab[i-1][j] + tab[i-1][j-arr[i-1]]
            else:
                tab[i][j] = tab[i-1][j]
    tab[n][k]%=mod
    return tab[n][k]

arr=[int(x) for x in input().split()]
print(findWays(arr,4))


