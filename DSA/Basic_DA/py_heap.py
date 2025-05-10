"""
Description: A heap is a specialized binary tree-based data structure that satisfies the heap property. 
In a max-heap, for any given node i, the value of i is greater than or equal to the values of its children. 
In a min-heap, the value of i is less than or equal to the values of its children. 
Heaps are commonly used to implement priority queues.

Time Complexity:
Read: O(1) 
  - Accessing the maximum or minimum element (the root) is fast because it is always at the top of the heap.
Write:
  - Insertion: O(log n) - Inserting a new element requires maintaining the heap property, which involves comparing and possibly swapping elements up the tree.
  - Deletion: O(log n) - Deleting the maximum or minimum element requires rebalancing the heap, typically involving a series of swaps down the tree.
情境	說明
Top-K 項目	最常見應用，保留前 K 小或大元素
排程器 / 任務優先順序	根據優先級執行任務，例如 A* 搜尋、CPU 模擬
模擬優先佇列	Dijkstra 演算法、Prim、Huffman 編碼等
Sliding Window 最小值	heap 維護動態範圍內最小 / 最大值
"""

import heapq

# by default, this is a min-heap. To get the max heap, multiply the number by -1 before inserting
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)

print(heapq.heappop(heap))  # 1
print(heapq.heappop(heap))  # 3

# Custom
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        self._swap(0, -1)
        val = self.heap.pop()
        self._sift_down(0)
        return val

    def peek(self):
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self._swap(idx, parent)
            self._sift_up(parent)

    def _sift_down(self, idx):
        child = 2 * idx + 1
        if child >= len(self.heap):
            return
        if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
            child += 1
        if self.heap[child] < self.heap[idx]:
            self._swap(child, idx)
            self._sift_down(child)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

h = MinHeap()
h.push(3)
h.push(1)
h.push(5)
print(h.pop())  # 1
print(h.pop())  # 3