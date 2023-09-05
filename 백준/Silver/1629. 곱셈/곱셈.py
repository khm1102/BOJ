a, b, c = map(int, input().split())

def pow(a, b, c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        temp = pow(a, b//2, c)
        return temp*temp % c
    else:
        temp = pow(a, b-1, c)
        return temp*a % c

print(pow(a, b, c))