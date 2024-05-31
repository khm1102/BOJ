n = int(input())
m = input()
k = n - int(input())

t = True
if k < 0:
    k = 0

while k < n:
    if m[k] == '1':
        t = False
        break
    k += 1

print("YES" if t else "NO")
