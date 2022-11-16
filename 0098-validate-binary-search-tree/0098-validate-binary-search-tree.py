# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        def dfs(root,low,high):
            #print(low , high)
            if root.val>=high or root.val<=low:
                #print(GG)
                self.flag = False
                return 
            if root.left:
                dfs(root.left,low,root.val)
            if root.right:
                dfs(root.right,root.val,high)
            return True
        dfs(root,float('-inf'),float('inf'))
        return self.flag
            
        