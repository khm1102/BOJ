def failfun(p):
    fail = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = fail[j - 1]
        if p[i] == p[j]:
            j += 1
            fail[i] = j
    return fail


def kmp(s, p):
    fail = failfun(p)
    cnt = 0
    q = []
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = fail[j - 1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                q.append(i - len(p) + 2)
                cnt += 1
                j = fail[j]
            else:
                j += 1
    return cnt, q


if __name__ == "__main__":
    s = input()
    p = input()

    cnt, positions = kmp(s, p)

    print(cnt)
    for pos in positions:
        print(pos, end=" ")
