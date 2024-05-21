# Given a singly linked list of integers and an integer n, find and return the index for the first occurrence of 'n' in the linked list. -1 otherwise.

# Follow a recursive approach to solve this.
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
def length(head): 


    count=0
    while head!=None or head==-1:
          count+=1
          head=head.next
    return count
def printll(head):
    while head != None:
          print(head.data," ->",end=' ')
          head=head.next
    print("None")
def findNodeRec(head, n):
    if head is None:
        return -1
    if head.data == n:
        return 0
    count = findNodeRec(head.next, n)
    if count!=-1:
        return 1+count
    else:
        return -1

head=takeInput()
print(findNodeRec(head,3))