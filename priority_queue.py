import heapq


class PriorityQueue:
    """Implementation of a priority queue using heapq"""
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1] # Index [1] is to get the item and not the priority

    def __str__(self):
        return str(self.elements)


if __name__ == "__main__":
    
    pq = PriorityQueue()
    print(pq)
    print(pq.is_empty())

    # item, priority
    pq.put("eat", 5)
    pq.put("code", 1)
    pq.put("sleep", 3)
    pq.put("train", 4)
    pq.put("breath", 0)
    pq.put("walk", 2)

    print(pq) 
    # Returns [(0, 'breath'), (1, 'code'), (2, 'walk'), (5, 'eat'), (4, 'train'), (3, 'sleep')]
    # The only thing that can be guaranteed about the order of the removed elements is that
    # the item removed each time was of the highest priority

    print(pq.get()) # breath
    print(pq.get()) # code
    print(pq.get()) # walk
    print(pq.get()) # sleep
    print(pq.get()) # train
    print(pq.get()) # eat

    print(pq) # Returns [], i.e. an empty list