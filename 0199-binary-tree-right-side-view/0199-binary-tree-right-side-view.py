# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.dic = {}
        self.l = []
        def dfs(root,level):
            if root is None:
                return 
            if level not in self.dic:
                self.dic[level] = 1
                self.l.append(root.val)
            p = level+1
            if root.right:
                dfs(root.right,p)
            if root.left:
                dfs(root.left,p)
                
        dfs(root,0)
        return self.l
            
            
        