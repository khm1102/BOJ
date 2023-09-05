s = input()

order = 0
for i in range(len(s)):
    if s[i] == 'x':
        order = 1
        stop = i
        break

if order == 0:
    coef = int(s)
    if coef == 0:
        print("W")
    elif abs(coef) == 1:
        if coef == 1:
            print("x+W")
        else:
            print("-x+W" if coef < 0 else "x+W")
    else:
        print(f"{coef}x+W")
else:
    check = ""
    for i in range(stop):
        check += s[i]
    coef = int(check) // 2

    check = ""
    for i in range(stop + 1, len(s)):
        check += s[i]

    if check == "":
        check = "0"

    k = int(check)

    if abs(coef) == 1:
        if coef == 1:
            print("xx", end="")
        else:
            print("-xx" if coef < 0 else "xx", end="")
    else:
        print(f"{coef}xx", end="")

    if k != 0:
        if abs(k) == 1:
            if k == 1:
                print("+x+W", end="")
            else:
                print("-x+W" if k < 0 else "+x+W", end="")
        elif k > 0:
            print(f"+{k}x+W", end="")
        else:
            print(f"{k}x+W", end="")
    else:
        print("+W", end="")
