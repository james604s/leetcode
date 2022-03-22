
"""
假設 input array: nums = [1, 2, 3, 4, 7], 目標 target = 6
起始 low = 0, high = nums.length — 1
當 low < high 時，sum = nums[low] + nums[high]
low = 0 < high = 4, sum = 1 + 7 = 8 , 8 > 6，所以把high的指針往前移動, high -=1
low = 0 < high = 3, sum = 1 + 4 = 5, 5 < 6，所以把low往後移動, low += 1
low = 1 < high = 3, sum = 2 + 4 =6, 6 = 6, 找到唯一解, 此時 return [low+1, high + 1] 因為要回傳第幾個數字
ans = [2, 4]
Time complexity: O(n), n個元素最多只會被造訪1次
Space complexity: O(1), 只用到兩個指針
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        res = []
        while start < end:
            sum = numbers[start] + numbers[end]
            if target > sum:
                start+=1
            elif target < sum:
                end-=1
            else:
                res = [start + 1, end + 1]
                return res