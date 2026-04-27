p=[[*map(int,input().split())]for _ in range(int(input()))]
print(max(a*d+c*f+e*b-c*b-e*d-a*f for a,b in p for c,d in p for e,f in p)/2)