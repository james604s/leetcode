"""
"""
# Solution1 初始想法, 只想先寫出一版
class Solution1:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        merged_words = ""
        if word1_len == word2_len:
            for i in range(word1_len):
                merged_words = merged_words + word1[i] + word2[i]
            return merged_words
        elif word1_len < word2_len:
            for i in range(word1_len):
                merged_words = merged_words + word1[i] + word2[i]
            merged_words = merged_words + word2[word1_len:]
            return merged_words
        elif word1_len > word2_len:
            for i in range(word2_len):
                merged_words = merged_words + word1[i] + word2[i]
            merged_words = merged_words + word1[word2_len:]
            return merged_words
        
# Solution2一行寫法
from itertools import zip_longest
class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))
    
# Solution3 預先分配 list
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        減少了記憶體分配的次數，也可能提升效能，尤其是在字串非常長的時候。
        """
        merged_words = [""] * (len(word1) + len(word2))
        i, j, k = 0, 0, 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged_words[k] = word1[i]
                i += 1
                k += 1
            if j < len(word2):
                merged_words[k] = word2[j]
                j += 1
                k += 1
        return "".join(merged_words)