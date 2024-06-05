from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans
def maxSumNodeHelper(root,resNode,maxSum):
    if root==None:
        return 
    currsum=root.data
    count=len(root.children)
    for i in range(0,count):
        currsum+=root.children[i].data
        resNode,maxSum=maxSumNodeHelper(root.children[i],resNode,maxSum)
    if currsum>maxSum:
        resNode=root
        maxSum=currsum
    return resNode,maxSum
    
def maxSumNode(tree):
    resNode,maxSum=treeNode(None),0
    resNode,maxSum=maxSumNodeHelper(tree,resNode,maxSum)
    return resNode,maxSum


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

# Main
arr = list(int(x) for x in stdin.readline().strip().split())
tree = createLevelWiseTree(arr)
temp, tempSum = maxSumNode(tree)
print(temp.data)