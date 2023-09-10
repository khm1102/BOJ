N, M, K = map(int, input().split())
strings = []
for _ in range(N):
    s = input().strip()
    strings.append(''.join(sorted(s)))

strings.sort()
T = ''.join(strings[:K])

sorted_T = ''.join(sorted(T))
print(sorted_T)