n=int(input())
s=[input().strip()for _ in range(n)]
s.sort(key=lambda x:(len(x),sum(int(d)for d in x if d.isdigit()),x))
print(*s,sep='\n')