class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result_arr=[0]*len(nums)
        index=len(nums)-1
        L=0
        R=len(nums)-1
        while L<=R:
            if abs(nums[L])>abs(nums[R]):
                result_arr[index]=(nums[L]**2)
                L=L+1
                index=index-1
            elif abs(nums[R])>abs(nums[L]):
                result_arr[index]=(nums[R]**2)
                R=R-1
                index=index-1
            elif abs(nums[R])==abs(nums[L]) and L!=R:
                result_arr[index]=(nums[R]**2)
                R=R-1
                index=index-1
                result_arr[index]=(nums[L]**2)
                L=L+1
                index=index-1
            elif abs(nums[R])==abs(nums[L]) and L==R:
                result_arr[index]=nums[R]**2
                L=L+1
        return result_arr
            
                
                    
            

