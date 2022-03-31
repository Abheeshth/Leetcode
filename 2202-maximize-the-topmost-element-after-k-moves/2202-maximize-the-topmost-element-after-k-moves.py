class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]
        if len(nums) == 1:
            if k%2==0:
                return nums[0]
            return -1

        #k = k%len(nums)
        if len(nums) < k:
            return max(nums)
        maxi = float('-inf')
        
        #remove all elements up to rest
        
        for i in range(k-1):
            q = nums.pop(0)
            maxi = max(q,maxi)
            
        #print(nums)
        
        # and then check if next is to remove or add
        if len(nums)>1:
            if nums[1] >maxi:
                return nums[1]
            else:
                return maxi
        else:
            return maxi
            
            
        
        
        
        