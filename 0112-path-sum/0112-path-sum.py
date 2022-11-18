# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.targetSum = targetSum
        self.flag = False
        def dfs(root,Sum):
            if root is None:
                return 
            Sum += root.val
            if root.left is None and root.right is None:
                if Sum == self.targetSum:
                    self.flag = True
            if root.left:
                dfs(root.left,Sum)
            if root.right:
                dfs(root.right,Sum)
        dfs(root,0)
        return self.flag
                    
            
        