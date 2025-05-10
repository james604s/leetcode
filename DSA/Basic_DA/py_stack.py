"""
Description: A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. Elements are added and removed from the top.

Time Complexity:

Read: O(1) - Accessing the top element is O(1).
Write: O(1) - Pushing (adding) and popping (removing) elements are O(1).
"""

# Simple
stack = [1, 2, 3]
# Adding an element (push)
stack.append(4)  # stack = [1, 2, 3, 4]

# Removing an element (pop)
element = stack.pop()  # element = 4, stack = [1, 2, 3]
print(f'The popped element is {element} and the remaining stack is {stack}')

# Custom
class SimpleStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # 加入到尾端（頂部）

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()  # 從尾端取出（頂部）

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]  # 查看頂部元素但不移除

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

s = SimpleStack()
s.push(1)
s.push(2)
s.push(3)

print(s.items)

print(s.pop())   # 3
print(s.peek())  # 2
print(s.size())  # 2