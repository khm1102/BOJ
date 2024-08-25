n,m,k = map(int,input().split())
print(min((n+m-k) // 3,min(n//2, m)))