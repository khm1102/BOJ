def calculate_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        while factorial % 10 == 0:
            factorial //= 10
        factorial %= 10**18
    return str(factorial)[-5:]

n = int(input())
print(calculate_factorial(n))
