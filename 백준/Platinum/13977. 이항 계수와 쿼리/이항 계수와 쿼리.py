import sys

def input(): return sys.stdin.readline().strip()
def print(var):return sys.stdout.write(str(f"{var}\n"))

mod = 10 ** 9 + 7
MAX = 4000001
A = [1] + [0] * (MAX - 1)
B = [0] * MAX

def pow(a, b):
    result = 1
    while b:
        if b & 1:
            result = (result * a) % mod
        b >>= 1
        a = (a * a) % mod
    return result

for i in range(1, MAX):
    A[i] = (A[i - 1] * i) % mod

B[MAX - 1] = pow(A[MAX - 1], mod - 2)
for i in range(MAX - 2, -1, -1):
    B[i] = (B[i + 1] * (i + 1)) % mod

for _ in range(int(input())):
    N, K = map(int, input().split())
    print(((A[N] * B[K]) % mod) * B[N - K] % mod)
    
