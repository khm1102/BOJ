import sys
def input(): return sys.stdin.readline().strip()

def mm(a, b):
    s = len(a)
    res = [[0 for _ in range(s)] for _ in range(s)]
    for i in range(s):
        for j in range(s):
            for k in range(s):
                res[i][j] += a[i][k] * b[k][j]
            res[i][j] %= 1000
    return res

def mp(a, n):
    s = len(a)
    res = [[0 for _ in range(s)] for _ in range(s)]
    for i in range(s):
        res[i][i] = 1
    while n > 0:
        if n % 2 == 1:
            res = mm(res, a)
        n //= 2
        a = mm(a, a)
    return res

def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        a = [[6, -4], [1, 0]]
        res = mp(a, n - 1)
        ans = (28 * res[1][0] + 6 * res[1][1] - 1) % 1000
        ans = (ans + 1000) % 1000
        ans_str = str(ans).zfill(3)
        print(f"Case #{i}: {ans_str}")

if __name__ == "__main__":
    main()
