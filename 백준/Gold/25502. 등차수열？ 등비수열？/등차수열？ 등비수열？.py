import sys

def check(num1, num2):
    return num1 >= num2 and num1 % num2 == 0

def increase(m, val):
    if val in m:
        m[val] += 1
    else:
        m[val] = 1

def decrease(m, val):
    if val in m:
        if m[val] == 1:
            del m[val]
        else:
            m[val] -= 1

n, m = map(int, sys.stdin.readline().split())

arr = [0] * 300001
a = {}
g = {}

arr_values = list(map(int, sys.stdin.readline().split()))

for i in range(1, n + 1):
    arr[i] = arr_values[i - 1]
    if i >= 2:
        if arr[i] > arr[i - 1]:
            increase(a, arr[i] - arr[i - 1])

        if check(arr[i], arr[i - 1]):
            increase(g, arr[i] // arr[i - 1])

output = []

for _ in range(m):
    i, x = map(int, sys.stdin.readline().split())

    if i > 1:
        if arr[i] > arr[i - 1]:
            decrease(a, arr[i] - arr[i - 1])
        if x > arr[i - 1]:
            increase(a, x - arr[i - 1])
        if check(arr[i], arr[i - 1]):
            decrease(g, arr[i] // arr[i - 1])
        if check(x, arr[i - 1]):
            increase(g, x // arr[i - 1])

    if i < n:
        if arr[i + 1] > arr[i]:
            decrease(a, arr[i + 1] - arr[i])
        if arr[i + 1] > x:
            increase(a, arr[i + 1] - x)
        if check(arr[i + 1], arr[i]):
            decrease(g, arr[i + 1] // arr[i])
        if check(arr[i + 1], x):
            increase(g, arr[i + 1] // x)

    arr[i] = x

    if a and min(a.values()) == n - 1:
        output.append("+")
    elif g and min(g.values()) == n - 1:
        output.append("*")
    else:
        output.append("?")

sys.stdout.write('\n'.join(output))
