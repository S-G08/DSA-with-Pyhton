def reverseQueue(inputQueue) :
    # Your code goes here
    if (inputQueue.qsize()<1):
        return 
    fr=inputQueue.get()
    
    reverseQueue(inputQueue)
    inputQueue.put(fr)
