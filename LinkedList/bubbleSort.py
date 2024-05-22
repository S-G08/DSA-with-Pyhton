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
def swap(x,y):
    temp = y.data
    y.data = x.data
    x.data = temp
def bubbleSort(head):
    swapped = True

    while swapped:
        swapped = False
        current = head

        while current.next:
            if current.data > current.next.data:
                swap(current, current.next)
                swapped = True
            current = current.next
    return head

head=takeInput()
printll(head)
head=bubbleSort(head)
printll(head)