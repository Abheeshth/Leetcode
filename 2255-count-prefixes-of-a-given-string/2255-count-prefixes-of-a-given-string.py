class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            
            if len(word)<=len(s):
                p = True
                for j in range(len(word)):
                    if word[j] != s[j]:
                        p = False
                if p:
                    count+=1
                
        return count
            
                    
        