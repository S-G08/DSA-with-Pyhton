from os import *
from sys import *
from collections import *
from math import *
import sys

def maximumProduct(arr, n):
    ans = -sys.maxsize - 1  # Initialize the answer to the minimum possible value
    product = 1
 
    for i in range(n):
        product *= arr[i]
        ans = max(ans, product)  # Update the answer with the maximum of the current answer and product
        if arr[i] == 0:
            product = 1  # Reset the product to 1 if the current element is 0
 
    product = 1
 
    for i in range(n - 1, -1, -1):
        product *= arr[i]
        ans = max(ans, product)
        if arr[i] == 0:
            product = 1
 
    return ans