import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(A, B, C):
    temp = (A.x * B.y) + (B.x * C.y) + (C.x * A.y) - (A.x * C.y) - (B.x * A.y) - (C.x * B.y)
    if temp > 0:
        return 1
    elif temp == 0:
        return 0
    else:
        return -1

def comp1(A, B):
    if A.y != B.y:
        return A.y < B.y
    else:
        return A.x < B.x

def comp2(A, B):
    dir = ccw(sp, A, B)
    if dir != 0:
        return dir == 1
    else:
        return comp1(A, B)

N = int(input())
arr = []

for _ in range(N):
    input_x, input_y = map(int, input().split())
    arr.append(Point(input_x, input_y))

arr.sort(key=lambda point: (point.x, point.y))
sp = arr[0]
arr[1:] = sorted(arr[1:], key=lambda point: (math.atan2(point.y - sp.y, point.x - sp.x), point.x, point.y))

s = []
s.append(sp)
s.append(arr[1])

for i in range(2, N):
    p3 = arr[i]
    
    while len(s) > 1:
        p2 = s.pop()
        p1 = s[-1]
        
        if ccw(p1, p2, p3) == 1:
            s.append(p2)
            break
    
    s.append(p3)

print(len(s))
