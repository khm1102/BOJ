def main():
    n, q = map(int, input().split())
    dp = list(map(int, input().split()))

    for _ in range(q):
        x = int(input())
        a1, a2 = [], []

        for i in range(x):
            if not a1 or dp[i] > a1[-1]:
                a1.append(dp[i])
                m = len(a1) - 1 if i == x - 1 else 0
            else:
                if dp[x - 1] < dp[i]:
                    continue
                it = next((j for j, val in enumerate(a1) if val >= dp[i]), len(a1))
                a1[it:it + 1] = [dp[i]]
                if i == x - 1:
                    m = it

        a2.append(dp[x - 1])
        for i in range(x, n):
            if dp[i] > a2[-1]:
                a2.append(dp[i])
            else:
                if dp[x - 1] > dp[i]:
                    continue
                it = next((j for j, val in enumerate(a2) if val >= dp[i]), len(a2))
                a2[it:it + 1] = [dp[i]]

        print(m + len(a2))


main()
