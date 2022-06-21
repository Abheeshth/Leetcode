class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.total = 0
        self.dire = [[0,1],[1,0],[0,-1],[-1,0]]
        self.dist = 1
        #seen = set()
        #print(len(grid),len(grid[0]))
        def dfs(grid,i,j):
            
            for di in self.dire:
                x = i+di[0]
                y = j+di[1]
                #print(x,y,grid[x][y])
                #print(seen)
                #print()
                if 0<=x<len(grid) and 0<=y<(len(grid[0])) and grid[x][y] == 1 :
                    #seen.add((x,y))
                    grid[x][y] = 0
                    self.dist+=1
                    
                    #print("ab aya ",x,y)
                    dfs(grid,x,y)
                    
            #self.total  = max(self.total)
                    
                    
                    
                    
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 :
                    #seen.add((i,j))
                    grid[i][j] = 0
                    #print(i,j)
                    dfs(grid,i,j)
                    self.total = max(self.total,self.dist)
                    self.dist = 1
        print(grid)
        return self.total
            