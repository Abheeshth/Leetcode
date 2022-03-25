class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        start = 1
        for i in range(1,len(nums)):
            if nums[i]!=prev:
                nums[start] = nums[i]
                prev = nums[i]
                start+=1
        return start
            
        