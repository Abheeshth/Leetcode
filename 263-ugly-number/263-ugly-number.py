class Solution:
    def isUgly(self, n: int) -> bool:
        l = [2,3,5]
        for q in l:
            while n%q == 0 and n%q<n:
                n = n/q
        return n == 1
        