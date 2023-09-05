def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(a, b):
    gcd_value = gcd(a, b)
    return a // gcd_value, b // gcd_value

def add_fractions(a1, b1, a2, b2):
    numerator = a1 * b2 + a2 * b1
    denominator = b1 * b2
    return simplify_fraction(numerator, denominator)

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

result_numerator, result_denominator = add_fractions(a1, b1, a2, b2)

print(result_numerator, result_denominator)
