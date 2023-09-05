a,b = map(int, input().split())
arr = [0]
cnt = 1

for i in range(1, (b+1) // 2 + 1):
    for j in range(cnt):
        arr.append(cnt)
    cnt += 1

for i in range(1, b+1):
    arr[i] += arr[i-1]
print(arr[b] - arr[a-1])