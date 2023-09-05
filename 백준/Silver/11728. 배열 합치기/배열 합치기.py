n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
res = a+b
res.sort()
print(*res)