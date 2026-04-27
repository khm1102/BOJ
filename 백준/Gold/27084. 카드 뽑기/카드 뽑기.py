from collections import Counter
from math import prod
input();print((prod(i + 1 for i in Counter(list(map(int, input().split()))).values()) - 1) % (10**9 + 7))