class Queue:
    # Stacks to be used in the operations.
    def __init__(self):
        self.stk1 = []
        self.stk2 = []
        self.__count=0
        

    # Enqueues 'X' into the queue. Returns true after enqueuing.
    def enqueue(self, X):
        self.stk1.append(X)
        return True
        
    """
      Dequeues top element from queue. Returns -1 if the queue is empty, 
      otherwise returns the popped element.
    """
    def dequeue(self):
        if len(self.stk1)<1:
            return -1
        while len(self.stk1)>1:
            ele=self.stk1.pop()
            self.stk2.append(ele)
        ele1=self.stk1.pop()
        while len(self.stk2)>0:
            ele=self.stk2.pop()
            self.stk1.append(ele)
        return ele1
    

q=Queue()
print(q.enqueue(10))
print(q.dequeue())