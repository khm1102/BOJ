def solve(n):
    ans, num = n, n

    for i in range(2, int(n**0.5) + 1):
        if num % i == 0:
            ans = ans // i * (i - 1)
            while num % i == 0:
                num //= i

    if num != 1:
        ans = ans // num * (num - 1)

    return ans

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        if n != 1:
            print(solve(n))
        else:
            print("0")

if __name__ == "__main__":
    main()
