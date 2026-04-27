n = int(input())
h = list(map(int, input().split()))
stack, res = [], [0] * n

for i in range(n):
    while stack and h[stack[-1]] <= h[i]:
        stack.pop()
    res[i] = stack[-1] + 1 if stack else 0
    stack.append(i)

print(*res)