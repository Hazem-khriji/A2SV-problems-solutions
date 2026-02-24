class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = {}
        res= 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=[i]
            else:
                d[nums[i]].append(i)
        for key,value in d.items():
            if(len(value))>1:
                for i in range(len(value)-1):
                    for j in range(i+1,len(value)):
                        if (value[i]*value[j])%k==0:
                            res+=1
        return res