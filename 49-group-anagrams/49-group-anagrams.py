class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        #print(sorted(strs[0]))
        for i,value in enumerate(strs):
            temp = ''.join(sorted(value))
            if temp in dic:
                dic[temp].append(i)
            else:
                dic[temp] = [i]
        final = []
        for i in dic:
            temp = dic[i]
            temp2 = []
            for j in temp:
                temp2.append(strs[j])
            final.append(temp2)
        #print(final)
        return final
            
                
        
        