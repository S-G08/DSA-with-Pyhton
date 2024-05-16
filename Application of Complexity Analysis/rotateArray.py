# You have been given a random integer array/list(ARR) of size N. Write a function that rotates the given array/list by D elements(towards the left).
def rotateArray(arr,n,d):
    #slicing array
    arr[:]=arr[d:n]+arr[0:d]
    return arr


arr=[1,2,3,4,5,6,7]
d=2
rotateArray(arr,len(arr),d)
print(arr)