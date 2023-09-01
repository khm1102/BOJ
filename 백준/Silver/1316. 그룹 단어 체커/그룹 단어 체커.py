n = int(input())
cnt = 0

for _ in range(n):
    w = input()
    s = set()
    g = True

    for i, c in enumerate(w):
        if c in s:
            if i > 0 and w[i - 1] != c:
                g = False
                break
        else:s.add(c)

    if g:cnt += 1

print(cnt)
