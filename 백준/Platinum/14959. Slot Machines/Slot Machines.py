n = int(input())
p = input().split()[::-1]

t = float('inf')
k = 0
q = 0
pi = [0]

for i in range(1, len(p)):
    j = pi[i - 1]
    while j > 0 and p[i] != p[j]:
        j = pi[j - 1]
    j += p[i] == p[j]
    pi.append(j)

for i, v in enumerate(pi):
    x, y = len(pi) - (i + 1), i + 1 - v
    if x + y < t:
        t, k, q = x + y, x, y

print(k, q)
