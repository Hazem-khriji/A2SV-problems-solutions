class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)-1):
            p=i
            for j in range(i+1,len(arr)):
                if(arr[j]<arr[p]):
                    p=j
            if(p!=i):
                arr[i],arr[p]=arr[p],arr[i]
        return arr
        
        
