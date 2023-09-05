def gcd(n, a):
    if a == 0:
        return n
    return gcd(a, n % a)

def extended_euclid(n, a):
    Si = [1, 0]
    Ti = [0, 1]
    Ri = [n, a]
    Qi = n // a
    while True:
        r2 = Ri[-2]
        r1 = Ri[-1]
        
        temp = r2 % r1
        Ri.append(temp)
        if temp == 0:
            return Ti[-1]
        Qi = r2 // r1
        Si.append(Si[-2] - Si[-1] * Qi)
        Ti.append(Ti[-2] - Ti[-1] * Qi)

def main():
    n, a = map(int, input().split())
 
    print(n - a, end=" ")
    if gcd(n, a) != 1:
        print(-1)
        return
 
    ret = extended_euclid(n, a)
    while ret < 0:
        ret += n
 
    print(ret)

if __name__ == "__main__":
    main()
