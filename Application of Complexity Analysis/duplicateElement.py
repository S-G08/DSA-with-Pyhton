# You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). Each number is present at least once. That is, if N = 5, the array/list constitutes values ranging from 0 to 3, and among these, there is a single integer value that is present twice. You need to find and return that duplicate number present in the array.

def duplicate(ar,n):
    ar.sort()
    if n==2 and ar[0]==ar[1]:
        return ar[0]

    i=1
    while i<n-1:
        if ar[i]==ar[i-1] or ar[i]==ar[i+1]:
            return(ar[i])
        i+=1
ar=[3,2,3]
print(duplicate(ar,len(ar)))