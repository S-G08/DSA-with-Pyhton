# Given a singly linked list of integers, reverse the nodes of the linked list 'k' at a time and return its modified list.

#  'k' is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of 'k,' then left-out nodes, in the end, should be reversed as well.

# Example :
# Given this linked list: 1 -> 2 -> 3 -> 4 -> 5

# For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5

# For k = 3, you should return: 3 -> 2 -> 1 -> 5 -> 4

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
def kReverse(head, k):
    if head == None: 
        return None
    if k<2:
        return head
    curr = head 
    next = None
    prev = None
    count = 0
  
    while (curr is not None and count < k): 
        next = curr.next
        curr.next = prev 
        prev = curr 
        curr = next
        count += 1

    if next is not None: 
        head.next = kReverse(next, k) 
      
    return prev

head=takeInput()
printll(head)
head=kReverse(head,0)
printll(head)