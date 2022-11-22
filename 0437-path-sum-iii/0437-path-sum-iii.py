# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        # let's define global result and path 
        self.result  = 0
        dic = {0:1}
        
        #let's do recursion to get the result
        
        self.dfs(root,target,0,dic)
        return self.result
        
    def dfs(self,root,target,currsum,dic):
        
        # base case 
        if root is None:
            return 
        currsum+=root.val
        
        oldsum = currsum-target
        
        # we will uodate the result and dic
        
        self.result+=dic.get(oldsum,0)
        dic[currsum] = dic.get(currsum,0)+1
        
        
        #dfs
        self.dfs(root.left,target,currsum,dic)
        self.dfs(root.right,target,currsum,dic)
        
        dic[currsum] -=1
        