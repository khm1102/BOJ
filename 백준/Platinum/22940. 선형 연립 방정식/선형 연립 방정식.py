def f(m):
    n=len(m)
    for i in range(n):
        d=m[i][i];
        for j in range(i,n+1):m[i][j]/=d
        for j in range(n):
            if i==j:continue
            d=-m[j][i]
            for k in range(n+1):m[j][k]+=m[i][k]*d
    return[row[n]for row in m]
l=[]
[l.append(list(map(float, input().split()))) for i in range(int(input()))]
print(*[f'{i:.0f}'for i in f(l)])