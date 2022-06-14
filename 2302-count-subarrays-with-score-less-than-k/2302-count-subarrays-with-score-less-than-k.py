class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])

        ans = 0

        for i in range(len(nums)+1):
            prev_sum = prefix_sum[i]
            lo = i+1
            hi = len(nums)+1

            while lo < hi:
                mid = (lo+hi)//2
                sub_len = mid - i
                sub_sum = prefix_sum[mid] - prev_sum
                if sub_sum * sub_len < k:
                    lo = mid+1
                else:
                    hi = mid
            
            ans += max(0, lo - i - 1) # total subarrays starting with i and ending before j
        return ans