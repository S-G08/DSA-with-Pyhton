from os import *
from sys import *
from collections import *
from math import *
dp=[]
def lps(s1, s2, n1, n2):
    global dp
    if (n1 == 0 or n2 == 0):
        return 0

    if (dp[n1][n2] != -1):
        return dp[n1][n2]

    if (s1[n1 - 1] == s2[n2 - 1]):
        dp[n1][n2] = 1 + lps(s1, s2, n1 - 1, n2 - 1)
        return dp[n1][n2]
    else:
        dp[n1][n2] = max(lps(s1, s2, n1 - 1, n2), lps(s1, s2, n1, n2 - 1))
        return dp[n1][n2]
def longestPalindromeSubsequence(s):
    global dp
    dp=[[-1 for i in range(1001)]for j in range(1001)]
    n=len(s)
    s2=s
    s2=s2[::-1]
    return lps(s2,s,n,n)

