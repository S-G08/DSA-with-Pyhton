# For a given a singly linked list of integers and a position 'i', print the node data at the 'i-th' position.

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

def printIthNode(head,i):
     if head==-1 or head==None:
          return
     if i>=length(head):
          return
     for j in range(i):
          head=head.next
     print(head.data)

a=takeInput()
i=1
printIthNode(a,i)

