class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # we have got the target 
        # if we sort the array 
        # if value is grater than then target then right to left
        # if value is lees then the target then left to right
        nums.sort()
        closest = {}
        miniout = float('inf')
        mini  = float('inf')
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            
            while left<right:
  
                temp = nums[i]+nums[left]+nums[right]
                if temp>target:
                    right-=1
                    if mini > abs(temp-target):
                        miniout = temp
                        mini = abs(temp-target)
                elif temp<target:

                    left+=1
                    if mini > abs(temp-target):
                        miniout = temp
                        mini = abs(temp-target)
                else:
                    return target
        return miniout
                
                    
            