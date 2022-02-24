class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.nextNode = None
    
    def __str__(self) -> str:
        return self.data
    
class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        if self.head is None:
            head = Node(data)
            return 
        currentNode = self.head
        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = Node(data)
    
    def prepend(self, data):
        newHead = Node(data)
        newHead.nextNode = self.head
        self.head = newHead

    # Method that deletes the first node that has a particular value
    def deleteWithValue(self, data):
        if self.head is None:
            return
        if self.head.data == data: # If the node we want to delete is the head node
            self.head = self.head.nextNode
            return
        # In this case, the node is not explicitly destroyed, but no one can access it

        currentNode = self.head
        while currentNode.nextNode != None:
            if currentNode.nextNode.data == data:
                currentNode.nextNode = currentNode.nextNode.nextNode
                return 
            currentNode = currentNode.nextNode
    
    def __str__(self) -> str:
        output = ""
        currentNode = self.head
        while currentNode is not None:
            output += str(currentNode) + ' '
            currentNode = currentNode.nextNode
        return output


if __name__ == "__main__":
    
    ll = LinkedList()
    ll.head = Node("Monday")
    ll.head.nextNode = Node("Tuesday")
    ll.head.nextNode.nextNode = Node("Wednesday")
    ll.head.nextNode.nextNode.nextNode = Node("Thursday")
    print(f"Head of the linked list: {ll.head}")
    print(f"Elements of the linked list: {ll}")
    ll.deleteWithValue("Wednesday")
    print(f"Elements of the linked list after removing an element: {ll}")
    ll.append("Friday")
    print(f"Elements of the linked list after appending an element: {ll}")
    ll.prepend("Sunday")
    print(f"Elements of the linked list after prepending an element: {ll}")
    print(f"Head of the linked list after prepending an element: {ll.head}")
    ll.deleteWithValue("Friday")
    print(f"Elements of the linked list after deleting the last element: {ll}")

