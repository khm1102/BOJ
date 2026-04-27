from sys import stdin

def input():
    return stdin.readline()

def solve(n):
    res  = 0
    temp = 1
    while temp * 10 <= n:
        res += 9 * temp * len(str(temp))
        temp *= 10
    res += (n- temp + 1) * len(str(n))
    return res

print(solve(int(input())))