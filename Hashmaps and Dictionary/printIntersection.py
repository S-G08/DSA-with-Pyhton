
from sys import stdin



def printIntersection(arr1, n1, arr2, n2) :
    count_dict = {}
    for num in arr1:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # Find the intersection of the two arrays and print the elements
    for num in arr2:
        if num in count_dict and count_dict[num] > 0:
            print(num)
            count_dict[num] -= 1
    # write your code here !!!! 



    


#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n




#Main Code   
arr1, n1 = takeInput()
arr2, n2 = takeInput()
printIntersection(arr1, n1, arr2, n2)