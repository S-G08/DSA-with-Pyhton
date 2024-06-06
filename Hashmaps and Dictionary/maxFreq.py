def maxfreq(arr):
    freq=dict()
    for ele in arr:
        if not freq.get(ele,None):
            freq[ele]=1
        else:
            freq[ele]+=1
    max=0
    maxitem=0
    print(freq)
    for item in freq:
        if freq[item]>max:
            max=freq[item]
            maxitem=item
    return(maxitem)

arr=[int(x) for x in input().split() ]
print(maxfreq(arr))