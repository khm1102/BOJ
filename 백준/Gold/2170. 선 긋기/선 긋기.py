n=int(input())
a=sorted([list(map(int,input().split()))for _ in range(n)])
s,e=a[0]
r=0
for x,y in a[1:]:
    if x<=e:e=max(e,y)
    else:r+=e-s;s,e=x,y
r+=e-s
print(r)