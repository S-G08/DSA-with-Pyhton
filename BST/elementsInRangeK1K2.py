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
def elementsInRangeK1K2(root,k1,k2):
    if root==None:
        return    
    if k1<root.data:
        elementsInRangeK1K2(root.left,k1,k2)
    if k1<=root.data and k2>=root.data:
        print(root.data,end=' ')
    elementsInRangeK1K2(root.right,k1,k2)
    

root=takeLevelWiseInput()
elementsInRangeK1K2(root,6,10)