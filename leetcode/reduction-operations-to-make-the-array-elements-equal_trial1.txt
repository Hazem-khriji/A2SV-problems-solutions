class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        curr=0
        for i in range(len(nums)-1,0,-1):
            curr+=1
            if(nums[i]!=nums[i-1]):
                res+=curr
        return res
