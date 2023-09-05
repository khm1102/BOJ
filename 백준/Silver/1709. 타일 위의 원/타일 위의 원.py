def dist(x, y):
    return x * x + y * y

def main():
    N = int(input())
    x = 0
    y = N // 2 - 1
    R = (N // 2) * (N // 2)
    cnt = 0

    while x <= N // 2 and y >= 0:
        down_left_dist = dist(x + 1, y)
        if down_left_dist <= R:
            x += 1
        if down_left_dist >= R:
            y -= 1
        cnt += 1

    print(cnt * 4)

if __name__ == "__main__":
    main()
