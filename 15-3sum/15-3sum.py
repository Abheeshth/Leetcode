class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array 
        nums.sort()
        
        #start from the first element and go to second last 
        final = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:           # we do not want the similar elements
                continue
            left = i+1
            right = len(nums)-1
            
            while left<right:
                temp = nums[i]+nums[left]+nums[right]
                
                if temp>0:
                    right-=1
                elif temp<0:
                    left+=1
                else:
                    final.append([nums[i],nums[left],nums[right]])
                    #this step to skip the similar digits
                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    while left<right and nums[right] == nums[right-1]:
                        right -=1
                    left+=1
                    right-=1
        return final
                
                