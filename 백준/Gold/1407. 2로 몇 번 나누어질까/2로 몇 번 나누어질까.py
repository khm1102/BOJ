def function(x):
    sum_value = 0
    i = 1

    while x > 0:
        y = (x + 1) // 2
        sum_value += y * i
        x //= 2
        i *= 2

    return sum_value


A, B = map(int, input().split())
result = function(B) - function(A - 1)
print(result)
