
import sys
def input():
    return  sys.stdin.readline()

def main():
    # print(math.sqrt(2562991876))

    N = int(input())

    res = 0

    arr_list = map(int, input().split())

    for t in arr_list:
        if 1 <= t < 4:
            t = 0
        elif 4 <= t < 16:
            t = 1
        elif 16 <= t < 82:
            t = 2
        elif 82 <= t < 6724:
            t = 0
        elif 6724 <= t < 50626:
            t = 3
        elif 50626 <= t < 2562991876:
            t = 1
        else:
            t = 2

        res ^= t

    print("koosaga" if res != 0 else "cubelover")


if __name__ == "__main__":
    main()
