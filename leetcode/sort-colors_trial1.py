from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c= Counter(nums)
        i=0
        value_0=c[0]
        value_1=c[1]
        value_2=c[2]
        if(value_0>0):
            nums[:value_0]=[0]*value_0
        if(value_1>0):
            nums[value_0:value_0+value_1]=[1]*value_1
        if(value_2>0):
            nums[value_0+value_1::]=[2]*value_2  
