import sys
def input(): return sys.stdin.readline().strip()
def f(x):return x if x < 10 else f(sum(map(int, str(x))))

for _ in range(int(input())):
    k, m = map(int, input().split())
    x, y, d = 0, 0, 0
    v = [0] * 10
    num = 1
    arr = []
    while k > 0:
        if v[num]:
            arr = arr[arr.index(num):]
            k %= (4 * len(arr))
            if k == 0:
                break
        v[num] = 1
        arr.append(num)
        x += [0, num, 0, -num][d]
        y += [num, 0, -num, 0][d]
        k, num, d = k - 1, f(num * m), (d + 1) % 4
    print(x, y)