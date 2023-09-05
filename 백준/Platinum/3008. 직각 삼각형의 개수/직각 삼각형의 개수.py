def rotate(v):
    v['r'] = (v['r'] + 1) % 4
    v['a'], v['b'] = v['b'], -v['a']


def compare(v1, v2):
    return v1['b'] * v2['a'] - v1['a'] * v2['b']


def count_points(v, i):
    n = len(v)
    cnt = [0, 0, 0, 0]

    vec = []
    for j in range(n):
        if i == j:
            continue
        x = {'r': 0, 'a': v[j]['x'] - v[i]['x'], 'b': v[j]['y'] - v[i]['y']}
        while not (x['a'] > 0 and x['b'] >= 0):
            rotate(x)
        vec.append(x)

    vec.sort(key=lambda x: (x['b'] / x['a'], x['r']))

    j, k = 0, 0
    ans = 0
    while j < len(vec):
        while k < len(vec) and compare(vec[j], vec[k]) == 0:
            cnt[vec[k]['r']] += 1
            k += 1

        ans += cnt[0] * cnt[1]
        ans += cnt[1] * cnt[2]
        ans += cnt[2] * cnt[3]
        ans += cnt[3] * cnt[0]

        while j < k:
            cnt[vec[j]['r']] = 0
            j += 1

    return ans



n = int(input())
v = []
for _ in range(n):
    x, y = map(int, input().split())
    v.append({'x': x, 'y': y})

ans = 0
for i in range(n):
    ans += count_points(v, i)

print(ans)

