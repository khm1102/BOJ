while True:
    try:
        a, b = input().split()
        aIdx = 0
        isTrue = False
        for i in range(len(b)):
            if a[aIdx] == b[i]:
                aIdx += 1
            if aIdx == len(a):
                isTrue = True
                break
        if isTrue:
            print("Yes")
        else:
            print("No")
    except EOFError:
        break
