def bitset_lcs(a, b):
    m, n = len(a), len(b)
    dp = [0] * (n + 1)

    for i in range(1, m + 1):
        prev = 0
        for j in range(1, n + 1):
            temp = dp[j]
            if a[i - 1] == b[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = temp

    return dp[n]

def is_prime(N):
    if N <= 1:
        return False
    if N <= 3:
        return True
    if N % 2 == 0 or N % 3 == 0:
        return False
    i = 5
    while i * i <= N:
        if N % i == 0 or N % (i + 2) == 0:
            return False
        i += 6
    return True

def find_prime(N):
    while not is_prime(N):
        N -= 1
    return N

def plcs_length(oa, ob, x, y):
    a = "".join(filter(lambda i: i != y, oa))
    b = "".join(filter(lambda i: i != y, ob))

    aidx = a.find(x)
    bidx = b.find(x)

    lcs1 = bitset_lcs(a[:aidx], b[:bidx])
    lcs2 = bitset_lcs(a[aidx:], b[bidx:])

    rst = lcs1 + lcs2

    if rst < 2:
        return -1

    return find_prime(rst)

oa = input()
ob = input()
x = input()
y = input()

print(plcs_length(oa, ob, x, y))
