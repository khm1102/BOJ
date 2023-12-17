import sys


def init_tree(node, start, end):
    if start == end:
        tree[node] = nums[start]
    else:
        mid = (start + end) // 2
        tree[node] = init_tree(node * 2, start, mid) + init_tree(node * 2 + 1, mid + 1, end)
    return tree[node]

def update_tree(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update_tree(node * 2, start, mid, index, diff)
        update_tree(node * 2 + 1, mid + 1, end, index, diff)

def query_tree(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query_tree(node * 2, start, mid, left, right) + query_tree(node * 2 + 1, mid + 1, end, left, right)


N, M, K = map(int, input().split())
nums = [0] * (N + 1)
tree = [0] * (4 * N)
for i in range(1, N + 1):
    nums[i] = int(input())


init_tree(1, 1, N)


for _ in range(M + K):
    cmd, a, b = map(int, input().split())
    if cmd == 1: 
        diff = b - nums[a]
        nums[a] = b
        update_tree(1, 1, N, a, diff)
    elif cmd == 2: 
        result = query_tree(1, 1, N, a, b)
        print(result)
