def t(n):
    cnt = 0
    
    for a in range(1, n):
        for b in range(a, n):
            c = n - (a + b)
            if c < b:
                break
            if b + a > c:
                cnt += 1
    
    return cnt

n = int(input())
result = t(n)
print(result)
