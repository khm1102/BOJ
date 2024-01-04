import math

def find(a, b, c, d):
    D = abs(d)
    for i in range(1, D + 1):
        if d % i == 0:
            if a * i ** 2 + b * i + c + d // i == 0:
                return float(i)
            if -a * i ** 2 + b * i - c + d // i == 0:
                return float(-i)
    return 0.0

def main():
    n = int(input())
    for _ in range(n):
        A, B, C, D = map(int, input().split())
        s = set()
        x1 = find(A, B, C, D)
        a, b, c = A, A * x1 + B, A * x1 ** 2 + B * x1 + C
        delta = b ** 2 - 4 * a * c

        if delta < 0:
            print(f"{x1:.6f}")
        elif delta == 0:
            x2 = -b / (2.0 * a)
            s.add(x1)
            s.add(x2)
            if x1 == x2:
                print(f"{x1:.6f}")
            else:
                print(" ".join(f"{x:.6f}" for x in sorted(s)))
        else:
            x2 = (-b + math.sqrt(delta)) / (2.0 * a)
            x3 = (-b - math.sqrt(delta)) / (2.0 * a)
            s.update([x1, x2, x3])
            print(" ".join(f"{x:.6f}" for x in sorted(s)))

if __name__ == "__main__":
    main()
