class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for i in strs:
            result=result+str(len(i))+'#'+i
        return result
    def decode(self, s: str) -> List[str]:
        starting=0
        j=0
        result=[]
        while(starting<len(s)):
            while(s[j]!='#'):
                j=j+1
            length=int(s[starting:j])
            result.append(s[j+1:j+length+1])
            j=j+length+1
            starting=j
        return result