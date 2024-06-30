class Node:
    def __init__(self, name="", depth=-1):
        self.children = {}
        self.depth = depth
        self.name = name


def insert(route, root):
    v = root
    for r in route:
        v = v.children.setdefault(r, Node(name=r, depth=v.depth + 1))


def dfs(node):
    if node.depth != -1:
        print(' ' * node.depth + node.name)
    for name in sorted(node.children):
        dfs(node.children[name])



import sys
from functools import reduce

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
r = Node(depth=-1)

for path in data[1:n + 1]:
    route = path.split('\\')
    reduce(lambda v, r: v.children.setdefault(r, Node(name=r, depth=v.depth + 1)), route, r)

dfs(r)


