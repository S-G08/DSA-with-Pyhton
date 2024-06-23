import queue
from sys import stdin


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root


def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    if (root1 is not None and root2 is not None):
        if root1.data == root2.data:
            return (isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left))
    return False

def isSymmetric(root):
    return isMirror(root, root)

#main
root = takeInput()
print ("true" if isSymmetric(root) == True else "false")
