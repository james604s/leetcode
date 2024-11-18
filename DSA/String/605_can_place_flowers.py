class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        d=0
        for i in flowerbed:
            if i==1:    # violation condition 
                if d==1:
                    c-=1
                d=1
            else:
                if d==1:  # not planted 
                    d=0
                else:
                    c+=1  #planted
                    d=1
        return c>=n
