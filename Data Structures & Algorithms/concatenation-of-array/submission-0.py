class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(2):
            for j in nums:
                arr.append(j)
        return arr