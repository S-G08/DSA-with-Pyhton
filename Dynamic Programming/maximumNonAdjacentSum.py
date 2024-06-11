from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def maximumNonAdjacentSum(nums):    
    N=len(nums)
    dp=[[0 for i in range(2)] for j in range(N)]
    if N==1:
        return nums[0]
    dp[0][0]=0
    dp[0][1]=nums[0]

    for i in range(1,N):
        dp[i][1]=dp[i-1][0]+nums[i]
        dp[i][0]=max(dp[i-1][1],dp[i-1][0])
    return max(dp[N - 1][0], dp[N - 1][1])

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1