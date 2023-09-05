def func(cnt, n, m, arr, res, chk):
    if cnt == m:
        print(*res)
        return

    xx = 0
    for i in range(n):
        if not chk[i] and arr[i] != xx:
            res[cnt] = arr[i]
            xx = res[cnt]
            chk[i] = True
            func(cnt + 1, n, m, arr, res, chk)
            chk[i] = False

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    res = [0] * m
    chk = [False] * n
    func(0, n, m, arr, res, chk)

if __name__ == "__main__":
    main()
