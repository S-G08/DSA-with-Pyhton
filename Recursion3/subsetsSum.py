import sys
sys.setrecursionlimit(10 ** 8)

def subsetsSumKHelper(nums,target,index,current_subset,result):
    if (target == 0) :
        result.append(current_subset[:])
        return
    if index == len(nums) or target<0:
        return
    current_subset.append(nums[index])
    subsetsSumKHelper(nums,target-nums[index],index+1,current_subset,result)

    current_subset.pop()
    subsetsSumKHelper(nums,target,index+1,current_subset,result)
def subsetsSumK(arr, k) :
    result=[]
    subsetsSumKHelper(arr,k,0,[],result)
    return result

#taking input
def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


#printing the list of lists
def printListOfList(liOfLi) :
    for li in liOfLi :
        for elem in li :
            print(elem, end = " ")
        print()

#main
arr, n = takeInput()

if n != 0 :
    k = int(input().strip())
    liOfLi = subsetsSumK(arr, k)

    printListOfList(liOfLi)
