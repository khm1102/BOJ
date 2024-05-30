MOD = 10 ** 9 + 7

input()
h = list(map(int, input().split()))
h.sort(reverse=True)

res = 0
for i in h:
    res = (res * 2 + i) % MOD

print(res)
