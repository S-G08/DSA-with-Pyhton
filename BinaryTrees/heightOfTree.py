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
def height(root):
    if root == None:
        return 0
    leftheight=height(root.left)
    rightheight=height(root.right)
    return (1 + max(leftheight,rightheight))

root=treeInput()
print(height(root))