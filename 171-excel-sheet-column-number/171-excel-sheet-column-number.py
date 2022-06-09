class Solution:
    def titleToNumber(self, S: str) -> int:
    # ord('A')-64 = 1
        count = 0
        l = len(S)
        i = 0
        while l>0 and i<len(S):
            count += (26**(l-1))*(ord(S[i])-64)
            l-=1
            i+=1

        return count
        
        