class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


    def insert(self, value):
        """Recursive implementation of inserting an element"""
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


    def contains(self, value):
        """Recursive implementation of checking if the BST contains a specific element"""
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
    

    def preorderTraversal(self):
        """Preorder traversal of a BST using recursion. Recall that preorder 
           traversal prints root node, left child, then right child"""

        print(self.data)
        if self.left is not None:
            self.left.preorderTraversal()
        if self.right is not None:
            self.right.preorderTraversal()
    

    def postorderTraversal(self):
        """Postorder traversal of a BST using recursion. Recall that inorder 
           traversal prints left child, right child, then root node"""

        if self.left is not None:
            self.left.postorderTraversal()
        if self.right is not None:
            self.right.postorderTraversal()
        print(self.data)
    

    def inorderTraversal(self):
        """Inorder traversal of a BST using recursion. Recall that inorder 
           traversal prints left child, then root, then right child"""

        if self.left is not None:
            self.left.inorderTraversal()
        print(self.data)
        if self.right is not None:
            self.right.inorderTraversal()

    
    def inorderTraversalIterative(self, node):
        """Inorder traversal of a BST done iteratively"""

        stack = []
        while node is not None or len(stack) != 0:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.data)
                node = node.right


if __name__ == "__main__":

    node = Node(10)
    for value in [5, 15, 8, 17, 2]:
        node.insert(value)

    print(f"Inorder traversal of binary search tree using recursion:")
    node.inorderTraversal()

    print(f"Inorder traversal of BST implemented iteratively:")
    node.inorderTraversalIterative(node)

    print(f"Preorder traversal")
    node.preorderTraversal()

    print(f"Postorder traversal")
    node.postorderTraversal()
