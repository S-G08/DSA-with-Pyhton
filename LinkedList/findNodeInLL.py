# You have been given a singly linked list of integers. Write a function that returns the index/position of integer data denoted by 'N' (if it exists). Return -1 otherwise.
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
def takeInput():
        inputList = [int(ele) for ele in input().split()]
        
        head=None
        tail=None
        for currData in inputList:
            if currData==-1:
                break
             
            new_node=Node(currData)
            if head==None:
                head=new_node
                tail=new_node
            else:
                tail.next=new_node
                tail=new_node
        return head
def printll(head):
    while head != None:
          print(head.data," ->",end=' ')
          head=head.next
    print("None")

def findNode(head,n):
    count=0
    if head is None:
         return -1
    while head.next is not None:
        if head.data==n:
            return count
        count+=1
        head=head.next
    if (head.data==n):
         return count
    return -1

head=takeInput()
print(findNode(head,5))
         