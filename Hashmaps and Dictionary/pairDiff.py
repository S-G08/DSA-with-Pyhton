#3
#5 1 2 4

def printPairDiffK(l, k):
    pairCount = 0
    m = {}
    for num in l:
        if num+k in m:
            pairCount += m[num+k]
        if k!=0 and num-k in m:
            pairCount += m[num-k]

        # Update map        
        if num in m:
            m[num] += 1
        else:
            m[num] = 1
            
    return pairCount
    

ar=[int(x) for x in input().split()]
print(printPairDiffK(ar,0))