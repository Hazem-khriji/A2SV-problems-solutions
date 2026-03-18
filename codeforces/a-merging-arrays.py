n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ap,bp=0,0
while ap<n and bp<m:
    if a[ap]<b[bp]:
        print(a[ap],end=' ')
        ap += 1
    elif a[ap]>b[bp]:
        print(b[bp],end=' ')
        bp += 1
    else:
        print(a[ap],end=' ')
        print(b[bp],end=' ')
        ap+=1
        bp+=1
if ap<n:
    for i in range(ap,n):
        print(a[i],end=' ')
if bp<m:
    for i in range(bp,m):
        print(b[i],end=' ')
