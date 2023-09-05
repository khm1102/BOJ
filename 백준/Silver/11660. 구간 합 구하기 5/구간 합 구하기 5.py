import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1] + row[j-1]

    sb = []
    for _ in range(m):
        sum = 0
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        for i in range(x1, x2+1):
            sum += dp[i][y2] - dp[i][y1-1]
        sb.append(str(sum) + "\n")

    sys.stdout.write(''.join(sb))

if __name__ == "__main__":
    main()
