import math
import sys
def input():
    return sys.stdin.readline()

n = int(input())
k = list(map(int, input().split()))

a = s = 1

for i in range(1, n):
    a += (k[i] > k[i - 1] and not s) or (k[i] < k[i - 1] and s)
    s ^= (k[i] > k[i - 1] and not s) or (k[i] < k[i - 1] and s)
print(int(math.ceil(math.log2(a))))
