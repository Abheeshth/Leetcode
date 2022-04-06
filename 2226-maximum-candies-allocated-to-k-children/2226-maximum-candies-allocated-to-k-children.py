class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        #start can be taken as 1 , highest we can distribute equally is average.
        #Use Binary Search and try to distribute the candies equal to mid, if possible try to maximize it by moving on right,             #else if not possible try it by decreasing the value by moving on left
        
        mini,maxi = 1,sum(candies)//k
        ans  = 0
        while mini<=maxi:
            mid = (mini+maxi)//2
            if k<= sum(a//mid for a in candies):
                mini = mid+1
                ans = mid
            else:
                maxi = mid-1
        return ans
            
        