n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ap,bp=0,0
res=[]
for x in b:
    if(ap==n):
        res.append(n)
        continue
    else:
        while(ap<n and a[ap]<x):
            ap+=1
        res.append(ap)
print(*res)
