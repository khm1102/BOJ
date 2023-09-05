def find_list(N, L):
    for length in range(L, 101):
        start = (2 * N - length * (length - 1)) // (2 * length)
        
        if start >= 0 and start * length + length * (length - 1) // 2 == N:
            return list(range(start, start + length))
    
    return None

N, L = map(int, input().split())

result = find_list(N, L)

if result is None:print(-1)
else:print(' '.join(map(str, result)))