n, t= map(int, input().split())
a = list(map(int, input().split()))
curr=0
res=0
l=0
for r in range(n):
    curr+=a[r]
    while curr>t:
        curr-=a[l]
        l+=1
    res=max(res, r-l+1)
print(res)
