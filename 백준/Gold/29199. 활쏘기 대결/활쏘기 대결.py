def solve(N, A):
    S = [0] * (N + 1)
    R = [0] * (N + 1)
    
    for i in range(1, N + 1):
        S[i] = S[i - 1] + A[i - 1]
    
    R[1] = max(0, S[1])
    for i in range(2, N + 1):
        R[i] = max(R[i - 1], S[i] - R[i - 1])
    
    return R[N]
N = int(input())
A = list(map(int, input().split()))

print(solve(N, A))
