class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        maxi  = 0
        i = 1
        while i<len(arr)-1:
            if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
                count = 1
                j = i
                while j>0 and arr[j]>arr[j-1]:
                    count+=1
                    j-=1
                while i<len(arr)-1 and arr[i]>arr[i+1]:
                    count+=1
                    i+=1
                maxi = max(count,maxi)
            else:
                i+=1
        return maxi
                
                
        