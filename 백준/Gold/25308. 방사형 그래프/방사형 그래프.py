from math import sqrt
from itertools import permutations
arr = list(map(int, input().split()))
print(sum(1 for p in permutations(range(8))
              if all(arr[p[i]] * arr[p[(i + 2) % 8]] * sqrt(2) <= arr[p[(i + 1) % 8]] * (arr[p[i]] + arr[p[(i + 2) % 8]])
                     for i in range(8))))