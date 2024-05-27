class Dequeue:
    def __init__(self):
        self.items=[]
    def insertFront(self,item):
        print("trigger1",item)
        if (len(self.items)>10):
            print(-1)
            return
        self.items.insert(0,item)
        print(self.items[0])
    def insertRear(self,item):
        if (len(self.items)>10):
            print(-1)
            return
        self.items.append(item)
    def deleteFront(self):
        if (len(self.items)<1):
            print(-1)
            return
        self.items.pop(0)
    def deleteRear(self):
        if (len(self.items)<1):
            print(-1)
            return
        self.items.pop()
    def getFront(self):
        if (len(self.items)<1):
            print(-1)
            return
        print(self.items[0])
    def getRear(self):
        if (len(self.items)<1):
            print(-1)
            return
        return self.items[len(self.items)-1]


# d=Dequeue()
# input=[int(ele) for ele in input().split()]
# for n in input: 
#     if n==1:
#         d.insertFront(input[n+1])
#     elif n==2:
#         d.insertRear(input[n+1])
#     elif n==3:
#         d.deleteFront()
#     elif n==4:
#         d.deleteRear()
#     elif n==5:
#         d.getFront()
#     elif n==6:
#         d.getRear()