"""
Description: Counter is a subclass of the dictionary in Python that helps count hashable objects. It is beneficial for counting the frequency of elements in an iterable.

Time Complexity:
- Access: O(1) - Accessing a specific element is O(1).
- Update: O(1) - Updating a count is O(1).
- Iteration: O(n) - Iterating through all elements is O(n).
"""


from collections import Counter, defaultdict, namedtuple, OrderedDict

# ✅ 非常適合處理文字頻率、投票統計、配對問題等。
c = Counter('banana')
print(c)         # Counter({'a': 3, 'n': 2, 'b': 1})
print(c['a'])    # 3
print(c.most_common(2))  # [('a', 3), ('n', 2)]

# Creating a Counter from a list
my_counter = Counter(['apple,' 'banana,' 'apple,' 'orange,' 'banana,' 'apple'])

print(my_counter)

# ✅ 避免 KeyError，常見於 group by、字典初始化。
from collections import defaultdict

dd = defaultdict(list)
dd['a'].append(1)
dd['b'].append(2)
print(dd)  # defaultdict(<class 'list'>, {'a': [1], 'b': [2]})

# ✅ 常用於表示不可變資料結構（比 class 較輕量）。
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # 1 2

