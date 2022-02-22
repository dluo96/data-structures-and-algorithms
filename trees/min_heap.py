class MinHeap():
    def __init__(self, items) -> None:
        self.items = items
        self.size = len(self.items)
    
    # Methods for getting indexes
    def getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1

    def getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2

    def getParentIndex(self, childIndex):
        return (childIndex - 1)//2

    # Methods for checking existence 
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    # Methods for returning actual values
    def leftChild(self, index):
        return self.items[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.items[self.getRightChildIndex(index)]

    def parent(self, index):
        return self.items[self.getParentIndex(index)]

    # Method for swapping the value in two nodes given their indexes
    def swap(self, indexOne, indexTwo):
        temp = self.items[indexOne]
        self.items[indexOne] = self.items[indexTwo]
        self.items[indexTwo] = temp

    # Method which returns the minimum element (root node element) of the min heap
    def peek(self):
        if self.size == 0:
            raise Exception
        return self.items[0]
    
    # Method which removes the root node element
    def poll(self):
        if self.size == 0:
            raise Exception
        item = self.items[0]
        self.items[0] = self.items[self.size-1] # Move last element to root node
        self.items = self.items[:-1] # Shrink the array (remove last element)
        self.size -= 1 # Update the size of items
        self.heapifyDown()
        return item

    # Method which inserts an element
    def add(self, item):
        self.items.append(item)
        self.size += 1 # Increse size by 1 since you've added a new element
        self.heapifyUp()

    # Restore heap order after insertion of a new element
    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.parent(index) > self.items[index]:
            self.swap(index, self.getParentIndex(index))
            index = self.getParentIndex(index)
    
    # Restore heap order after removing the root node element
    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index): # If no left child, then no right child

            # Determine which child node has the smallest value - that is the one to swap with
            smallerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.getRightChildIndex(index)

            # If smaller than both children -> heap is restored
            if self.items[index] < self.items[smallerChildIndex]:
                break # Terminates current loop
            else: 
                self.swap(index, smallerChildIndex)
                index = smallerChildIndex


if __name__ == "__main__": 

    heap_a = MinHeap(items=[3,4,8,9,5,10,9,15,20,13,7])
    print(f"Heap A before removing the root node element: {heap_a.items}")
    heap_a.poll()
    print(f"Heap A after removing the root node element: {heap_a.items}")

    heap_b = MinHeap(items=[3,4,8,9,5,10,9,15,20,13,7])
    print(f"Heap B before inserting a new element: {heap_b.items}")
    heap_b.add(6)
    print(f"Heap B after inserting a new element: {heap_b.items}")