from os import *
from sys import *
from collections import *
from math import *

def getCount(currStep, nStairs, dp, mod) -> int:
    if currStep >= nStairs:
        return currStep == nStairs

    if dp[currStep] != -1:
        return dp[currStep]

    a = getCount(currStep + 1, nStairs, dp, mod)
    b = getCount(currStep + 2, nStairs, dp, mod)

    dp[currStep] = (a + b) % mod
    return dp[currStep]

def countDistinctWays(nStairs: int) -> int:
    #  Write your code here.
    mod = 1000000007
    dp = [-1 for _ in range(nStairs)]
    ways = getCount(0, nStairs, dp, mod)
    return int(ways)