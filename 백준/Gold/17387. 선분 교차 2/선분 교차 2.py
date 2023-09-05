def ccw(x1, y1, x2, y2, x3, y3):
    temp = x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0

def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    ab = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    cd = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    if ab == 0 and cd == 0:
        if [x1, y1] > [x2, y2]:
            x1, y1, x2, y2 = x2, y2, x1, y1
        if [x3, y3] > [x4, y4]:
            x3, y3, x4, y4 = x4, y4, x3, y3
        return int([x1, y1] <= [x4, y4] and [x3, y3] <= [x2, y2])
    return int(ab <= 0 and cd <= 0)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
print(is_intersect(x1, y1, x2, y2, x3, y3, x4, y4))
