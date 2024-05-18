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

def appendLastNtoFirst(head,n):
    if n==0 or n>=length(head):
         return head
    count=0
    lenh=length(head)
    curr=head
    prev=None
    tail=head
    while count< lenh - n:
        count+=1
        prev=curr
        curr=curr.next
    temp=head
    while head.next is not None:
         head=head.next
    tail=head
    
    head=curr
    tail.next=temp
    prev.next=None

    return head
head=takeInput()
printll(head)
head=appendLastNtoFirst(head,5)
printll(head)