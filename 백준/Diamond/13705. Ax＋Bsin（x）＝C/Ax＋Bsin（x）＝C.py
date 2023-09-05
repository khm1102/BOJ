import decimal
import math

decimal.getcontext().prec = 100
PI2 = decimal.Decimal(
    "6.2831853071795864769252867665590057683943387" +
    "98750211641949889184615632812572417997256069650684234136")

def sin(x):
    x = x % PI2
    acc = decimal.Decimal(0)
    coeff = x
    for i in range(50):
        acc += coeff
        coeff = coeff * x**2 / decimal.Decimal(-(2 * i + 2) * (2 * i + 3))
    return acc

def main():
    A, B, C = map(decimal.Decimal, input().split())

    low = decimal.Decimal(-400000)
    high = decimal.Decimal(400000)
    m = decimal.Decimal(0)
    for i in range(1000):
        m = (low + high) / 2
        v = A * m + B * sin(m) - C
        cmp = v.compare(0)
        if cmp < 0:
            low = m
        else:
            high = m
    print(format(m, '.6f'))

if __name__ == "__main__":
    main()
