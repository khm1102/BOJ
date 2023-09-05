import math
n = int(input())
ans = 0
if n % 2 == 1:
    ans = (n // 2) * (n // 2)
else:
    ans = (n // 2) * (n // 2) - (n // 2)
print(ans)
ans = 0
factors = []
chk = [False] * (n + 1)
for i in range(1, (n // 2) + 1):
    if n % i == 0:
        factors.append(i)
        chk[i] = True
chk[n] = True
for i in range(len(factors)):
    for j in range(i, len(factors)):
        x = factors[i]
        y = factors[j]
        if chk[x + y]:
            ans += 1
print(ans)
ans = 0
prime = [True] * (n + 1)
prime[0] = prime[1] = False
for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i]:
        for j in range(i * i, n + 1, i):
            prime[j] = False
for i in range(n - 1):
    if prime[i] and prime[i + 2]:
        ans += 1
print(ans)