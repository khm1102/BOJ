def modulo(a, b):
    sum = 1

    while b:
        if b % 2:
            sum = sum * a % mod
        a = a * a % mod
        b //= 2

    return sum

def go(x):
    if not x:
        return 1
    if x == 1:
        return (r + 1) % mod
    if x % 2:
        return go(x // 2) * (1 + modulo(r, x // 2 + 1)) % mod
    return (go(x // 2 - 1) * (1 + modulo(r, x // 2)) % mod + modulo(r, x) % mod) % mod

if __name__ == "__main__":
    aa, r, n, mod = map(int, input().split())
    if not mod:
        print("0")
    else:
        print(aa * go(n - 1) % mod)
