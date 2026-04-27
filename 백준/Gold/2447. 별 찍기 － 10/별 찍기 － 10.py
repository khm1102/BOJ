def f(N):
    dp = [["*" for _ in range(N)] for _ in range(N)]

    def r(x, y, size):
        if size == 3:
            dp[x + 1][y + 1] = " "
            return

        if dp[x][y] == " ":
            return

        next = size // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    for k in range(next):
                        dp[x + next + k][y + next:y + 2 * next] = [" "] * next
                else:
                    r(x + i * next, y + j * next, next)

    r(0, 0, N)

    for row in dp:
        print("".join(row))
f(int(input()))
