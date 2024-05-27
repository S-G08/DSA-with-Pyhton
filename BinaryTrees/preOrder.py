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
def preOrder(root):
    if root==None:
        return 
    print(root.data,end=' ')
    preOrder(root.left)
    preOrder(root.right)

root=treeInput()
preOrder(root)