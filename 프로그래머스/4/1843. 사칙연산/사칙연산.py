def solution(arr):
    n = len(arr) // 2
    dp = [[[None for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(2)]
    num = [int(arr[i]) for i in range(0, len(arr), 2)]
    ops = [arr[i] for i in range(1, len(arr), 2)]

    def calculate(flag, start, end):
        if start == end:
            return num[start]

        if dp[flag][start][end] is not None:
            return dp[flag][start][end]

        res = float('-inf') if flag == 0 else float('inf')
        for mid in range(start, end):
            if ops[mid] == "-":
                if flag == 0:
                    res = max(res, calculate(0, start, mid) - calculate(1, mid + 1, end))

                else:
                    res = min(res, calculate(1, start, mid) - calculate(0, mid + 1, end))
            else:
                if flag == 0:
                    res = max(res, calculate(0, start, mid) + calculate(0, mid + 1, end))

                else:
                    res = min(res, calculate(1, start, mid) + calculate(1, mid + 1, end))

        dp[flag][start][end] = res
        return res

    return calculate(0, 0, n)
