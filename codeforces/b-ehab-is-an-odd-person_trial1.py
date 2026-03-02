n = int(input())
a = list(map(int, input().split()))
even= False
odd= False

for num in a:
    if num % 2 == 0:
        even=True
    else:
        odd=True
    if(even and odd):
        break
if(even and odd):
    a.sort()
for num in a:
    print(num, end=' ')