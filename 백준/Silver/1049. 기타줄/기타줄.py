N, M = map(int, input().split())

pack_min = 1001
one_min = 1001

for _ in range(M):
    pack, one = map(int, input().split())
    pack_min = min(pack_min, pack)
    one_min = min(one_min, one)

if pack_min > one_min * 6:
    res = N * one_min
else:
    res = (N // 6) * pack_min
    if pack_min > (N % 6) * one_min:
        res += one_min * (N % 6)
    else:
        res += pack_min

print(res)
