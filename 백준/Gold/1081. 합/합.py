def sum_digits(n):
    if n <= 0:
        return 0
    
    c = [0] * 10
    s = 1
    total_sum = 0
    
    while n > 0:
        t = n // (s * 10)
        r = n % (s * 10)
        
        for i in range(10):
            c[i] += t * s
        
        for i in range(1, r // s + 1):
            c[i] += s
        
        c[(r // s + 1) % 10] += r % s
        n -= 9 * s
        s *= 10
    
    for i in range(1, 10):
        total_sum += i * c[i]
    
    return total_sum

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(sum_digits(b) - sum_digits(a - 1))
