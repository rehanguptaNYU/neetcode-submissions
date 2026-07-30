class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color=image[sr][sc]
        if original_color==color:
            return image
        def dfs(image,sr,sc,original_color,color):
            ROWS=len(image)
            COLUMNS=len(image[0])
            if (min(sr,sc)<0 or sr==ROWS or sc==COLUMNS):
                return None
            if(image[sr][sc]==original_color):
                image[sr][sc]=color
                dfs(image,sr+1,sc,original_color,color)
                dfs(image,sr-1,sc,original_color,color)
                dfs(image,sr,sc+1,original_color,color)
                dfs(image,sr,sc-1,original_color,color)
            else:
                return None
        dfs(image,sr,sc,original_color,color)
        return image
            


