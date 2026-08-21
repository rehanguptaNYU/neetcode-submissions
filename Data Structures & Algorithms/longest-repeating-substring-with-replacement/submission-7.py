class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap={}
        R=0
        L=0
        longest=0
        while R<len(s):
            charMap[s[R]]=charMap.get(s[R],0)+1
            window_length=R-L+1
            max_freq=max(list(charMap.values()))
            if window_length-max_freq<=k:
                R=R+1
                if window_length>longest:
                    longest=window_length
            else:
                charMap[s[L]]=charMap.get(s[L])-1
                L=L+1
                R=R+1
        return longest


        