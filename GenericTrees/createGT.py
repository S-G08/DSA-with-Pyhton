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
def numNodes(root):
    count=1
    for child in root.children:
        count+=numNodes(child)
    return count
# n1=TreeNode(1)
# n2=TreeNode(2)
# n3=TreeNode(3)
# n4=TreeNode(4)
# n5=TreeNode(5)
# n6=TreeNode(6)
# n7=TreeNode(7)

# n1.children.append(n2)
# n1.children.append(n3)
# n1.children.append(n4)
# n1.children.append(n5)

# n3.children.append(n6)
# n3.children.append(n7)
n1=takeTreeInput()
printTree(n1)
print(numNodes(n1))