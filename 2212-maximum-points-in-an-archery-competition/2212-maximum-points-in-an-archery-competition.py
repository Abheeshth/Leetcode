class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        def dp(numArrows, idx, path):
            if numArrows < 0:
                return float("-inf"), path
            if idx < 0:
                return 0, path
            
            res1, path1 = dp(numArrows, idx-1, path)
            res2, path2 = dp(numArrows - (aliceArrows[idx]+1), idx-1, path + [idx])
            res2 += idx
            if res1 > res2:
                res = res1
                path = path1
            else:
                res = res2
                path = path2
            return res, path
        
        res, path = dp(numArrows, len(aliceArrows) - 1, [])
        bobArr = [0] * 12
        for idx in path:
            bobArr[idx] = aliceArrows[idx] + 1
        if sum(bobArr) < sum(aliceArrows):
            bobArr[0] += sum(aliceArrows) - sum(bobArr)
        return bobArr
        
    
                
            
                
            
        