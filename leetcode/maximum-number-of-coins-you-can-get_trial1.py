class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)
        part=n//3
        res=0
        i = n-2
        while(part>0):
            res+=piles[i]
            i-=2
            part-=1
        return res
