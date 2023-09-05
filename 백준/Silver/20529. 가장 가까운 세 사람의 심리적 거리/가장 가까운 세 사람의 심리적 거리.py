from collections import defaultdict
from itertools import combinations


def check(a, b):
    if a == b:
        return 0
    else:
        return 1


def optimize_code():
    T = int(input())
    for _ in range(T):
        result = float('inf')
        N = int(input())
        people = [*map(str, input().rstrip().split())]
        mbties = defaultdict(int)
        for i in people:
            mbties[i] += 1

        for i in mbties:
            if mbties[i] >= 3:
                print(0)
                break
        else:
            for j in combinations(people, 3):
                k = j[0]
                l = j[1]
                u = j[2]
                cnt = 0
                for m in range(4):
                    a = check(k[m], l[m])
                    b = check(k[m], u[m])
                    c = check(l[m], u[m])
                    cnt += a + b + c
                if cnt < result:
                    result = cnt
            print(result)


optimize_code()
