class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count1 = 0
        count2 = 0
        
        for i in t:
            count1+=ord(i)
            
        for j in s:
            count2+=ord(j)
            
        return chr(count1-count2)
            