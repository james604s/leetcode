class Solution:
    def buildArray(self, nums):
        res = []
        for i in range(0, len(nums)):
            res.append(nums[nums[i]])
        return res