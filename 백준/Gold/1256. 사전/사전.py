def find_kth_string(N, M, K):
    if K > comb(N + M, N):
        return -1

    result = ''
    while N > 0 or M > 0:
        if N == 0:
            result += 'z'
            M -= 1
        elif M == 0:
            result += 'a'
            N -= 1
        else:
            cnt = comb(N + M - 1, N - 1)
            if K <= cnt:
                result += 'a'
                N -= 1
            else:
                result += 'z'
                M -= 1
                K -= cnt

    return result

def comb(n, r):
    if r > n - r:
        r = n - r
    result = 1
    for i in range(r):
        result *= n - i
        result //= i + 1
    return result

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    answer = find_kth_string(N, M, K)
    print(answer)
