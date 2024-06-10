def fibRec(n):
    if n==0 or n==1:
        return n
    elif mem[n] != -1:
        return mem[n]
    mem[n]=fibRec(n-1) + fibRec(n-2)
    return mem[n]

def fibIte(n):
    # dp=[-1]*(n+1)
    # dp[0]=0
    # dp[1]=1
    # for i in range(2,n+1):
    #     dp[i]=dp[i-1]+dp[i-2]
    # return dp[n]
    ## Space optimizing code
    a=0
    b=1
    c=0
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    return c

n=int(input())
mem=[-1] * (n+1)
print("Recursively:",fibRec(n))
print("Iteratively:",fibIte(n))