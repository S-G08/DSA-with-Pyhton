import heapq
def getFourthLargest(arr, n):
    x = heapq.nlargest(4, arr)  
    if len(x)<4:
        return -2147483648
    return x[3] 