def kara(a,b):
    if len(str(a)) == 1 or len(str(b)) == 1:
        return a*b

    else:
        n = max(len(str(a)),len(str(b)))    
        k = n // 2

        a1 = a // 10**k 
        a0 = a % 10**k
        b1 = b // 10**k
        b0 = b % 10**k

        a1b1 = kara(a1,b1)
        a0b0 = kara(a0,b0)
        a1b0_plus_a0b1 = kara(a0+a1,b0+b1) - a1b1 - a0b0

        result = a1b1 * pow(10,k*2) + a1b0_plus_a0b1 * pow(10,k) + a0b0 

        return result

n,m = map(int,input().split())

print(kara(n,m))
