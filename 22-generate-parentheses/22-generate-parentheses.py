class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.l = []
        def dfs(right,left,stri):
            if right<0 or left<0:
                return
            if right > left:
                return
            if right == 0 and left == 0:
                self.l.append(stri)
                return 
            dfs(right-1,left,stri+'(')
            dfs(right,left-1,stri+')')
        dfs(n,n,'')
        return self.l
                
                
            
                
            
        