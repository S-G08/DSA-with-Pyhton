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
def numLeafNodes(root):
    if root == None:
        return 0
    if root.left ==None and root.right==None:
        return 1
    leftnum=numLeafNodes(root.left)
    rightnum=numLeafNodes(root.right)
    return leftnum + rightnum

root=treeInput()
print(numLeafNodes(root))
