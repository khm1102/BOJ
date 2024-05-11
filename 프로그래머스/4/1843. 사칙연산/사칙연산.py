def solution(arr):
    def calculate(flag, start, end):
        if start == end:
            dp[flag][start][end] = numbers[start]
            return dp[flag][start][end]

        if dp[flag][start][end] is not None:
            return dp[flag][start][end]

        result = float('-inf') if flag == 0 else float('inf')
        for mid in range(start, end):
            if operations[mid] == "-":
                if flag == 0:
                    result = max(result, calculate(0, start, mid) - calculate(1, mid + 1, end))
                else:
                    result = min(result, calculate(1, start, mid) - calculate(0, mid + 1, end))
            else:
                if flag == 0:
                    result = max(result, calculate(0, start, mid) + calculate(0, mid + 1, end))
                else:
                    result = min(result, calculate(1, start, mid) + calculate(1, mid + 1, end))

        dp[flag][start][end] = result
        return result

    n = len(arr) // 2
    dp = [[[None for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(2)]
    numbers = [int(arr[i]) for i in range(0, len(arr), 2)]
    operations = [arr[i] for i in range(1, len(arr), 2)]

    return calculate(0, 0, n)