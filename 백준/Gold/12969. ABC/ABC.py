n, k = map(int, input().split())
ans = [''] * 32
d = [[[[-1 for _ in range(450)] for _ in range(31)] for _ in range(31)] for _ in range(31)]

def go(i, a, b, p):
    if i == n:
        if p == k:
            return True
        else:
            return False
    if d[i][a][b][p] != -1:
        return False
    d[i][a][b][p] = 1
    ans[i] = 'A'
    if go(i+1, a+1, b, p):
        return True
    ans[i] = 'B'
    if go(i+1, a, b+1, p+a):
        return True
    ans[i] = 'C'
    if go(i+1, a, b, p+a+b):
        return True
    return False

if go(0, 0, 0, 0):
    print(''.join(ans[:n]))
else:
    print(-1)
