class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # (a+a+(n-1)*d)/(n/2) = N
        # we need to find a and we will interate for n
        # a = (2*N + n- n**2)/ 2*n      // d == 1
        count = 1
        n = 2
        while (2*N + n- n**2) >0:
            a = (2*N + n- n**2)/(2*n)
            #let's just check if our a is real or not
            if int(a) - a == 0:
                count+=1
            n+=1
        return count
            
            
        
        