class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0 for __ in range(num_people)]
        intial = 1
        while candies>0:
            if candies>intial:
                ans[(intial-1)%num_people] +=intial
                candies-=intial
                intial+=1
            else:
                ans[(intial-1)%num_people] += candies
                candies = 0
                
        return ans
                
                
            
        
        
        
        
        
        
        
        
        
        
        