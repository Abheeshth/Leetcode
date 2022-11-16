# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        l = []
        queue = [root]
        while queue:
            level = queue.copy()
            t = [i.val for i in level ]
            l.append(t)
            for node in level:
                queue.pop(0)
                if node.left:
                    #p.append(node.left)
                    queue.append(node.left)
                if node.right:
                    #p.append(node.right)
                    queue.append(node.right)
                    
        return l
        
                    
                    
                
                
                
                    
                
                
        
        