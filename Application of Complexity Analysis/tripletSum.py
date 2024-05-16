# You have been given a random integer array/list(ARR) and a number X. Find and return the triplet(s) in the array/list which sum to X.

def tripletSum(arr, n, sum):
    arr.sort()
    triplet_count=0
    for i in range(n):
        pair_sum=sum-arr[i]
        pair_count=pairSum(arr[i+1:],n-1,pair_sum)
        triplet_count+=pair_count
    return triplet_count

def pairSum(arr,n,target_sum):
   
    count = 0  # Initialize count of pairs
    
    # Create a dictionary to store the frequency of each element
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    # Iterate through the array and check if complement exists in the dictionary
    for num in arr:
        complement = target_sum - num
        if complement in frequency:
            count += frequency[complement]  # Increment count by the frequency of complement
        
        # If the complement is equal to the current number, decrement count by 1
        if complement == num:
            count -= 1
    
    # Divide count by 2 as each pair is counted twice
    return count // 2


arr=[1,2,3,4,5,6,7]
sum=15
print(tripletSum(arr,len(arr),sum))