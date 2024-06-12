from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

dp=[]
def count(coins, sum, n):
    global dp
    if (sum == 0):
        dp[n][sum] = 1
        return dp[n][sum]

    if (n == 0 or sum < 0):
        return 0

    if (dp[n][sum] != -1):
        return dp[n][sum]

    dp[n][sum] = count(coins, sum - coins[n - 1], n) + \
        count(coins, sum, n - 1)
 
    return dp[n][sum]
def countWaysToMakeChange(denominations, value) :
    global dp
    n=len(denominations)
    dp=[[-1 for i in range(value+1)]for j in range(n+1)]
    return count(denominations,value,n)

#main
ar=[5,3,2]
v=1
print(countWaysToMakeChange(ar,v))