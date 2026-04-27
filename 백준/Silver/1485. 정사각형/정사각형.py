tc = int(input())

for _ in range(tc):
    x = []
    y = []
    for i in range(4):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)

    s = []
    for i in range(4):
        for j in range(i + 1, 4):
            s.append((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)

    s.sort()
    print(int(s[0] == s[1] == s[2] == s[3] and s[4] == s[5]))
