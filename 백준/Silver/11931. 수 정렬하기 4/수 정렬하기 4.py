import sys

N = int(sys.stdin.readline())

num = []

for _ in range(0, N):
    num.append(int(sys.stdin.readline()))

num.sort()
num.reverse()
for i in range(0, N):
    print(num[i])