from os import *
from sys import *
from collections import *
from math import *

dp=[]
def helper(n,m,N, triangle):
    global dp 
    if n==N-1:
        return triangle[n][m] 
    
    if dp[n][m] != -1:
        return dp[n][m]
    
    dp[n][m] = min(helper(n+1,m,N,triangle), helper(n+1,m+1,N,triangle)) + triangle[n][m]
    return dp[n][m]
def minimumPathSum(triangle, n):
    global dp
    dp=[[-1 for i in range(n)] for i in range (n)]
    return helper(0,0,n,triangle)