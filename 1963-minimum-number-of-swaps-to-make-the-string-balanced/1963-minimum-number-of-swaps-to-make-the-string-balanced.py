class Solution:
    def minSwaps(self, s: str) -> int:
        # let's make a vector for position of '['
        stack = []
        p=0
        for i,value in enumerate(s):
            if s[i] == '[':
                stack.append(s[i])
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    p+=1
        return (p+1)//2
                
                
                
                