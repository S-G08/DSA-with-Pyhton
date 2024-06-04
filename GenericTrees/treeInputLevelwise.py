import queue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()
def printTree(root):
    print(root.data,end=':')
    for child in root.children:
        print(child.data,end=",")
    print()
    for child in root.children:
        printTree(child)
def takeInputLevelwise():
    q=queue.Queue()
    rootdata=int(input())
    if rootdata==-1:
        return None
    root=TreeNode(rootdata)
    q.put(root)
    while (not(q.empty())):
        currentnode=q.get()
        numchildren=int(input())
        for i in range(numchildren):
            childdata=int(input())
            child=TreeNode(childdata)
            currentnode.children.append(child)
            q.put(child)
    return root
root=takeInputLevelwise()
printTree(root)