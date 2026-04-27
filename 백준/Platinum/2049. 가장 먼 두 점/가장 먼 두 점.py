import sys
import os
import math
import cmath
import decimal
import itertools
import heapq
from bisect import bisect_left, bisect_right
from collections import deque

def input(): return sys.stdin.readline().strip()
def print(val):return sys.stdout.write(str(val))

def dist_squared(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points.sort()
    
    lower_hull = []
    upper_hull = []
    
    for p in points:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], p) <= 0:
            lower_hull.pop()
        lower_hull.append(p)
        
    for p in reversed(points):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], p) <= 0:
            upper_hull.pop()
        upper_hull.append(p)
    
    return lower_hull[:-1] + upper_hull[:-1]

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

convex_points = convex_hull(points)
max_dist_sq = 0

for i in range(len(convex_points)):
    for j in range(i + 1, len(convex_points)):
        max_dist_sq = max(max_dist_sq, dist_squared(convex_points[i], convex_points[j]))

print(max_dist_sq)
