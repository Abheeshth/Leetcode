class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        forward = []
        total = 0
        for i, num in enumerate(nums):
            total += num
            forward.append(total // (i + 1))
        
        backward = [0]
        total = 0
        for i, num in enumerate(nums[::-1][:len(nums) - 1]):
            total += num
            backward.append(total // (i + 1))
        result = float('inf')
        n = len(nums)
        for i in range(len(forward)):
            if result > abs(forward[i] - backward[n - i- 1]):
                ans = i
                result = abs(forward[i] - backward[n - i - 1])
        if len(nums) == 1:
            return 0
        return ans