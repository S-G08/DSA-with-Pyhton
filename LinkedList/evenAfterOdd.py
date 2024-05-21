# For a given singly linked list of integers, arrange the nodes such that all the even number nodes are placed after the all odd number nodes. The relative order of the odd and even terms should remain unchanged.

# Note :
# 1. No need to print the linked list, it has already been taken care. Only return the new head to the list.
# 2. Don't create a new linked list.
# 3.  Just change the data, instead rearrange the provided list.

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
def evenAfterOdd(head):
    if head is None:
        return
    fh=head
    prev=None
    curr=head
    end=head
    #get last node
    while end.next != None:
        end=end.next
    fe=end

    #consider all even nodes before getting the first odd node
    while (curr.data%2==0 and curr != end):
        fe.next=curr
        curr=curr.next
        fe.next.next=None
        fe=fe.next
    #if odd node
    if (curr.data%2 !=0):
        head=curr  
        #curr = first odd node
        while curr != end:
            if(curr.data%2 != 0):  #if odd hten go to next node
                prev=curr
                curr=curr.next
            else:             # if even move it to last
                prev.next=curr.next
                curr.next=None
                fe.next=curr
                fe=curr
                curr=prev.next
    else:
        prev = curr
    
    if(fe != end and end.data %2 ==0):
        prev.next = end.next
        end.next = None
        fe.next=end
    return head

head=takeInput()
printll(head)
head=evenAfterOdd(head)
printll(head)


     