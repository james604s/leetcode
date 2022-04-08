class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        S = set()
        
        for x in nums:
            if x in S: 
                return True
            S.add(x)
            
        return False