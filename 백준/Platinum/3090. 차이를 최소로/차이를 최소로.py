def is_possible(mid):
    global oprCnt
    oprCnt = 0
    copyArr = arr[:]

    for i in range(N - 1):
        if copyArr[i + 1] - copyArr[i] > mid:
            oprCnt += copyArr[i + 1] - (copyArr[i] + mid)
            copyArr[i + 1] = copyArr[i] + mid

    for i in range(N - 1, 0, -1):
        if copyArr[i - 1] - copyArr[i] > mid:
            oprCnt += copyArr[i - 1] - (copyArr[i] + mid)
            copyArr[i - 1] = copyArr[i] + mid

    return oprCnt <= T

def print_ans_arr(mid):
    for i in range(N - 1):
        if arr[i + 1] - arr[i] > mid:
            arr[i + 1] = arr[i] + mid

    for i in range(N - 1, 0, -1):
        if arr[i - 1] - arr[i] > mid:
            arr[i - 1] = arr[i] + mid

    print(' '.join(str(x) for x in arr))

N, T = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 10**9
while left < right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid
    else:
        left = mid + 1

print_ans_arr(right)