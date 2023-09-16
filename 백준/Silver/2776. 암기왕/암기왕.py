T = int(input())

for _ in range(T):
    N = int(input())
    notebook1 = set(map(int, input().split()))

    M = int(input())
    notebook2 = list(map(int, input().split()))

    for num in notebook2:
        if num in notebook1:
            print(1)
        else:
            print(0)
