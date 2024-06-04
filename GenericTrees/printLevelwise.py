import queue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()
def printLevelwise(root):
    if(root==None):
        print(-1)
    q=[]
    q.append(root)
    while(len(q)!=0):
        count=len(q)
        while count>0:
            curr=q[0]
            q.pop(0)
            print(curr.data,end=":")
            for i in range(len(curr.children)):
                if i<len(curr.children)-1:
                    print(curr.children[i].data,end=',')
                else:
                    print(curr.children[i].data,end='')
            for i in range(len(curr.children)):
                q.append(curr.children[i])
            
            count-=1
            print()

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
root=takeInputLevelwise()
printLevelwise(root)