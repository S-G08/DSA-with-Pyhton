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


def insertAtIRecursively(head,i,data):
    if i<0:
         return head
    if i==0:
         new_node=Node(data)
         new_node.next=head
         return new_node
    if head==None:
         return None
    
    smallhead=insertAtIRecursively(head.next, i-1, data)
    head.next=smallhead
    return head
  
head=takeInput()
printll(head)
head=insertAtIRecursively(head,1,3)
printll(head)
head=insertAtIRecursively(head,0,7)
printll(head)
