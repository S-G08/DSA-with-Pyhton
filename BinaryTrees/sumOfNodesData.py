class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
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
def sumOfNodes(root):
    if root == None:
        return 0
    leftsum=sumOfNodes(root.left)
    rightsum=sumOfNodes(root.right)
    return root.data + leftsum + rightsum

root=treeInput()
printTree(root)
print(sumOfNodes(root))