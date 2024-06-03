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
def findPathBST(root,data):
    if root==None:
        return None
    if root.data==data:
        l=[]
        l.append(root.data)
        return l
    
    lefttree=findPathBST(root.left,data)
    if lefttree!=None:
        lefttree.append(root.data)
        return lefttree
    
    righttree=findPathBST(root.right,data)
    if righttree!=None:
        righttree.append(root.data)
        return righttree
    else:
        return None
    
root=takeLevelWiseInput()
ar=findPathBST(root,2)
print(ar)