class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1=set()
        if(len(s)!=len(t)):
            return False
        for i in s:
            set1.add(i)
        for j in t:
            if j not in set1:
                return False
        s_hashmap={}
        for i in s:
            if i not in s_hashmap:
                s_hashmap[i]=0
            else:
                s_hashmap[i]=s_hashmap[i]+1
        t_hashmap={}
        for i in t:
            if i not in t_hashmap:
                t_hashmap[i]=0
            else:
                t_hashmap[i]=t_hashmap[i]+1
        for i in s_hashmap:
            if s_hashmap[i]!=t_hashmap[i]:
                return False
        return True


        
