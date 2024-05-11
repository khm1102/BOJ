import math


def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1):
        start = math.ceil(math.sqrt(r1**2 - i**2)) if i < r1 else 0
        end = int(math.sqrt(r2**2 - i**2))
        answer += end - start + 1
    return answer * 4
