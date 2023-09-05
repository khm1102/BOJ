import sys

N, M = map(int, sys.stdin.readline().split())

listen = {sys.stdin.readline().strip(): 0 for _ in range(N)}
arr = []
for _ in range(M):
    a = sys.stdin.readline().strip()
    if a in listen:
        arr.append(a)

arr.sort()

sys.stdout.write(str(len(arr)) + "\n")
sys.stdout.write("\n".join(arr))
