# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # let's do bfs
        if root is None:
            return []
        queue = [root]
        res = []
        
        while queue:
            l = len(queue)
            curr_level = []
            for i in range(l):
                node = queue.pop(0)
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(curr_level)
            
        return res 
                    
                
                
        
        