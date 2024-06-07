from sys import maxsize 

class HeapNode: 
    def __init__(self, val, r, c): 
        self.val = val
        self.r = r 
        self.c = c 

def minHeapify(harr, i, heap_size): 
    l = i * 2 + 1
    r = i * 2 + 2
    if(l < heap_size and r<heap_size and harr[l].val < harr[i].val and harr[r].val < harr[i].val):
      temp= HeapNode(0,0,0)
      temp=harr[r]
      harr[r]=harr[i]
      harr[i]=harr[l]
      harr[l]=temp
      minHeapify(harr ,l,heap_size)
      minHeapify(harr ,r,heap_size)
    if (l < heap_size and harr[l].val < harr[i].val):
      temp= HeapNode(0,0,0)
      temp=harr[i]
      harr[i]=harr[l]
      harr[l]=temp
      minHeapify(harr ,l,heap_size)

def kMinFloor(mat, n, k): 
    if k < 0 or k > n * n: 
        return maxsize 
    harr = [0] * n 
    for i in range(n): 
        harr[i] = HeapNode(mat[0][i], 0, i) 
 
    hr = HeapNode(0, 0, 0) 
    for i in range(k): 

        hr = harr[0] 

        nextval = mat[hr.r + 1][hr.c] if (hr.r < n - 1) else maxsize 

        harr[0] = HeapNode(nextval, hr.r + 1, hr.c) 

        minHeapify(harr, 0, n) 

    return hr.val