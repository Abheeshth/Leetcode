class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        leftcount = [0]
        n = len(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count+=1
            leftcount.append(count)
            
        rightcount = [0]
        count2 = 0
        for i in range(len(nums)):
            if nums[n-i-1] == 1:
                count2+=1
            rightcount.append(count2)
        rightcount = rightcount[::-1]
            
        #print(leftcount)
        #print(rightcount)
        
        p = []
        for i in range(len(leftcount)):
            p.append(leftcount[i]+rightcount[i])
        maxi = max(p)
        ans = []
        #print(p)
        for i in range(len(p)):
            if p[i] == maxi:
                ans.append(i)
        return ans
            
                
                
            
        