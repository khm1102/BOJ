K, N = map(int, input().split())
lan_cables = []

for _ in range(K):
    lan_cables.append(int(input()))

start = 1
end = max(lan_cables)

result = 0
while start <= end:
    mid = (start + end) // 2
    count = 0

    for cable in lan_cables:
        count += cable // mid

    if count >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
