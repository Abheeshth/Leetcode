class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 < cost2:
            cost1,cost2 = cost2,cost1
        count = 0
        # now cost1 is larger
        while total >= 0:
            remain = total //cost2
            count+=(remain+1)
            total-=cost1
            
        return count
            
            
        