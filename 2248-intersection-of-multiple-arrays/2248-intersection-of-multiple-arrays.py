class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dic = {}
        for num in nums:
            for j in num:
                if j in dic:
                    dic[j]+=1
                else:
                    dic[j] = 1
        p = []
        for q in dic:
            if dic[q] == len(nums):
                p.append(q)
        p.sort()
        return p
                
        