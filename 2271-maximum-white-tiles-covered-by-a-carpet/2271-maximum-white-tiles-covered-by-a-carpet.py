class Solution:
    def maximumWhiteTiles(self, T: List[List[int]], clen: int) -> int:
        T.sort()
        
        pref = [0]* (len(T)+1)
        
        for i in range(1,len(T)+1):
            pref[i] = pref[i-1]+(T[i-1][1]- T[i-1][0]+1)
            
        print(pref)
        res =0
        j = 0
        # two conditions 
        # first one is 
        for i in range(len(T)):
            start,p = T[i][0],T[i][1]
            if p>= start+clen-1:
                return clen
            
            end = min(T[-1][1],start+clen-1)
            
            #j = i
            while j<len(T) and T[j][1] < end:
                j+=1
                
                
            
            # fist one is of end point is not cvering carpet partially
            if T[j][0]> end:
                res = max(res,pref[j]-pref[i])
            else:
                res = max(res,pref[j+1] - pref[i] - (T[j][1] - end ))
                
        return res
        
            
        

        