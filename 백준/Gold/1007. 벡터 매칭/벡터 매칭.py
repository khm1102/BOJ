import math

# N개의 점 중에서 N/2개를 선택하는 조합을 생성하는 함수
def comb(arr, r):
    res = []

    def f(index, cc):
        if len(cc) == r:
            res.append(cc[:])
            return

        if index == len(arr):
            return

        cc.append(index)
        f(index + 1, cc)
        cc.pop()
        f(index + 1, cc)

    f(0, [])
    return res

def dist(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

T = int(input())

for _ in range(T):
    N = int(input())
    points = []

    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    half_N = N // 2
    ac = comb(range(N), half_N)
    min_length = float('inf')

    for combination in ac:
        sum_x = 0
        sum_y = 0

        for i in range(N):
            if i in combination:
                sum_x += points[i][0]
                sum_y += points[i][1]
            else:
                sum_x -= points[i][0]
                sum_y -= points[i][1]

        length = dist((sum_x, sum_y), (0, 0))
        min_length = min(min_length, length)

    print("{:.12f}".format(min_length))
