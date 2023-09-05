def f(n, xi):
    total_sum = 0
    

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + xi[i - 1]

    for a in range(1, n):
        total_sum += (prefix_sum[n] - prefix_sum[a]) * xi[a - 1]
    
    return total_sum

n = int(input())
xi = list(map(int, input().split()))

result = f(n, xi)
print(result)
