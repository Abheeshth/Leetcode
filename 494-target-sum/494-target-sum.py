class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # so it's a subset sum problem 
        # if we devide this array into two subsets then 
        # first equations is S1+S2 = Sum of array
        # second equations is S1-S2 = Target
        # final is euations is S1 = (target+sum)//2
        S = abs(S)
        if(sum(nums) < S):
            return 0
        #if len(nums)
        def count_subsets_sum(nums, target):

            m = len(nums) + 1
            n = target + 1
            dp = [[0]*n for i in range (m)]
            dp[0][0] = 1


            for k in range(m):
                dp[k][0] = 1

            for i in range(1,m):
                for j in range(0,n):
                    curr_target = j
                    curr_val = nums[i-1]
                    if(curr_val > curr_target):
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i - 1][curr_target-curr_val]
                        
            return dp[m-1][n-1]
        
        if((S + sum(nums)) % 2 != 0):
            return 0
        effec_no = (S + sum(nums)) // 2      
        c = count_subsets_sum(nums,effec_no)
        return (c)
            