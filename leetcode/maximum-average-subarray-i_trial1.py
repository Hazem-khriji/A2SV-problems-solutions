class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pref = [nums[0]]
        for i in range(1,len(nums)):
            pref.append(pref[i-1]+nums[i])
        maxi = pref[k-1]
        for i in range(k,len(nums)):
            maxi = max(maxi , pref[i]-pref[i-k])
        return maxi/k