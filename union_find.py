class UnionFind():
    """Array-based implementation of the union-find DS"""

    def __init__(self, size : int) -> None:

        # The number of elements in this union-find DS
        self.size = size
        if self.size <= 0:
            raise ValueError("Size <= 0 is not allowed")

        # Used to track the size of each group
        self.sz = [None] * self.size

        # id[i] points to the parent of i. If id[i] = i, then i is a root node
        self.id = [None] * self.size
        
        # Number of groups in the union-find DS
        # Initially the number of groups is the number of elements
        self.numGroups = size 

        # Construct the array
        for i in range(0, self.size):
            self.id[i] = i # Link the node to itself (self-root)
            self.sz[i] = 1 # Each group is originally of size 1
            i += 1
        
    
    def find(self, p : int):
        """Find which group the element p belongs to. Takes amortized constant time."""

        # Find the root of the group
        root = p
        while root != self.id[root]:
            root = self.id[root]
        
        # Path compression: compress the path leading back to the root
        # This results in amortized constant time complexity
        # We do it iteratively (but could also have done it recursively)
        while p != root:
            next = self.id[p]
            self.id[p] = root
            p = next
        
        return root
    

    def connected(self, p : int, q : int):
        """Return whether the elements p and q are in the same group"""
        return self.find(p) == self.find(q)
    

    def groupSize(self, p : int):
        """Return the size of the group that p belongs to"""
        return self.sz[self.find(p)]
    

    def unify(self, p : int, q : int):
        """Merge the group containing the element p with the group containing q"""
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            print(f"Elements {p} and {q} already belong to the same group")
            return

        # Merge two groups (merge the smaller group into the larger group)
        if self.sz[root_p] < self.sz[root_q]:
            self.sz[root_q] += self.sz[root_p]
            self.id[root_p] = root_q
        else:
            self.sz[root_p] += self.sz[root_q]
            self.id[root_q] = root_p
        
        # Since the root nodes were different, we know
        # that the number of groups has decreased by 1
        self.numGroups -= 1

if __name__ == "__main__":

    uf = UnionFind(10)

    