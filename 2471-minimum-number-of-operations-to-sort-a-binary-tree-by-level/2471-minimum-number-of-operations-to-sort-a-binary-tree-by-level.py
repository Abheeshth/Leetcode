# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def swapa(arr):
            temp = [i for i in arr]
            temp.sort()
            ans = 0
            has = {}
            for i in range(len(arr)):
                has[arr[i]] = i
            
            for i in range(len(arr)):
                if temp[i] != arr[i]:
                    ans+=1
                    init = arr[i]
                    arr[i],arr[has[temp[i]]] = arr[has[temp[i]]],arr[i]
                    has[init] = has[temp[i]]
                    has[temp[i]] = i
                    
            return ans
        def level_order_traversal(root):
            queue = []
            level = 0
            queue.append([root,level])
            l = []
            dic = {}
            
            while queue:
                root,level = queue.pop(0)
                if level in dic:
                    dic[level].append(root.val)
                else:
                    dic[level]  = [root.val]
                if root.left:
                    l = level+1
                    queue.append([root.left,l])
                if root.right:
                    l = level+1
                    queue.append([root.right,l])
            return dic
        dic = level_order_traversal(root)
        ans = 0
        for i in dic:
            #print(dic[i])
            #print('answer',swapa(dic[i]))
            ans+=int(swapa(dic[i]))
            #print(ans)
        return ans
        
            
            
                
                    
            
                
                
                
                
                
                
                
                
                
                
                
                
                
                    
                    
                    
                    
                    