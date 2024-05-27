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

#approach1 
def printKdepth1(root,k):
    if root == None:
        return 
    if k == 0:
        print(root.data)
        return
    printKdepth1(root.left,k-1)
    printKdepth1(root.right,k-1)

#approach2
def printKdepth2(root,k,d=0):
    if root == None:
        return 
    if k == d:
        print(root.data)
        return
    printKdepth2(root.left,k,d+1)
    printKdepth2(root.right,k,d+1)


root=treeInput()
printKdepth1(root,2)
printKdepth2(root,2)