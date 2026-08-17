class Solution:
    def isPalindrome(self, s: str) -> bool:
        length=len(s)
        L=0
        R=length-1
        while L<=R:
            while L<=R and s[L].isalnum()==False:
                L=L+1
            while L<=R and s[R].isalnum()==False:
                R=R-1
            if(L>R):
                return True
            if(s[L].isupper()==True and s[R].islower()==True):
                if s[L]!=s[R].upper():
                    return False
            elif(s[L].islower()==True and s[R].isupper()==True):
                if(s[L].upper()!=s[R]):
                    return False
            else:
                if(s[L]!=s[R]):
                    return False
            L=L+1
            R=R-1
        return True