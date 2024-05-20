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
def midPoint(head):
    if head is None:
         return 
    slow=head
    fast=head
    while fast.next != None and fast.next.next != None:
        slow=slow.next
        fast=fast.next.next
    return slow
head=takeInput()
printll(head)
mid=midPoint(head)
print(mid.data)