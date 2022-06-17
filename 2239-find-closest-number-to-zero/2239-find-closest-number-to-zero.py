class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        mini = float('inf')
        maxi = float('-inf') 
        
        for i in nums:
            if abs(i-0) <=  mini:
                mini = abs(i-0)
                maxi = i
        return maxi
            
        