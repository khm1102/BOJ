n, k = map(int, input().split())

idx = 1
while k > 9 * 10**(idx - 1) * idx:
    k -= 9 * 10 ** (idx - 1) * idx
    idx += 1

num = 10 ** (idx - 1) + (k - 1) // idx
if num > n:
    print("-1")
else:
    print(str(num)[(k - 1) % idx])