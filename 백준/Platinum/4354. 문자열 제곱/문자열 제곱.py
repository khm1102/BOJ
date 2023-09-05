def greatest_n(s):
    length = len(s)
    for i in range(1, length + 1):
        if length % i == 0:
            candidate = s[:i]
            if candidate * (length // i) == s:
                return length // i
    return 1

while True:
    s = input()
    if s == ".":
        break
    result = greatest_n(s)
    print(result)
