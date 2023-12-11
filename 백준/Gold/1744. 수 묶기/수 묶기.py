import sys

def input() :
    return sys.stdin.readline()
def print(value):
    return sys.stdout.write(str(value))

def solve(n, arr):
    arr.sort()
    pos = []
    neg = []

    for num in arr:
        if num <= 0:
            neg.append(num)
        else:
            pos.append(num)

    pos.reverse()
    neg.sort()
    result = 0

    for i in range(0, len(pos) - 1, 2):
        result += max(pos[i] * pos[i + 1], pos[i] + pos[i + 1])

    for i in range(0, len(neg) - 1, 2):
        result += neg[i] * neg[i + 1]

    if len(pos) % 2 == 1:
        result += pos[-1]

    if len(neg) % 2 == 1:
        result += neg[-1]

    return result


n = int(input())
seq = []
for _ in range(n):
    seq.append(int(input()))

print(solve(n, seq))