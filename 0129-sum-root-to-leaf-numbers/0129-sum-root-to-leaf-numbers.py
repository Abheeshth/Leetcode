# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.results = []
        
        def dfs(root,string):
            if root is None:
                return 
            p = string+str(root.val)
            if root.left is None and root.right is None:
                self.results.append(int(p))
            
            dfs(root.left,p)
            dfs(root.right,p)
        dfs(root,'')
        #print(self.results)
        return sum(self.results)
        
            
            
        