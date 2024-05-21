# You have been given a singly linked list of integers along with two integers, 'M,' and 'N.' Traverse the linked list such that you retain the 'M' nodes, then delete the next 'N' nodes. Continue the same until the end of the linked list. Indexing starts from 1.

# To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.

# Note :
# No need to print the list, it has already been taken care. Only return the new head to the list. You can return null in case where all nodes will be deleted.

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
def deleteNode(head,i):
    curr=head
    prev=None
    count=0
    while count<i:
        prev=curr
        curr=curr.next
        count+=1
    if prev is not None:
        prev.next=curr.next
    else:
        head=curr.next  
    return head 
def skipMdeleteN(head, M, N):
    prev = curr = head
    q = 0
    p = 0

    while curr:
      q += 1
      if q == M:
         for i in range(N):
            if curr.next is not None:
               curr = curr.next
         prev.next = curr.next
         q = 0

      prev = prev.next
      curr = curr.next

    return head
    
    
        
head=takeInput()
printll(head)
head=skipMdeleteN(head,2,3)
printll(head)