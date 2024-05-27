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

def removeLeafNodes(root):
    if root == None:
        return
    if root.left == None and root.right==None:
        return None
    root.left=removeLeafNodes(root.left)
    root.right=removeLeafNodes(root.right)
    return root

root=treeInput()
printTree(root)
root=removeLeafNodes(root)
printTree(root)