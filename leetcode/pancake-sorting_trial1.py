class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res=[]
        for i in range(len(arr)-1,0,-1):
            p = i
            for j in range(i):
                if(arr[j]<arr[p]):
                    p = j
            if(p!=i):
                arr[:p+1] = arr[:p+1][::-1]
                res.append(p+1)
                arr[:i+1] = arr[:i+1][::-1]
                res.append(i+1)
        res.append(len(arr))
        print(arr[::-1])
        return res
                    
                
