class Solution:
    def lastRemaining(self, n: int) -> int:
        # relations
        # 1. elimination(2k) = elimination(2k+1)
        # 2. left(2k) = 2*right(k)       # left(1,2,3,4,5,6,7,8,9,10) = 2*right(1,2,3,4,5) 
        # 3. left(k) -1 = k- right(k)  # elemnt which is remain is having same postion from both sides
        
        # results from these three equations
        # left(n) = 2*(n//2 - left(n//2) +1)
        
        if n == 1:
            return 1
        else:
            return 2*(n//2 +1 - self.lastRemaining(n//2))
                
            
        