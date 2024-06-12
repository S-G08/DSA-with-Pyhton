from sys import stdin
import sys 
sys.setrecursionlimit(10**7)


def ceilIndex(dp, l, r, key): 
  
    while (r - l > 1): 
      
        m = l + (r - l)//2
        if (dp[m] >= key): 
            r = m 
        else: 
            l = m 
    return r 

def longestIncreasingSubsequence(arr, n) :

    # Creating dp list of size n + 1
    dp = [0 for i in range(n + 1)] 

   
    dp[0] = arr[0] 
    # As Subsequence of length 1 is always considered
    len = 1
    for i in range(1, n): 
      
        if (arr[i] < dp[0]): 
  
            # new smallest value 
            dp[0] = arr[i] 
   
        elif (arr[i] > dp[len-1]): 
  
            # arr[i] wants to extend 
            # largest subsequence 
            dp[len] = arr[i] 
            len+= 1
   
        else: 
            # arr[i] wants to be current 
            # end candidate of an existing 
            # subsequence. It will replace 
            # ceil value in tailTable 
            dp[ceilIndex(dp, -1, len-1, arr[i])] = arr[i] 
          
   
    return len



#taking inpit using fast I/O
def takeInput() :
    n = int(input())

    if n==0 :
        return list(), n
        
    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(longestIncreasingSubsequence(arr, n))