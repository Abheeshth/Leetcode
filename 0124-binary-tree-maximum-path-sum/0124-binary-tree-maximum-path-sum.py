# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        # first we aill interate till leaf node
        # then forward the max of (left,right)
        # after checking the value of root.value +left +right
        self.maxi = float('-inf')
        
        def dfs(root):
            if root is None:
                return 0
            
            left = max(dfs(root.left),0)
            right = max(dfs(root.right),0)
            self.maxi = max(self.maxi,left+right+root.val)
            #print(left,right)
            return max(left,right)+root.val
        dfs(root)
        return self.maxi
            
            
            
            
            