# Given a singly linked list of integers, reverse it using recursion and return the head to the modified list. You have to do this in O(N) time complexity where N is the size of the linked list.

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
def reverseLL(head):
    # if head is None or head.next is None:
    #     return head,head
    # smallhead,smalltail=reverseLL(head.next)
    # smalltail.next=head
    # head.next=None
    # return smallhead,head

    #another approach
    if head is None or head.next is None:
        return head
    smallhead=reverseLL(head.next)
    tail=head.next
    tail.next=head
    head.next=None
    return smallhead
    
head=takeInput()
printll(head)
head=reverseLL(head)
printll(head)