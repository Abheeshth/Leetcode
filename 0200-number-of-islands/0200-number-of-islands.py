class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        m = len(self.grid[0])
        n = len(self.grid)
        def dfs(i,j,m,n):
            #print('haha')
            if self.grid[i][j] == '0' or self.grid[i][j] == '#':
                return 
            self.grid[i][j] = '#'
            direcs = [[0,-1],[0,1],[1,0],[-1,0]]
            for direc in direcs:
                p = i+direc[0]
                q = j+direc[1]
                if p<n and p>=0 and q<m and q>=0:
                    dfs(p,q,m,n)
        count = 0
        for i in range(n):
            for j in range(m):
                if self.grid[i][j] == '1':
                    dfs(i,j,m,n)
                    count+=1
        print(self.grid)
        return count
            
            
                
        