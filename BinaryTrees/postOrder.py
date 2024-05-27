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
def postOrder(root):
    if root==None:
        return 
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=' ')

root=treeInput()
postOrder(root)