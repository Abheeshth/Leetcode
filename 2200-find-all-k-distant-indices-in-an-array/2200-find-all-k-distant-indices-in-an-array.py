class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        p = []
        for i in range(len(nums)):
            if nums[i] == key:
                p.append(i)
        l = []
        for j in p:
            for q in range(max(0,j-k),min(j+k+1,len(nums))):
                l.append(q)
                
        l = list(set(l))
        l.sort()
        return l
                
        
                
                
                
        