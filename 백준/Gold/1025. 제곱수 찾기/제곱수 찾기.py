n, m = map(int, input().split())
grid = [input().rstrip() for _ in range(n)]
ans = -1
for i in range(n):
    for j in range(m):
        for k in range(-n + 1, n):
            for t in range(-m + 1, m):
                if k == 0 and t == 0:
                    v = int(grid[i][j])
                    r = int(v ** 0.5)
                    if r * r == v and v > ans:
                        ans = v
                else:
                    x = i;
                    y = j;
                    s = ''
                    while 0 <= x < n and 0 <= y < m:
                        s += grid[x][y]
                        v = int(s)
                        r = int(v ** 0.5)
                        if r * r == v and v > ans:
                            ans = v
                        x += k;
                        y += t
print(ans)
