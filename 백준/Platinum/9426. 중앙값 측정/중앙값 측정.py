import math

def update(tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        tree[node] += val
        return
    mid = (start + end) // 2
    update(tree, node * 2, start, mid, index, val)
    update(tree, node * 2 + 1, mid + 1, end, index, val)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def kth(tree, node, start, end, k):
    if start == end:
        return start
    else:
        mid = (start + end) // 2
        if k <= tree[node * 2]:
            return kth(tree, node * 2, start, mid, k)
        else:
            return kth(tree, node * 2 + 1, mid + 1, end, k - tree[node * 2])

n, k = map(int, input().split())
MAXN = 66666
h = int(math.ceil(math.log2(MAXN + 1)))
tree_size = 1 << (h + 1)
cnt = (k + 1) // 2
tree = [0] * tree_size
a = [0] * (n + 1)
ans = 0

for i in range(1, n + 1):
    a[i] = int(input())
    update(tree, 1, 0, MAXN, a[i], 1)
    if i >= k:
        if i != k:
            update(tree, 1, 0, MAXN, a[i - k], -1)
        pos = kth(tree, 1, 0, MAXN, cnt)
        ans += pos

print(ans)
