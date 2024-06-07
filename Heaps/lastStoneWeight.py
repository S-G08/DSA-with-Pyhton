from sys import stdin
import sys
import heapq
sys.setrecursionlimit(10**7) 
def weightOfLastStone(stones, n) :
    heap=[]
    for stone in stones:
        heapq.heappush(heap,-stone)
    while len(heap)>=2:
        x1 = heapq.heappop(heap)
        x2 = heapq.heappop(heap)
        if x1 != x2:
            heapq.heappush(heap,(x1-x2))
    return -heap[-1] if heap else 0
    

    
#taking inpit using fast I/O
def takeInput() :
    n=int(input())

    stones=list(map(int, input().strip().split(" ")))

    return stones, n

#main
stones, n  = takeInput()
print(weightOfLastStone(stones, n))
