class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans, lower = 0, 1
        count = 0
        for num in sorted(nums):
            if num > lower:
                hi = min(num - 1, k - 1 + lower)
                count = hi - lower + 1
                ans += (lower + hi) * count // 2 
                k -= count
                if k == 0:
                    return ans
            lower = num + 1
        if k > 0:
            ans += (lower + lower + k - 1) * k // 2
        return ans
                
            
                
        