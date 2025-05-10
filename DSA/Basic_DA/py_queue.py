"""
Description: A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. Elements are added at the rear and removed from the front.

Time Complexity:

Read: O(1) - Accessing the front element is O(1) if using deque.
Write: O(1) - Enqueuing (adding) and dequeuing (removing) operations are O(1) with deque.

"""

# Libray Version
from collections import deque

queue = deque([1, 2, 3])
# Adding an element
queue.append(4)  # queue = deque([1, 2, 3, 4])
print(queue)

# Removing an element
element = queue.popleft()  # element = 1, queue = deque([2, 3, 4])
print(f'The popped element is {element} and the remaining queue is {queue}')

# Custom Version
class SimpleQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # 加入到尾端

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)  # 從頭部取出

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


q = SimpleQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  # 10
print(q.peek())     # 20
print(q.size())     # 2