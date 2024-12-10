class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count+=1
        k = len(nums)-count
                
        i = 0
        
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
                j+=1
            else:
                j+=1
        #print(nums)
        return k

                
        