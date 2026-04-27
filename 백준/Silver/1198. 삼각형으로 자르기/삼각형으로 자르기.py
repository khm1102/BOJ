def g(a, b, c, p):return abs((p[a][1]-p[b][1])*(p[c][0]-p[b][0])-(p[a][0]-p[b][0])*(p[c][1]-p[b][1]))
n = int(input())
p = []
for _ in range(n):
    x,y = map(int,input().split())
    p.append((x, y))
a = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            a = max(a,g(i,j,k,p))
print(a/2)