"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# do right to left bfs on each level 

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        queue = [root]
        while queue:
            length = len(queue)  
            rightmost = None
            for i in range(length):
                node = queue.pop(0)
                node.next  = rightmost
                rightmost = node
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return root
                
        
        