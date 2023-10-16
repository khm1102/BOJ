n = int(input())

contains_7 = '7' in str(n)

divisible_by_7 = n % 7 == 0

if contains_7 and divisible_by_7:
    print(3)
elif contains_7:
    print(2)
elif divisible_by_7:
    print(1)
else:
    print(0)
