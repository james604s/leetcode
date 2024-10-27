from collections import deque
"""
https://docs.python.org/zh-tw/3/library/collections.html#collections.deque
"""

class RecentCounter:
    def __init__(self):
        """
        初始化計數器，最近請求數為零。
        """
        self.requests = deque()

    def ping(self, t: int) -> int:
        """
        在時間 t 添加新的請求，其中 t 表示以毫秒為單位的時間，並返回過去 3000 毫秒內發生的請求數（包括新請求）。
        具體來說，返回包含範圍 [t - 3000, t] 中發生的請求數。

        Args:
          t: 新請求的時間（以毫秒為單位）。

        Returns:
          過去 3000 毫秒內發生的請求數。
        """
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)

class MyDeque:
    def __init__(self):
        """
        初始化一個空的 deque。
        """
        self.items = []

    def append(self, item):
        """
        將一個項目添加到 deque 的右側。

        Args:
          item: 要添加的項目。
        """
        self.items.append(item)

    def popleft(self):
        """
        從 deque 的左側移除並返回一個項目。

        Returns:
          從 deque 中移除的項目。
        """
        return self.items.pop(0)

    def __len__(self):
        """
        返回 deque 中的項目數量。

        Returns:
          deque 中的項目數量。
        """
        return len(self.items)

### 自製 deque ###
class RecentCounter:
    def __init__(self):
        """
        初始化計數器，最近請求數為零。
        """
        self.requests = MyDeque()

    def ping(self, t: int) -> int:
        """
        在時間 t 添加新的請求，其中 t 表示以毫秒為單位的時間，並返回過去 3000 毫秒內發生的請求數（包括新請求）。
        具體來說，返回包含範圍 [t - 3000, t] 中發生的請求數。

        Args:
          t: 新請求的時間（以毫秒為單位）。

        Returns:
          過去 3000 毫秒內發生的請求數。
        """
        self.requests.append(t)
        while self.requests.items and self.requests.items[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)