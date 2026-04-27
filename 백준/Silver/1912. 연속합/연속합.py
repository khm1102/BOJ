import sys
def input(): return sys.stdin.readline().strip()
def print(val): sys.stdout.write(str(val))

n = int(input())
arr = list(map(int, input().split()))
cur_sum = max_sum = arr[0]

for i in range(1, n):
    cur_sum = max(arr[i], cur_sum + arr[i])
    max_sum = max(max_sum, cur_sum)

print(max_sum)