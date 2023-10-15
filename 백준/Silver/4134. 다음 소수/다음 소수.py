import sys
def input(): return sys.stdin.readline().strip()
def print(val):return sys.stdout.write(str(f"{val}\n"))
def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

for _ in range(int(input())):
    n = int(input())
    while not is_prime(n): n += 1
    print(n)