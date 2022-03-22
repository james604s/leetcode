# class RecentCounter(object):
#     def __init__(self):
#         self.L = []

#     def ping(self, t):
#         """
#         :type t: int
#         :rtype: int
#         """
#         self.L.append(t)
#         while self.L[0] < t -3000:
#             self.L.pop(0)
#         return len(self.L)

import collections
class RecentCounter:
    """
    找出最近的3000毫秒內有多少個呼叫請求。
    每個呼叫請求是ping(t)函式，
    其中t是請求的時間，可以保證每次ping的引數t是大於前面的。
    """
    def __init__(self):
        self.que = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.que and self.que[0] < t - 3000:
            self.que.popleft()
        self.que.append(t)
        return len(self.que)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)