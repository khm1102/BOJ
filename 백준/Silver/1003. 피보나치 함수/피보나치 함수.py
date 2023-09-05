n = int(input())

for _ in range(n):
    a = int(input())
    if a < 2:
        if a == 0:
            print("1 0")
        else:
            print("0 1")
    else:
        arr = [0] * 41
        arr[0] = 1
        arr[1] = 1
        for i in range(2, a + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
        print(arr[a - 2], arr[a - 1])
