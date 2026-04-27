n=int(input())
s=[input() for _ in range(n)]
l=len(s[0])
for i in range(1,l+1):
    if len(set(x[-i:] for x in s))==n:
        print(i)
        break