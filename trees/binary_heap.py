#BinaryHeap() creates a new, empty, binary heap.
#insert(k) adds a new item to the heap.
#findMin() returns the item with the minimum key value, leaving item in the heap.
#delMin() returns the item with the minimum key value, removing the item from the heap.
#isEmpty() returns true if the heap is empty, false otherwise.
#size() returns the number of items in the heap.
#buildHeap(list) builds a new heap from a list of keys.

#notice structure is just a list
#new items get appended to list
#???
#Notice that we can compute the parent of any node by using simple integer division. 
#The parent of the current node can be computed by dividing the index of the current node by 2.

#it is imperative to remember that this implementation is done with a list data structure
#therefore we access nodes with the var i and there parents or childern by 
#writing i // 2 for parents and i * 2 or i * 2 + 1 for children

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

def percUp(self,i):
    while i // 2 > 0:
      if self.heapList[i] < self.heapList[i // 2]:
         tmp = self.heapList[i // 2]
         self.heapList[i // 2] = self.heapList[i]
         self.heapList[i] = tmp
      i = i // 2

def insert(self,k):
    self.heapList.append(k)
    self.currentSize = self.currentSize + 1
    self.percUp(self.currentSize)

#this is a helper function of percDown and then percDown with help delMin
def minChild(self,i):
    if i * 2 + 1 > self.currentSize:
        return i * 2
    else:
        if self.heapList[i*2] < self.heapList[i*2+1]:
            return i * 2
        else:
            return i * 2 + 1

def percDown(self,i):
    while (i * 2) <= self.currentSize:
        mc = self.minChild(i)
        if self.heapList[i] > self.heapList[mc]:
            tmp = self.heapList[i]
            self.heapList[i] = self.heapList[mc]
            self.heapList[mc] = tmp
        i = mc

def delMin(self):
    retval = self.heapList[1]
    self.heapList[1] = self.heapList[self.currentSize]
    self.currentSize = self.currentSize - 1
    self.heapList.pop()
    self.percDown(1)
    return retval

def buildHeap(self,alist):
    i = len(alist) // 2
    self.currentSize = len(alist)
    self.heapList = [0] + alist[:]
    while (i > 0):
        self.percDown(i)
        i = i - 1