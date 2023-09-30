M = 55

def G(x):
    r = x & 1

    for i in range(M - 1, 0, -1):
        if x & (1 << i):
            r += P[i - 1] + (x - (1 << i) + 1)
            x -= 1 << i

    return r

A, B = map(int, input().split())

P = [0] * M
P[0] = 1
for i in range(1, M):
    P[i] = 2 * P[i - 1] + (1 << i)

R = G(B) - G(A - 1)
print(R)
