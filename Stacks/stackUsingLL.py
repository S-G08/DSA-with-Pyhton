class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None

class Stack :

    #Define data members and __init__()
    def __init__(self):
        self.__head=None
        self.__count=0

    '''----------------- Public Functions of Stack -----------------'''
    
    def getSize(self) :
        return self.__count
    def isEmpty(self) :
        return self.getSize()==0
    def push(self, data) :
        #Implement the push(element) function
        new_node=Node(data)
        new_node.next=self.__head
        self.__head=new_node
        self.__count+=1
    def pop(self) :
        if self.isEmpty() is True:
            return -1
        data=self.__head.data
        self.__head= self.__head.next
        self.__count-=1
        return data
    def top(self) :
        if self.isEmpty() is True:
            return -1
        return self.__head.data
        

s=Stack()
s.push(10)
s.push(11)
print(s.getSize())