
"""
不是要把val remove掉
list 重新排過一遍 不加val
記憶體還在值不在
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ptr = 0 
        for num in nums:
            if num != val:
                nums[ptr] = num
                ptr += 1
        return ptr
        # new_nums = [num for num in nums if num != val]
        # print(new_nums)
        # return len(new_nums)
        #TC: O(n): n is length of nums
        #SC: O(1), 