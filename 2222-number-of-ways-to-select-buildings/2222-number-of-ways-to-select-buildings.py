class Solution:
    def numberOfWays(self, s: str) -> int:
        precount1 = []
        precount0 = []
        
        count1 = 0
        count0 = 0
        for i,val in enumerate(s):
            if val == '1':
                count1+=1
                
            else:
                count0+=1
                
            precount0.append(count0)
            precount1.append(count1)
            
        answer = 0
        for i in range(1,len(s)-1):
            if s[i] == '0':
                leftside = precount1[i-1]
                rightside  = precount1[-1]- precount1[i]
                answer+= (leftside*rightside)
            else:
                leftside = precount0[i-1]
                rightside = precount0[-1] - precount0[i]
                
                answer+=(leftside*rightside)
                
        return answer
                
                
                
                
        