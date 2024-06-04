import queue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()
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
def containsX(root, x):
    if root==None:
        return False
    if root.data==x:
        return True
    for child in root.children:
        if containsX(child,x):
            return True
    return False

root=takeInputLevelwise()
print(containsX(root,9))
