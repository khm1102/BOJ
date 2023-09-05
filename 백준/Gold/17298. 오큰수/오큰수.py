def f(arr):
    n = len(arr)
    res = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            res[stack.pop()] = arr[i]
        stack.append(i)
    return res

n = int(input())
k = list(map(int, input().split()))
print(*f(k))