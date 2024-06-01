# For a given Binary Tree of type integer and a number K, print out all root-to-leaf paths where the sum of all the node data along the path is equal to K.

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
def printLevelWise(root):
    q=queue.Queue()
    q.put(root)
    while (not(q.empty())):
        current=q.get()
        print(current.data,end=':')
        if(current.left ==None):
            print("L:-1",end=',')
        else:
            print("L:",end='')
            print(current.left.data,end=',')
        if(current.right==None):
            print("R:-1",end="")       
        else:
            print("R:",end='')
            print(current.right.data,end="")
        print()
        if(current.left !=None):
            q.put(current.left)
        if(current.right!= None):
            q.put(current.right)
def isLeaf(root):
    return (root.left==None and root.right==None)
def rootToLeafPaths(root,k,path):
    if root==None:
        return 
    path.append(root.data)
    if isLeaf(root):
        # print(list(path))
        sum=0
        for i in range(len(path)):
            sum+=path[i]
        if sum==k:
            for ele in path:
                print(ele,end=" ")
            print()
    rootToLeafPaths(root.left,k,path)
    rootToLeafPaths(root.right,k,path)
    path.pop()
def rootToLeafPathsSumToK(root, k):
    path=[]
    rootToLeafPaths(root,k,path)

root=takeLevelWiseInput()
rootToLeafPathsSumToK(root,13)
