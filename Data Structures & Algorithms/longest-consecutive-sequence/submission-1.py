class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        longest=[]
        for i in nums:
            k=i
            list1=[]
            while(k in set1 and i-1 not in set1):
                list1.append(k)
                k=k+1
            print(list1)
            if(len(list1)>len(longest)):
                longest=list1
        return len(longest)


                