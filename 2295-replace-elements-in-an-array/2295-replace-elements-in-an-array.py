class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        for i,value in enumerate(nums):
            dic[value] = i
        print(dic)
        for p in operations:
            dic[p[1]] = dic.pop(p[0])
        sorted_touple = sorted(dic.items(),key = lambda x:x[1])
        ans = [k for k,v in sorted_touple]
        return ans