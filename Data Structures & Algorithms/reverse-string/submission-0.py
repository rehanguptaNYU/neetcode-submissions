class Solution:
    def reverseString(self, s: List[str]) -> None:
        L=0
        R=len(s)-1
        while L<=R:
            temp=s[L]
            s[L]=s[R]
            s[R]=temp
            L=L+1
            R=R-1
        return s
        