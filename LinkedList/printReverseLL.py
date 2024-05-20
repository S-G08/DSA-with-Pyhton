# You have been given a singly linked list of integers. Write a function to print the list in a reverse order.

# To explain it further, you need to start printing the data from the tail and move towards the head of the list, printing the head data at the end.

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
def printreverse(head):
    if head == None:
        return head 
    printreverse(head.next)
    print(head.data,end=' ')
    
head=takeInput()
head=printreverse(head)

