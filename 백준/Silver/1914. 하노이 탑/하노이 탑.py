import math

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, end, mid)
    print(start, end)
    hanoi(n - 1, mid, start, end)


def main():
    n = int(input())
    a = int(math.pow(2, n))
    a -= 1
    print(a)

    if n <= 20:
        hanoi(n, 1, 2, 3)


if __name__ == "__main__":
    main()
