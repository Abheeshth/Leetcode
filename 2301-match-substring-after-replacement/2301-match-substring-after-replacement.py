class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        h = collections.defaultdict(set)
        for a,b in mappings:
            h[a].add(b)
        l = len(sub)
        for i in range(len(s)-len(sub)+1):
            flag =True
            for s_val, sub_val in zip(s[i:i+l], sub):
                if s_val==sub_val or (s_val in h[sub_val]): continue
                else:
                    flag = False
                    break
            if flag: 
                return True
        return False