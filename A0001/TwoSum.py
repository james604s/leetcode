# class Solution:
#     def twoSum(self, nums ,target):
#         numMap = {}
#         for i in range(len(nums)):
#             print(1,numMap,target,nums)
#             print(2,numMap.__contains__(target-nums[i]))
#             if numMap.__contains__(target-nums[i]):
#                 print(3,[numMap.get(target-nums[i]), i])
#                 return [numMap.get(target-nums[i]), i]
#             else:
#                 numMap[nums[i]] = i
#                 print(4,numMap[nums[i]])

class Solution:
    def twoSum(self, nums,target):
        dic={}   ##key儲存nums裡的數  value 儲存下標
        for i in range(len(nums)):
            if (target-nums[i]) in dic:
                return [dic[target-nums[i]],i]
            else:
                dic[nums[i]]=i

a = Solution()
# a.twoSum([2,7,11,15], 9)
a.twoSum([15,11,7,2], 9)

