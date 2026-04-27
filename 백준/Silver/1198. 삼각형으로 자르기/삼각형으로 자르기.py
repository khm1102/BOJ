_,*p=[[*map(int,v.split())]for v in open(0)]
print(max(a*(d-f)+c*(f-b)+e*(b-d)for a,b in p for c,d in p for e,f in p)/2)