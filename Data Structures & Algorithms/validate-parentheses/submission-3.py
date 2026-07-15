class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        x=0
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            if i==')' or i==']' or i=='}':
                if(len(stack)==0):
                    return False
                x=stack.pop()
                if i==')':
                    if x=='[' or x=='{':
                        return False
                if i==']':
                    if x=='(' or x=='{':
                        return False
                if i=='}':
                    if x=='(' or x=='[':
                        return False
        if len(stack)!=0:
            return False
        return True
         