

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        data =[]
        for rec in rectangles:
            print(rec)
            data.append(min(rec[0], rec[1]))
            print(data)
        return data.count(max(data))