# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        cnt  = 0
        l = []
        
        while queue:
            length = len(queue)
            curr_level = []  
            for i in range(length):
                node = queue.pop(0)
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if cnt%2 == 0 :
                l.append(curr_level)
            else:
                curr_level = curr_level[::-1]
                l.append(curr_level)
            cnt+=1
        return l
                    
        