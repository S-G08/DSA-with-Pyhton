# You have been given a linked list of integers. Your task is to write a function that deletes a node from a given position, 'POS'.

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
def deleteNode(head,i):
    if i<0 or i>length(head)-1:
        return head
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

head=takeInput()
printll(head)
head=deleteNode(head,5)
printll(head)