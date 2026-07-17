import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1=[]
        count=Counter(nums)
        for (key,val) in count.items():
            list1.append((-val,key))
        result=[]
        heapq.heapify(list1)
        for i in range(k):
            (final_val,final_key)=heapq.heappop(list1)
            result.append(final_key)
        return result
        