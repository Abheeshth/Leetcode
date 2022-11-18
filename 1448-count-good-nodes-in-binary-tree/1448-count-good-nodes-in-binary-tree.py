# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root,maxi_parent):
            if root is None:
                return 
            if root.val>=maxi_parent:
                self.count+=1
                maxi_parent = root.val
            if root.left:
                dfs(root.left,maxi_parent)
            if root.right:
                dfs(root.right,maxi_parent)
        dfs(root,root.val)
        return self.count
            