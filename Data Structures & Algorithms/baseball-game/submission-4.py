class Solution:
    def calPoints(self, operations: List[str]) -> int:
        list1=[]
        for i in range(len(operations)):
            if(operations[i]!='+' and operations[i]!='D' and operations[i]!='C'):
                list1.append(int(operations[i]))
            if(operations[i]=="D"):
                list1.append(2 * list1[-1])
            if(operations[i]=="C"):
                list1.pop()
            if(operations[i]=="+"):
                val=list1[-2]+list1[-1]
                list1.append(val)
        return sum(list1)