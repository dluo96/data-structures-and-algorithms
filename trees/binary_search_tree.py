class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    # Recursive implementation of inserting an element
    def insert(self, value):
        if value <= self.data:
            if self.left == None: 
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    # Recursive implementation of checking if the BST contains a specific element
    def contains(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left == None:
                return False
            else:
                self.left.contains(value)
        else:
            if self.right == None:
                return False
            else:
                self.right.contains(value)

    # Inorder traversal to print all the nodes in the BST
    def traversalInOrder(self):
        # Recall that inorder traversal prints left child, then root, then right child
        if self.left != None:
            self.left.traversalInOrder()

        print(self.data)

        if self.right != None:
            self.right.traversalInOrder()


if __name__ == "__main__":
    node = Node(10)
    for value in [5, 15, 8, 17, 2]:
        node.insert(value)
    node.traversalInOrder()
