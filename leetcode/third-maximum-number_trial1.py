class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1=max2=max3= None
        for num in nums:
            if num==max1 or num==max2 or num==max3:
                continue
            if max1 is None or num>max1:
                max1,max2,max3 = num,max1,max2
            elif max2 is None or num>max2:
                max2,max3 = num,max2 
            elif max3 is None or num>max3:
                max3 = num
        if(max3!=None):
            return max3
        return max1
                
            