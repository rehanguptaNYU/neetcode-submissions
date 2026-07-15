class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum=0
        list1=[]
        for i in nums:
            if(i==0):
                list1.append(sum)
                sum=0
            else:
                sum=sum+i
        list1.append(sum)
        return max(list1)
        