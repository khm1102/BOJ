N = int(input())
v = []
for _ in range(N):
    x, r = map(int, input().split())
    v.append((x - r, -1))
    v.append((x + r, 1))

v.sort(key=lambda x: (x[0], -x[1]))

ans = 0
last = 0
s = []

for i in range(len(v)):
    if not s:
        s.append((v[i][0], 0))
        last = v[i][0]
    elif v[i][1] == -1:
        if v[i][0] == last:
            vec_tmp = []
            tmp = s.pop()
            if tmp[1] != -1:
                tmp = (tmp[0], 1)
            s.append(tmp)
            s.append((v[i][0], 0))
        else:
            tmp = s.pop()
            tmp = (tmp[0], -1)
            s.append(tmp)
            s.append((v[i][0], 0))
            last = v[i][0]
    elif v[i][1] == 1:
        tmp = s.pop()
        if tmp[1] == 1 and last == v[i][0]:
            ans += 2
        else:
            ans += 1
        last = v[i][0]

print(ans + 1)