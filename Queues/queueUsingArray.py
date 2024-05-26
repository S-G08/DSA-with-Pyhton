class Queue:

    def __init__(self):
        self.__ar=[]
        self.__count=0
        self.__front=0
    def enqueue(self,element):
        self.__ar.append(element)
        self.__count+=1
    
    def dequeue(self):
        if self.isEmpty():
            return -1
        element=self.__ar[self.__front]
        self.__front+=1
        self.__count-=1
        return element
    def size(self):
        return self.__count
    def isEmpty(self):
        return self.size()==0
    def front(self):
        if self.__count==0:
            return -1
        return self.__ar[self.__front]

q=Queue()
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
q.enqueue(13)
q.enqueue(14)
q.enqueue(15)
while q.isEmpty() is False:
    print(q.front())
    q.dequeue()
print(q.dequeue())