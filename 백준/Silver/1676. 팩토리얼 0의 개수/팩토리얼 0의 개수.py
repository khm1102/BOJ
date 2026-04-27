N = int(input())
print(sum(N // 5**i for i in range(1, N//5 + 1)))
