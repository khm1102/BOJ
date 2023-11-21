import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def input():
    return sys.stdin.readline().strip()
# def print(e):
#     return sys.stdout.write(f"{e}")

def f(r):
    def ccw(p1, p2, p3):
        res = (p1.x * p2.y + p2.x * p3.y + p3.x * p1.y) - (p2.x * p1.y + p3.x * p2.y + p1.x * p3.y)
        return 1 if res > 0 else (-1 if res < 0 else 0)

    r.sort(key=lambda p: (p.x, p.y))

    def ch(p):
        hull = []
        for p in p:
            while len(hull) > 1 and ccw(hull[-2], hull[-1], p) < 0:
                hull.pop()
            hull.append(p)
        hull.pop()
        return hull

    l = ch(r)
    u = ch(r[::-1])
    l.extend(u)
    return l


def main():
    arr = []
    for _ in range(int(input())):
        x, y, s = input().split()
        if s == "Y":
            arr.append(Point(int(x), int(y)))
    print(len(f(arr)))
    print(*(f"{point.x} {point.y}" for point in f(arr)), sep="\n")
if __name__ == "__main__":
    main()