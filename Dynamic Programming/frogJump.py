from os import *
from sys import *
from collections import *
from math import *

from typing import *

dp=[]

def frogJumpHelper(n,heights,N):
    # n=current stair
    # N=last stair
    global dp
    if n==N:
        return 0
    elif n==N-1:
        return abs(heights[N-1]-heights[N-2])
    if dp[n]!=-1:
        return dp[n]
    else:
        dp[n]= min(frogJumpHelper(n+1,heights,N)+abs(heights[n-1]-heights[n]),
                   frogJumpHelper(n+2,heights,N)+abs(heights[n-1]-heights[n+1]))
        return dp[n]
    
def frogJump(n: int, heights: List[int]) -> int:
    global dp
    dp=[-1]*(n+1)

    # Recursive way
    # return frogJumpHelper(1,heights,n)

    #Iterative Way
    # dp[i]=min ( dp[i+1]+abs(heights[i]-heights[i+1]), 
    #            dp[i+2]+abs(heights[i]-heights[i+2]) )
    dp[n]=0
    dp[n-1]=abs(heights[n-1]-heights[n-2])
    for i in range(n-2,0,-1):
        dp[i]=min(dp[i+1]+abs(heights[i-1]-heights[i]),dp[i+2]+abs(heights[i-1]-heights[i+1]))
    return dp[1]
ar=[10,20,30,10]
n=4
print(frogJump(n,ar))