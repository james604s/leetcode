class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        print(s, indices)
        my_map={}
        for i in range(len(s)):
            my_map.setdefault(indices[i], s[i])
        return "".join(my_map.values())

"""
class Solution:
    def restoreString(self, s, indices):
        
        str_dict = {}
        string = ''
        
        count = 0
        for i in indices:
            str_dict[i] = s[count]
            count += 1
            
        for e in range(len(s)):
            string += str_dict[e]
            
        return string
"""