class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        large = nums[0]
        for i in range(1,len(nums)):
            if large<0:
                large = nums[i]
                
            else:
                large +=nums[i]
            largest = max(large,largest)
                
        return largest
            
        
        