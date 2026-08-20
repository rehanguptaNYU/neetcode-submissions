class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()
        L=0
        R=0
        while R<len(nums):
            if R-L<=k:
                if nums[R] not in window:
                    window.add(nums[R])
                    R=R+1
                else:
                    return True
            else:
                window.remove(nums[L])
                L=L+1
        return False

