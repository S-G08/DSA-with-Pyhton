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
def largest(root):
    if root == None:
        return -1
    leftlargest=largest(root.left)
    rightlargest=largest(root.right)
    return max(root.data,leftlargest,rightlargest)

root=treeInput()
print(largest(root))