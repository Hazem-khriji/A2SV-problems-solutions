class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l,r=0,1
        while(r<n):
            if(nums[l]==0):
                if(nums[r]==0):
                    r+=1
                else:
                    nums[l],nums[r]=nums[r],nums[l]
            else:
                l+=1
                r+=1
        
