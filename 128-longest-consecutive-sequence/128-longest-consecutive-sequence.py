class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # main concept is that if nums[i]-1 is not in set then it's a starting point of a subsequence. in that wa we need not to track aal the visits
        
        s= set()
        if len(nums)<=0:
            return 0
        for i in nums:
            s.add(i)
           
        maxi = float('-inf')
        for j in range(len(nums)):
            count = 0
            if nums[j]-1 not in s:
                p = nums[j]
                while p in s:
                    p+=1
                    count+=1
            maxi = max(maxi,count)
        return maxi
            
        