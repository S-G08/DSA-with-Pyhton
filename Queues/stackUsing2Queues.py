import queue

class Stack :
    def __init__(self):
        self.q1=queue.Queue()
        self.q2=queue.Queue()

    def getSize(self) :
		
        return self.q1.qsize()


    def isEmpty(self) :
        return self.q1.empty()

    def push(self,data):
        self.q1.put(data)
        
        
    def pop(self):
        if self.q1.qsize()<1:
            return -1
        while self.q1.qsize()>1:
            self.q2.put(self.q1.get())
        ele1=self.q1.get()
        while self.q2.qsize()>0:
            self.q1.put(self.q2.get())
        return ele1
    def top(self):
        if self.q1.qsize()<1:
            return -1
        while self.q1.qsize()>1:
            self.q2.put(self.q1.get())
        ele1= self.q1.get()
        self.q2.put(ele1)
        while self.q2.qsize()>0:
            self.q1.put(self.q2.get())
        return ele1
        

s=Stack()
s.push(10)
s.push(11)
s.push(12)
print(s.top())
while s.isEmpty() is False:
    print(s.pop())

