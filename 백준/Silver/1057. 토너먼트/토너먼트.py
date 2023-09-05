def find(n, k, l):
    round = 1

    while True:
        if abs(k - l) == 1 and max(k, l) % 2 == 0:
            return round

        k = (k + 1) // 2
        l = (l + 1) // 2

        round += 1

        if n == 1:  
            break

        n = (n + 1) // 2

    return -1

n, k, l = map(int, input().split())

print(find(n, k, l))
