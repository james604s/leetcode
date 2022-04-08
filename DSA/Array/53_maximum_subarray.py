class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        c=0
        s=0
        for i in range (len(nums)):
            if c>=0:
                c=c+nums[i]
            else:
                c=nums[i]
            s=max(s,c)
        return s