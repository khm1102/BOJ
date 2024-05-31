n, w = int(input()),sorted(map(int, input().split()))
s = 0
for i in w:
    if i > s + 1:
        break
    s += i
print(s + 1)
