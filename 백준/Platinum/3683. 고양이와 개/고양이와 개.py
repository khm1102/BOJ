import sys
input = sys.stdin.read
from collections import defaultdict, deque

def f(s):
    return int(s[1:])

def dfs(v, g, chk, par):
    chk[v] = True
    for u in g[v]:
        if not chk[u]:
            chk[u] = True
            if par[u] == -1 or dfs(par[u], g, chk, par):
                par[u] = v
                return True
    return False

def solve():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        c = int(data[idx])
        d = int(data[idx + 1])
        n = int(data[idx + 2])
        idx += 3

        votes = []
        for i in range(n):
            a = data[idx]
            b = data[idx + 1]
            if a[0] == 'C':
                cat_vote = a
                dog_vote = b
                op = 0
            else:
                cat_vote = b
                dog_vote = a
                op = 1
            votes.append((f(cat_vote), f(dog_vote), op))
            idx += 2

        g = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if votes[i][2] != votes[j][2] and (votes[i][0] == votes[j][0] or votes[i][1] == votes[j][1]):
                    if votes[i][2] == 0:
                        g[i + 1].append(j + 1)
                    else:
                        g[j + 1].append(i + 1)

        par = [-1] * (n + 1)
        ans = 0

        for i in range(1, n + 1):
            if votes[i - 1][2] == 0:
                chk = [False] * (n + 1)
                if dfs(i, g, chk, par):
                    ans += 1

        results.append(str(n - ans))
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
