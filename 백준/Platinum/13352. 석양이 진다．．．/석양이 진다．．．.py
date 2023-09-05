import random

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(a, b, c):
    s = (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)
    return s == 0

def main():
    n = int(input())
    arr = []
    for _ in range(n):
        x, y = map(int, input().split())
        arr.append(Vec2(x, y))

    if n <= 4:
        print("success")
        return

    def myrand():
        return random.randint(0, n - 1)

    k = 100
    visit = [False] * (n + 1)
    for i in range(1, k + 1):
        visit = [False] * (n + 1)

        can = []
        while len(can) < 4:
            t = myrand()
            while visit[t]:
                t = myrand()

            visit[t] = True
            can.append(t)

        cnt = 0
        for j in range(n):
            if ccw(arr[can[0]], arr[can[1]], arr[j]) or ccw(arr[can[2]], arr[can[3]], arr[j]):
                cnt += 1

        if cnt == n:
            print("success")
            return

    print("failure")

if __name__ == "__main__":
    main()
