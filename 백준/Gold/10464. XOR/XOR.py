T = int(input())
for _ in range(T):
    S, F = map(int, input().split())
    
    def xor_sum(n):
        if n % 4 == 0:
            return n
        if n % 4 == 1:
            return 1
        if n % 4 == 2:
            return n + 1
        return 0
    
    result = xor_sum(F) ^ xor_sum(S - 1)
    print(result)

