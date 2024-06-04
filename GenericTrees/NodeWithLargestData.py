class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()
def printTree(root):
    #not base case but edge case
    if root==None:
        return
    # #1st way
    # print(root.data)
    # for child in root.children:
    #     printTree(child)

    #2nd way
    print(root.data,end=':')
    for child in root.children:
        print(child.data,end=",")
    print()
    for child in root.children:
        printTree(child)
def takeTreeInput():
    print("enter root data")
    rootdata=int(input())
    if rootdata==-1:
        return None
    root=TreeNode(rootdata)
    print("Enter number of children for ",rootdata)
    childrenCount=int(input())
    for i in range(childrenCount):
        child=takeTreeInput()
        root.children.append(child)
    return root
max=None
def maxDataNode(tree):
    global max
    if tree==None:
        return None
    if max==None:
        max=tree
    if tree.data>max.data:
        max=tree
    for child in tree.children:
        maxDataNode(child)
    return max
root=takeTreeInput()
print(maxDataNode(root).data)