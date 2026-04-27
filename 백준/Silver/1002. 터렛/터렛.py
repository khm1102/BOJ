import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리 원의방정식
    if distance == 0 and r1 == r2 :  
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:  
        print(1)
    elif abs(r1-r2) < distance < (r1+r2) :  
        print(2)
    else:
        print(0) 
        
# 원의 방정식을 여기서 사용해 보네