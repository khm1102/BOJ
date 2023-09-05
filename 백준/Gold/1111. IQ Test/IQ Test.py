N = int(input())
numbers = list(map(int, input().split()))
if N == 1:print('A')
elif N == 2:
    if numbers[0] == numbers[1]:print(numbers[0])
    else:print('A')
else:
    a, b = 0, 0
    if numbers[1] - numbers[0] != 0:
        a = (numbers[2] - numbers[1]) // (numbers[1] - numbers[0])
    b = numbers[1] - numbers[0] * a
    for i in range(N-1):
        if numbers[i+1] != numbers[i] * a + b:
            print('B')
            break
    else:print(numbers[-1]*a + b)