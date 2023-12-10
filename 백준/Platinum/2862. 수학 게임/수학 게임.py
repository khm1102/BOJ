import sys
def input(): return sys.stdin.readline().strip()
def print(val):return sys.stdout.write(str(val))
fibo = [0] * 80
fibo[1] = fibo[2] = 1

for i in range(3, 80):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

N = int(input())
while True:
    temp = N
    for i in range(1, 80):
        if temp < fibo[i]:
            temp = fibo[i - 1]
            break
    if temp == N:
        break

    N -= temp

print(N)