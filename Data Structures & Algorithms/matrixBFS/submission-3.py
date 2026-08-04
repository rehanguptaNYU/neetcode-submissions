class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLUMNS=len(grid[0])
        visited=set()
        queue=deque([(0,0,0)])
        visited.add((0,0))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        if grid[0][0]==1 or grid[ROWS-1][COLUMNS-1]==1:
            return -1
        while len(queue)>0:
            for i in range(len(queue)):
                (row,column,distance)=queue.popleft()
                if (row,column)==(ROWS-1,COLUMNS-1):
                    return distance
                for (dr,dc) in directions:
                    new_row=row+dr
                    new_column=column+dc
                    if(new_row>=0 and new_row<ROWS and new_column>=0 and new_column<COLUMNS and (new_row,new_column) not in visited and grid[new_row][new_column]==0):
                        visited.add((new_row,new_column))
                        queue.append((new_row,new_column,distance+1))
        return -1