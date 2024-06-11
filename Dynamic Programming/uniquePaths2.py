# F(n,m)= F(n+1,m)+F(n,m+1)
#cell should be inside matrix and it should be valid

dp=[]

def isValid(n,m,mat):
    global dp
    N=len(mat)
    M=len(mat[0])
    if n<0 or n>=N or m<0 or m>=M or mat[n][m]==-1:
         return False
    return True

def count(n,m,N,M,mat):
    if n==N-1 and m==M-1:
        return 1
    if dp[n][m] != -1:
        return dp[n][m]
    mod=1000000007
    ans=0
    if isValid(n,m+1,mat):
        ans+=count(n,m+1,N,M,mat)
    if isValid(n+1,m,mat):
        ans+=count(n+1,m,N,M,mat)
    ans%=mod
    dp[n][m]=ans
    return ans

def mazeObstacles(n, m, mat):
    global dp
    dp=[[-1 for j in range(m)] for i in range(n)]

    # Recursive
    count(0,0,n,m,mat)
    return dp[0][0]

    
