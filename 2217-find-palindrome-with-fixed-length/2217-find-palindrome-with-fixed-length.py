class Solution:
    def kthPalindrome(self, queries: List[int], n: int) -> List[int]:
        
        power = 0
        if n%2 == 0:
            power = n//2 -1
        else:
            power = n//2
           
        
        ans = []
        start = pow(10,power)
        for i in queries:
            half = str(start + i -1)
            
            if n%2 == 0:
                if len(half+half[::-1])>n:
                    ans.append(-1)
                else:
                    ans.append(int(half+half[::-1]))
            else:

                p = half[::-1]
                if len(half+p[1:])>n:
                    ans.append(-1)
                else:
                    ans.append(int(half+p[1:]))
                           
        return ans
                
        
        # for help
        #https://www.youtube.com/watch?v=A98psR_mIMQ
        # watch this 
                
                
                
        