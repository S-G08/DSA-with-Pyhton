
def printminArray(arr,overallmin=10000000):
    if len(arr)==0:
        print(overallmin)
        return
    minele=min(overallmin,arr[0])
    printminArray(arr[1:],minele)

ar=[1,2,3,4,3,5]
printminArray(ar)



