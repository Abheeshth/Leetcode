class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        while (original in nums):
            #print(original)
            for i,value in enumerate(nums):
                if value == original:
                    original = original*2
                    break
                    
                
        return original
                    
        