import sys
n = int(input().strip())
cnt = 2
while n > 0:
    cnt += (cnt - 1)
    n -= 1
print(cnt * cnt)