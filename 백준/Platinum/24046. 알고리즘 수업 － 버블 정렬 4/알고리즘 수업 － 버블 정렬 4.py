def solve(n, k, a):
    if n * (n - 1) // 2 < k:
        return "-1"

    idx = list(range(n - 1))
    while idx:
        arr = []
        for idx_p in idx:
            if a[idx_p] > a[idx_p + 1]:
                a[idx_p], a[idx_p + 1] = a[idx_p + 1], a[idx_p]
                k -= 1
                if k == 0:
                    return f"{a[idx_p]} {a[idx_p + 1]}"
                if idx_p > 0:
                    arr.append(idx_p - 1)
        idx = arr

    return "-1"


n, k = map(int, input().split())  
arr = list(map(int, input().split()))


print(solve(n, k, arr))

