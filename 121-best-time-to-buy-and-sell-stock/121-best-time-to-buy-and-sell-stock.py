class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        init = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < init:
                init = prices[i]
            else:
                maxi = max(maxi,prices[i]-init)
        return maxi