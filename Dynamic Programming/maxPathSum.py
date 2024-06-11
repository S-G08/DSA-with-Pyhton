from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

dp=[]
def isValid(n,m,N,M):
    if n<0 or n>=N or m<0 or m>=M:
        return False
    return True
def helper(n,m,N,M,mat):
    global dp
    if n==N-1:
        return mat[n][m]
    if dp[n][m]!=float('-inf'):
        return dp[n][m]
    ans=helper(n+1,m,N,M,mat)
    if isValid(n+1,m-1,N,M):
        ans=max(ans, helper(n+1,m-1,N,M,mat))
    if isValid(n+1,m+1,N,M):
        ans=max(ans, helper(n+1,m+1,N,M,mat))
    
    ans+=mat[n][m]
    dp[n][m]=ans
    return ans 
def getMaxPathSum(matrix):
    global dp
    ans=float('-inf')
    n=len(matrix)
    m=len(matrix[0])
    dp=[[float('-inf') for i in range(m)] for i in range (n)]
    for i in range(m):
        ans=max(ans, helper(0,i,n,m,matrix))
    
    return ans 


    

