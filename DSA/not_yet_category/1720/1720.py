class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        res = [first]
        for i in encoded:
            res.append(i^res[-1])
        return res