import math

def cmp(item):
    return (item[1], item[0])

def main():
    m, n = map(int, input().split())
    a = []
    f = list(map(int, input().split()))
    s = list(map(int, input().split()))
    for i in range(n):
        a.append((f[i], s[i]))

    if m == n:
        for i in range(n):
            if a[i][0] != a[i][1]:
                print(-1)
                return
        print(0)
        return

    a.sort(key=cmp)
    for i in range(n - 1):
        if a[i][1] == a[i + 1][1]:
            print(-1)
            return

    ans = 0
    cnt = 0

    for i in range(n - 1):
        if a[i][0] > a[i + 1][0]:
            ce = math.ceil((a[i][0] - a[i + 1][0]) / m) * m
            a[i + 1] = (a[i + 1][0] + ce, a[i + 1][1])

    for i in range(n):
        if a[i][0] + (cnt * m) < a[i][1]:
            cnt += 1

    for i in range(n):
        a[i] = (a[i][0] + cnt * m, a[i][1])

    if a[0][0] + m <= a[-1][0]:
        print(-1)
        return

    for i in range(n):
        ans += a[i][0] - a[i][1]

    print(ans)

if __name__ == "__main__":
    main()
