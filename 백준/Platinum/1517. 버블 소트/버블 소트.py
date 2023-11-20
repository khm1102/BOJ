N = int(input())
arr = list(map(int, input().split()))

indexed_arr = [(arr[i], i) for i in range(N)]

indexed_arr.sort(key=lambda x: x[0])

def query(bit, i):
    result = 0
    while i > 0:
        result += bit[i]
        i -= i & -i
    return result

def update(bit, i, val):
    while i < len(bit):
        bit[i] += val
        i += i & -i

bit = [0] * (N + 1)
ans = 0
for i in range(N):
    q = indexed_arr[i][1] + 1
    ans += i - query(bit, q)
    update(bit, q, 1)

print(ans)
