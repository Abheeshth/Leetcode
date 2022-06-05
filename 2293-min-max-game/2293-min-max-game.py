class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        p = [i for i in nums]
        
        while len(p)!= 1:
            q = len(p)//2
            for i in range(len(p)-1):
                if i%2 == 0:
                    a = p.pop(0)
                    b = p.pop(0)
                    p.append(min(a,b))
                else:
                    a = p.pop(0)
                    b = p.pop(0)
                    p.append(max(a,b))
            print(p)
        return p[0]
            
        