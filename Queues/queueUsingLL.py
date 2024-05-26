class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__count=0

    def enqueue(self,data):
        new_node=Node(data)
        if self.__head==None:
            self.__head=new_node
            self.__tail=new_node
            self.__tail.next=None
        self.__tail.next=new_node
        self.__tail=new_node
        self.__tail.next=None
        self.__count+=1
    def dequeue(self):
        if self.__count == 0:
            return -1
        element=self.__head.data
        self.__head=self.__head.next
        self.__count-=1
        return element
    def front(self):
        if self.__count ==0:
            return -1
        return self.__head.data
    def size(self):
        return self.__count
    def isEmpty(self):
        return self.size() == 0
    
q=Queue()
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
q.enqueue(13)
q.enqueue(14)
q.enqueue(15)
print(q.front())
print(q.size())
print(q.dequeue())
print(q.front())
print(q.size())