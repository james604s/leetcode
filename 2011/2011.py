class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_list = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    nums_list[i] = nums_list[i] + 1
        return nums_list
            
"""
O(nlogn)
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        :type nums: List[int]
        :rtype: List[int]
        indics = {}
        for index, num in enumerate(sorted(nums)):
            indics.setdefault(num, index)
        return [indics[num] for num in nums]
"""

"""
O(n)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)

        for i in range(1,101):
            count[i] += count[i-1]
        
        return [count[x-1] for x in nums]
"""