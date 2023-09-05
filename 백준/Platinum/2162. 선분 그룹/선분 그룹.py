def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if x_root == y_root:
        return

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def count_groups(segments):
    n = len(segments)
    parent = [i for i in range(n)]
    rank = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if do_segments_intersect(segments[i], segments[j]):
                union(parent, rank, i, j)

    group_sizes = [0] * n
    for i in range(n):
        group_sizes[find(parent, i)] += 1

    max_group_size = max(group_sizes)
    num_groups = sum(size > 0 for size in group_sizes)

    return num_groups, max_group_size

def do_segments_intersect(segment1, segment2):
    x1, y1, x2, y2 = segment1
    x3, y3, x4, y4 = segment2

    def orientation(x1, y1, x2, y2, x3, y3):
        return (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2)

    o1 = orientation(x1, y1, x2, y2, x3, y3)
    o2 = orientation(x1, y1, x2, y2, x4, y4)
    o3 = orientation(x3, y3, x4, y4, x1, y1)
    o4 = orientation(x3, y3, x4, y4, x2, y2)

    if (o1 * o2 < 0) and (o3 * o4 < 0):
        return True

    if (o1 == 0) and is_point_on_segment(x1, y1, x2, y2, x3, y3):
        return True

    if (o2 == 0) and is_point_on_segment(x1, y1, x2, y2, x4, y4):
        return True

    if (o3 == 0) and is_point_on_segment(x3, y3, x4, y4, x1, y1):
        return True

    if (o4 == 0) and is_point_on_segment(x3, y3, x4, y4, x2, y2):
        return True

    return False

def is_point_on_segment(x1, y1, x2, y2, x, y):
    return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)


N = int(input())
segments = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    segments.append((x1, y1, x2, y2))

num_groups, max_group_size = count_groups(segments)

print(num_groups)
print(max_group_size)
