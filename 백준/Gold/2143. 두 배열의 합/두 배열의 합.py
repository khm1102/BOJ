def countSubarrayPairs(A, B, T):
    v = []
    w = []

    # A로 만들 수 있는 부분합
    for i in range(len(A)):
        total = 0
        for j in range(i, len(A)):
            total += A[j]
            v.append(total)

    # B로 만들 수 있는 부분합
    for i in range(len(B)):
        total = 0
        for j in range(i, len(B)):
            total += B[j]
            w.append(total)

    w.sort()

    ans = 0
    for item in v:
        diff = T - item
        ub = upper_bound(w, diff)
        lb = lower_bound(w, diff)
        ans += (ub - lb)

    return ans

def upper_bound(arr, target):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low

def lower_bound(arr, target):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

# 입력 받기
T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# 함수 호출 및 결과 출력
result = countSubarrayPairs(A, B, T)
print(result)
