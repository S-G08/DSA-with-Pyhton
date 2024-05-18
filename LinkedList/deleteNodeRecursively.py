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
def delNodeR(head,i):
    if i<0:
         return head
    if i==0:
        head=head.next 
        return head
    if head.next is None:
         return head
    smallhead=delNodeR(head.next,i-1)
    head.next=smallhead
    return head
    
head=takeInput()
printll(head)
head=delNodeR(head,3)
printll(head)

