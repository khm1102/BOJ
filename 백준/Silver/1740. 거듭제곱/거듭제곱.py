def get_nth_number(N):
    result = 0
    pow_of_3 = 1

    while N > 0:
        if N % 2 == 1:
            result += pow_of_3
        pow_of_3 *= 3
        N //= 2

    return result

N = int(input())
nth_number = get_nth_number(N)
print(nth_number)
