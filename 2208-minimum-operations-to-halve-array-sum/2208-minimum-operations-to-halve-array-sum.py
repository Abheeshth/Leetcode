from heapq import heapify, heappush, heappop
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half, ops = sum(nums) / 2, 0
        heap = [-num for num in nums]
        heapify(heap)
        while half > 0:
            num = -heappop(heap)
            num /= 2.0
            half -= num
            heappush(heap, -num)
            ops += 1
        return ops
            
            
            
        