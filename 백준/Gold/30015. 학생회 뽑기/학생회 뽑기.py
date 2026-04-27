def solve(n, k, arr):
    ability = 0

    for i in range(20, -1, -1):
        cnt = 0
        new_ability = ability | (1 << i)

        for i in range(n):
            if (arr[i] & new_ability) == new_ability:
                cnt += 1

        if cnt >= k:
            ability = new_ability

    return ability


n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(solve(n, k, arr))