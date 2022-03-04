from collections import deque


class Queue:
    """Implementation of a queue using using collections.deque"""
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items
        # return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q)
    print(q.is_empty())
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(f"Queue after adding three elements: {q}")
    print(f"Element removed by dequeue: {q.dequeue()}")
    print(f"Element removed by dequeue: {q.dequeue()}")
    print(f"Queue after dequeuing twice: {q}")
    print(f"Size of queue: {q.size()}")
    print(f"Next element that dequeue will remove: {q.peek()}")
