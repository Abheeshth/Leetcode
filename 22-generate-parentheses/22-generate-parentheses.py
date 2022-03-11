class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # let's write a recurssion function
        self.final = []
        def function(temp,left,right,n):
            print(left,right)
            if left+right == 2*n and left == right:
                print('1')
                self.final.append(temp)

            if left>right and left<n and right<n:
                print('2')
                function(temp+'(',left+1,right,n)
                function(temp+')',left,right+1,n)
            if left>right and left == n and right<n:
                function(temp+')',left,right+1,n)
                
    
            if left == right and left<n and right<n:
                print('3')
                function(temp+'(',left+1,right,n)
 
        function("",0,0,n)
        return self.final
                
                
            
                
            
        