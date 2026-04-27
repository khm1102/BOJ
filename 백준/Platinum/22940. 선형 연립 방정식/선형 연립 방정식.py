l=[list(map(float,input().split()))for _ in range(int(input()))]
for i in range(len(l)):
    for j in range(len(l)):
        if i!=j:
            r=l[j][i]/l[i][i]
            for k in range(len(l[0])):l[j][k]-=r*l[i][k]
    l[i]=[x/l[i][i]for x in l[i]]
print(*[f'{r[-1]:.0f}'for r in l])