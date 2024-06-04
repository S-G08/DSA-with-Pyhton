class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def min1(self,root):
        if root==None:
            return 1000000
        if root.left==None:
            return root.data
        return self.min1(root.left)
    def printTreeHelper(self,root):   
        if root == None:
            return
        print(root.data,end=":")
        if root.left != None:
            print("L:",end="")
            print(root.left.data,end=',')
        if root.right != None:
            print("R:",end='')
            print(root.right.data,end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    
    def printTree(self):
        self.printTreeHelper(self.root)
    
    def searchHelper(self,root,data):
        if root==None:
            return False
        if root.data==data:
            return True
        if root.data>data:
            return self.searchHelper(root.left,data)
        else:
            return self.searchHelper(root.right,data)
    def search(self, data):
        return self.searchHelper(self.root,data)
        
    def insertHelper(self, root, data):    
        if root==None:
            node=BinaryTree(data)
            return node
            
        if root.data>=data:
            root.left=self.insertHelper(root.left,data)
            return root
        else:
            root.right=self.insertHelper(root.right,data)
            return root
    def insert(self, data):
        self.numNodes+=1
        self.root=self.insertHelper(self.root,data)

    def deleteHelper(self,root,data):
        if root==None:
            return False,None
        
        if root.data>data:
            deleted,newLeftNode=self.deleteHelper(root.left,data)
            root.left=newLeftNode
            return deleted,root
        if root.data<data:
            deleted,newRightNode=self.deleteHelper(root.right,data)
            root.right=newRightNode
            return deleted,root
        #root is leaf
        if root.left==None and root.right==None:
            return True,None
        #root has 1 child
        if root.left==None:
            return True,root.right
        if root.right==None:
            return True,root.left
        #root has 2 children
        replacement = self.min1(root.right)
        root.data=replacement
        deleted,newRightNode=self.deleteHelper(root.right,replacement)
        root.right=newRightNode
        return True,root

    def delete(self, data):
        deleted,newroot=self.deleteHelper(self.root,data)
        if deleted:
            self.numNodes-=1
        self.root=newroot
    def count(self):
        return self.numNodes
    
b=BST()

b.insert(2)
b.insert(3)
b.insert(1)
b.printTree()
b.delete(2)
b.printTree()
# b = BST()
# q = int(input())
# while (q > 0) :
#     li = [int(ele) for ele in input().strip().split()]
#     choice = li[0]
#     q-=1
#     if choice == 1:
#         data = li[1]
#         b.insert(data)
#     elif choice == 2:
#         data = li[1]
#         b.delete(data)
#     elif choice == 3:
#         data = li[1]
#         ans = b.search(data)
#         if ans is True:
#             print('true')
#         else:
#             print('false')
#     else:
#         b.printTree()