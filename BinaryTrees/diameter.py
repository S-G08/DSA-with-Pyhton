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

class height:
    def __init__(self):
        self.h=0
def diameter(root,h) :
    lh=height()
    rh=height()
    if root == None:
        height.h=0
        return 0
    ldm=diameter(root.left,lh)
    rdm=diameter(root.right,rh)
    h.h=max(lh.h,rh.h)+1
    return max(lh.h+rh.h+1,max(ldm,rdm))
def diameterOfBinaryTree(root):
    h=height()
    return diameter(root,h)

root=treeInput()
dia=diameterOfBinaryTree(root)
print(dia)