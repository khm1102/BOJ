n = int(input())
a = list(map(int, input().split()))

s = sum(a)
res = 0
b = [0]*(n+1)

for i in range(n):
    a.append(a[i])

for i in range(n):
    for j in range(n):
        b[j+1] = b[j] + a[i+j]
        if b[j+1] < 0:
            res += (-b[j+1]+s-1)//s

print(res)
