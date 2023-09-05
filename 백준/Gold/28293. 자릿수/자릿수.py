import math
a, b = map(int, input().split())
print(math.floor(b * math.log10(a))+1)