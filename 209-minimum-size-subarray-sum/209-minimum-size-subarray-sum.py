class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        initial ,res = 0,len(nums)+1
        
        for j in range(len(nums)):
            target-=nums[j]
            while target<=0:
                res = min(res,(j-initial+1))
                target+=nums[initial]
                initial+=1
        return res%(len(nums)+1)
                
            
        