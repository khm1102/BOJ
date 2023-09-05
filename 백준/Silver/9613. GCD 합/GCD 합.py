def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def sol(arr):
    cnt = 0
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            cnt += gcd(arr[i], arr[j])

    print(cnt)
    return 0


for _ in range(int(input())):
    sol(list(map(int, input().split()[1:])))
