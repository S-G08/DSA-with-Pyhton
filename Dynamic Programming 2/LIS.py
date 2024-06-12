from sys import stdin
import sys 
sys.setrecursionlimit(10**7)

dp=[]
def longestIncreasingSubsequence(arr, n) :
    global dp
    dp=[-1 for i in range(n)]
    for i in range(n-1,-1,-1):
        dp[i]=1
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                dp[i]=max(dp[i],dp[j]+1)
    ans=dp[0]
    for i in range(1,n):
        ans=max(ans,dp[i])
    return ans