def maximize_ability(N, K, A):
    max_ability = 0
    for bit in range(20, -1, -1):
        count = 0
        new_max_ability = max_ability | (1 << bit)
        
        for i in range(N):
            if (A[i] & new_max_ability) == new_max_ability:
                count += 1
        
        if count >= K:
            max_ability = new_max_ability
    
    return max_ability

N, K = map(int, input().split())
A = list(map(int, input().split()))
print(maximize_ability(N, K, A))