isHeap=True

def isleaf(node):
    if not node.left and not node.right:
        return True
    
    return False

def check(node):
    global isHeap
    if isleaf(node):
        return node.data
    
    if not node.left:
        isHeap=False
        return node.data
    
    if node.left and not node.right and not isleaf(node.left):
        isHeap = False
        return node.data
    
    maxleft=check(node.left)
    maxright=node.data
    if node.right:
        maxright=check(node.right)

    maxim=max(maxleft,maxright,node.data)
    if maxim==node.data:
        return node.data
    else:
        isHeap=False
        return maxim 



def isBinaryHeapTree(root):
    global isHeap
    isHeap=True
    check(root)
    return isHeap