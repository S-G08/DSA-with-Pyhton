class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def treeInput():
    rootInput=int(input())
    if rootInput == -1:
        return
    rootnode=BinaryTree(rootInput)
    leftnode=treeInput()
    rightnode=treeInput()
    rootnode.left=leftnode
    rootnode.right=rightnode
    return rootnode
def isNodePresent(root, x):
    if root == None:
        return False
    if root.data == x:  
        return True
    left=isNodePresent(root.left,x)
    if left==True:
        return True
    right=isNodePresent(root.right,x)
    return right
    

root=treeInput()
print(isNodePresent(root,1))