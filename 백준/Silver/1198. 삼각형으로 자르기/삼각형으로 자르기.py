p=[[*map(int,input().split())]for _ in range(int(input()))]
print(max(a*(d-f)+c*(f-b)+e*(b-d)for a,b in p for c,d in p for e,f in p)/2)