def solve(d, p, q):
    if p < q:
        p, q = q, p

    if d % p == 0 or d % q == 0 or d % (p + q) == 0:
        return d

    ans = (d // p) * p + p
    temp = ans

    for i in range(1, (temp // p) + 1):
        t = temp - p * i
        if (d - t) % q == 0:
            return d
        else:
            t = t + ((d - t) // q) * q + q
        
        if t == ans:
            break
        ans = min(ans, t)

    return ans


d, p, q = map(int, input().split())
print(solve(d, p, q))
