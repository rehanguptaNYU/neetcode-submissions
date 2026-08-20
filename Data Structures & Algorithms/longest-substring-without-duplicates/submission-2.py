class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        L=0
        R=0
        substring=set()
        while R<len(s):
            if s[R] not in substring:
                substring.add(s[R])
                R=R+1
            else:
                if len(substring)>longest:
                    longest=len(substring)
                substring.remove(s[L])
                L=L+1
        if len(substring)>longest:
            longest=len(substring)
        return longest