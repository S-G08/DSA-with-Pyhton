dp=[]
def minimumElementsUtil(arr, ind, T):
    global dp
    if ind == 0:
        if T % arr[0] == 0:
            return T // arr[0]
        else:
            return int(1e9)

    if dp[ind][T] != -1:
        return dp[ind][T]
    notTaken = 0 + minimumElementsUtil(arr, ind - 1, T)
    taken = int(1e9)

    if arr[ind] <= T:
        taken = 1 + minimumElementsUtil(arr, ind, T - arr[ind])

    dp[ind][T] = min(notTaken, taken)
    return dp[ind][T]

def minimumElements(arr, T):
    global dp
    n = len(arr)
    dp = [[-1 for j in range(T + 1)] for i in range(n)]
    ans = minimumElementsUtil(arr, n - 1, T)
    if ans >= int(1e9):
        return -1
    return ans

#main
arr = [2,1]
T = 11
print(minimumElements(arr, T))



