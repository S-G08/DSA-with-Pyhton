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
def countNodesGreaterThanX(root, x) :
    if root == None:
        return 0
    leftcount=countNodesGreaterThanX(root.left,x)
    rightcount=countNodesGreaterThanX(root.right,x)
    if (root.data>x):
        return 1 + leftcount + rightcount
    else:
        return leftcount + rightcount

root=treeInput()
print(countNodesGreaterThanX(root, 3))