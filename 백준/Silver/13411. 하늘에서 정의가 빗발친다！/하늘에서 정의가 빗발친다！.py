import math

class Robot:
    def __init__(self, num, x, y, v):
        self.num = num
        self.time = math.sqrt(x ** 2 + y ** 2) / v

n = int(input())
robots = [Robot(i, *map(int, input().split())) for i in range(n)]
robots.sort(key=lambda r: (r.time, r.num))

for robot in robots:
    print(robot.num + 1)
