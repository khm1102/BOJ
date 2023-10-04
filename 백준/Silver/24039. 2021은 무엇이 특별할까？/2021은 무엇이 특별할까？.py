def sp():
    ck = [False] * 10001
    p = []

    for i in range(2, int(10000**0.5) + 1):
        if not ck[i]:
            for j in range(i * 2, 10001, i):
                ck[j] = True

    for i in range(2, 10001):
        if not ck[i]:
            p.append(i)

    return p

def m():
    p = sp()
    n = int(input())
    a = 0

    for i in range(len(p) - 1):
        m = p[i] * p[i + 1]
        if m > n:
            a = m
            break

    print(a)

if __name__ == "__main__":
    m()
