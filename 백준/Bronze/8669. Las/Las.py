import sys

n = int(sys.stdin.readline().strip())

max_grubosc = {}

for _ in range(n):
    g, r = map(int, sys.stdin.readline().strip().split())
    
    if r in max_grubosc:
        max_grubosc[r] = max(max_grubosc[r], g)
    else:
        max_grubosc[r] = g

liczba_kandydatow = len(max_grubosc)

sys.stdout.write(str(liczba_kandydatow) + '\n')
