n = int(input())
cnt = 1
i = 1
while n > i:
    i += 6 * cnt
    cnt += 1
print(cnt)