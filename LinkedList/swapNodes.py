# You have been given a singly linked list of integers along with two integers, 'i,' and 'j.' Swap the nodes that are present at the 'i-th' and 'j-th' positions and return the new head to the list.


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
def swapNodes(head,i,j):
    if head == None:
        return
    if i==j:
        return head
    
    curr=head
    curr1=head
    prev=None
    prev1=None
    count=0
    while count<i:
        prev=curr
        curr=curr.next
        count+=1
    count1=0
    while count1<j:
        prev1=curr1
        curr1=curr1.next
        count1+=1
    
    if prev!=None:
        prev.next=curr1
    else:
        head=curr1
    
    if prev1!=None:
        prev1.next=curr
    else:
        head=curr

    temp=curr.next
    curr.next=curr1.next
    curr1.next=temp
    return head


head=takeInput()
printll(head)
head=swapNodes(head,0,3)
printll(head)















