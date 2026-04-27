def c(x, y):
    return x - y, x + y

def f(x, y, X, Y, k):
    return sum(1 for i in range(len(X)) if X[i] >= x and X[i] <= x + k and Y[i] >= y and Y[i] <= y + k)

def o(n, m, t, k, p):
    X, Y = zip(*[c(x, y) for x, y in p])
    max_points = 0
    mx = my = 0

    for i in range(t):
        for j in range(t):
            x = X[i]
            y = Y[j]
            if (x + y) % 2:
                xv = [x, x, x - 1, x + 1]
                yv = [y + 1, y - 1, y, y]
            else:
                xv = [x]
                yv = [y]

            for idx in range(len(xv)):
                x = xv[idx]
                y = yv[idx]
                u = y - x
                if x + y + k > 2 * n:
                    x = n - u // 2 - k // 2
                    y = n + u // 2 - k // 2

                count = f(x, y, X, Y, k)

                if max_points < count:
                    max_points = count
                    mx = x + k // 2
                    my = y + k // 2

    return (mx + my) // 2, (my - mx) // 2, max_points


n, m, t, k = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(t)]

mx, my, ans = o(n, m, t, k, points)
print(mx, my)
print(ans)
