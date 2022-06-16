class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = [0 for i in range(len(prices)+1)]
        right = [0 for i in range(len(prices)+1)]
        
        # for left
        mini = prices[0]
        for i in range(1,len(prices)):
            left[i] = max(left[i-1],prices[i]-mini)
            mini = min(mini,prices[i])
           
        #for right
        prices = prices[::-1]
        maxi = prices[0]
        for i in range(1,len(prices)):
            right[i] = max(right[i+1],maxi- prices[i])
            maxi = max(maxi,prices[i])
        right = right[::-1]
        
        profit = 0
            
        #print(left,right)
        for i in range(len(left)):
            profit = max(profit,left[i-1]+right[i])
        return profit
            
            
            