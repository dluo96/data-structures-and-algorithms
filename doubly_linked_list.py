class DoublyLinkedList():
    def __init__(self) -> None:
        self.size = 0
        self.head = None
        self.tail = None
    
    def __str__(self) -> str:
        output = 'Doubly Linked List: '
        trav = self.head
        while trav is not None:
            output += str(trav) + ' '
            trav = trav.next
        return output
    
    class Node():
        def __init__(self, data, prev, next) -> None:
            self.data = data
            self.prev = prev
            self.next = next
        
        def __str__(self) -> str:
            return str(self.data)

    # Empty the doubly linked list, O(n)
    def clear(self):
        trav = self.head
        while trav != None:
            next = trav.next
            trav.prev = None
            trav.next = None
            trav = next
        self.head = None
        self.tail = None
        trav = None
        self.size = 0
    
    def size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    # Add an element to the beginning of the linked list, O(1)
    def addFirst(self, elem):
        if self.isEmpty():
            self.head = self.Node(elem, None, None)
            self.tail = self.Node(elem, None, None)
        else:
            self.head.prev = self.Node(elem, None, self.head)
            self.head = self.head.prev
        self.size += 1

    # Add an element to the end of the linked list, O(1)
    def addLast(self, elem):
        if self.isEmpty():
            self.head = self.Node(elem, None, None)
            self.tail = self.Node(elem, None, None)
        else:
            self.tail.next = self.Node(elem, self.tail, None)
            self.tail = self.tail.next
        self.size += 1
    
    # Check the value of the first node if it exists, O(1)
    def peekFirst(self):
        if self.isEmpty():
            raise Exception("Linked list is empty")
        else:
            return self.head.data
    
    # Check the value of the last node if it exists, O(1)
    def peekLast(self):
        if self.isEmpty():
            raise Exception("Linked list is empty")
        else:
            return self.tail.data
    
    # Remove the first element (head) of the linked list, O(1)
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("Cannot remove element from an empty list")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1

        if self.isEmpty():
            self.tail = None # If the list is empty, set the tail to None too
        else:
            self.head.prev = None # Memory clean of previous node if in C/C++

        return data # Return the data at the node that was just removed

    # Remove the last element (tail) of the linked list, O(1)
    def removeLast(self):
        if self.isEmpty():
            raise Exception("Cannot remove element from an empty list")
        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1

        if self.isEmpty():
            self.head = None
        else:
            self.tail.next = None

        return data # Return the data at he node that was just removed

    # Remove an arbitrary node from the linked list, O(1)
    def removeNode(self, node):
        # If the node is the head or the tail, handle these independently
        if node.prev is None:
            return self.removeFirst()
        if node.next is None:
            return self.removeLast()
        
        # Adjust the pointers to skip over the node to be removed
        node.next.prev = node.prev
        node.prev.next = node.next

        # Store the value of the node we are removing
        data = node.data

        # Memory cleanup (more relevant for C/C++)
        node.data = None
        node.prev = None
        node.next = None
        node = None

        self.size -= 1

        return data

    # Remove a particular value the linked list, O(n)
    def removeGivenValue(self, value):
        trav = self.head
        while trav is not None:
            if trav.data == value:
                self.removeNode(trav)
                return True
            trav = trav.next
        return False

    def indexOf(self, value):
        index = 0
        trav = self.head
        while trav is not None:
            if trav.data == value:
                return index
            index += 1
            trav = trav.next
        return -1
    
    def contains(self, value):
        return self.indexOf(value) != -1


if __name__ == "__main__":

    dll = DoublyLinkedList()
    dll.addFirst(7)
    dll.addFirst(3)
    dll.addFirst(-5)
    dll.addFirst(10)
    print(dll)
    print(f"Tail of the doubly linked list: {dll.tail.data}")
    print(f"Head of the doubly linked list: {dll.head.data}")
    print(f"Size of the doubly linked list: {dll.size}")

    dll.removeGivenValue(3)
    print(f"Index of the element 3 is: {dll.indexOf(3)}")

    print(f"Index of the element 10 is: {dll.indexOf(10)}")
    print(f"Index of the element -5 is: {dll.indexOf(-5)}")
    print(f"Index of the element 7 is: {dll.indexOf(7)}")
