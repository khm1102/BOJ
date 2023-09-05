n = int(input())

a = []
for _ in range(n):
    s, e = map(int, input().split())
    a.append((s, e))

a.sort(key=lambda x: (x[1], x[0]))  

cnt = 1
cur = a[0] 
for i in range(1, n):
    nx = a[i]  
  
    if nx[0] >= cur[1]:
        cnt += 1
        cur = nx

print(cnt)
