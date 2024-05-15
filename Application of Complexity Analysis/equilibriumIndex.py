def equliIndex(ar):
    tsum=0
    for ele in ar:
        tsum+=ele
    lsum=0
    index=0

    while index<len(ar):
        rsum=tsum-ar[index]-lsum
        if rsum==lsum:
            return index
        lsum=lsum+ar[index]
        index+=1
    return -1

ar=[1,4,3,3,1,5,2,2]
print(equliIndex(ar))
