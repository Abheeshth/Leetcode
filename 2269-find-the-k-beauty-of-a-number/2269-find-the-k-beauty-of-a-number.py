class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        count = 0
        for i in range(len(str(num))-k+1):
            #print(num[i:i+k])
            if int(num[i:i+k])!= 0:
                if int(num) % int(num[i:i+k]) == 0:
                    count+=1
        return count
        