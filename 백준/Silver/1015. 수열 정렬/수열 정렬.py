def find_p_array(n, a):
    pairs = [(a[i], i) for i in range(n)]

    pairs.sort()

    p = [0] * n
    for i, (_, index) in enumerate(pairs):
        p[index] = i

    return p

n = int(input())
a = list(map(int, input().split()))

p = find_p_array(n, a)
print(*p)
