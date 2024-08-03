def c(d,a,n):
    q,w=0,0
    for i in range(1,n):
        q+=abs(a[i]-i*d)
        w+=abs(a[i]-i*(d+1))
    return q if q<w else-1
def p(l,r,a,n):
    b=0
    while l<r:
        m=(l+r)//2
        t=c(m,a,n)
        if t==-1:l=m+1
        else:r=m;b=t
    return b
n=int(input())
a=list(map(int,input().split()))
print(p(1,a[n-1],a,n))