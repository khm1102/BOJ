n = int(input())
straws = []
for i in range(n):
    straws.append(int(input()))

straws.sort(reverse=True)

max_sum = -1
for i in range(n-2):
    if straws[i] < straws[i+1] + straws[i+2]:
        max_sum = max(max_sum, straws[i] + straws[i+1] + straws[i+2])

if max_sum == -1:
    print(-1)
else:
    print(max_sum)
