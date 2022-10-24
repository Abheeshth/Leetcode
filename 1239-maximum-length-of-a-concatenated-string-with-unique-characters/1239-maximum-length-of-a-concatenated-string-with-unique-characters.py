class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # we will define a set 
        
        S = [set()]
        # first we'll check if string is having same elemnts then skip it
        for s in arr:
            if len(set(s))!= len(s):
                continue
            s = set(s)
            for c in S:
                if s&c:
                    continue
                else:
                    S.append(s|c)
        #print(S)
        return max(len(a) for a in S)
            
                