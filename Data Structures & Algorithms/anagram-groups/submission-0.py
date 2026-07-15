class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for i in strs:
            counts=[0]*26
            for c in i:
                counts[ord(c)-ord('a')]=counts[ord(c)-ord('a')]+1
            tuple1=tuple(counts)
            groups[tuple1]=groups.get(tuple1,[])
            groups[tuple1].append(i)
        return list(groups.values())
