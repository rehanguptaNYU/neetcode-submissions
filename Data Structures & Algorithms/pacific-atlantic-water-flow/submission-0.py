class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS=len(heights)
        COLUMNS=len(heights[0])
        pacific_set=set()
        atlantic_set=set()
        result=[]
        def dfs(heights,i,j,visited_set,previous_height):
            if i==ROWS or j==COLUMNS or min(i,j)<0 or heights[i][j]<previous_height or (i,j) in visited_set:
                return None
            if heights[i][j]>=previous_height:
                visited_set.add((i,j))
                previous_height=heights[i][j]
                dfs(heights,i+1,j,visited_set,previous_height)
                dfs(heights,i-1,j,visited_set,previous_height)
                dfs(heights,i,j+1,visited_set,previous_height)
                dfs(heights,i,j-1,visited_set,previous_height)
        for i in range(ROWS):
            for j in range(COLUMNS):
                if i==0 or j==0:
                    dfs(heights,i,j,pacific_set,heights[i][j])
                if i==ROWS-1 or j==COLUMNS-1:
                   dfs(heights,i,j,atlantic_set,heights[i][j])
        for i in range(ROWS):
            for j in range(COLUMNS):
                if(i,j) in pacific_set and (i,j) in atlantic_set:
                    result.append([i,j])
        return result
