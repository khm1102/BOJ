n = int(input())
arr = list(map(int,input().split()))
cl = arr.count(-1)
cr = arr.count(1)
cs = arr.count(0)
res = cr - cl
print("Right") if res > 0 else (print("Left") if res < 0 else print("Stay"))