class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          maps={}
          count=0
          for i in nums:
            maps[i]=count
            count=count+1
            for j in range(len(nums)):
                val=nums[j]
                diff=target-val
                if diff in maps and maps[diff]!=j:
                    if(j<maps[diff]):
                        return[j,maps[diff]]
                    else:
                        return[maps[diff],j]
        
            
        