#Create a stack using array
class Stack:
    def __init__(self):
        self.__data=[]
    def push(self,item):
        self.__data.append(item)
    def pop(self):
        if self.isEmpty():
            print("Empty Stack")
        return self.__data.pop()
    def top(self):
        if self.isEmpty():
            print("Empty Stack")
        return self.__data[self.size()-1]
    def size(self):
        return len(self.__data)   
    def isEmpty(self):
        return self.size()==0

s=Stack()
s.push(10)
s.push(11)
s.push(12)
s.push(13)
s.push(14)
print(s.isEmpty())
