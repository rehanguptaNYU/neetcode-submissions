class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[]
        for i in range(len(nums)+1):
            freq.append([])
        counts={}
        for i in nums:
            counts[i]=counts.get(i,0)
            counts[i]=counts[i]+1
        for (key,val) in counts.items():
            freq[val].append(key)
        iterator=len(nums)
        result=[]
        counter=0
        while(counter<k):
            if(len(freq[iterator])!=0):
                internal=0
                while(internal<len(freq[iterator]) and counter<k):
                    result.append(freq[iterator][internal])
                    counter=counter+1
                    internal=internal+1
                iterator=iterator-1
            else:
                iterator=iterator-1
        return result

        
            
        