n, k = map(int, input().split())

sieve = [True] * (n+1)
sieve[0] = sieve[1] = False

cnt = 0
for i in range(2, n+1):
    if sieve[i]:
        cnt += 1
        if cnt == k:
            print(i)
            break
        for j in range(i*i, n+1, i):
            if sieve[j]:
                sieve[j] = False
                cnt += 1
                if cnt == k:
                    print(j)
                    break
    if cnt == k:
        break
