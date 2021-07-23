"""
输入：arr = [3,3,3,3,5,5,5,2,2,7]
输出：2
解释：选择 {3,7} 使得结果数组为 [5,5,5,2,2]、长度为 5（原数组长度的一半）。
大小为 2 的可行集合有 {3,5},{3,2},{5,2}。
选择 {2,7} 是不可行的，它的结果数组为 [3,3,3,3,5,5,5]，新数组长度大于原数组的二分之一。
"""
import time

#explan 1
import collections
class Solution:
    def minSetSize(self, arr):
        #dict計算各有幾個
        cnt = collections.Counter(arr)
        print(1, cnt)
        f = list(cnt.values())
        print(2, f)
        #value小到大
        f.sort()
        print(3, f)

        ans, removed, half = 0, 0, len(arr) // 2
        print(4, ans,removed,half)
        while removed < half:
            ans += 1
            print(5, ans)
            #從最大開始+ 超過原長度一半即停止
            removed += f.pop()
            print(6, removed)
        return ans

c = [5,5,1,3,4,4,5,2]
test = Solution()

start = time.process_time()
print(test.minSetSize(c))
end = time.process_time()
print("執行時間：%f 秒" % (end-start))