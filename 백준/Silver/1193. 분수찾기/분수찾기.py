n=int(input());i=1
while n>i:n-=i;i+=1
a=n;b=i-n+1
if i%2:a,b=b,a
print(f"{a}/{b}")