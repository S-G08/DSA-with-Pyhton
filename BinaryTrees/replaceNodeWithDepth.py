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
def changeToDepthTree(root,d=0) :
    if root == None:
        return
    root.data=d
    left=changeToDepthTree(root.left,d+1)
    right=changeToDepthTree(root.right,d+1)
    return root

root=treeInput()
printTree(root)
root=changeToDepthTree(root)
printTree(root)

    