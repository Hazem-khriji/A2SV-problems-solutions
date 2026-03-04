class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        athletes=sorted(score,reverse=True)
        res= []
        for sc in score:
            index = athletes.index(sc)
            if(index==0):
                res.append("Gold Medal")
            elif(index==1):
                res.append("Silver Medal")
            elif(index==2):
                res.append("Bronze Medal")
            else:
                res.append(str(index+1))
        return res
