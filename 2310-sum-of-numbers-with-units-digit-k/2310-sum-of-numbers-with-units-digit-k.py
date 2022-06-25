class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        # last digit of num should be a multiple of k
        # then we will decide the carry 
        #
        if num == 0:
            return 0
        for i in range(1,11):
            if num%10 == (k*i)%10 and i*k <=num:
                return i
        return -1