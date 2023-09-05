N = int(input())
heights = [int(input()) for _ in range(N)]

stack, max_area = [], 0

for i in range(N+1):
    while stack and (i == N or heights[i] < heights[stack[-1]]):
        h = heights[stack.pop()]
        w = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, h * w)
    stack.append(i)

print(max_area)
