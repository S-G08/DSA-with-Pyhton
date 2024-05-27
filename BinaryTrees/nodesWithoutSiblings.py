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
def printNodesWithoutSibling(root) :
    if root==None:
        return 
    if (root.right!=None and root.left==None):
        print(root.right.data,end=' ')
    if (root.right==None and root.left!=None):
        print(root.left.data,end=' ')
    left=printNodesWithoutSibling(root.left)
    right=printNodesWithoutSibling(root.right)
root=treeInput()
printNodesWithoutSibling(root)