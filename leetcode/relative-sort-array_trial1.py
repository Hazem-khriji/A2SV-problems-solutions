from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        a = []
        for i in range(len(arr1)):
            if(arr1[i] not in arr2):
                a.append(arr1[i])
        a.sort()
        b=[]
        for i in range(len(arr2)):
            b+=[arr2[i]]*c[arr2[i]]
        return b+a