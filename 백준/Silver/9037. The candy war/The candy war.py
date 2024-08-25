def solve(c):
    n,r = len(c), 0
    
    while len(set(c)) > 1:
        nc = [0] * n
        
        for i in range(n):
            g = c[i] // 2
            nc[i] -= g
            nc[(i + 1) % n] += g
        
        for i in range(n):
            c[i] += nc[i]
            if c[i] % 2 != 0:
                c[i] += 1
        
        r += 1
    
    return r

for _ in range(int(input())):
    input()
    c = list(map(int, input().split()))
    c = [x + (x % 2) for x in c]
    
    print(solve(c))
