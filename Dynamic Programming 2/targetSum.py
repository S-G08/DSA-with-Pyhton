from typing import List
dp=[]
def find_total_ways(arr, i, s, target, total_sum):
    global dp
    if s == target and i == len(arr):
        return 1
    if i >= len(arr):
        return 0
    if dp[i][s + total_sum] != -1:
        return dp[i][s + total_sum]
    dp[i][s + total_sum] = find_total_ways(arr, i + 1, s + arr[i], target, total_sum) + \
                          find_total_ways(arr, i + 1, s - arr[i], target, total_sum)
     
    return dp[i][s + total_sum]
def targetSum(arr: List[int], target: int) -> int:
    global dp
    total_sum = sum(arr)
    dp = [[-1] * (2 * total_sum + 1) for _ in range(len(arr))]
    return find_total_ways(arr, 0, 0, target, total_sum)

arr=[1,2,3,1]
t=3
print(targetSum(arr,t))