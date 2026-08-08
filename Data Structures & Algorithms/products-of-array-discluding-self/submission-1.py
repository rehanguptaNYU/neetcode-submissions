class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.prefix=[]
        pre_total=1
        for i in range(len(nums)):
            pre_total=pre_total*nums[i]
            self.prefix.append(pre_total)
        self.temp_postfix=[]
        post_total=1
        for i in range(-1,(-1*len(nums)-1),-1):
            post_total=post_total*nums[i]
            self.temp_postfix.append(post_total)
        self.postfix=[]
        for i in range(-1,(-1*len(self.temp_postfix)-1),-1):
            self.postfix.append(self.temp_postfix[i])
        self.output=[]
        for i in range(len(nums)):
            if len(self.output)==0:
                self.output.append(self.postfix[1])
            elif i==len(nums)-1:
                self.output.append(self.prefix[i-1])
            else:
                self.output.append(self.prefix[i-1]*self.postfix[i+1])
        return self.output
