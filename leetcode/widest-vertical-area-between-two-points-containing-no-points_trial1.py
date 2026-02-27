class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l = sorted(point[0] for point in points)
        print(l)
        res = 0
        for i in range(len(l)-1):
            res=max(res,l[i+1]-l[i])
        return res