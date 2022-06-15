class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftsum = [0]
        rightsum = [0]
        for i,value in enumerate(nums):
            leftsum.append(value+leftsum[i])
        for j,value in enumerate(nums[::-1]):
            rightsum.append(value+rightsum[j])
        rightsum = rightsum[::-1]
        
        count=  0
        for i in range(1,len(leftsum)-1):
            if leftsum[i] >= rightsum[i]:
                count+=1
        return count
            
        