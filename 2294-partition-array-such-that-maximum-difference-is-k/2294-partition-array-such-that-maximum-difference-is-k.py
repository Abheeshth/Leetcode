class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        mini = nums[0]
        count = 1
        while i<len(nums):
            if nums[i] - mini > k:
                count+=1
                mini = nums[i]
            else:
                i+=1
        return count
                
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        