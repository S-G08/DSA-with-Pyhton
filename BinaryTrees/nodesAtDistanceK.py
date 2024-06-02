import queue
class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def takeLevelWiseInput():
    q=queue.Queue()
    print("Enter root data")
    rootdata=int(input())
    if(rootdata == -1):
        return None
    root=BinaryTree(rootdata)
    q.put(root)
    while (not(q.empty())):
        current_node=q.get()
        print("Enter left child of ",current_node.data)
        leftnode_data=int(input())
        if(leftnode_data!=-1):
            leftnode=BinaryTree(leftnode_data)
            current_node.left=leftnode
            q.put(leftnode)
        
        print("Enter right child of ",current_node.data)
        rightnode_data=int(input())
        if(rightnode_data!=-1):
            rightnode=BinaryTree(rightnode_data)
            current_node.right=rightnode
            q.put(rightnode)
    return root

def nodesAtDistanceKHelper(root, target, k) :
    if root is None :
        return -1


    if root.data == target :
        nodesAtDistanceKDown(root, k)
        return 0


    leftD = nodesAtDistanceKHelper(root.left, target, k)
    if leftD != -1 :
        if (leftD + 1) == k :
            print(root.data)
        else :
            nodesAtDistanceKDown(root.right, k - leftD - 2)
    

        return 1 + leftD


    rightD = nodesAtDistanceKHelper(root.right, target, k);
    if rightD != -1 :
        if (rightD + 1) == k :
            print(root.data)
        else :
            nodesAtDistanceKDown(root.left, k - rightD - 2)


        return 1 + rightD

    return -1


def nodesAtDistanceKDown(root, k) :
    if root is None : 
        return

    if k == 0 :
        print(root.data)
        return

    
    nodesAtDistanceKDown(root.left, k - 1)
    nodesAtDistanceKDown(root.right, k - 1)


def nodesAtDistanceK(root, node, k) :
    nodesAtDistanceKHelper(root, node, k)

root=takeLevelWiseInput()
nodesAtDistanceK(root,3,1)