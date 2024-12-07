class Solution:
    def reverseVowels(self, s: str) -> str:
        l=['a','e','i','o','u','A','E','I','O','U']
        m=[]
        for i in s:
            if i in l:
                m.append(i)
        n=len(m)
        s=list(s)
        for i in range(len(s)):
            if s[i] in l:
                n-=1
                s[i]=m[n]
        return ''.join(s)
    
class Solution2:
    # https://ithelp.ithome.com.tw/articles/10286034
    def reverseVowels(self, s: str) -> str:
        l=0
        r=len(s)-1
        s=list(s)
        
        while l<r:
            while l<r and s[l] not in "AEIOUaeiou":
                l=l+1
                
            while l<r and s[r] not in "AEIOUaeiou":
                r=r-1
                
            if l<r:
                s[l],s[r]=s[r],s[l]
                l=l+1
                r=r-1
                
        return "".join(s)