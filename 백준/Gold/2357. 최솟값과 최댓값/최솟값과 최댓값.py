import sys

def build_tree(arr):
    n = len(arr)
    tree = [(float('inf'), float('-inf'))] * (4 * n)

    def build(node, start, end):
        if start == end:
            tree[node] = [arr[start], arr[start]]
            return
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = [min(tree[2 * node][0], tree[2 * node + 1][0]), max(tree[2 * node][1], tree[2 * node + 1][1])]

    build(1, 0, n - 1)
    return tree

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return [float('inf'), float('-inf')]
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    min_left, max_left = query(tree, 2 * node, start, mid, left, right)
    min_right, max_right = query(tree, 2 * node + 1, mid + 1, end, left, right)
    return [min(min_left, min_right), max(max_left, max_right)]

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    arr = [int(sys.stdin.readline()) for _ in range(N)]

    tree = build_tree(arr)

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        result = query(tree, 1, 0, N - 1, a - 1, b - 1)
        sys.stdout.write(f"{result[0]} {result[1]}\n")
