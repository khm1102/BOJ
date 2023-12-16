import sys

def get_cumulative_sum(idx, fenwick_tree):
    result = 0
    while idx > 0:
        result += fenwick_tree[idx]
        idx -= idx & -idx
    return result

def update_fenwick_tree(idx, fenwick_tree):
    while idx <= n:
        fenwick_tree[idx] += 1
        idx += idx & -idx

n = int(input())
fenwick_tree = [0] * (n + 1)

value_to_index1 = {}
index_to_index2 = {}

values1 = list(map(int, sys.stdin.readline().split()))
values2 = list(map(int, sys.stdin.readline().split()))

for i, value in enumerate(values1, start=1):
    value_to_index1[value] = i

for i, value in enumerate(values2, start=1):
    index_to_index2[value_to_index1[value]] = i

result = 0

for key in sorted(index_to_index2):
    num = index_to_index2[key]
    update_fenwick_tree(num, fenwick_tree)
    result += key - get_cumulative_sum(num, fenwick_tree)

print(result)
