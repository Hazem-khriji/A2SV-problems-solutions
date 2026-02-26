from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        a = [num for num in arr1 if num not in arr2]
        a.sort()
        b=[]
        for i in range(len(arr2)):
            b.extend([arr2[i]]*c[arr2[i]])
        return b+a