from os import *
from sys import *
from collections import *
from math import *
from typing import List

def houseRobber(valueInHouse):
    if len(valueInHouse) == 1:
            return valueInHouse[0]
    if len(valueInHouse) == 2 or len(valueInHouse) == 3:
            return max(valueInHouse)
        
    def find(nums):
        n = len(nums)
        
        dp = [0] * n
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[2] + nums[0]
        
        for i in range(3, n):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        
       
        return max(dp[-1], dp[-2])
    
    return max(find(valueInHouse[1:]), find(valueInHouse[:-1]))

        


nums=[1,5,1,2,6]
print(houseRobber(nums))
