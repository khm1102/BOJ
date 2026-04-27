def f(n):
    if n == 1:
        return 1
    if n % 2 == 0 or n % 5 == 0:return -1
    r = 1  
    length = 1
    while r != 0:
        r = (r * 10 + 1) % n
        length += 1
    return length

n = int(input())
print(f(n))
