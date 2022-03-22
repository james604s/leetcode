#https://ithelp.ithome.com.tw/articles/10213271

class Solution:
    """利用Python的進位制轉換函式，先將兩個加數轉成10進位制，
    再把和轉換成二進位制返回即可。雖然速度還挺快的，但這麼做忽略了可能的大整數相加的細節"""
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        return bin(int(a, 2) + int(b, 2))[2:]

#用遞迴實現，要注意，當兩個加數都是1時要進位。
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b:
            return a if a else b
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'