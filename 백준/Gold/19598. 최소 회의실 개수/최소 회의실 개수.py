arr = []
curr = res = 0

for _ in range(int(input())):
    s, e = map(int, input().split())
    arr.append((s, 1))
    arr.append((e, -1))
    
for _, i in sorted(arr):
    curr += i
    res = max(res, curr)

print(res)