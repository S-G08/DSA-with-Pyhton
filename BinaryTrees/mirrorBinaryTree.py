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
def printTree(root):
    if root == None:
        return
    print(root.data,end=":")
    if root.left != None:
        print("L",root.left.data,end=",")
    if root.right != None:
        print("R",root.right.data,end='')
    print()
    printTree(root.left)
    printTree(root.right)
def mirrorBinaryTree(root) :
    if root==None:
        return
    temp=mirrorBinaryTree(root.right)
    root.right=mirrorBinaryTree(root.left)
    root.left=temp
    return root
root=treeInput()
printTree(root)
root=mirrorBinaryTree(root)
printTree(root)