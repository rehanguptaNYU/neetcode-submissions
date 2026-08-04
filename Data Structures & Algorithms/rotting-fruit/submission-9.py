from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLUMNS=len(grid[0])
        queue=deque()
        num_1=0
        max_distance=0
        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j]==2:
                    queue.append((i,j,0))
                if grid[i][j]==1:
                    num_1=num_1+1
        if(len(queue)==0 and num_1==0):
            return 0 
        if len(queue)==0 and num_1!=0:
            return -1
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while(len(queue)>0):
            (row,column,distance)=queue.popleft()
            if(distance>max_distance):
                max_distance=distance
            for (dr,dc) in directions:
                new_row=row+dr
                new_column=column+dc
                if(new_row>=0 and new_row<ROWS and new_column>=0 and new_column<COLUMNS and grid[new_row][new_column]==1):
                    queue.append((new_row,new_column,distance+1))
                    grid[new_row][new_column]=2
                    num_1=num_1-1
        if num_1!=0:
            return -1
        else:
            return max_distance

