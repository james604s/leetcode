"""
Binary Search 是一種在 已排序陣列 上非常高效的搜尋演算法。它透過每次「對半切割」來縮小搜尋範圍，時間複雜度是 O(log n)。

👇 操作流程
將搜尋區間設為 left = 0, right = n-1

計算中間索引 mid = (left + right) // 2

比較 arr[mid] 與 target

相等 ➜ 找到目標，回傳 mid

arr[mid] < target ➜ 搜尋右半部 (left = mid + 1)

arr[mid] > target ➜ 搜尋左半部 (right = mid - 1)

"""


# 迭代實作
# 無遞迴限制，適用大規模資料
# 空間效率更佳（無 call stack）
def iterative_binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

# 遞迴實作
# 寫法更簡潔
# 適合教學或理解遞迴流程


def recursive_binary_search(arr, target, left, right):
    if left > right:
        return -1  # Target not found

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)

arr = [1, 3, 5, 7, 9, 11, 13, 15]

# Test case 1: Iterative Binary Search
iterative_result = iterative_binary_search(arr, 7)
print("Iterative Binary Search for 7:", iterative_result)  # Should print index 3

# Test case 2: Recursive Binary Search
recursive_result = recursive_binary_search(arr, 7, 0, len(arr) - 1)
print("Recursive Binary Search for 7:", recursive_result)  # Should print index 3

# Test case 3: Target not found
iterative_not_found = iterative_binary_search(arr, 4)
recursive_not_found = recursive_binary_search(arr, 4, 0, len(arr) - 1)
print("Iterative Binary Search for 4:", iterative_not_found)  # Should print -1
print("Recursive Binary Search for 4:", recursive_not_found)  # Should print -1