import sys;input = sys.stdin.readline
for _ in range(int(input())):
	p,m,f,c=map(int,input().split())
	print(((c*(m//p)-c)//(f-c))-(c*(m//p)//f)if c*(m//p)>f else 0)