## Read input as specified in the question.
## Print output as specified in the question.
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkCousins(root,a,b):
    if root == None:
        return False

    parA = None

    parB = None

    q = [] 

    tmp = BinaryTreeNode(-1) 

    q.append((root, tmp)) 
     
    while len(q) > 0:  
 
        levSize = len(q) 
        while levSize:  
 
            ele = q.pop(0) 

            if ele[0].data == a:  
                parA = ele[1] 
              
            if ele[0].data == b:  
                parB = ele[1] 

            if ele[0].left:  
                q.append((ele[0].left, ele[0])) 
              
            if ele[0].right:  
                q.append((ele[0].right, ele[0])) 
            levSize -= 1

            if parA and parB: 
                break

        if parA and parB:  
            return parA != parB 

        if (parA and not parB) or (parB and not parA): 
            return False
          
    return False

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
p = int(input())
q = int(input())
ans = checkCousins(root,p,q)
if ans== 1:
    print('true')
else:
    print('false')
