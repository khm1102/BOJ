def SUM(number):
    if number <= 0:
        return 0

    arr = [0] * 10
    num = 1
    ret = 0

    while number > 0:
        div = number // (num * 10)
        mod = number % (num * 10)

        for i in range(10):
            arr[i] += div * num

        for i in range(1, (mod // num) + 1):
            arr[i] += num

        arr[(mod // num + 1) % 10] += mod % num

        number -= 9 * num
        num *= 10

    for i in range(1, 10):
        ret += arr[i] * i
    return ret


T = int(input())
for _ in range(T):
    input_values = input().split()
    A = int(input_values[0])
    B = int(input_values[1])
    print(SUM(B) - SUM(A - 1))
