class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        j = 0
        while i < len(t):
            if s[j] == t[i]:
                #print(s[j])
                i+=1
                j+=1
                if j == len(s):
                    return True
            else:
                i+=1
        return False
                
            
            
        