MOD = 1000000007

def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = (init(node * 2, start, mid) * init(node * 2 + 1, mid + 1, end)) % MOD
    return tree[node]

def update(node, start, end, index, value):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = value
        return
    mid = (start + end) // 2
    update(node * 2, start, mid, index, value)
    update(node * 2 + 1, mid + 1, end, index, value)
    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD

def query(node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    left_result = query(node * 2, start, mid, left, right)
    right_result = query(node * 2 + 1, mid + 1, end, left, right)
    return (left_result * right_result) % MOD

N, M, K = map(int, input().split())
nums = [0] * (N + 1)
tree = [0] * (4 * (N + 1))

for i in range(1, N + 1):
    nums[i] = int(input())

init(1, 1, N)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 1, N, b, c)
    else:
        result = query(1, 1, N, b, c)
        print(result)
