import decimal
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key = lambda x:x[0])
        lines = 0
        slope = float('inf')
        prev = stockPrices[0]
        for stock in stockPrices[1:]:
            slopecur = decimal.Decimal(stock[1]-prev[1])/decimal.Decimal(stock[0]-prev[0])
            #print(slopecur)
            if slopecur != slope:
                #print(slopecur)
                lines+=1
                #print(lines)
                slope = slopecur
            prev = stock
        return lines
        