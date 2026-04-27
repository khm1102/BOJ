from collections import deque

def solve(arr):
    res = []
    arr = deque(arr)
    while arr:
        res.append(arr[0][1])
        temp = arr.popleft()[0]
        
        if temp > 0:
            arr.rotate(-temp + 1)
        else:
            arr.rotate(-temp)
    return res

n = int(input())
arr = list(map(int, input().split()))
arr = [(arr[i], i + 1) for i in range(n)]
print(*solve(arr))
