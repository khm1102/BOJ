import math

def eratos(n):
    chk = [1] * (n + 1)
    prime = []
    for i in range(2, n + 1):
        if chk[i]:
            prime.append(i)
            for j in range(i + i, n + 1, i):
                chk[j] = 0
    return prime

def solve(idx):
    a, b, n = map(int, input().split())
    divi = []
    m = {}
    flag = True
    while n > 1:
        flag = True
        for i in prime:
            if n % i == 0:
                n //= i
                flag = False
                m[i] = 1
                break
        if flag:
            break
    if n != 1:
        m[n] = 1
    for key in m:
        divi.append(key)

    ans = 0
    bit = 1 << len(divi)
    for i in range(1, bit):
        cnt = 0
        sum_val = 1
        for j in range(len(divi)):
            if not (i & (1 << j)):
                continue
            cnt += 1
            sum_val *= divi[j]
        aa = (a + sum_val - 1) // sum_val
        bb = b // sum_val
        if aa > bb:
            continue
        if cnt % 2 == 1:
            ans += bb - aa + 1
        else:
            ans -= bb - aa + 1
    print(f"Case #{idx}: {b - a + 1 - ans}")


global prime
prime = eratos(100000)
t = int(input())
for i in range(1, t + 1):
    solve(i)


    
    