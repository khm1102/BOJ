class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.init(1, n, 1)
    
    def init(self, start, end, node):
        if start == end:
            self.tree[node] = 1
            return 1
        
        mid = (start + end) // 2
        self.tree[node] = self.init(start, mid, node * 2) + self.init(mid + 1, end, node * 2 + 1)
        return self.tree[node]
    
    def get_num_and_update(self, start, end, node, index):
        self.tree[node] -= 1
        if start == end:
            return start
        
        mid = (start + end) // 2
        if index > self.tree[node * 2]:
            return self.get_num_and_update(mid + 1, end, node * 2 + 1, index - self.tree[node * 2])
        else:
            return self.get_num_and_update(start, mid, node * 2, index)

n, k = map(int, input().split())

seg_tree = SegmentTree(n)

idx = k - 1
res = []
for i in range(1, n + 1):
    get_idx = seg_tree.get_num_and_update(1, n, 1, idx + 1)
    res.append(str(get_idx))
    
    if seg_tree.tree[1] == 0:
        break
    
    idx = (idx + k - 1) % seg_tree.tree[1]

print("<{}>".format(", ".join(res)))
