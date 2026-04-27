f=-1e9
print(sum(y-max(x,f)+(f:=y)*0for x,y in sorted([*map(int,i.split())]for i in[*open(0)][1:])if y>f))