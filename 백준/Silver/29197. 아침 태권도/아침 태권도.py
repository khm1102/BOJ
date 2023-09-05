import math

def angle(x, y):
    return math.atan2(y, x)

def visible_students(positions):
    angles = [angle(x, y) for x, y in positions]
    sorted_students = sorted(zip(angles, positions))
    
    count = 0
    max_angle = float('-inf')
    
    for a, (x, y) in sorted_students:
        if a > max_angle:
            max_angle = a
            count += 1
    
    return count

N = int(input())
positions = []

for _ in range(N):
    x, y = map(int, input().split())
    positions.append((x, y))

print(visible_students(positions))
