from os import *
from sys import *
from collections import *
from math import *


"""
F(n,k)=F(n-1,k-a[n]) || F(n-1,k)
"""
dp=[]
visited=[]
def f(n,k,arr):
    global dp,visited
    if k==0:
        return True
    elif n==0:
        return False 
    elif visited[n][k]:
        return dp[n][k]
    visited[n][k]=True
    if (k-arr[n-1])>=0:
        dp[n][k]= f(n-1,k-arr[n-1],arr) | f(n-1, k,arr)
    else:
        dp[n][k]=f(n-1,k,arr )
    return dp[n][k]

def subsetSumToK(n, k, arr):
    global dp,visited
    dp=[[False for j in range(k+1)] for i in range(n+1)]
    visited=[[False for j in range(k+1)]for i in range (n+1)]
    return f(n,k,arr)
    
    

