class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)
    if root1 != root2:
        parent[root1] = root2

def kruskal(edges, V):
    edges.sort(key=lambda edge: edge.weight) 
    parent = list(range(V + 1))  
    mst_weight = 0 

    for e in edges:
        if find(parent, e.src) != find(parent, e.dest):
            mst_weight += e.weight
            union(parent, e.src, e.dest)

    return mst_weight


n, m = map(int, input().split())
arr = []

for _ in range(m):
    A, B, C = map(int, input().split())
    arr.append(Edge(A, B, C))

print(kruskal(arr, n))

