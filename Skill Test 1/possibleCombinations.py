
def printCombination(arr, n):
    r=12
    data = [0]*r
    combinationUtil(arr, data, 0,n - 1, 0)

def combinationUtil(arr, data, start, end, index):
    r=12
    if (index == r):
        for j in range(r):
            print(data[j], end = " ")
        print()
        return
    i = start
    while(i <= end and end - i + 1 >= r - index):
        data[index] = arr[i]
        combinationUtil(arr, data, i + 1,end, index + 1)
        i += 1

# Driver Code
n=int(input())
arr=[int(ele) for ele in input().split()]
printCombination(arr, n)


