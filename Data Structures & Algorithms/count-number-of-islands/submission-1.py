class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS=len(grid)
        COLUMNS=len(grid[0])
        count=0
        def dfs(grid,i,j):
            if min(i,j)<0 or i==ROWS or j==COLUMNS or grid[i][j]=='0':
                return 
            if(grid[i][j]=='1'):
                grid[i][j]='0'
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j]=='1':
                    count=count+1
                    dfs(grid,i,j)
        return count
        
        
        