# You have been given an integer array/list(ARR) and a number 'num'. Find and return the total number of pairs in the array/list which sum to 'num'.
def pairSum(arr,n,target_sum):
   
    count = 0  # Initialize count of pairs
    
    # Create a dictionary to store the frequency of each element
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    print(frequency)
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

ar=[1,3,6,2,5,4,3,2,4]
sum=7
print(pairSum(ar,len(ar),sum))