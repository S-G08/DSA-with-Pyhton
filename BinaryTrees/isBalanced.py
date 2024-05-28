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
def height(root):
    if root == None:
        return 0 
    return (1+max(height(root.left),height(root.right)))

def isBalanced(root):
    if root == None:
        return True
    lh=height(root.left)
    rh=height(root.right)
    if (lh-rh>1 or rh-lh>1):
        return False
    leftbalanced=isBalanced(root.left)
    rightbalanced=isBalanced(root.right)
    if leftbalanced and rightbalanced:
        return True
    else:
        return False

root=treeInput()
print(isBalanced(root))