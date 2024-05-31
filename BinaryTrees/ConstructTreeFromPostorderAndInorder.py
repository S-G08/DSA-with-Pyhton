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
def buildTree(postOrder, inOrder, n=0) :
    if(len(postOrder)==0):
        return None
    rootdata=postOrder[len(postOrder)-1]
    root=BinaryTree(rootdata)
    count=-1
    for i in range(len(inOrder)):
        if(inOrder[i]==rootdata):
            count=i
            break
    leftIn=inOrder[0:count]
    rightIn=inOrder[count+1:]
    len1=len(leftIn)
    leftPost=postOrder[0:len1]
    rightPost=postOrder[len1:len(postOrder)-1]
    lefttree=buildTree(leftPost,leftIn)
    righttree=buildTree(rightPost,rightIn)
    root.left=lefttree
    root.right=righttree
    return root

postOrder=[4,5,2,6,7,3,1]
inOrder=[4,2,5,1,6,3,7]
root=buildTree(postOrder,inOrder,7)
printLevelWise(root)