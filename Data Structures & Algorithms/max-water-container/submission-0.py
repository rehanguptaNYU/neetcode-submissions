class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L=0
        R=len(heights)-1
        max_area=0
        while L<R:
            height=min(heights[L],heights[R])
            width=R-L
            area=height*width
            if area>max_area:
                max_area=area
            if heights[L]<=heights[R]:
                L=L+1
            else:
                R=R-1
        return max_area