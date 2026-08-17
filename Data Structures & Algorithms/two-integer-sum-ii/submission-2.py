class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result_arr=[]
        L=0
        R=len(numbers)-1
        sum1=0
        while L<R:
            sum1=numbers[L]+numbers[R]
            if sum1==target:
                result_arr.append(L+1)
                result_arr.append(R+1)
                return result_arr
            elif sum1>target:
                R=R-1
            elif sum1<target:    
                L=L+1
        return result_arr
            
