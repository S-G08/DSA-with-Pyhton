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

def printll(head):
    while head != None:
          print(head.data,end=' ')
          head=head.next
    print("None")

def merge_in_between(list1, a, b, list2):
    head = None
    last = None
    i = 1
    t = list1
    while t:
        if i == a:
            head = t
        if i == b + 1:
            last = t.next
            break
        t = t.next
        i += 1
    head.next = list2
    while head.next:
        head = head.next
    head.next = last
    return list1

list1=takeInput()
li=[int(ele) for ele in input().split()]
a=li[0]
b=li[1]
list2=takeInput()
ans=merge_in_between(list1,a,b,list2)
printll(ans)

