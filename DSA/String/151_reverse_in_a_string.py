class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        reverse_words = []
        for word in words:
            if "" != word:
                reverse_words.append(word)
        reverse_words = reverse_words[::-1]
        return " ".join(reverse_words)