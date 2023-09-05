# 유클리드 호제법
def uclid(a, b):
    while a % b != 0:
        a, b = b, a % b

    if b == 1:
        return True
    else:
        return False


def solution(N, M):
    num = M // N  # 최소공배수를 최대공약수로 나눈 값의 약수를 구한다.
    arr = []
    # 빠른 약수 구하기(제곱수 일지라도 2개를 넣어준다. ex)9 => 1, 3, 3, 9)
    for i in range(1, num + 1):
        if i * i > num:
            break

        if num % i == 0:
            arr.append(i)
            arr.append(num // i)

    # 오름차순으로 정렬
    arr.sort()

    # 중간부터 양쪽으로 탐색하기 위해 인덱스 설정
    i = len(arr) // 2 - 1
    j = len(arr) // 2

    # 서로소인 약수 구하기
    while True:
        # 만약 2개의 수가 서로소이면 탈출
        if uclid(arr[j], arr[i]):
            break

        i -= 1
        j += 1

    return arr[i] * N, arr[j] * N


N, M = map(int, input().split())

print(*solution(N, M))