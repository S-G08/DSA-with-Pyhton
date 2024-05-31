import queue
class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def takeLevelWiseInput():
    q=queue.Queue()
    print("Enter root data")
    rootdata=int(input())
    if(rootdata == -1):
        return None
    root=BinaryTree(rootdata)
    q.put(root)
    while (not(q.empty())):
        current_node=q.get()
        print("Enter left child of ",current_node.data)
        leftnode_data=int(input())
        if(leftnode_data!=-1):
            leftnode=BinaryTree(leftnode_data)
            current_node.left=leftnode
            q.put(leftnode)
        
        print("Enter right child of ",current_node.data)
        rightnode_data=int(input())
        if(rightnode_data!=-1):
            rightnode=BinaryTree(rightnode_data)
            current_node.right=rightnode
            q.put(rightnode)
    return root
def printLevelWise(root):
    q=queue.Queue()
    q.put(root)
    while (not(q.empty())):
        current=q.get()
        print(current.data,end=':')
        if(current.left ==None):
            print("L:-1",end=',')
        else:
            print("L:",end='')
            print(current.left.data,end=',')
        if(current.right==None):
            print("R:-1",end="")       
        else:
            print("R:",end='')
            print(current.right.data,end="")
        print()
        if(current.left !=None):
            q.put(current.left)
        if(current.right!= None):
            q.put(current.right)
class Pair :

    def __init__(self, minimum, maximum) :
        self.minimum = minimum
        self.maximum = maximum
def getMinAndMax(root) :
    if root==None:
        return None
    min=root.data
    max=root.data
    q=queue.Queue()
    q.put(root)
    while (not(q.empty())):
        curr=q.get()
        if(curr.data>max):
            max=curr.data
        if(curr.data<min):
            min=curr.data
        if(curr.left!=None):
            q.put(curr.left)
        if(curr.right!=None):
            q.put(curr.right)
    p=Pair(min,max)
    return p

root=takeLevelWiseInput()
a=getMinAndMax(root)
print(a)
