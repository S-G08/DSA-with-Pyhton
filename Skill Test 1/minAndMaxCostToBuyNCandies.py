def minimumCost(cost, n, k):
    res = 0
    i = 0
    while(i<n):
        res += cost[i] 
        n = n-k 
        i += 1
    return res 

def maximumCost(cost, n, k):
    res = 0
    index = 0
    i = n-1
    while(i >= index):
        res += cost[i]
        index += k 
        i -= 1
    return res

arr = [9,8,2,6,4] 
n = len(arr) 
k = 2
  
arr.sort() 
  
# Function call 
print(minimumCost(arr, n, k),maximumCost(arr, n, k)) 
    
    