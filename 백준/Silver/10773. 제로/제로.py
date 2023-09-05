import sys

stack = []
k = int(sys.stdin.readline().rstrip())

for i in range(k):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
