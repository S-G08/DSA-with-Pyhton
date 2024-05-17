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


def lenRecursively(head):
    if head == None:
        return 0
    if head.next == None:
        return 1
    return 1+lenRecursively(head.next)
     
a=takeInput()

print(lenRecursively(a))