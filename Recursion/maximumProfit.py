# You have made a smartphone app and want to set its subscription price such that the profit earned is maximised. There are certain users who will subscribe to your app only if their budget is greater than or equal to your price.
# You will be provided with a list of size N having budgets of subscribers and you need to return the maximum profit that you can earn.

# Lets say you decide that price of your app is Rs. x and there are N number of subscribers. So maximum profit you can earn is :
# m*x
# where m is total number of subscribers whose budget is greater than or equal to x.

def maximumProfit(arr):
    n = len(arr)
    arr.sort()

    max_profit = 0
    current_profit = 0

    for i in range(n):
        current_profit = arr[i] * (n - i)
        max_profit = max(max_profit, current_profit)

    return max_profit

n = int(input())
arr = [int(ele) for ele in input().split()]

ans = maximumProfit(arr)
print(ans)