class Heap:

    def __init__(self, capacity):
        self.array = []
        self.capacity = capacity
        self.size = 0


    def getSize(self):
        return len(self.array)

    def insert(self, newElem):
        # @todo check number? Check capacity
        if (len(self.array) == self.capacity - 1):
            # @assert error
            return
        self.array.append(newElem)
        newElemIdx = self.size
        self.size += 1
        self.heapify(newElemIdx)


    def heapify(self, newElemIdx):
        if newElemIdx == 0:
            return
        parentIdx = self.getParentIdx(newElemIdx)
        parent = self.array[parentIdx]
        newElem = self.array[newElemIdx]
        if (newElem <= parent):
            tmp = parent
            self.array[parentIdx] = newElem
            self.array[newElemIdx] = parent
            self.heapify(parentIdx)
        

    def getLeftChild(self, index):
        assert(index < self.capacity)

    def getRightChild(self, index):
        assert(index < self.capacity)
        
    def getParentIdx(self, index):
        assert(index > 0 and index < self.capacity)
        return index / 2

    def printHeap(self):
        print self.array



myHeap = Heap(100)
myHeap.insert(10)
myHeap.printHeap()
myHeap.insert(15)
myHeap.printHeap()
myHeap.insert(18)
myHeap.printHeap()
myHeap.insert(5)
myHeap.printHeap()
myHeap.insert(20)
myHeap.printHeap()
