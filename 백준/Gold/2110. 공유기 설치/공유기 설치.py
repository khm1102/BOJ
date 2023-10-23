import sys

def input(): return sys.stdin.readline().strip()
def print(val):return sys.stdout.write(str(val))

n, c = map(int, input().split())

# h = []
# for i in range(int(input())):
#     h.append(int(input()))

h = [int(input()) for _ in range(n)]
h.sort()

res = 0
left, right = 1, h[-1] - h[0]


while left <= right:
    mid = (left + right) // 2
    cnt = 1
    # print(cnt)
    temp = h[0]

    for i in h:
        if i - temp >= mid:
            cnt += 1
            # print(cnt)
            temp = i

    if cnt >= c:
        res = mid
        left = mid + 1

    else:right = mid - 1

print(res)
