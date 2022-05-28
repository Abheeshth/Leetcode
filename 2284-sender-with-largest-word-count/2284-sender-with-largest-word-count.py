class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        dic = {}
        for i,sender in enumerate(senders):
            if sender in dic:
                dic[sender]+=len(messages[i].split())
            else:
                dic[sender] = len(messages[i].split())
        sorted_dic = dict(sorted(dic.items(),key = lambda x:x[1],reverse = True))
        l = []
        intial = float('inf')
        l = []
        print(sorted_dic)
        for j in sorted_dic:
            if intial == float('inf'):
                print(sorted_dic[j])
                intial = sorted_dic[j]
                l.append(j)
            elif intial == sorted_dic[j]:
                l.append(j)
            else:
                break
                
        l.sort(reverse = True)
        return l[0]
            
        
        