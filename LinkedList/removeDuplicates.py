# You have been given a singly linked list of integers where the elements are sorted in ascending order. Write a function that removes the consecutive duplicate values such that the given list only contains unique elements and returns the head to the updated list.

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
def removeDuplicates(head):
    if head == None:
        return
    curr=head.next
    temp=head
 
    while head.next != None:
        if head.data == curr.data:
            head.next=curr.next
            curr=curr.next
        else:
            head=head.next
            curr=curr.next
            
    head=temp
    return head   

head=takeInput()
printll(head)
head=removeDuplicates(head)
printll(head)