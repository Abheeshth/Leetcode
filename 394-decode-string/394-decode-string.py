class Solution:
    def decodeString(self, s: str) -> str:
        currstr = ''
        currnum = 0
        i = 0
        stack = []
        while i < len(s):
            if s[i] == '[':
                stack.append(currstr)
                stack.append(currnum)
                currstr = ''
                currnum = 0
            elif s[i] == ']':
                num = stack.pop()
                prevstr = stack.pop()
                currstr = prevstr +num*currstr
                
            elif s[i].isdigit():
                currnum = currnum*10+int(s[i])
            else:
                currstr += s[i]
            i+=1

        return currstr
                    
        