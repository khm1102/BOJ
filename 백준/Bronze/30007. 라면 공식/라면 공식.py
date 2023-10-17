
N = int(input())


for _ in range(N):
    A, B, X = map(int, input().split())
    

    W = A * (X - 1) + B

    print(W)
