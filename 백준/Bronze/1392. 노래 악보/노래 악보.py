n, k = map(int, input().split())
list_a = [int(input()) for _ in range(n)]
for _ in range(k):
    t = int(input())
    for i in range(n):
        if t < sum(list_a[:i+1]):
            print(i+1)
            break