import sys
print(sum(2**i % (10**9 + 7) for i, c in enumerate(sys.stdin.readline().rstrip()) if c == 'O') % (10**9 + 7))