def solution():
    n = int(input())
    if n == 1:
        print(0)
        return
    a = int(input())
    arr = [int(input()) for _ in range(n - 1)]
    cnt = 0
    while True:
        arr.sort()
        if arr[-1] < a:
            break
        cnt += 1
        arr[-1] -= 1
        a += 1
    print(cnt)

if __name__ == "__main__":
    solution()
