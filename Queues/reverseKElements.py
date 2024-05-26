import queue
from collections import deque

def printQueue(q):
    while q.qsize()>0:
        print(q.get())
def reverse(q):
    if q.qsize()<1:
        return
    fr=q.get()
    reverse(q)
    q.put(fr)
def reverseKElements(inputQueue, k) :
    q1=queue.Queue()
    count=0
    while count<k:
        ele=inputQueue.get()
        q1.put(ele)
        count+=1
    reverse(q1)
    q3=queue.Queue()
    while(q1.qsize()>0):  
        q3.put(q1.get())
    while(inputQueue.qsize()>0):
        q3.put(inputQueue.get())
    return q3


q1=queue.Queue()
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)
q1.put(5)
q1.put(6)
q1.put(7)
q1.put(8)
q1.put(9)
q1.put(10)
q2=reverseKElements(q1, 4)
while (q2.qsize()>0):
    print(q2.get())