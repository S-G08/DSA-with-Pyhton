# Given a large number represented in the form of a linked list. Write code to increment the number by 1 in-place(i.e. without using extra space).
# Sample Input 1 :
# 3 9 2 5 -1
# Sample Output 1 :
# 3 9 2 6
# Sample Input 2 :
# 9 9 9 -1
# Sample Output 1 :
# 1 0 0 0 

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

def reverseLLIter(head):
    curr=head
    prev=None
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
    
    return head
def nextNumber(head):
    head=reverseLLIter(head)
    k = head
    carry = 0
    prev = None
    head.data += 1

    while(head != None) and (head.data > 9 or carry > 0):
        prev = head
        head.data += carry
        carry = head.data // 10
        head.data = head.data % 10
        head = head.next
    
    if carry > 0:
        prev.next = Node(carry)
    # Reverse the modified list
    return reverseLLIter(k)

head=takeInput()
printll(head)
head=nextNumber(head)
printll(head)