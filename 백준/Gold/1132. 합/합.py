
n = int(input())
numbers = [input() for _ in range(n)]

use = [0] * 10
check = [False] * 10

for num in numbers:
    check[ord(num[0]) - 65] = True
    d = 1
    for j in range(len(num) - 1, -1, -1):
        use[ord(num[j]) - 65] += d
        d *= 10

remaining_digits = [i for i in range(10) if not check[i]]
z = min(remaining_digits, key=lambda i: use[i])

use[z] = 0
use.sort(reverse=True)

ans = sum((9 - i) * use[i] for i in range(10))
print(ans)
