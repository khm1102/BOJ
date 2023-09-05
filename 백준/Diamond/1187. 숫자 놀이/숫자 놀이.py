# https://dynamiccube.tistory.com/70?category=1222791 블로그를 참고하여 풀었습니다.


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # 분할 정복을 이용한 재귀함수 dnc
    def dnc(l, r):
        # 분할할 그룹 크기 계산
        N = (r-l+2) // 2

        # 그룹의 크기 1이하인 경우 배열의 값 자체를 반환
        if N <= 1:
            return a[l]

        # 세 그룹의 합 저장 리스트
        h = [0]*3

        # 세 그룹 합 계산
        for i in range(3):
            h[i] = dnc(l+i*(N//2), l+i*(N//2)+N-2) // (N//2)

        # 첫 번째 그룹과 두 번째 그룹의 합이 같은 경우, 두 그룹을 합침
        if h[0] % 2 == h[1] % 2:
            return (h[0] + h[1]) * (N//2)

        # 첫 번째 그룹과 세 번째 그룹의 합이 같은 경우, 두 그룹을 합침
        elif h[0] % 2 == h[2] % 2:
            # 두 번째 그룹과 세 번째 그룹의 원소를 교환
            for i in range(N//2):
                a[l+i+N//2], a[l+i+N] = a[l+i+N], a[l+i+N//2]
            return (h[0] + h[2]) * (N//2)

        # 위의 두 경우가 아닌 경우(즉, 두 번째 그룹과 세 번째 그룹의 합이 같은 경우)
        else:
            # 첫 번째 그룹과 두 번째 그룹의 원소를 교환
            for i in range(N//2):
                a[l+i], a[l+i+N] = a[l+i+N], a[l+i]
            return (h[2] + h[1]) * (N//2)

    dnc(0, 2*(n-1))
    # 결과 출력. 처음부터 n개의 원소를 출력
    print(' '.join(map(str, a[:n])))

solve()
