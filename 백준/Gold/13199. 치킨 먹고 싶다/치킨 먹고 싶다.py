import sys

def main():
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        p, m, f, c = map(int, sys.stdin.readline().split())

        d = 0
        n = (m // p) + ((m // p) * c) // f
        d = (m // p)
        res = (m // p) * c
        if res >= f:
            d += (res - f) // (f - c) + 1
        
        sys.stdout.write(str(d - n) + "\n")

if __name__ == "__main__":
    main()
