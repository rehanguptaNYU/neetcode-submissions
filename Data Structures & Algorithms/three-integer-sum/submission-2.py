class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a_index=0
        result_arr=[]
        result_set=set()
        for i in range(len(nums)-1):
            a=nums[i]
            L=i+1
            R=len(nums)-1
            while L<R:
                sum1=nums[L]+nums[R]
                if sum1+a==0:
                    if (a,nums[L],nums[R]) not in result_set:
                        result_arr.append([a,nums[L],nums[R]])
                        result_set.add((a,nums[L],nums[R]))
                    L=L+1
                    R=R-1
                elif sum1+a<0:
                    L=L+1
                elif sum1+a>0:
                    R=R-1
        return result_arr




