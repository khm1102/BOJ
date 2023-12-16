import bisect

def main():
    n = int(input())
    x = [tuple(map(int, input().split())) for _ in range(n)]
    x.sort()

    ans = [x[0][1]]
    idx = [0]

    for a, b in x[1:]:
        if ans[-1] < b:
            ans.append(b)
            idx.append(len(ans) - 1)
        else:
            pos = bisect.bisect_left(ans, b)
            ans[pos] = b
            idx.append(pos)

    print(len(x) - len(ans))

    sibal = []
    now = len(ans) - 1
    for i in range(len(idx) - 1, -1, -1):
        if now == idx[i]:
            now -= 1
        else:
            sibal.append(x[i][0])

    sibal.sort()
    for i in sibal:
        print(i)

if __name__ == "__main__":
    main()
