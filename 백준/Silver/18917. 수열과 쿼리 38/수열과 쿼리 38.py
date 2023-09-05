import sys

sum_val = 0
xr = 0

M = int(sys.stdin.readline().strip())
for _ in range(M):
    query = sys.stdin.readline().split()
    q = int(query[0])

    if q == 1:
        x = int(query[1])
        sum_val += x
        xr ^= x
    elif q == 2:
        x = int(query[1])
        sum_val -= x
        xr ^= x
    elif q == 3:
        sys.stdout.write(str(sum_val) + '\n')
    else:
        sys.stdout.write(str(xr) + '\n')

sys.stdout.flush()
