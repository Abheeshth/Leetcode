# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result = []
        def helper(root,target,curr,path):

            
            if root is None:
                return 
            curr += root.val
            path.append(root.val)
            if root.left is None and root.right is None and curr == target:

                self.result.append(path.copy())
            
            
            helper(root.left,target,curr,path)
            helper(root.right,target,curr,path)
            path.pop()
        path = []
        helper(root,targetSum,0,path)
        return self.result
        