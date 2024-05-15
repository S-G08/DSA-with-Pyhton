# You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].

# Now, in the given array/list, 'M' numbers are present twice and one number is present only once.

# You need to find and return that number which is unique in the array/list.

def unique(ar,n):
    ar.sort()
    if n==1:
        return ar[0]
    if ar[0]!=ar[1]:
        return ar[0]
    if ar[n-1]!=ar[n-2]:
        return ar[n-1]
    i=1
    while i<n-1:
        if ar[i]!=ar[i-1] and ar[i]!=ar[i+1]:
            return(ar[i])
        i+=1
ar=[1,3,1,3,6,6,7,10,7]
print(unique(ar,len(ar)))

    