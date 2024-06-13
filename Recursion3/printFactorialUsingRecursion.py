def printFactorial(n,ans=1):
    if n==0:
        print(ans)
        return
    ans=ans*(n)
    printFactorial(n-1,ans)

printFactorial(5)