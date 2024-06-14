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
    for ele in result:
        print(*ele,end=" ")
        print()


#main

n=int(input())
arr=[int(i) for i in input().split()]
sum=int(input())
subsetsSumK(arr,sum)