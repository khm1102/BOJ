n = int(input())
v = list(map(int, input().split()))
s = int(input())

for i in range(n):
    if s == 0:
        break
    max_index = i
    for j in range(i + 1, min(n, i + s + 1)):
        if v[max_index] < v[j]:
            max_index = j
    s -= max_index - i
    v[i:max_index + 1] = [v[max_index]] + v[i:max_index]
    
print(*v)