def calculate_direction(x1, y1, x2, y2, x3, y3):
    vector1 = ((x2 - x1), (y2 - y1))
    vector2 = ((x3 - x2), (y3 - y2))
    cross_product = (vector1[0] * vector2[1]) - (vector1[1] * vector2[0])
    if cross_product > 0:
        return 1 
    elif cross_product < 0:
        return -1
    else:
        return 0 
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
direction = calculate_direction(x1, y1, x2, y2, x3, y3)
print(direction)