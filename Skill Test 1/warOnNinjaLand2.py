import queue
from sys import stdin

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    if levelOrder==-1:
        return None
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
def search(root, num, level_order_map):
    if root is not None:
        if root.data == num:
            levelOrderStoredInMap(root.left, 1, level_order_map)
            levelOrderStoredInMap(root.right, 1, level_order_map)
            return 1
        k = search(root.left, num, level_order_map)
        if k > 0:
            storeRootAtK(root, k, level_order_map)
            levelOrderStoredInMap(root.right, k + 1, level_order_map)
            return k + 1
        k = search(root.right, num, level_order_map)
        if k > 0:
            storeRootAtK(root, k, level_order_map)
            levelOrderStoredInMap(root.left, k + 1, level_order_map)
            return k + 1
    return -1

def levelOrderStoredInMap(root, k, level_order_map):
    if root is not None:
        storeRootAtK(root, k, level_order_map)
        levelOrderStoredInMap(root.left, k + 1, level_order_map)
        levelOrderStoredInMap(root.right, k + 1, level_order_map)

def storeRootAtK(root, k, level_order_map):
    if k in level_order_map:
        level_order_map[k].add(root.data)
    else:
        level_order_map[k] = set([root.data])

def bomb(root, target):
    level_order_map = {}
    search(root, target, level_order_map)

    print(target)
    for level in level_order_map:
        for val in level_order_map[level]:
            print(val, end=" ")
        print()

root=takeInput()
if root is None:
    print()
else:
    k=int(input())
    bomb(root,k)