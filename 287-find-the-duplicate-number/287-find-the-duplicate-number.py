class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i,val in enumerate(nums):
            if nums[abs(val)-1] <0:
                #print(nums[val-1])
                return abs(val)
            else:
                nums[abs(val)-1]*=-1
        
        