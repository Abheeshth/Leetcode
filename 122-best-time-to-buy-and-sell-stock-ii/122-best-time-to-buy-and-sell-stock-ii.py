class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        diff = 0
        for i in range(1,n):
            if prices[i-1] < prices[i]:
                diff+= (prices[i]-prices[i-1])
        return diff
                