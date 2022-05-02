class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        #print(sorted(strs[0]))
        for i,value in enumerate(strs):
            temp = ''.join(sorted(value))
            if temp in dic:
                dic[temp].append(value)
            else:
                dic[temp] = [value]
        final = []
        for i in dic:
            final.append(dic[i])
        return final
            
                
        
        