class Solution:
    def digitCount(self, num: str) -> bool:
        for i,val in enumerate(num):
            if str(num.count(str(i))) != val:
                return False
        return True
                
        