class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        last = {}
        
        for i,value in enumerate(s):
            last[value] = i
            
        stack = []
        for i, value in enumerate(s):
            if value in stack:
                continue
            while stack and stack[-1]> value and i <last[stack[-1]]:
                stack.pop()
            stack.append(value)
            
        return ''.join(stack)
            
            
                
        