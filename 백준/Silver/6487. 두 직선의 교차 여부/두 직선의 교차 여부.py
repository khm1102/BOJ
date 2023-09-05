def calc():


    a = (x2 - x1, y2 - y1)
    b = (x4 - x3, y4 - y3)

    if a[0] * b[1] - a[1] * b[0] != 0:
        if a[0] == 0 and a[1] != 0 and b[0] != 0 and b[1] != 0:
            x = x1
            y = ((x - x3) / b[0]) * b[1] + y3
        elif a[0] == 0 and a[1] != 0 and b[0] != 0 and b[1] == 0:
            x = x1
            y = y3
        elif a[0] != 0 and a[1] == 0 and b[0] != 0 and b[1] != 0:
            y = y1
            x = ((y - y3) / b[1]) * b[0] + x3
        elif a[0] != 0 and a[1] == 0 and b[0] == 0 and b[1] != 0:
            x = x3
            y = y1
        elif a[0] != 0 and a[1] != 0 and b[0] == 0 and b[1] != 0:
            x = x3
            y = ((x - x1) / a[0]) * a[1] + y1
        elif a[0] != 0 and a[1] != 0 and b[0] != 0 and b[1] == 0:
            y = y3
            x = ((y - y1) / a[1]) * a[0] + x1
        elif a[0] != 0 and a[1] != 0 and b[0] != 0 and b[1] != 0:
            p1 = a[1] / a[0]
            q1 = y1 - p1 * x1
            p2 = b[1] / b[0]
            q2 = y3 - p2 * x3
            x = (-1) * (q1 - q2) / (p1 - p2)
            y = p1 * ((-1) * (q1 - q2) / (p1 - p2)) + q1

        print("POINT", "{:.2f}".format(x), "{:.2f}".format(y))
    else:

        c = (x3 - x1, y3 - y1)
        if a[0] * c[1] - a[1] * c[0] == 0:
            print("LINE")
        else:
            print("NONE")


N = int(input())
while N > 0:
    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
    calc()
    N -= 1
