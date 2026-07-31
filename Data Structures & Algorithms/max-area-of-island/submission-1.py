class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLUMNS=len(grid[0])
        max_array=[]
        def dfs(grid,i,j,count):
            if min(i,j)<0 or i==ROWS or j==COLUMNS or grid[i][j]==0:
                return count
            if grid[i][j]==1:
                count=count+1
                grid[i][j]=0
            count=dfs(grid,i+1,j,count)
            count=dfs(grid,i-1,j,count)
            count=dfs(grid,i,j+1,count)
            count=dfs(grid,i,j-1,count)
            return count
        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j]==1:
                    count=dfs(grid,i,j,0)
                    max_array.append(count)
        if len(max_array)!=0:
            return max(max_array)
        else:
            return 0
                