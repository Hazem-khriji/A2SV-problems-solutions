class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,r = 0,n-1
        maxi = (n-1)*min(height[l],height[r])
        while(l<r-1):
            if(height[l]<=height[r]):
                l+=1
            else:
                r-=1
            maxi =max(maxi,(r-l)*min(height[l],height[r]))
        return maxi 
                
                

            


                