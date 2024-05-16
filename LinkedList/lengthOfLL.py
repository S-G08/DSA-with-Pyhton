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

a=takeInput()

print(length(a))