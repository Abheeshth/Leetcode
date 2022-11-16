"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        queue = [root]
        
        while queue:
            length = len(queue)
            right_most = None
            for __ in range(length):
                curr_node = queue.pop(0)
                curr_node.next = right_most
                right_most = curr_node
                
                if curr_node.right:
                    queue.append(curr_node.right)
                if curr_node.left:
                    queue.append(curr_node.left)
                    
        return root
                
                