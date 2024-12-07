class Solution:
    def removeStars(self, s: str) -> str:
        #Make a list in which you will add or remove the element
        word=[]
        #Iterate through the s until the end
        for i in s:
        #if * come while iteration pop the elements else append it to the list
            if i=="*":
                word.pop()
            else:
                word.append(i)
        #Convert the list into string and then return it
        return "".join(word)