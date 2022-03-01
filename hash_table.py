from linked_list import LinkedList

class HashTable():
    """Implementation of a hash table which uses chaining to resolve collisions"""
    def __init__(self) -> None:
        self.size = 30
        self.array = [None] * self.size

    def getHashCode(self, string):
        return hash(string)
    
    def convertToIndex(self, integer):
        return hash(integer) % self.size

    def put(self, key, value):
        hashCode = self.getHashCode(key)
        index = self.convertToIndex(hashCode)
        p = key, value
        if self.array[index] is None:
            self.array[index] = LinkedList()
        self.array[index].append(p)
        
    def __getitem__(self, key):
        hashCode = self.getHashCode(key)
        index = self.convertToIndex(hashCode)

        # Find the correct key-value pair in the linked list
        if self.array[index] is None:
            return None
        currentNode = self.array[index].head
        while currentNode is not None:
            if key == currentNode.data[0]:
                return currentNode.data
            currentNode = currentNode.nextNode


if __name__ == "__main__":

    ht = HashTable()

    ht.put('A', 1)
    ht.put('B', 2)
    ht.put('C', 3)
    ht.put('D', 4)
    ht.put('E', 5)
    ht.put('F', 6)
    ht.put('G', 7)
    ht.put('H', 8)
    ht.put('I', 9)
    ht.put('J', 10)
    ht.put('K', 11)
    ht.put('L', 12)

    for i in range(ht.size):
        if ht.array[i] is not None:
            print(f"{ht.array[i]} at index {i}")
    print("----------------------------")

    # Find an element using the key
    print("Find an element of the hash table using the key:")
    print(ht['A'])
    print(ht['C'])
    print(ht['Z']) # None
