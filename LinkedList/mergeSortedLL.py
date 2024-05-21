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
def merge(head1,head2):
    if head1==None:
        return head2
    if head2==None:
        return head1
    if head1.data<=head2.data:
        fh=head1
        ft=head1
        head1=head1.next
    else:
        fh=head2
        ft=head2
        head2=head2.next

    while head1 != None and head2 != None:
        if head1.data<head2.data:
            ft.next=head1
            ft=ft.next
            head1=head1.next  
            
        elif head1.data>=head2.data:
            ft.next=head2
            ft=ft.next
            head2=head2.next

    if head1!=None:
        ft.next=head1
        head1=head1.next
    elif head2!=None:
        ft.next=head2
        head2=head2.next
            
    return fh        


head1=takeInput()
head2=takeInput()
fh=merge(head1,head2)
printll(fh)