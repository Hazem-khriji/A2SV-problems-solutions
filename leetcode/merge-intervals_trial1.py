class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr=[]
        res=[]
        for i in range(len(intervals)):
            if(curr==[]):
                curr=intervals[i]
            else:
                if(intervals[i][0] <= curr[1]):
                    curr[1]=max(intervals[i][1],curr[1])
                else:
                    res.append(curr)
                    curr=intervals[i]
        if(curr != []):
            res.append(curr)
        return res
