import math
import sys


def main():
    arr = [False] * 1000001
    arr[1] = True
    arr[2] = False


    for i in range(1, int(math.sqrt(1000000)) + 1):
        arr[i * i] = True

    for i in range(2, 1000001):
        if not arr[i]:
            for j in range(1, int(math.sqrt(1000000)) + 1):
                if i + j * j <= 1000000:
                    arr[i + j * j] = True

    T = int(sys.stdin.readline())

    sb = []
    for _ in range(T):
        N = int(sys.stdin.readline())
        sb.append("koosaga\n" if arr[N] else "cubelover\n")

    sys.stdout.write("".join(sb))


if __name__ == "__main__":
    main()
