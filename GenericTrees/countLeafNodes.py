import queue
import sys
class treeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()
def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root
def leafNodeCount(root):
    count=0
    if root==None:
        return 0
    if root.children==[]:
        return 1
    for child in root.children:
        count+=leafNodeCount(child)
    return count
    





# Main
sys.setrecursionlimit(10**6)
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(leafNodeCount(tree))