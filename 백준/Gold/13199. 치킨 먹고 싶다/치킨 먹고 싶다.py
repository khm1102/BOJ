import sys;k=sys.stdin.readline
print(*[((c*(m//p)-c)//(f-c))-(c*(m//p)//f)if c*(m//p)>f else 0 for _ in range(int(k()))for p,m,f,c in [map(int,k().split())]])