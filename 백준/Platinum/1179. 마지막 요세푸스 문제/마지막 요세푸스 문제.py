n,k=map(int,input().split())

if k==1:
    print(n)
else:
    a=0
    b=1
    for _ in range(n):
        x=(b-a-1)//(k-1)+1
        if b+x>n:
            a+=(n-b)*k
            break
        a=(a+k*x)%(b+x)
        b+=x

    print(a+1)
