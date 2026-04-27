from collections import deque
import sys

def burst_balloons(balloons):
    result = []
    balloons = deque(balloons)
    while balloons:
        result.append(balloons[0][1])
        move = balloons.popleft()[0]
        if move > 0:
            balloons.rotate(-move + 1)
        else:
            balloons.rotate(-move)
    return result

n = int(input())
arr = list(map(int, input().split()))
arr = [(arr[i], i + 1) for i in range(n)]
print(*burst_balloons(arr))
