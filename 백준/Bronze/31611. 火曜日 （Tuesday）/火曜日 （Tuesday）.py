import sys
input = sys.stdin.read

X = int(input().strip())
if X % 7 == 2:
    print(1)
else:
    print(0)
